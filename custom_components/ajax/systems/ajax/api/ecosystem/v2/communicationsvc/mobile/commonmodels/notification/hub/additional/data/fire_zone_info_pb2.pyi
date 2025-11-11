from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FireZoneInfo(_message.Message):
    __slots__ = ("fire_zone_id_hex", "fire_zone_name")
    FIRE_ZONE_ID_HEX_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    fire_zone_id_hex: str
    fire_zone_name: str
    def __init__(
        self, fire_zone_id_hex: str | None = ..., fire_zone_name: str | None = ...
    ) -> None: ...
