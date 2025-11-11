from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class HubAlarmInfo(_message.Message):
    __slots__ = ("alarm_id",)
    ALARM_ID_FIELD_NUMBER: _ClassVar[int]
    alarm_id: str
    def __init__(self, alarm_id: str | None = ...) -> None: ...
