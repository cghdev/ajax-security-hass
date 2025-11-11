from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class KeyarmLock(_message.Message):
    __slots__ = ("keyarm_id",)
    KEYARM_ID_FIELD_NUMBER: _ClassVar[int]
    keyarm_id: int
    def __init__(self, keyarm_id: int | None = ...) -> None: ...
