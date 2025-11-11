from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteDayAlarmZoneRequest(_message.Message):
    __slots__ = ("hub_id", "id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    id: str
    def __init__(self, hub_id: str | None = ..., id: str | None = ...) -> None: ...
