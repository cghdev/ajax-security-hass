"""The Ajax Security System integration."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import config_validation as cv

from .api import AjaxRestApi, AjaxRestApiError, AjaxRestAuthError
from .const import (
    AUTH_MODE_DIRECT,
    AUTH_MODE_PROXY_HYBRID,
    AUTH_MODE_PROXY_SECURE,
    CONF_API_KEY,
    CONF_AUTH_MODE,
    CONF_AWS_ACCESS_KEY_ID,
    CONF_AWS_SECRET_ACCESS_KEY,
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_PROXY_URL,
    CONF_QUEUE_NAME,
    DOMAIN,
)
from .coordinator import AjaxDataCoordinator

if TYPE_CHECKING:
    from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

# Service names
SERVICE_FORCE_ARM = "force_arm"
SERVICE_FORCE_ARM_NIGHT = "force_arm_night"
SERVICE_GENERATE_DEVICE_INFO = "generate_device_info"
SERVICE_GET_RAW_DEVICE = "get_raw_device"

PLATFORMS: list[Platform] = [
    Platform.ALARM_CONTROL_PANEL,
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.DEVICE_TRACKER,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Ajax Security System component."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ajax Security System from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Get authentication mode (default to direct for backwards compatibility)
    auth_mode = entry.data.get(CONF_AUTH_MODE, AUTH_MODE_DIRECT)

    # Get common credentials
    email = entry.data[CONF_EMAIL]
    password_hash = entry.data[CONF_PASSWORD]  # Already hashed in config_flow

    # Variables for different modes
    api_key = None
    proxy_url = None
    proxy_mode = None
    sse_url = None
    aws_access_key_id = None
    aws_secret_access_key = None
    queue_name = None

    if auth_mode == AUTH_MODE_DIRECT:
        # Direct mode: API key provided, optional SQS for real-time events
        api_key = entry.data[CONF_API_KEY]
        aws_access_key_id = entry.data.get(CONF_AWS_ACCESS_KEY_ID)
        aws_secret_access_key = entry.data.get(CONF_AWS_SECRET_ACCESS_KEY)
        queue_name = entry.data.get(CONF_QUEUE_NAME)
        _LOGGER.info("Using direct authentication mode")

    elif auth_mode == AUTH_MODE_PROXY_SECURE:
        # Proxy Secure: All requests via proxy, SSE for real-time events
        proxy_url = entry.data[CONF_PROXY_URL]
        proxy_mode = AUTH_MODE_PROXY_SECURE
        _LOGGER.info("Using proxy secure authentication mode")

    elif auth_mode == AUTH_MODE_PROXY_HYBRID:
        # Proxy Hybrid: Login via proxy to get API key, then direct requests, SSE for events
        proxy_url = entry.data[CONF_PROXY_URL]
        proxy_mode = AUTH_MODE_PROXY_HYBRID
        _LOGGER.info("Using proxy hybrid authentication mode")

    # Create REST API instance
    # password_is_hashed=True because we store only SHA256 hash, never plain password
    api = AjaxRestApi(
        api_key=api_key,
        email=email,
        password=password_hash,
        password_is_hashed=True,  # Password is already SHA256 hash
        proxy_url=proxy_url,
        proxy_mode=proxy_mode,
    )

    try:
        # Login to get temporary token (and API key + SSE URL if using proxy)
        await api.async_login()
        _LOGGER.info("Successfully logged in to Ajax REST API")

        # Get SSE URL if using proxy mode
        if auth_mode in (AUTH_MODE_PROXY_SECURE, AUTH_MODE_PROXY_HYBRID):
            sse_url = api.sse_url
            if sse_url:
                _LOGGER.info("SSE URL obtained from proxy: %s", sse_url)
            else:
                _LOGGER.warning("No SSE URL received from proxy")

        # Test API connection by getting hubs
        await api.async_get_hubs()
        _LOGGER.info("Successfully connected to Ajax REST API")

    except AjaxRestAuthError as err:
        _LOGGER.error("Authentication failed: %s", err)
        await api.close()
        return False
    except AjaxRestApiError as err:
        _LOGGER.error("API error during setup: %s", err)
        await api.close()
        raise ConfigEntryNotReady from err

    # Create coordinator
    # - REST polling: Baseline updates every 30s
    # - AWS SQS: Optional real-time events (direct mode only)
    # - SSE: Real-time events via proxy (proxy modes only)
    coordinator = AjaxDataCoordinator(
        hass,
        api,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        queue_name=queue_name,
        sse_url=sse_url,
    )

    # Store coordinator
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Set up platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register services
    await _async_setup_services(hass, coordinator)

    return True


async def _async_setup_services(
    hass: HomeAssistant, coordinator: AjaxDataCoordinator
) -> None:
    """Set up Ajax services."""

    async def handle_force_arm(call: ServiceCall) -> None:
        """Handle force arm service call."""
        entity_id = call.data.get("entity_id")
        _LOGGER.info("Force arming via service call (entity: %s)", entity_id)

        # Get the first hub from coordinator
        if coordinator.account and coordinator.account.spaces:
            for hub_id in coordinator.account.spaces:
                try:
                    await coordinator.api.async_arm(hub_id, ignore_problems=True)
                    await coordinator.async_request_refresh()
                    _LOGGER.info("Force armed hub %s", hub_id)
                except Exception as err:
                    _LOGGER.error("Failed to force arm hub %s: %s", hub_id, err)

    async def handle_force_arm_night(call: ServiceCall) -> None:
        """Handle force arm night mode service call."""
        entity_id = call.data.get("entity_id")
        _LOGGER.info("Force arming night mode via service call (entity: %s)", entity_id)

        if coordinator.account and coordinator.account.spaces:
            for hub_id in coordinator.account.spaces:
                try:
                    await coordinator.api.async_night_mode(hub_id, enabled=True)
                    await coordinator.async_request_refresh()
                    _LOGGER.info("Force armed night mode hub %s", hub_id)
                except Exception as err:
                    _LOGGER.error(
                        "Failed to force arm night mode hub %s: %s", hub_id, err
                    )

    async def handle_generate_device_info(call: ServiceCall) -> None:
        """Handle generate device info service call."""
        _LOGGER.info("Generating device info report")

        device_info: dict[str, Any] = {
            "integration_version": "1.0.0",
            "device_types": {},
            "device_count": 0,
        }

        if coordinator.account:
            for _space_id, space in coordinator.account.spaces.items():
                for _device_id, device in space.devices.items():
                    device_type = device.raw_type
                    if device_type not in device_info["device_types"]:
                        device_info["device_types"][device_type] = {
                            "count": 0,
                            "attributes": set(),
                            "firmware_versions": set(),
                        }

                    type_info = device_info["device_types"][device_type]
                    type_info["count"] += 1
                    type_info["attributes"].update(device.attributes.keys())

                    if "firmware_version" in device.attributes:
                        type_info["firmware_versions"].add(
                            device.attributes["firmware_version"]
                        )

                    device_info["device_count"] += 1

        # Convert sets to lists for JSON serialization
        for type_info in device_info["device_types"].values():
            type_info["attributes"] = sorted(type_info["attributes"])
            type_info["firmware_versions"] = sorted(type_info["firmware_versions"])

        # Write to file
        output_path = Path(hass.config.path("ajax_device_info.json"))
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(device_info, f, indent=2, default=str)

        _LOGGER.info("Device info written to %s", output_path)

        # Create persistent notification
        from homeassistant.components.persistent_notification import async_create

        async_create(
            hass,
            f"Device info report generated: {output_path}",
            title="Ajax Device Info",
            notification_id="ajax_device_info",
        )

    async def handle_get_raw_device(call: ServiceCall) -> None:
        """Handle get raw device service call - get raw API data for a device."""
        from homeassistant.helpers import device_registry as dr

        ha_device_id = call.data.get("device")
        device_id = call.data.get("device_id", "").upper()

        # If HA device selector was used, extract the Ajax device ID from identifiers
        if ha_device_id:
            device_registry = dr.async_get(hass)
            ha_device = device_registry.async_get(ha_device_id)
            if ha_device:
                for identifier in ha_device.identifiers:
                    if identifier[0] == DOMAIN:
                        device_id = identifier[1].upper()
                        break

        if not device_id:
            _LOGGER.warning("No device_id provided")
            from homeassistant.components.persistent_notification import async_create

            async_create(
                hass,
                "No device_id provided. Use the device selector or provide device_id.",
                title="Ajax Get Raw Device",
                notification_id="ajax_get_raw_device",
            )
            return

        _LOGGER.info("Getting raw device data for id=%s", device_id)

        # Find the hub_id for this device
        hub_id = None
        if coordinator.account:
            for _space_id, space in coordinator.account.spaces.items():
                if device_id in space.devices:
                    hub_id = space.hub_id
                    break

        if not hub_id:
            _LOGGER.warning("Device not found in any hub: id=%s", device_id)
            from homeassistant.components.persistent_notification import async_create

            async_create(
                hass,
                f"Device not found: id={device_id}",
                title="Ajax Get Raw Device",
                notification_id="ajax_get_raw_device",
            )
            return

        try:
            # Call API directly to get raw device data
            raw_data = await coordinator.api.async_get_device(hub_id, device_id)

            # Write to file
            output_path = Path(hass.config.path("ajax_raw_device.json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(raw_data, f, indent=2, default=str, ensure_ascii=False)

            _LOGGER.info("Raw device data written to %s", output_path)

            # Create notification with summary
            from homeassistant.components.persistent_notification import async_create

            device_name = raw_data.get("deviceName", device_id)
            device_type = raw_data.get("deviceType", "unknown")
            attr_count = len(raw_data)

            message = (
                f"**Device:** {device_name}\n"
                f"**Type:** {device_type}\n"
                f"**ID:** {device_id}\n"
                f"**Attributes:** {attr_count}\n\n"
                f"Full raw JSON saved to: {output_path}"
            )

            async_create(
                hass,
                message,
                title=f"Ajax Raw: {device_name}",
                notification_id="ajax_get_raw_device",
            )

        except Exception as err:
            _LOGGER.error("Failed to get raw device data: %s", err)
            from homeassistant.components.persistent_notification import async_create

            async_create(
                hass,
                f"Failed to get raw device data: {err}",
                title="Ajax Get Raw Device Error",
                notification_id="ajax_get_raw_device",
            )

    # Register services if not already registered
    if not hass.services.has_service(DOMAIN, SERVICE_FORCE_ARM):
        hass.services.async_register(
            DOMAIN,
            SERVICE_FORCE_ARM,
            handle_force_arm,
            schema=vol.Schema({vol.Optional("entity_id"): cv.entity_ids}),
        )

    if not hass.services.has_service(DOMAIN, SERVICE_FORCE_ARM_NIGHT):
        hass.services.async_register(
            DOMAIN,
            SERVICE_FORCE_ARM_NIGHT,
            handle_force_arm_night,
            schema=vol.Schema({vol.Optional("entity_id"): cv.entity_ids}),
        )

    if not hass.services.has_service(DOMAIN, SERVICE_GENERATE_DEVICE_INFO):
        hass.services.async_register(
            DOMAIN,
            SERVICE_GENERATE_DEVICE_INFO,
            handle_generate_device_info,
        )

    if not hass.services.has_service(DOMAIN, SERVICE_GET_RAW_DEVICE):
        hass.services.async_register(
            DOMAIN,
            SERVICE_GET_RAW_DEVICE,
            handle_get_raw_device,
            schema=vol.Schema(
                {
                    vol.Optional("device"): cv.string,
                    vol.Optional("device_id"): cv.string,
                }
            ),
        )


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        coordinator: AjaxDataCoordinator = hass.data[DOMAIN].pop(entry.entry_id)

        # Shutdown coordinator (closes SQS manager, API connection, and all tasks)
        await coordinator.async_shutdown()

    return unload_ok
