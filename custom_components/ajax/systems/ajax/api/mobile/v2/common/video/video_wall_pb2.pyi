from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class VideoWall(_message.Message):
    __slots__ = ("visible",)
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    visible: bool
    def __init__(self, visible: bool = ...) -> None: ...
