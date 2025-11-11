from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Decimal(_message.Message):
    __slots__ = ("scale", "unscaledBytes")
    SCALE_FIELD_NUMBER: _ClassVar[int]
    UNSCALEDBYTES_FIELD_NUMBER: _ClassVar[int]
    scale: int
    unscaledBytes: bytes
    def __init__(
        self, scale: int | None = ..., unscaledBytes: bytes | None = ...
    ) -> None: ...
