from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareVersion(_message.Message):
    __slots__ = ("extra", "major", "minor")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    extra: str
    def __init__(
        self, major: int | None = ..., minor: int | None = ..., extra: str | None = ...
    ) -> None: ...
