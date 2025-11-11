from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCrossZoneRequest(_message.Message):
    __slots__ = ("cross_zone_name", "hub_hex_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    CROSS_ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    cross_zone_name: str
    def __init__(
        self, hub_hex_id: str | None = ..., cross_zone_name: str | None = ...
    ) -> None: ...
