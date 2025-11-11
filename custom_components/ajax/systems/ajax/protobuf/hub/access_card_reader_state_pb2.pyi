from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCardReaderState(_message.Message):
    __slots__ = ("id", "reader_active", "timeout_seconds")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    READER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    timeout_seconds: int
    reader_active: bool
    def __init__(
        self,
        id: str | None = ...,
        timeout_seconds: int | None = ...,
        reader_active: bool = ...,
    ) -> None: ...
