from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FireZoneId(_message.Message):
    __slots__ = ("fire_zone_id",)
    FIRE_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    fire_zone_id: str
    def __init__(self, fire_zone_id: str | None = ...) -> None: ...
