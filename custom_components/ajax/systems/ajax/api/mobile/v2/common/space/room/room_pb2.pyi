from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Room(_message.Message):
    __slots__ = ("id", "images", "name", "sorting_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    images: _image_pb2.Images
    sorting_key: str
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        images: _image_pb2.Images | _Mapping | None = ...,
        sorting_key: str | None = ...,
    ) -> None: ...
