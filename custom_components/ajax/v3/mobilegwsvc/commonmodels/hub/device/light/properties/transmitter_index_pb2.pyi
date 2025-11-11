from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class TransmitterIndex(_message.Message):
    __slots__ = ("transmitter_index",)
    TRANSMITTER_INDEX_FIELD_NUMBER: _ClassVar[int]
    transmitter_index: int
    def __init__(self, transmitter_index: int | None = ...) -> None: ...
