from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FireZoneDeviceRepresentation(_message.Message):
    __slots__ = ("fire_zone_id_bound",)
    FIRE_ZONE_ID_BOUND_FIELD_NUMBER: _ClassVar[int]
    fire_zone_id_bound: int
    def __init__(self, fire_zone_id_bound: int | None = ...) -> None: ...
