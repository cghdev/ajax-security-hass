from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SessionDescription(_message.Message):
    __slots__ = ("sdp", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    type: str
    sdp: str
    def __init__(self, type: str | None = ..., sdp: str | None = ...) -> None: ...
