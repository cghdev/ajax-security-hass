from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceLocationInfo(_message.Message):
    __slots__ = ("device_location",)
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    device_location: str
    def __init__(self, device_location: str | None = ...) -> None: ...
