from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class StorageDevicePortNumber(_message.Message):
    __slots__ = ("actual_number", "display_number")
    ACTUAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    actual_number: int
    display_number: int
    def __init__(
        self, actual_number: int | None = ..., display_number: int | None = ...
    ) -> None: ...
