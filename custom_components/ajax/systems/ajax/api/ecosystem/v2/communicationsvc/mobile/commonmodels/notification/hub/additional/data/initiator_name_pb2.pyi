from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorName(_message.Message):
    __slots__ = ("initiator_name",)
    INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    initiator_name: str
    def __init__(self, initiator_name: str | None = ...) -> None: ...
