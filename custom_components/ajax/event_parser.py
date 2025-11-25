"""Ajax event parser for SQS messages.

This module parses Ajax events received from SQS and converts them
into actionable data for Home Assistant.

Event Structure (from SQS):
{
    "eventId": "unique_id",
    "hubId": "hub_serial",
    "eventType": "ALARM|MALFUNCTION|ARM|DISARM|...",
    "eventCode": "M_01_20",
    "sourceObjectType": "device|user|hub",
    "sourceObjectName": "Living Room Motion",
    "timestamp": 1700820123,
    "transition": "TRIGGERED|RECOVERED|IMPULSE",
    "additionalData": {...}
}
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

_LOGGER = logging.getLogger(__name__)


# Event Type Mapping
EVENT_TYPE_ALARM = "ALARM"
EVENT_TYPE_MALFUNCTION = "MALFUNCTION"
EVENT_TYPE_ARM = "ARM"
EVENT_TYPE_DISARM = "DISARM"
EVENT_TYPE_TEST = "TEST"
EVENT_TYPE_CONNECTION = "CONNECTION"
EVENT_TYPE_BATTERY = "BATTERY"

# Event Transition States
TRANSITION_TRIGGERED = "TRIGGERED"
TRANSITION_RECOVERED = "RECOVERED"
TRANSITION_IMPULSE = "IMPULSE"

# Common Event Codes (200+ exist, mapping most important)
EVENT_CODES = {
    # Motion Detection
    "M_01_01": "motion_detected",
    "M_01_02": "motion_detected",

    # Door/Window Contacts
    "M_01_20": "door_opened",
    "M_01_21": "external_contact_opened",

    # Smoke/Fire Detection
    "M_03_20": "smoke_detected",
    "M_03_21": "temperature_alarm",
    "M_03_22": "co_detected",

    # Water Leak Detection
    "M_04_20": "leak_detected",

    # Glass Break Detection
    "M_05_20": "glass_break_detected",

    # Tamper/Sabotage
    "M_06_01": "device_tampered",
    "M_06_02": "device_case_opened",

    # Connection Status
    "C_01_01": "device_offline",
    "C_01_02": "device_jamming",

    # Battery Status
    "B_01_01": "battery_low",
    "B_01_02": "battery_critical",

    # Hub Arming
    "A_01_01": "armed_full",
    "A_01_02": "armed_partial",
    "A_01_03": "armed_night",
    "A_02_01": "disarmed",

    # Malfunctions
    "F_01_01": "device_malfunction",
    "F_02_01": "power_failure",
    "F_03_01": "communication_error",
}


class AjaxEventParser:
    """Parser for Ajax SQS events."""

    @staticmethod
    def parse_event(event_data: dict[str, Any]) -> dict[str, Any] | None:
        """Parse Ajax event from SQS message.

        Args:
            event_data: Raw event data from SQS

        Returns:
            Parsed event dict or None if invalid
        """
        try:
            # SQS wraps the event in {"recipient": ..., "event": {...}}
            if "event" in event_data:
                event_data = event_data["event"]

            event_id = event_data.get("eventId")
            hub_id = event_data.get("hubId")
            event_type = event_data.get("eventType") or event_data.get("eventTypeV2")
            event_code = event_data.get("eventCode", "")
            event_tag = event_data.get("eventTag", "")  # Arm, Disarm, NightModeOn
            source_type = event_data.get("sourceObjectType", "")
            source_name = event_data.get("sourceObjectName", "")
            timestamp = event_data.get("timestamp", 0)
            transition = event_data.get("transition", "")
            additional_data = event_data.get("additionalData", {})

            if not event_id or not hub_id:
                _LOGGER.warning("Invalid event: missing eventId or hubId")
                return None

            # Parse event code to action, prefer eventTag for arming events
            if event_tag:
                # Use eventTag directly: Arm, Disarm, NightModeOn
                action = event_tag.lower()
            else:
                action = EVENT_CODES.get(event_code, f"unknown_{event_code}")

            # Convert timestamp to datetime (timestamp is in milliseconds)
            event_time = None
            if timestamp:
                try:
                    # Ajax timestamps are in milliseconds
                    event_time = datetime.fromtimestamp(timestamp / 1000)
                except (ValueError, OSError):
                    _LOGGER.warning("Invalid timestamp: %s", timestamp)

            # Determine if event is active (triggered) or cleared (recovered)
            is_active = transition == TRANSITION_TRIGGERED

            parsed = {
                "event_id": event_id,
                "hub_id": hub_id,
                "space_id": hub_id,  # hub_id is the space_id
                "event_type": event_type,
                "event_code": event_code,
                "event_tag": event_tag,
                "action": action,
                "source_type": source_type,
                "source_name": source_name,
                "timestamp": timestamp / 1000 if timestamp else 0,  # Convert to seconds
                "event_time": event_time,
                "transition": transition,
                "is_active": is_active,
                "additional_data": additional_data,
            }

            _LOGGER.info(
                "Parsed SQS event: %s - %s (%s)",
                event_tag or event_type,
                action,
                source_name,
            )

            return parsed

        except Exception as err:
            _LOGGER.error("Failed to parse event: %s", err)
            return None

    @staticmethod
    def is_alarm_event(event: dict[str, Any]) -> bool:
        """Check if event is an alarm event.

        Args:
            event: Parsed event dict

        Returns:
            True if alarm event
        """
        return event.get("event_type") == EVENT_TYPE_ALARM

    @staticmethod
    def is_arming_event(event: dict[str, Any]) -> bool:
        """Check if event is an arming/disarming event.

        Args:
            event: Parsed event dict

        Returns:
            True if arming event
        """
        # Check eventTag first (arm, disarm, nightmodeon)
        action = event.get("action", "").lower()
        if action in ["arm", "disarm", "nightmodeon"]:
            return True

        # Fallback to event_type
        event_type = event.get("event_type", "")
        return event_type in [EVENT_TYPE_ARM, EVENT_TYPE_DISARM]

    @staticmethod
    def is_malfunction_event(event: dict[str, Any]) -> bool:
        """Check if event is a malfunction event.

        Args:
            event: Parsed event dict

        Returns:
            True if malfunction event
        """
        return event.get("event_type") == EVENT_TYPE_MALFUNCTION

    @staticmethod
    def is_connection_event(event: dict[str, Any]) -> bool:
        """Check if event is a connection/offline event.

        Args:
            event: Parsed event dict

        Returns:
            True if connection event
        """
        return event.get("event_type") == EVENT_TYPE_CONNECTION

    @staticmethod
    def get_device_id_from_event(event: dict[str, Any]) -> str | None:
        """Extract device ID from event if available.

        Args:
            event: Parsed event dict

        Returns:
            Device ID or None
        """
        # Device ID might be in additional_data or source_name
        additional_data = event.get("additional_data", {})
        device_id = additional_data.get("deviceId") or additional_data.get("device_id")

        return device_id

    @staticmethod
    def should_trigger_fast_poll(event: dict[str, Any]) -> bool:
        """Determine if event should trigger fast polling.

        Args:
            event: Parsed event dict

        Returns:
            True if should fast poll
        """
        # Fast poll for:
        # - Alarm events
        # - Door/window opening
        # - Motion detection
        # - Malfunction events

        if AjaxEventParser.is_alarm_event(event):
            return True

        if AjaxEventParser.is_malfunction_event(event):
            return True

        action = event.get("action", "")
        if action in [
            "motion_detected",
            "door_opened",
            "external_contact_opened",
            "smoke_detected",
            "leak_detected",
            "glass_break_detected",
        ]:
            return True

        return False
