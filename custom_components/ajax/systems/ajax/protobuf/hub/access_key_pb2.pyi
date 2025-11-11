from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class AccessKeyUpdate(_message.Message):
    __slots__ = ("keyId",)
    KEYID_FIELD_NUMBER: _ClassVar[int]
    keyId: str
    def __init__(self, keyId: str | None = ...) -> None: ...
