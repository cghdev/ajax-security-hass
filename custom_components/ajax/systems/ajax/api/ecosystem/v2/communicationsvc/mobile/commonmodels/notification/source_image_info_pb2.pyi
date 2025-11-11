from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SourceImageInfo(_message.Message):
    __slots__ = ("base_image_url",)
    BASE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    base_image_url: str
    def __init__(self, base_image_url: str | None = ...) -> None: ...
