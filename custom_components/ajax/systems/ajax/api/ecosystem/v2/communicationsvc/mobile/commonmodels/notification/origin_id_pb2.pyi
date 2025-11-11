from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationOriginId(_message.Message):
    __slots__ = ("hub_hex_id", "space_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    space_id: str
    def __init__(
        self, hub_hex_id: str | None = ..., space_id: str | None = ...
    ) -> None: ...
