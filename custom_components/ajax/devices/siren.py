"""Siren device handler for Ajax HomeSiren series.

Handles:
- HomeSiren
- StreetSiren
- StreetSiren DoubleDeck
"""

from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfTemperature,
)

from .base import AjaxDeviceHandler


class SirenHandler(AjaxDeviceHandler):
    """Handler for Ajax HomeSiren sirens."""

    def get_binary_sensors(self) -> list[dict]:
        """Return binary sensor entities for sirens."""
        sensors = []

        # Note: "armed_in_night_mode" is now a switch, not a binary sensor

        # Tamper / Couvercle
        sensors.append(
            {
                "key": "tamper",
                "translation_key": "tamper",
                "device_class": BinarySensorDeviceClass.TAMPER,
                "icon": "mdi:lock-open-alert",
                "value_fn": lambda: self.device.attributes.get("tampered", False),
                "enabled_by_default": True,
            }
        )

        return sensors

    def get_sensors(self) -> list[dict]:
        """Return sensor entities for sirens."""
        sensors = []

        # Battery level
        sensors.append(
            {
                "key": "battery",
                "translation_key": "battery",
                "device_class": SensorDeviceClass.BATTERY,
                "native_unit_of_measurement": PERCENTAGE,
                "state_class": SensorStateClass.MEASUREMENT,
                "value_fn": lambda: self.device.battery_level if self.device.battery_level is not None else None,
                "enabled_by_default": True,
            }
        )

        # Signal strength
        sensors.append(
            {
                "key": "signal_strength",
                "translation_key": "signal_strength",
                "icon": "mdi:signal",
                "native_unit_of_measurement": PERCENTAGE,
                "state_class": SensorStateClass.MEASUREMENT,
                "value_fn": lambda: self.device.signal_strength if self.device.signal_strength is not None else None,
                "enabled_by_default": True,
            }
        )

        # Temperature
        if "temperature" in self.device.attributes:
            sensors.append(
                {
                    "key": "temperature",
                    "translation_key": "temperature",
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "native_unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT,
                    "value_fn": lambda: self.device.attributes.get("temperature"),
                    "enabled_by_default": True,
                }
            )

        # Alarm volume level (sirenVolumeLevel from API)
        if "siren_volume_level" in self.device.attributes:
            sensors.append(
                {
                    "key": "alarm_volume_level",
                    "translation_key": "alarm_volume_level",
                    "icon": "mdi:volume-high",
                    "value_fn": lambda: self._format_volume(self.device.attributes.get("siren_volume_level")),
                    "enabled_by_default": True,
                }
            )

        # Beep volume level
        if "beep_volume_level" in self.device.attributes:
            sensors.append(
                {
                    "key": "beep_volume_level",
                    "translation_key": "beep_volume_level",
                    "icon": "mdi:volume-medium",
                    "value_fn": lambda: self._format_volume(self.device.attributes.get("beep_volume_level")),
                    "enabled_by_default": True,
                }
            )

        # Alarm duration
        if "alarm_duration" in self.device.attributes:
            sensors.append(
                {
                    "key": "alarm_duration",
                    "translation_key": "alarm_duration",
                    "icon": "mdi:timer-outline",
                    "value_fn": lambda: self._format_duration(self.device.attributes.get("alarm_duration")),
                    "enabled_by_default": True,
                }
            )

        # LED indication
        if "led_indication" in self.device.attributes:
            sensors.append(
                {
                    "key": "led_indication",
                    "translation_key": "led_indication",
                    "icon": "mdi:led-on",
                    "value_fn": lambda: self._format_led(self.device.attributes.get("led_indication")),
                    "enabled_by_default": True,
                }
            )

        return sensors

    def _format_volume(self, volume: str | None) -> str | None:
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

    def _format_duration(self, duration: int | str | None) -> str | None:
        """Format alarm duration to French."""
        if duration is None:
            return None
        # If it's a number (seconds), convert to minutes
        if isinstance(duration, (int, float)):
            minutes = int(duration) // 60
            if minutes == 0:
                return f"{int(duration)} secondes"
            return f"{minutes} minutes"
        # If it's a string like "3_MINUTES", "180_SECONDS", etc.
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

    def _format_led(self, led: bool | str | None) -> str | None:
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
