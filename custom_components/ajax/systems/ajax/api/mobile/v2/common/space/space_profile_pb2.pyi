from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceProfile(_message.Message):
    __slots__ = ("images", "name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    images: _image_pb2.Images
    def __init__(
        self, name: str | None = ..., images: _image_pb2.Images | _Mapping | None = ...
    ) -> None: ...
