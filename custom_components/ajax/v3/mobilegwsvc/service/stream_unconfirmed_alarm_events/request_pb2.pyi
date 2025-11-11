from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class StreamUnconfirmedAlarmEventsRequest(_message.Message):
    __slots__ = ("parent_alarm_id", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ALARM_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    parent_alarm_id: str
    def __init__(
        self, space_id: str | None = ..., parent_alarm_id: str | None = ...
    ) -> None: ...
