from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDayAlarmZoneRequest(_message.Message):
    __slots__ = ("hub_id", "name")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    name: str
    def __init__(self, hub_id: str | None = ..., name: str | None = ...) -> None: ...
