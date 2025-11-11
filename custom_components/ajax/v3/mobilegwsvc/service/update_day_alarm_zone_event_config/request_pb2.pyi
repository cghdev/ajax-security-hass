from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateDayAlarmZoneEventConfigRequest(_message.Message):
    __slots__ = ("event_config", "hub_hex_id")
    class DayAlarmZoneEventConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DAY_ALARM_ZONE_EVENT_CONFIG_UNSPECIFIED: _ClassVar[
            UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
        ]
        DAY_ALARM_ZONE_EVENT_CONFIG_CMS_OFF: _ClassVar[
            UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
        ]
        DAY_ALARM_ZONE_EVENT_CONFIG_CMS_ON: _ClassVar[
            UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
        ]

    DAY_ALARM_ZONE_EVENT_CONFIG_UNSPECIFIED: (
        UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
    )
    DAY_ALARM_ZONE_EVENT_CONFIG_CMS_OFF: (
        UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
    )
    DAY_ALARM_ZONE_EVENT_CONFIG_CMS_ON: (
        UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
    )
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    event_config: UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
    def __init__(
        self,
        hub_hex_id: str | None = ...,
        event_config: UpdateDayAlarmZoneEventConfigRequest.DayAlarmZoneEventConfig
        | str
        | None = ...,
    ) -> None: ...
