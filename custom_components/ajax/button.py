"""Ajax button platform."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.button import ButtonEntity, ButtonDeviceClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import AjaxDataCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Ajax buttons from a config entry."""
    coordinator: AjaxDataCoordinator = hass.data[DOMAIN][entry.entry_id]

    # Create a panic button for each space
    entities = []

    if coordinator.account:
        for space_id, space in coordinator.account.spaces.items():
            entities.append(AjaxPanicButton(coordinator, entry, space_id))

    if entities:
        async_add_entities(entities)
        _LOGGER.info("Added %d Ajax button(s)", len(entities))
    else:
        _LOGGER.info("No Ajax spaces found, no buttons created (yet)")


class AjaxPanicButton(CoordinatorEntity[AjaxDataCoordinator], ButtonEntity):
    """Representation of an Ajax panic button."""

    _attr_device_class = ButtonDeviceClass.IDENTIFY
    _attr_icon = "mdi:alarm-light"

    def __init__(
        self, coordinator: AjaxDataCoordinator, entry: ConfigEntry, space_id: str
    ) -> None:
        """Initialize the panic button."""
        super().__init__(coordinator)
        self._entry = entry
        self._space_id = space_id

        # Get initial space data
        space = coordinator.get_space(space_id)
        space_name = space.name if space else "Unknown"

        self._attr_name = f"Ajax Panic - {space_name}"
        self._attr_unique_id = f"{entry.entry_id}_panic_{space_id}"

    async def async_press(self) -> None:
        """Handle the button press."""
        _LOGGER.warning("PANIC BUTTON pressed by user!")

        try:
            await self.coordinator.async_press_panic_button(self._space_id)
        except Exception as err:
            _LOGGER.error("Failed to trigger panic: %s", err)
            raise

    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        space = self.coordinator.get_space(self._space_id)
        if not space:
            return {}

        return {
            "identifiers": {(DOMAIN, self._space_id)},
            "name": f"Ajax Hub - {space.name}",
            "manufacturer": "Ajax Systems",
            "model": "Security Hub",
            "sw_version": None,  # TODO: Add hub firmware version when available
        }
