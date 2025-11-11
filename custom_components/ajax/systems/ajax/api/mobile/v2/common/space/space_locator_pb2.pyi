from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceLocator(_message.Message):
    __slots__ = ("hub_id", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    hub_id: str
    def __init__(
        self, space_id: str | None = ..., hub_id: str | None = ...
    ) -> None: ...
