from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveTzEntry(_message.Message):
    __slots__ = ("ts", "tz_offset")
    TS_FIELD_NUMBER: _ClassVar[int]
    TZ_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ts: int
    tz_offset: int
    def __init__(self, ts: int | None = ..., tz_offset: int | None = ...) -> None: ...
