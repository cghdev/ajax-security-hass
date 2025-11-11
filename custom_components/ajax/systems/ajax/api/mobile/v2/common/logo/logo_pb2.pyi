from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Logo(_message.Message):
    __slots__ = ("image_id", "images")
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
    def __init__(
        self,
        image_id: str | None = ...,
        images: _Iterable[_image_pb2.Image | _Mapping] | None = ...,
    ) -> None: ...
