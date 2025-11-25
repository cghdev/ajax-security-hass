"""Ajax sensor platform.

This module creates sensors for:
- Space-level statistics (device counts, notifications, etc.)
- Device-level measurements (battery, signal, temperature, etc.)
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
import logging
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.helpers.entity import EntityCategory
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, UnitOfTemperature
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, get_event_message
from .coordinator import AjaxDataCoordinator
from .models import AjaxDevice, AjaxSpace, DeviceType

_LOGGER = logging.getLogger(__name__)


# ==============================================================================
# Helper Functions
# ==============================================================================


def format_timezone(tz_string: str | None) -> str | None:
    """Format timezone string to be more readable.

    Converts formats like:
    - EUROPE_PARIS -> Europe/Paris
    - AMERICA_NEW_YORK -> America/New_York
    """
    if not tz_string:
        return None

    # Replace underscores with slashes and title case each part
    parts = tz_string.split("_")
    if len(parts) >= 2:
        # First part is region (Europe, America, etc.)
        region = parts[0].title()
        # Rest is city (may contain underscores)
        city = "_".join(parts[1:]).replace("_", " ").title().replace(" ", "_")
        return f"{region}/{city}"

    return tz_string


def format_hub_type(hub_type: str | None) -> str | None:
    """Format hub type string to be more readable.

    Converts formats like:
    - HUB_2_PLUS -> Hub 2 Plus
    - HUB_HYBRID_2G -> Hub Hybrid 2G
    """
    if not hub_type:
        return None

    # Replace underscores with spaces and title case
    return hub_type.replace("_", " ").title()


def format_signal_level(signal: str | None) -> str | None:
    """Format signal level string to be more readable.

    Converts formats like:
    - STRONG -> Fort
    - WEAK -> Faible
    - MEDIUM -> Moyen
    """
    if not signal:
        return None

    signal_map = {
        "STRONG": "Fort",
        "WEAK": "Faible",
        "MEDIUM": "Moyen",
        "EXCELLENT": "Excellent",
        "GOOD": "Bon",
        "POOR": "Mauvais",
    }

    return signal_map.get(signal.upper(), signal.title())


def format_event_text(event: dict) -> str:
    """Format an SQS event into readable French text.

    Args:
        event: Event dictionary from SQS

    Returns:
        Human-readable event text like on Ajax mobile app
    """
    event_type = event.get("event_type", "")
    action = event.get("action", "")
    device_name = event.get("device_name")
    user_name = event.get("user_name")
    room_name = event.get("room_name")

    # Event translations
    event_messages = {
        # Arming/Disarming
        ("arm", "ARM"): "Armement",
        ("arm", "DISARM"): "Désarmement",
        ("arm", "NIGHT_MODE"): "Mode nuit activé",
        ("arm", "PARTIAL"): "Armement partiel",
        # Alarms
        ("alarm", "MOTION"): "Mouvement détecté",
        ("alarm", "OPEN"): "Ouverture détectée",
        ("alarm", "TAMPER"): "Sabotage détecté",
        ("alarm", "GLASS_BREAK"): "Bris de glace détecté",
        ("alarm", "SMOKE"): "Fumée détectée",
        ("alarm", "FLOOD"): "Inondation détectée",
        ("alarm", "PANIC"): "Alarme panique",
        # Device events
        ("device", "ONLINE"): "Appareil en ligne",
        ("device", "OFFLINE"): "Appareil hors ligne",
        ("device", "LOW_BATTERY"): "Batterie faible",
        ("device", "TAMPER_OPEN"): "Couvercle ouvert",
        ("device", "TAMPER_CLOSE"): "Couvercle fermé",
        # Hub events
        ("hub", "POWER_ON"): "Alimentation connectée",
        ("hub", "POWER_OFF"): "Alimentation déconnectée",
        ("hub", "TAMPER_OPEN"): "Couvercle Hub ouvert",
        ("hub", "TAMPER_CLOSE"): "Couvercle Hub fermé",
    }

    # Get base message
    key = (event_type.lower(), action.upper()) if event_type and action else None
    message = event_messages.get(key, action or event_type or "Événement")

    # Add context
    parts = [message]
    if device_name:
        parts.append(f"- {device_name}")
    if room_name:
        parts.append(f"({room_name})")
    if user_name:
        parts.append(f"par {user_name}")

    return " ".join(parts)


def get_last_event_text(space) -> str:
    """Get the last event formatted as text."""
    if not space.recent_events:
        return "Aucun événement"
    return format_event_text(space.recent_events[0])


# ==============================================================================
# Sensor Descriptions
# ==============================================================================


@dataclass
class AjaxSpaceSensorDescription(SensorEntityDescription):
    """Description for Ajax space-level sensors."""

    value_fn: Callable[[AjaxSpace], Any] | None = None
    should_create: Callable[[AjaxSpace], bool] | None = None
    entity_category: EntityCategory | None = None


@dataclass
class AjaxDeviceSensorDescription(SensorEntityDescription):
    """Description for Ajax device-level sensors."""

    value_fn: Callable[[AjaxDevice], Any] | None = None
    should_create: Callable[[AjaxDevice], bool] | None = None
    enabled_by_default: bool = True
    extra_attributes_fn: Callable[[AjaxDevice], dict[str, Any]] | None = None


# Space-level sensor descriptions
SPACE_SENSORS: tuple[AjaxSpaceSensorDescription, ...] = (
    AjaxSpaceSensorDescription(
        key="total_devices",
        translation_key="total_devices",
        icon="mdi:devices",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: len(space.devices),
    ),
    AjaxSpaceSensorDescription(
        key="online_devices",
        translation_key="online_devices",
        icon="mdi:check-network",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: len(space.get_online_devices()),
    ),
    AjaxSpaceSensorDescription(
        key="devices_with_malfunctions",
        translation_key="devices_with_malfunctions",
        icon="mdi:alert-circle",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: space.hub_details.get("warnings", {}).get("allDevices", 0) if space.hub_details else len(space.get_devices_with_malfunctions()),
    ),
    AjaxSpaceSensorDescription(
        key="bypassed_devices",
        translation_key="bypassed_devices",
        icon="mdi:shield-off",
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: len(space.get_bypassed_devices()),
    ),
    # Recent events (from SQS)
    AjaxSpaceSensorDescription(
        key="recent_events",
        translation_key="recent_events",
        icon="mdi:history",
        value_fn=lambda space: get_last_event_text(space),
    ),
    # Hub hardware information
    AjaxSpaceSensorDescription(
        key="hub_battery",
        translation_key="hub_battery",
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda space: space.hub_details.get("battery", {}).get("chargeLevelPercentage") if space.hub_details else None,
    ),
    AjaxSpaceSensorDescription(
        key="hub_tamper",
        translation_key="hub_tamper",
        icon="mdi:lock-open-alert",
        value_fn=lambda space: "Ouvert" if space.hub_details.get("tampered") else "Fermé" if space.hub_details else None,
    ),
    AjaxSpaceSensorDescription(
        key="hub_external_power",
        translation_key="hub_external_power",
        icon="mdi:power-plug",
        value_fn=lambda space: "Connecté" if space.hub_details.get("externallyPowered") else "Déconnecté" if space.hub_details else None,
    ),
    # Network - Ethernet
    AjaxSpaceSensorDescription(
        key="hub_ethernet_ip",
        translation_key="hub_ethernet_ip",
        icon="mdi:ethernet",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: space.hub_details.get("ethernet", {}).get("ip") if space.hub_details and space.hub_details.get("ethernet", {}).get("enabled") else None,
    ),
    # Network - WiFi
    AjaxSpaceSensorDescription(
        key="hub_wifi",
        translation_key="hub_wifi",
        icon="mdi:wifi",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: format_signal_level(space.hub_details.get("wifi", {}).get("signalLevel")) if space.hub_details and space.hub_details.get("wifi", {}).get("enabled") else None,
        should_create=lambda space: space.hub_details and space.hub_details.get("wifi", {}).get("enabled", False),
    ),
    # Network - GSM
    AjaxSpaceSensorDescription(
        key="hub_gsm",
        translation_key="hub_gsm",
        icon="mdi:sim",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: format_signal_level(space.hub_details.get("gsm", {}).get("signalLevel")) if space.hub_details else None,
        should_create=lambda space: space.hub_details and space.hub_details.get("gsm") is not None,
    ),
    # System info
    AjaxSpaceSensorDescription(
        key="hub_led_brightness",
        translation_key="hub_led_brightness",
        icon="mdi:brightness-6",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: space.hub_details.get("ledBrightnessLevel") if space.hub_details else None,
    ),
    AjaxSpaceSensorDescription(
        key="hub_timezone",
        translation_key="hub_timezone",
        icon="mdi:clock-outline",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: format_timezone(space.hub_details.get("timeZone")) if space.hub_details else None,
    ),
    AjaxSpaceSensorDescription(
        key="hub_rooms",
        translation_key="hub_rooms",
        icon="mdi:door",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: len(getattr(space, "_rooms_map", {})),
        should_create=lambda space: hasattr(space, "_rooms_map") and len(getattr(space, "_rooms_map", {})) > 0,
    ),
    # Limits
    AjaxSpaceSensorDescription(
        key="hub_limits",
        translation_key="hub_limits",
        icon="mdi:counter",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: space.hub_details.get('limits', {}).get('sensors', 0) if space.hub_details else None,
        should_create=lambda space: space.hub_details and space.hub_details.get('limits'),
    ),
    # Noise Level (radio interference)
    AjaxSpaceSensorDescription(
        key="hub_noise_level",
        translation_key="hub_noise_level",
        icon="mdi:signal-off",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: (
            "Élevé" if space.hub_details.get('noiseLevel', {}).get('high', False) else "Normal"
            if space.hub_details and space.hub_details.get('noiseLevel')
            else None
        ),
        should_create=lambda space: space.hub_details and space.hub_details.get('noiseLevel'),
    ),
    # Grade Mode (security level)
    AjaxSpaceSensorDescription(
        key="hub_grade_mode",
        translation_key="hub_grade_mode",
        icon="mdi:shield-check",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: {
            "GRADE_1": "Grade 1",
            "GRADE_2": "Grade 2",
            "GRADE_3": "Grade 3",
        }.get(space.hub_details.get('gradeMode'), space.hub_details.get('gradeMode')) if space.hub_details else None,
        should_create=lambda space: space.hub_details and space.hub_details.get('gradeMode'),
    ),
    # Active Channels (WiFi, Ethernet, GSM)
    AjaxSpaceSensorDescription(
        key="hub_active_channels",
        translation_key="hub_active_channels",
        icon="mdi:access-point-network",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: (
            ", ".join(space.hub_details.get('activeChannels', []))
            if space.hub_details and space.hub_details.get('activeChannels')
            else None
        ),
        should_create=lambda space: space.hub_details and space.hub_details.get('activeChannels'),
    ),
    # Ping Period
    AjaxSpaceSensorDescription(
        key="hub_ping_period",
        translation_key="hub_ping_period",
        icon="mdi:timer-outline",
        native_unit_of_measurement="s",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: space.hub_details.get('pingPeriodSeconds') if space.hub_details else None,
        should_create=lambda space: space.hub_details and space.hub_details.get('pingPeriodSeconds'),
    ),
    # Offline Alarm Delay
    AjaxSpaceSensorDescription(
        key="hub_offline_delay",
        translation_key="hub_offline_delay",
        icon="mdi:timer-alert-outline",
        native_unit_of_measurement="s",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: space.hub_details.get('offlineAlarmSeconds') if space.hub_details else None,
        should_create=lambda space: space.hub_details and space.hub_details.get('offlineAlarmSeconds'),
    ),
    # Users count
    AjaxSpaceSensorDescription(
        key="hub_users",
        translation_key="hub_users",
        icon="mdi:account-group",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda space: len(getattr(space, "_users", [])),
        should_create=lambda space: hasattr(space, "_users") and len(getattr(space, "_users", [])) > 0,
    ),
)

# Device-level sensor descriptions
DEVICE_SENSORS: tuple[AjaxDeviceSensorDescription, ...] = (
    AjaxDeviceSensorDescription(
        key="battery",
        translation_key="battery",
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda device: device.battery_level,
        should_create=lambda device: device.has_battery,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="signal_strength",
        translation_key="signal_strength",
        icon="mdi:signal",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.signal_strength,
        should_create=lambda device: device.signal_strength is not None,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="temperature",
        translation_key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda device: device.attributes.get("temperature"),
        should_create=lambda device: device.type == DeviceType.TEMPERATURE_SENSOR
        or "temperature" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="humidity",
        translation_key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda device: device.attributes.get("humidity"),
        should_create=lambda device: "humidity" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="co2",
        translation_key="co2",
        device_class=SensorDeviceClass.CO2,
        native_unit_of_measurement="ppm",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda device: device.attributes.get("co2"),
        should_create=lambda device: "co2" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="sensitivity",
        translation_key="sensitivity",
        icon="mdi:tune",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: {0: "Faible", 1: "Normal", 2: "Élevé"}.get(device.attributes.get("sensitivity"), device.attributes.get("sensitivity")),
        should_create=lambda device: "sensitivity" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="room",
        translation_key="room",
        icon="mdi:door",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.room_name,
        should_create=lambda device: device.room_name is not None,
        enabled_by_default=True,
    ),
    # LED indicator mode
    AjaxDeviceSensorDescription(
        key="indicator_light_mode",
        translation_key="indicator_light_mode",
        icon="mdi:led-on",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.attributes.get("indicatorLightMode"),
        should_create=lambda device: "indicatorLightMode" in device.attributes,
        enabled_by_default=False,
    ),
    # MotionCam image resolution
    AjaxDeviceSensorDescription(
        key="image_resolution",
        translation_key="image_resolution",
        icon="mdi:camera",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.attributes.get("imageResolution"),
        should_create=lambda device: "imageResolution" in device.attributes,
        enabled_by_default=True,
    ),
    # MotionCam photos per alarm
    AjaxDeviceSensorDescription(
        key="photos_per_alarm",
        translation_key="photos_per_alarm",
        icon="mdi:camera-burst",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.attributes.get("photosPerAlarm"),
        should_create=lambda device: "photosPerAlarm" in device.attributes,
        enabled_by_default=True,
    ),
)

# Hub-specific sensor descriptions
HUB_SENSORS: tuple[AjaxDeviceSensorDescription, ...] = (
    AjaxDeviceSensorDescription(
        key="sim_status",
        translation_key="sim_status",
        icon="mdi:sim",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.attributes.get("sim_status"),
        should_create=lambda device: (
            "sim_status" in device.attributes
            and device.attributes.get("sim_slots_used", 0) > 0
        ),
        enabled_by_default=True,
        extra_attributes_fn=lambda device: {
            "sim_slots_total": device.attributes.get("sim_slots_total", 0),
            "sim_slots_used": device.attributes.get("sim_slots_used", 0),
            "sim_cards": device.attributes.get("sim_cards", []),
        } if "sim_cards" in device.attributes else {},
    ),
    AjaxDeviceSensorDescription(
        key="gsm_type",
        translation_key="gsm_type",
        icon="mdi:signal",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.attributes.get("gsm_type"),
        should_create=lambda device: (
            "gsm_type" in device.attributes
            and device.attributes.get("sim_slots_used", 0) > 0
        ),
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="gsm_connection_status",
        translation_key="gsm_connection_status",
        icon="mdi:access-point-network",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.attributes.get("gsm_connection_status"),
        should_create=lambda device: (
            "gsm_connection_status" in device.attributes
            and device.attributes.get("sim_slots_used", 0) > 0
        ),
        enabled_by_default=True,
        extra_attributes_fn=lambda device: device.attributes.get("gsm_info", {}),
    ),
)


def _format_volume(volume: str | None) -> str | None:
    """Format volume level to French."""
    if volume is None:
        return None
    volume_map = {
        "OFF": "Désactivé",
        "QUIET": "Silencieux",
        "NORMAL": "Normal",
        "LOUD": "Fort",
        "VERY_LOUD": "Très fort",
    }
    return volume_map.get(volume, volume)


def _format_duration(duration: int | str | None) -> str | None:
    """Format alarm duration to French."""
    if duration is None:
        return None
    if isinstance(duration, (int, float)):
        minutes = int(duration)
        if minutes == 1:
            return "1 minute"
        return f"{minutes} minutes"
    duration_map = {
        "1_MINUTE": "1 minute",
        "2_MINUTES": "2 minutes",
        "3_MINUTES": "3 minutes",
        "5_MINUTES": "5 minutes",
        "10_MINUTES": "10 minutes",
        "15_MINUTES": "15 minutes",
        "CONTINUOUS": "Continue",
    }
    return duration_map.get(str(duration), str(duration))


def _format_led(led: bool | str | None) -> str | None:
    """Format LED indication to French."""
    if led is None:
        return None
    if isinstance(led, bool):
        return "Activé" if led else "Désactivé"
    led_map = {
        "ON": "Activé",
        "OFF": "Désactivé",
        "ENABLED": "Activé",
        "DISABLED": "Désactivé",
        "TRUE": "Activé",
        "FALSE": "Désactivé",
        "BLINK_WHILE_ARMED": "Clignote en armé",
        "ALWAYS_ON": "Toujours allumé",
        "ALWAYS_OFF": "Toujours éteint",
    }
    return led_map.get(str(led).upper(), str(led))


# Siren-specific sensor descriptions
SIREN_SENSORS: tuple[AjaxDeviceSensorDescription, ...] = (
    AjaxDeviceSensorDescription(
        key="alarm_volume_level",
        translation_key="alarm_volume_level",
        icon="mdi:volume-high",
        value_fn=lambda device: _format_volume(device.attributes.get("siren_volume_level")),
        should_create=lambda device: "siren_volume_level" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="beep_volume_level",
        translation_key="beep_volume_level",
        icon="mdi:volume-medium",
        value_fn=lambda device: _format_volume(device.attributes.get("beep_volume_level")),
        should_create=lambda device: "beep_volume_level" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="alarm_duration",
        translation_key="alarm_duration",
        icon="mdi:timer-outline",
        value_fn=lambda device: _format_duration(device.attributes.get("alarm_duration")),
        should_create=lambda device: "alarm_duration" in device.attributes,
        enabled_by_default=True,
    ),
    AjaxDeviceSensorDescription(
        key="led_indication",
        translation_key="led_indication",
        icon="mdi:led-on",
        value_fn=lambda device: _format_led(device.attributes.get("led_indication")),
        should_create=lambda device: "led_indication" in device.attributes,
        enabled_by_default=True,
    ),
)

# Additional device sensor descriptions (metadata, etc.)
DEVICE_METADATA_SENSORS: tuple[AjaxDeviceSensorDescription, ...] = (
    AjaxDeviceSensorDescription(
        key="device_label",
        translation_key="device_label",
        icon="mdi:label",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.device_label,
        should_create=lambda device: device.device_label is not None,
        enabled_by_default=False,
    ),
    AjaxDeviceSensorDescription(
        key="device_marketing_id",
        translation_key="device_marketing_id",
        icon="mdi:identifier",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda device: device.device_marketing_id,
        should_create=lambda device: device.device_marketing_id is not None,
        enabled_by_default=False,
    ),
    AjaxDeviceSensorDescription(
        key="malfunctions",
        translation_key="malfunctions",
        icon="mdi:alert-circle",
        entity_category=EntityCategory.DIAGNOSTIC,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda device: len(device.malfunctions) if isinstance(device.malfunctions, list) else (device.malfunctions if isinstance(device.malfunctions, int) else 0),
        should_create=lambda device: True,
        enabled_by_default=True,
    ),
)


# ==============================================================================
# Setup
# ==============================================================================


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Ajax sensors from a config entry."""
    coordinator: AjaxDataCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SensorEntity] = []

    if not coordinator.account:
        _LOGGER.warning("No Ajax account found, no sensors created")
        return

    # Check if SQS is configured
    sqs_configured = coordinator.sqs_manager is not None

    # Create space-level sensors for each space (hub)
    for space_id, space in coordinator.account.spaces.items():
        space_sensor_count = 0
        for description in SPACE_SENSORS:
            # Check if sensor should be created
            if description.should_create and not description.should_create(space):
                continue
            # Skip recent_events sensor if SQS is not configured
            if description.key == "recent_events" and not sqs_configured:
                continue
            entities.append(
                AjaxSpaceSensor(coordinator, entry, space_id, description)
            )
            space_sensor_count += 1
        _LOGGER.debug(
            "Created %d space-level sensors for space '%s'",
            space_sensor_count,
            space.name,
        )

    # Create device-level sensors for each device
    for space_id, space in coordinator.account.spaces.items():
        for device_id, device in space.devices.items():
            # Regular device sensors
            for description in DEVICE_SENSORS:
                if description.should_create and description.should_create(device):
                    entities.append(
                        AjaxDeviceSensor(
                            coordinator, entry, space_id, device_id, description
                        )
                    )

            # Hub-specific sensors
            if device.type == DeviceType.HUB:
                for description in HUB_SENSORS:
                    if description.should_create and description.should_create(device):
                        entities.append(
                            AjaxDeviceSensor(
                                coordinator, entry, space_id, device_id, description
                            )
                        )

            # Siren-specific sensors
            if device.type == DeviceType.SIREN:
                for description in SIREN_SENSORS:
                    if description.should_create and description.should_create(device):
                        entities.append(
                            AjaxDeviceSensor(
                                coordinator, entry, space_id, device_id, description
                            )
                        )

            # Device metadata sensors (color, label, marketing ID)
            for description in DEVICE_METADATA_SENSORS:
                if description.should_create and description.should_create(device):
                    entities.append(
                        AjaxDeviceSensor(
                            coordinator, entry, space_id, device_id, description
                        )
                    )

            _LOGGER.debug(
                "Created sensors for device '%s' (type: %s)",
                device.name,
                device.type.value,
            )

    if entities:
        async_add_entities(entities)
        _LOGGER.info("Added %d Ajax sensor(s)", len(entities))
    else:
        _LOGGER.warning("No Ajax sensors created")


# ==============================================================================
# Space-level Sensors
# ==============================================================================


class AjaxSpaceSensor(CoordinatorEntity[AjaxDataCoordinator], SensorEntity):
    """Representation of an Ajax space-level sensor (statistics about the space/hub)."""

    entity_description: AjaxSpaceSensorDescription

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        entry: ConfigEntry,
        space_id: str,
        description: AjaxSpaceSensorDescription,
    ) -> None:
        """Initialize the space sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._space_id = space_id
        self._entry = entry

        # Get initial space data
        space = coordinator.get_space(space_id)
        space_name = space.name if space else "Unknown"

        # Set entity attributes - use translation_key instead of hardcoded name
        self._attr_has_entity_name = True
        self._attr_translation_key = description.translation_key
        self._attr_unique_id = f"{entry.entry_id}_{space_id}_{description.key}"

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        space = self.coordinator.get_space(self._space_id)
        if not space or not self.entity_description.value_fn:
            return None

        return self.entity_description.value_fn(space)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        # Avoid redundant name like "Ajax Hub - Hub" when space.name is already "Hub"
        hub_display_name = "Ajax Hub" if space.name == "Hub" else f"Ajax Hub - {space.name}"
        device_info = {
            "identifiers": {(DOMAIN, self._space_id)},
            "name": hub_display_name,
            "manufacturer": "Ajax Systems",
            "model": format_hub_type(space.hub_details.get("hubSubtype")) if space.hub_details else "Security Hub",
        }

        # Add firmware version if available
        if space.hub_details and space.hub_details.get("firmware"):
            firmware = space.hub_details["firmware"]
            if firmware.get("version"):
                device_info["sw_version"] = firmware["version"]

        return device_info

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra state attributes."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        attributes = {
            "space_id": space.id,
            "space_name": space.name,
            "hub_id": space.hub_id,
        }

        # Add detailed info for last_alert sensor
        if self.entity_description.key == "last_alert" and space.notifications:
            # Get the latest alert/security event
            for notification in space.notifications:
                if notification.type.value in ["alarm", "security_event"]:
                    # Get room name if available
                    room_name = None
                    if notification.device_id and notification.device_id in space.devices:
                        device = space.devices[notification.device_id]
                        if device.room_id and device.room_id in space.rooms:
                            room = space.rooms[device.room_id]
                            room_name = room.name
                            attributes["room_name"] = room.name
                            attributes["room_id"] = room.id

                    # Format message like the Ajax app
                    # Get language from Home Assistant (default to English)
                    language = self.hass.config.language if self.hass.config.language in ["en", "fr"] else "en"

                    # Create human-readable message
                    formatted_message = get_event_message(
                        notification.title,
                        language=language,
                        device_name=notification.device_name,
                        room_name=room_name,
                    )

                    attributes["event_type"] = notification.title  # Keep raw event type
                    attributes["device_name"] = notification.device_name
                    attributes["device_id"] = notification.device_id
                    attributes["notification_type"] = notification.type.value
                    attributes["message"] = formatted_message  # Use formatted message
                    attributes["raw_message"] = notification.message  # Keep original
                    if notification.user_name:
                        attributes["user_name"] = notification.user_name
                    break

        # Add room breakdown for device-related sensors
        if "device" in self.entity_description.key and space.rooms:
            attributes["rooms"] = {
                room_id: {
                    "name": room.name,
                    "device_count": len(room.device_ids),
                }
                for room_id, room in space.rooms.items()
            }

        # Add list of devices with malfunctions
        if self.entity_description.key == "devices_with_malfunctions":
            problem_list = []

            # Check hub for issues (tampered, warnings, etc.)
            if space.hub_details:
                hub_issues = []
                if space.hub_details.get("tampered"):
                    hub_issues.append("Couvercle ouvert")
                if not space.hub_details.get("externallyPowered", True):
                    hub_issues.append("Alimentation externe déconnectée")
                if space.hub_details.get("battery", {}).get("chargeLevelPercentage", 100) < 20:
                    hub_issues.append("Batterie faible")

                if hub_issues:
                    problem_list.append({
                        "name": "Hub",
                        "type": "hub",
                        "issues": hub_issues,
                    })

            # Add devices with malfunctions
            problem_devices = space.get_devices_with_malfunctions()
            for device in problem_devices:
                problem_list.append({
                    "name": device.name,
                    "type": device.type.value,
                    "room": device.room_name,
                    "malfunctions": device.malfunctions if isinstance(device.malfunctions, int) else len(device.malfunctions),
                })

            if problem_list:
                attributes["devices"] = problem_list
                attributes["device_names"] = [d["name"] for d in problem_list]

        # Add list of bypassed devices
        if self.entity_description.key == "bypassed_devices":
            bypassed = space.get_bypassed_devices()
            if bypassed:
                attributes["devices"] = [
                    {
                        "name": device.name,
                        "type": device.type.value,
                        "room": device.room_name,
                    }
                    for device in bypassed
                ]
                attributes["device_names"] = [device.name for device in bypassed]

        # Add recent events details (from SQS)
        if self.entity_description.key == "recent_events":
            attributes["event_count"] = len(space.recent_events)
            if space.recent_events:
                # List of formatted event texts
                attributes["events"] = [
                    format_event_text(event) for event in space.recent_events[:10]
                ]
                # Raw event data for automations
                attributes["events_raw"] = [
                    {
                        "type": event.get("event_type"),
                        "action": event.get("action"),
                        "device": event.get("device_name"),
                        "user": event.get("user_name"),
                        "timestamp": event.get("timestamp"),
                    }
                    for event in space.recent_events[:10]
                ]

        # Add WiFi details for hub_wifi sensor
        if self.entity_description.key == "hub_wifi" and space.hub_details:
            wifi = space.hub_details.get("wifi", {})
            if wifi and wifi.get("enabled"):
                attributes["ssid"] = wifi.get("ssid")
                attributes["ip"] = wifi.get("ip")
                attributes["signal_level"] = format_signal_level(wifi.get("signalLevel"))
                attributes["security"] = wifi.get("securityProtocol")
                attributes["channel"] = wifi.get("channel")

        # Add GSM/SIM details for hub_gsm sensor
        if self.entity_description.key == "hub_gsm" and space.hub_details:
            gsm = space.hub_details.get("gsm", {})
            if gsm:
                attributes["network_status"] = gsm.get("networkStatus")
                attributes["signal_level"] = format_signal_level(gsm.get("signalLevel"))

                # Modem IMEI
                if space.hub_details.get("modemImei"):
                    attributes["modem_imei"] = space.hub_details.get("modemImei")

                # SIM cards info
                sim_cards = gsm.get("simCards", [])
                active_sim = gsm.get("activeSimCard", 0)
                attributes["active_sim"] = active_sim + 1 if sim_cards else None
                attributes["total_sims"] = len(sim_cards)

                # SIM 1 details
                if len(sim_cards) > 0:
                    sim1 = sim_cards[0]
                    attributes["sim1_apn"] = sim1.get("apn") or "Non configuré"
                    attributes["sim1_active"] = active_sim == 0
                    attributes["sim1_traffic_tx_kb"] = sim1.get("trafficTxKb", 0)
                    attributes["sim1_traffic_rx_kb"] = sim1.get("trafficRxKb", 0)

                # SIM 2 details
                if len(sim_cards) > 1:
                    sim2 = sim_cards[1]
                    attributes["sim2_apn"] = sim2.get("apn") or "Non configuré"
                    attributes["sim2_active"] = active_sim == 1
                    attributes["sim2_traffic_tx_kb"] = sim2.get("trafficTxKb", 0)
                    attributes["sim2_traffic_rx_kb"] = sim2.get("trafficRxKb", 0)

        # Add rooms list for hub_rooms sensor
        if self.entity_description.key == "hub_rooms":
            rooms_map = getattr(space, "_rooms_map", {})
            if rooms_map:
                # List of room names
                attributes["room_names"] = list(rooms_map.values())
                # Detailed room info with IDs
                attributes["rooms"] = {
                    room_id: room_name
                    for room_id, room_name in rooms_map.items()
                }

        # Add limits details
        if self.entity_description.key == "hub_limits" and space.hub_details:
            limits = space.hub_details.get("limits", {})
            if limits:
                attributes["max_rooms"] = limits.get("rooms")
                attributes["max_groups"] = limits.get("groups")
                attributes["max_cameras"] = limits.get("cameras")
                attributes["max_sensors"] = limits.get("sensors")
                attributes["max_users"] = limits.get("users")

        # Add noise level details
        if self.entity_description.key == "hub_noise_level" and space.hub_details:
            noise = space.hub_details.get("noiseLevel", {})
            if noise:
                attributes["channel_1_dbm"] = noise.get("avgValueChannel1")
                attributes["channel_2_dbm"] = noise.get("avgValueChannel2")
                attributes["data_channel_dbm"] = noise.get("avgValueDataChannel")
                attributes["high"] = noise.get("high", False)

        # Add active channels as list
        if self.entity_description.key == "hub_active_channels" and space.hub_details:
            channels = space.hub_details.get("activeChannels", [])
            if channels:
                attributes["channels"] = channels
                attributes["ethernet"] = "ETHERNET" in channels
                attributes["wifi"] = "WIFI" in channels
                attributes["gsm"] = "GSM" in channels

        # Add hardware versions details
        if self.entity_description.key == "hub_hardware_version" and space.hub_details:
            hw = space.hub_details.get("hardwareVersions", {})
            if hw:
                attributes["cpu"] = hw.get("cpu")
                attributes["wifi"] = hw.get("wifi")
                attributes["ethernet"] = hw.get("ethernet")
                attributes["flash"] = hw.get("flash")
                attributes["pcb"] = hw.get("pcb")
                attributes["rfm"] = hw.get("rfm")
                attributes["modem"] = hw.get("modem")

        # Add users details
        if self.entity_description.key == "hub_users":
            users = getattr(space, "_users", [])
            if users:
                attributes["user_names"] = [u.get("firstName", "Unknown") for u in users]
                attributes["users"] = [
                    {
                        "name": u.get("firstName"),
                        "role": u.get("hubBindingRole"),
                        "keypad_prefix": u.get("keypadPrefix"),
                    }
                    for u in users
                ]

        return attributes


# ==============================================================================
# Device-level Sensors
# ==============================================================================


class AjaxDeviceSensor(CoordinatorEntity[AjaxDataCoordinator], SensorEntity):
    """Representation of an Ajax device-level sensor (measurements from a specific device)."""

    entity_description: AjaxDeviceSensorDescription

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        entry: ConfigEntry,
        space_id: str,
        device_id: str,
        description: AjaxDeviceSensorDescription,
    ) -> None:
        """Initialize the device sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._space_id = space_id
        self._device_id = device_id
        self._entry = entry

        # Get initial device data
        device = coordinator.get_device(space_id, device_id)
        device_name = device.name if device else "Unknown"

        # Set entity attributes - use translation_key instead of hardcoded name
        self._attr_has_entity_name = True
        self._attr_translation_key = description.translation_key
        self._attr_unique_id = f"{entry.entry_id}_{device_id}_{description.key}"
        self._attr_entity_registry_enabled_default = description.enabled_by_default

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device or not self.entity_description.value_fn:
            return None

        return self.entity_description.value_fn(device)

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if not self.coordinator.last_update_success:
            return False

        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return False

        # Device-level sensors are unavailable if device is offline
        return device.online

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass, update device info in registry."""
        await super().async_added_to_hass()

        # Update device info in registry to reflect current model, firmware, etc.
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if device and device.firmware_version:
            device_registry = dr.async_get(self.hass)
            device_entry = device_registry.async_get_device(
                identifiers={(DOMAIN, self._device_id)}
            )
            if device_entry:
                device_registry.async_update_device(
                    device_entry.id,
                    model=self._get_device_model_name(device.type.value),
                    sw_version=device.firmware_version,
                    hw_version=device.hardware_version,
                )

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        # Update device registry once on first update (for existing entities)
        if not getattr(self, "_device_info_updated", False):
            self._device_info_updated = True
            self._update_device_registry()
        self.async_write_ha_state()

    def _update_device_registry(self) -> None:
        """Update device info in registry with model, firmware, and color."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return

        device_registry = dr.async_get(self.hass)
        device_entry = device_registry.async_get_device(
            identifiers={(DOMAIN, self._device_id)}
        )
        if not device_entry:
            return

        # Get model name with color
        model_name = self._get_device_model_name(device.type.value)
        if device.device_color:
            color_name = {
                "WHITE": "Blanc", "White": "Blanc",
                "BLACK": "Noir", "Black": "Noir"
            }.get(str(device.device_color), str(device.device_color))
            model_name = f"{model_name} ({color_name})"

        device_registry.async_update_device(
            device_entry.id,
            model=model_name,
            sw_version=device.firmware_version,
            hw_version=device.hardware_version,
        )

    def _get_device_model_name(self, device_type_value: str) -> str:
        """Get translated device model name.

        Args:
            device_type_value: Device type enum value (e.g., "door_contact")

        Returns:
            Translated model name in French
        """
        translations = {
            "motion_detector": "Détecteur de mouvement",
            "door_contact": "Capteur de porte",
            "glass_break": "Détecteur bris de glace",
            "combi_protect": "Détecteur combiné",
            "smoke_detector": "Détecteur de fumée",
            "flood_detector": "Détecteur d'inondation",
            "temperature_sensor": "Capteur de température",
            "keypad": "Clavier",
            "remote_control": "Télécommande",
            "button": "Bouton",
            "siren": "Sirène",
            "transmitter": "Transmetteur",
            "repeater": "Répéteur",
            "wire_input": "Module d'entrée filaire",
            "line_splitter": "Répartiteur de ligne",
            "socket": "Prise connectée",
            "relay": "Relais",
            "thermostat": "Thermostat",
            "life_quality": "Capteur qualité de l'air",
            "camera": "Caméra",
            "hub": "Hub",
            "unknown": "Appareil inconnu",
        }
        return translations.get(device_type_value, device_type_value.replace("_", " ").title())

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return {}

        # Get model name with color
        model_name = self._get_device_model_name(device.type.value)
        if device.device_color:
            color_name = {
                "WHITE": "Blanc", "White": "Blanc",
                "BLACK": "Noir", "Black": "Noir"
            }.get(str(device.device_color), str(device.device_color))
            model_name = f"{model_name} ({color_name})"

        # For hub devices, use the space identifier to merge with space-level sensors
        # This prevents duplicate hub devices in Home Assistant
        if device.type == DeviceType.HUB:
            # Avoid redundant name if device.name is already "Hub"
            hub_name = "Ajax Hub" if device.name == "Hub" else f"Ajax {device.name}"
            return {
                "identifiers": {(DOMAIN, self._space_id)},
                "name": hub_name,
                "manufacturer": "Ajax Systems",
                "model": model_name,
                "sw_version": device.firmware_version,
                "hw_version": device.hardware_version,
            }

        # For non-hub devices, use device identifier
        # Get room name if available
        room_name = None
        if device.room_id:
            space = self.coordinator.get_space(self._space_id)
            if space and device.room_id in space.rooms:
                room_name = space.rooms[device.room_id].name

        # Include room name in device name if available
        device_display_name = f"{room_name} - {device.name}" if room_name else device.name

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": f"Ajax {device_display_name}",
            "manufacturer": "Ajax Systems",
            "model": model_name,
            "via_device": (DOMAIN, self._space_id),
            "sw_version": device.firmware_version,
            "hw_version": device.hardware_version,
        }

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra state attributes."""
        device = self.coordinator.get_device(self._space_id, self._device_id)
        if not device:
            return {}

        attributes = {
            "device_id": device.id,
            "device_type": device.type.value,
            "space_id": device.space_id,
            "hub_id": device.hub_id,
            "online": device.online,
            "bypassed": device.bypassed,
        }

        # Add room information if available
        if device.room_id:
            room = self.coordinator.get_room(self._space_id, device.room_id)
            if room:
                attributes["room_id"] = room.id
                attributes["room_name"] = room.name

        # Add battery state for battery sensors
        if self.entity_description.key == "battery" and device.battery_state:
            attributes["battery_state"] = device.battery_state
            attributes["is_low_battery"] = device.is_low_battery

        # Add custom attributes from description if available
        if hasattr(self.entity_description, "extra_attributes_fn") and self.entity_description.extra_attributes_fn:
            custom_attrs = self.entity_description.extra_attributes_fn(device)
            if custom_attrs:
                attributes.update(custom_attrs)

        return attributes
