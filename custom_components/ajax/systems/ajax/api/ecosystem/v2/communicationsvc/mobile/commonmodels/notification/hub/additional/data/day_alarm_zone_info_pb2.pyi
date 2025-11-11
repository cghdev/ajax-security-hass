from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DayAlarmZoneInfo(_message.Message):
    __slots__ = ("day_alarm_zone_id_hex", "day_alarm_zone_name")
    DAY_ALARM_ZONE_ID_HEX_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    day_alarm_zone_id_hex: str
    day_alarm_zone_name: str
    def __init__(
        self,
        day_alarm_zone_id_hex: str | None = ...,
        day_alarm_zone_name: str | None = ...,
    ) -> None: ...
