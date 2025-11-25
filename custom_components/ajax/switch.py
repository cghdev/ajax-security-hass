"""Ajax switch platform for Home Assistant.

This module creates switches for Ajax device settings like:
- alwaysActive: Keep device active even when disarmed
- indicatorLightMode: LED indicator on device
- alertsBySirens: Alert by sirens when alarm triggered
- armedInNightMode: Include device in night mode
"""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import AjaxDataCoordinator

_LOGGER = logging.getLogger(__name__)

# Device types that support alwaysActive setting
DEVICES_WITH_ALWAYS_ACTIVE = [
    "MotionProtect",
    "MotionProtectS",
    "MotionProtectFibra",
    "MotionProtectPlus",
    "MotionProtectSPlus",
    "MotionProtectPlusFibra",
    "MotionProtectOutdoor",
    "MotionCam",
    "MotionCamPhod",
    "MotionCamSPhod",
    "MotionCamOutdoor",
    "MotionCamOutdoorPhod",
    "MotionCamFibra",
    "MotionCamPhodFibra",
    "DoorProtect",
    "DoorProtectS",
    "DoorProtectFibra",
    "DoorProtectPlus",
    "DoorProtectPlusFibra",
    "GlassProtect",
    "GlassProtectS",
    "GlassProtectFibra",
]

# Device types that support LED indicator mode setting
DEVICES_WITH_INDICATOR_LIGHT = [
    "MotionProtect",
    "MotionProtectS",
    "MotionProtectFibra",
    "MotionProtectPlus",
    "MotionProtectSPlus",
    "MotionProtectPlusFibra",
    "MotionProtectOutdoor",
    "MotionCam",
    "MotionCamPhod",
    "MotionCamSPhod",
    "MotionCamOutdoor",
    "MotionCamOutdoorPhod",
    "MotionCamFibra",
    "MotionCamPhodFibra",
    "DoorProtect",
    "DoorProtectS",
    "DoorProtectFibra",
    "DoorProtectPlus",
    "DoorProtectPlusFibra",
    "GlassProtect",
    "GlassProtectS",
    "GlassProtectFibra",
    "LeaksProtect",
    "LeaksProtectFibra",
    "FireProtect",
    "FireProtectS",
    "FireProtect2",
    "FireProtectFibra",
]

# Device types that support night mode arming setting
DEVICES_WITH_NIGHT_MODE = [
    "MotionProtect",
    "MotionProtectS",
    "MotionProtectFibra",
    "MotionProtectPlus",
    "MotionProtectSPlus",
    "MotionProtectPlusFibra",
    "MotionProtectOutdoor",
    "MotionCam",
    "MotionCamPhod",
    "MotionCamSPhod",
    "MotionCamOutdoor",
    "MotionCamOutdoorPhod",
    "MotionCamFibra",
    "MotionCamPhodFibra",
    "DoorProtect",
    "DoorProtectS",
    "DoorProtectFibra",
    "DoorProtectPlus",
    "DoorProtectPlusFibra",
    "GlassProtect",
    "GlassProtectS",
    "GlassProtectFibra",
    "LeaksProtect",
    "LeaksProtectFibra",
    "HomeSiren",
    "HomeSirenFibra",
    "StreetSiren",
    "StreetSirenFibra",
]

# Device types that support DoorProtect Plus features
DEVICES_WITH_DOOR_PLUS_FEATURES = [
    "DoorProtectPlus",
    "DoorProtectPlusFibra",
]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Ajax switches from a config entry."""
    coordinator: AjaxDataCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SwitchEntity] = []

    # Create switches for each device that supports settings
    for space_id, space in coordinator.account.spaces.items():
        for device_id, device in space.devices.items():
            device_type = device.raw_type or ""

            # Always Active switch
            if device_type in DEVICES_WITH_ALWAYS_ACTIVE:
                entities.append(
                    AjaxAlwaysActiveSwitch(
                        coordinator,
                        space_id,
                        device_id,
                    )
                )
                _LOGGER.debug(
                    "Created alwaysActive switch for device: %s (%s)",
                    device.name,
                    device_type,
                )

            # LED Indicator switch
            if device_type in DEVICES_WITH_INDICATOR_LIGHT:
                entities.append(
                    AjaxIndicatorLightSwitch(
                        coordinator,
                        space_id,
                        device_id,
                    )
                )
                _LOGGER.debug(
                    "Created indicatorLight switch for device: %s (%s)",
                    device.name,
                    device_type,
                )

            # Armed in Night Mode switch
            if device_type in DEVICES_WITH_NIGHT_MODE:
                entities.append(
                    AjaxNightModeSwitch(
                        coordinator,
                        space_id,
                        device_id,
                    )
                )
                _LOGGER.debug(
                    "Created nightMode switch for device: %s (%s)",
                    device.name,
                    device_type,
                )

            # DoorProtect Plus specific switches
            if device_type in DEVICES_WITH_DOOR_PLUS_FEATURES:
                # External contact switch
                entities.append(
                    AjaxExternalContactSwitch(coordinator, space_id, device_id)
                )
                # Shock sensor switch
                entities.append(
                    AjaxShockSensorSwitch(coordinator, space_id, device_id)
                )
                # Ignore simple impact switch
                entities.append(
                    AjaxIgnoreImpactSwitch(coordinator, space_id, device_id)
                )
                # Tilt sensor switch
                entities.append(
                    AjaxTiltSensorSwitch(coordinator, space_id, device_id)
                )
                # Siren trigger switches
                entities.append(
                    AjaxSirenTriggerReedSwitch(coordinator, space_id, device_id)
                )
                entities.append(
                    AjaxSirenTriggerShockSwitch(coordinator, space_id, device_id)
                )
                entities.append(
                    AjaxSirenTriggerTiltSwitch(coordinator, space_id, device_id)
                )
                _LOGGER.debug(
                    "Created DoorProtect Plus switches for device: %s",
                    device.name,
                )

    if entities:
        async_add_entities(entities)
        _LOGGER.info("Added %d Ajax switch(es)", len(entities))


class AjaxAlwaysActiveSwitch(CoordinatorEntity[AjaxDataCoordinator], SwitchEntity):
    """Switch to control device alwaysActive setting."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        space_id: str,
        device_id: str,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id

        space = coordinator.get_space(space_id)
        device = space.devices.get(device_id) if space else None
        device_name = device.name if device else "Unknown"

        self._attr_unique_id = f"{device_id}_always_active"
        self._attr_name = "Toujours actif"
        self._attr_icon = "mdi:shield-alert"
        self._attr_translation_key = "always_active"

    @property
    def is_on(self) -> bool | None:
        """Return true if the switch is on."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return None

        device = space.devices.get(self._device_id)
        if not device:
            return None

        return device.attributes.get("always_active", False)

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return False

        device = space.devices.get(self._device_id)
        if not device:
            return False

        return device.online

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        await self._set_always_active(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        await self._set_always_active(False)

    async def _set_always_active(self, value: bool) -> None:
        """Set the alwaysActive value."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            _LOGGER.error("Space %s not found", self._space_id)
            return

        try:
            await self.coordinator.api.async_update_device(
                space.hub_id,
                self._device_id,
                {"alwaysActive": value}
            )
            _LOGGER.info(
                "Set alwaysActive=%s for device %s",
                value,
                self._device_id,
            )
            # Refresh data to get updated state
            await self.coordinator.async_request_refresh()
        except Exception as err:
            _LOGGER.error(
                "Failed to set alwaysActive for device %s: %s",
                self._device_id,
                err,
            )

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra state attributes."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        device = space.devices.get(self._device_id)
        if not device:
            return {}

        return {
            "device_type": device.raw_type,
            "device_id": self._device_id,
        }

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        device = space.devices.get(self._device_id)
        if not device:
            return {}

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": device.name,
            "manufacturer": "Ajax Systems",
            "model": device.raw_type,
            "via_device": (DOMAIN, self._space_id),
        }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()


class AjaxIndicatorLightSwitch(CoordinatorEntity[AjaxDataCoordinator], SwitchEntity):
    """Switch to control device LED indicator light setting."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        space_id: str,
        device_id: str,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id

        self._attr_unique_id = f"{device_id}_indicator_light"
        self._attr_name = "Indication LED"
        self._attr_icon = "mdi:led-on"
        self._attr_translation_key = "indicator_light"

    @property
    def is_on(self) -> bool | None:
        """Return true if the switch is on."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return None

        device = space.devices.get(self._device_id)
        if not device:
            return None

        # indicatorLightMode: "STANDARD" = on, "DONT_BLINK_ON_ALARM" = off
        mode = device.attributes.get("indicatorLightMode", "STANDARD")
        return mode == "STANDARD"

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return False

        device = space.devices.get(self._device_id)
        if not device:
            return False

        return device.online

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        await self._set_indicator_light("STANDARD")

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        await self._set_indicator_light("DONT_BLINK_ON_ALARM")

    async def _set_indicator_light(self, value: str) -> None:
        """Set the indicatorLightMode value."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            _LOGGER.error("Space %s not found", self._space_id)
            return

        try:
            await self.coordinator.api.async_update_device(
                space.hub_id,
                self._device_id,
                {"indicatorLightMode": value}
            )
            _LOGGER.info(
                "Set indicatorLightMode=%s for device %s",
                value,
                self._device_id,
            )
            await self.coordinator.async_request_refresh()
        except Exception as err:
            _LOGGER.error(
                "Failed to set indicatorLightMode for device %s: %s",
                self._device_id,
                err,
            )

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra state attributes."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        device = space.devices.get(self._device_id)
        if not device:
            return {}

        return {
            "device_type": device.raw_type,
            "device_id": self._device_id,
            "mode": device.attributes.get("indicatorLightMode"),
        }

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        device = space.devices.get(self._device_id)
        if not device:
            return {}

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": device.name,
            "manufacturer": "Ajax Systems",
            "model": device.raw_type,
            "via_device": (DOMAIN, self._space_id),
        }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()


class AjaxNightModeSwitch(CoordinatorEntity[AjaxDataCoordinator], SwitchEntity):
    """Switch to control device armed in night mode setting."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: AjaxDataCoordinator,
        space_id: str,
        device_id: str,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id

        self._attr_unique_id = f"{device_id}_night_mode"
        self._attr_name = "Armé en mode nuit"
        self._attr_icon = "mdi:weather-night"
        self._attr_translation_key = "night_mode"

    @property
    def is_on(self) -> bool | None:
        """Return true if the switch is on."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return None

        device = space.devices.get(self._device_id)
        if not device:
            return None

        return device.attributes.get("armed_in_night_mode", False)

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return False

        device = space.devices.get(self._device_id)
        if not device:
            return False

        return device.online

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        await self._set_night_mode(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        await self._set_night_mode(False)

    async def _set_night_mode(self, value: bool) -> None:
        """Set the armedInNightMode value."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            _LOGGER.error("Space %s not found", self._space_id)
            return

        try:
            # API uses nightModeArm or armedInNightMode
            await self.coordinator.api.async_update_device(
                space.hub_id,
                self._device_id,
                {"nightModeArm": value}
            )
            _LOGGER.info(
                "Set nightModeArm=%s for device %s",
                value,
                self._device_id,
            )
            await self.coordinator.async_request_refresh()
        except Exception as err:
            _LOGGER.error(
                "Failed to set nightModeArm for device %s: %s",
                self._device_id,
                err,
            )

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra state attributes."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        device = space.devices.get(self._device_id)
        if not device:
            return {}

        return {
            "device_type": device.raw_type,
            "device_id": self._device_id,
        }

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        device = space.devices.get(self._device_id)
        if not device:
            return {}

        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": device.name,
            "manufacturer": "Ajax Systems",
            "model": device.raw_type,
            "via_device": (DOMAIN, self._space_id),
        }

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self.async_write_ha_state()


# =============================================================================
# DoorProtect Plus specific switches
# =============================================================================


class AjaxDoorPlusBaseSwitch(CoordinatorEntity[AjaxDataCoordinator], SwitchEntity):
    """Base class for DoorProtect Plus switches."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator)
        self._space_id = space_id
        self._device_id = device_id

    def _get_device(self):
        space = self.coordinator.get_space(self._space_id)
        return space.devices.get(self._device_id) if space else None

    @property
    def available(self) -> bool:
        device = self._get_device()
        return device.online if device else False

    @property
    def device_info(self) -> dict[str, Any]:
        return {"identifiers": {(DOMAIN, self._device_id)}}

    @callback
    def _handle_coordinator_update(self) -> None:
        self.async_write_ha_state()


class AjaxExternalContactSwitch(AjaxDoorPlusBaseSwitch):
    """Switch to control external contact feature."""

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_external_contact"
        self._attr_name = "Contact externe"
        self._attr_icon = "mdi:electric-switch"

    @property
    def is_on(self) -> bool | None:
        device = self._get_device()
        return device.attributes.get("extra_contact_aware", False) if device else None

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self._set_value(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self._set_value(False)

    async def _set_value(self, value: bool) -> None:
        space = self.coordinator.get_space(self._space_id)
        if space:
            try:
                await self.coordinator.api.async_update_device(space.hub_id, self._device_id, {"extraContactAware": value})
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error("Failed to set extraContactAware: %s", err)


class AjaxShockSensorSwitch(AjaxDoorPlusBaseSwitch):
    """Switch to control shock sensor feature."""

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_shock_sensor"
        self._attr_name = "Capteur de choc"
        self._attr_icon = "mdi:vibrate"

    @property
    def is_on(self) -> bool | None:
        device = self._get_device()
        return device.attributes.get("shock_sensor_aware", False) if device else None

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self._set_value(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self._set_value(False)

    async def _set_value(self, value: bool) -> None:
        space = self.coordinator.get_space(self._space_id)
        if space:
            try:
                await self.coordinator.api.async_update_device(space.hub_id, self._device_id, {"shockSensorAware": value})
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error("Failed to set shockSensorAware: %s", err)


class AjaxIgnoreImpactSwitch(AjaxDoorPlusBaseSwitch):
    """Switch to control ignore simple impact feature."""

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_ignore_impact"
        self._attr_name = "Ignorer impact simple"
        self._attr_icon = "mdi:shield-off"

    @property
    def is_on(self) -> bool | None:
        device = self._get_device()
        return device.attributes.get("ignore_simple_impact", False) if device else None

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self._set_value(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self._set_value(False)

    async def _set_value(self, value: bool) -> None:
        space = self.coordinator.get_space(self._space_id)
        if space:
            try:
                await self.coordinator.api.async_update_device(space.hub_id, self._device_id, {"ignoreSimpleImpact": value})
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error("Failed to set ignoreSimpleImpact: %s", err)


class AjaxTiltSensorSwitch(AjaxDoorPlusBaseSwitch):
    """Switch to control tilt sensor (accelerometer) feature."""

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_tilt_sensor"
        self._attr_name = "Capteur d'inclinaison"
        self._attr_icon = "mdi:angle-acute"

    @property
    def is_on(self) -> bool | None:
        device = self._get_device()
        return device.attributes.get("accelerometer_aware", False) if device else None

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self._set_value(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self._set_value(False)

    async def _set_value(self, value: bool) -> None:
        space = self.coordinator.get_space(self._space_id)
        if space:
            try:
                await self.coordinator.api.async_update_device(space.hub_id, self._device_id, {"accelerometerAware": value})
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error("Failed to set accelerometerAware: %s", err)


class AjaxSirenTriggerBaseSwitch(AjaxDoorPlusBaseSwitch):
    """Base class for siren trigger switches."""

    _trigger_key: str = ""  # REED, SHOCK, TILT, etc.

    @property
    def is_on(self) -> bool | None:
        device = self._get_device()
        if not device:
            return None
        triggers = device.attributes.get("siren_triggers", [])
        return self._trigger_key in triggers

    async def async_turn_on(self, **kwargs: Any) -> None:
        await self._set_trigger(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        await self._set_trigger(False)

    async def _set_trigger(self, enabled: bool) -> None:
        space = self.coordinator.get_space(self._space_id)
        device = self._get_device()
        if not space or not device:
            return

        current_triggers = list(device.attributes.get("siren_triggers", []))

        if enabled and self._trigger_key not in current_triggers:
            current_triggers.append(self._trigger_key)
        elif not enabled and self._trigger_key in current_triggers:
            current_triggers.remove(self._trigger_key)

        try:
            await self.coordinator.api.async_update_device(
                space.hub_id, self._device_id, {"sirenTriggers": current_triggers}
            )
            _LOGGER.info("Set sirenTriggers=%s for device %s", current_triggers, self._device_id)
            await self.coordinator.async_request_refresh()
        except Exception as err:
            _LOGGER.error("Failed to set sirenTriggers: %s", err)


class AjaxSirenTriggerReedSwitch(AjaxSirenTriggerBaseSwitch):
    """Switch for siren alert on door/window opening (REED)."""

    _trigger_key = "REED"
    _attr_has_entity_name = False

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_siren_trigger_reed"
        self._attr_name = "Sirène si ouverture"
        self._attr_icon = "mdi:door-open"


class AjaxSirenTriggerShockSwitch(AjaxSirenTriggerBaseSwitch):
    """Switch for siren alert on shock detection."""

    _trigger_key = "SHOCK"
    _attr_has_entity_name = False

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_siren_trigger_shock"
        self._attr_name = "Sirène si choc"
        self._attr_icon = "mdi:vibrate"


class AjaxSirenTriggerTiltSwitch(AjaxSirenTriggerBaseSwitch):
    """Switch for siren alert on tilt detection."""

    _trigger_key = "TILT"
    _attr_has_entity_name = False

    def __init__(self, coordinator: AjaxDataCoordinator, space_id: str, device_id: str) -> None:
        super().__init__(coordinator, space_id, device_id)
        self._attr_unique_id = f"{device_id}_siren_trigger_tilt"
        self._attr_name = "Sirène si inclinaison"
        self._attr_icon = "mdi:angle-acute"
