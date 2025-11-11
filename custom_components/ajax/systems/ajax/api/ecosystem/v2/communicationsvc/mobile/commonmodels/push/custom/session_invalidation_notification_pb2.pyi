from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SessionInvalidation(_message.Message):
    __slots__ = ("sessionId",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: int
    def __init__(self, sessionId: int | None = ...) -> None: ...
