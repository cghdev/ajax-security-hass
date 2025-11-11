from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteCrossZoneRequest(_message.Message):
    __slots__ = ("cross_zone_id", "hub_hex_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    CROSS_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    cross_zone_id: str
    def __init__(
        self, hub_hex_id: str | None = ..., cross_zone_id: str | None = ...
    ) -> None: ...
