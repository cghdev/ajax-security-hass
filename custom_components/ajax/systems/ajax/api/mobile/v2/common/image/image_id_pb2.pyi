from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ImageIdValue(_message.Message):
    __slots__ = ("image_id",)
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    def __init__(self, image_id: str | None = ...) -> None: ...
