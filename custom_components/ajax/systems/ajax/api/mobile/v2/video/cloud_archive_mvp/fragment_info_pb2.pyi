from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveFragmentInfo(_message.Message):
    __slots__ = ("duration", "fragment_id", "ts")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    fragment_id: int
    ts: int
    duration: int
    def __init__(
        self,
        fragment_id: int | None = ...,
        ts: int | None = ...,
        duration: int | None = ...,
    ) -> None: ...
