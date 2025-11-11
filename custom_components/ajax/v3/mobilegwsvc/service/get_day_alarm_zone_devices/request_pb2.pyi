from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class GetDayAlarmZoneDevicesRequest(_message.Message):
    __slots__ = ("day_alarm_zone_id", "hub_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    day_alarm_zone_id: str
    def __init__(
        self, hub_id: str | None = ..., day_alarm_zone_id: str | None = ...
    ) -> None: ...
