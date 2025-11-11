from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ImageUrls(_message.Message):
    __slots__ = ("base_path", "big", "medium", "small")
    SMALL_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    BIG_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    small: str
    medium: str
    big: str
    base_path: str
    def __init__(
        self,
        small: str | None = ...,
        medium: str | None = ...,
        big: str | None = ...,
        base_path: str | None = ...,
    ) -> None: ...
