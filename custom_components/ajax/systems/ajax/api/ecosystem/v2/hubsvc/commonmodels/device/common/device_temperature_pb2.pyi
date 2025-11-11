from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTemperature(_message.Message):
    __slots__ = ("is_extreme", "value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_EXTREME_FIELD_NUMBER: _ClassVar[int]
    value: int
    is_extreme: bool
    def __init__(self, value: int | None = ..., is_extreme: bool = ...) -> None: ...
