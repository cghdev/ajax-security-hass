from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteScheduledAccessRequest(_message.Message):
    __slots__ = ("hub_id", "id")
    ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    hub_id: str
    def __init__(self, id: int | None = ..., hub_id: str | None = ...) -> None: ...
