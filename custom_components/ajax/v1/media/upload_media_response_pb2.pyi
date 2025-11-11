from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from v1.common import image_pb2 as _image_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UploadMediaResponse(_message.Message):
    __slots__ = ("expiration_time", "image_id", "images")
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
    expiration_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        image_id: str | None = ...,
        images: _Iterable[_image_pb2.Image | _Mapping] | None = ...,
        expiration_time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...
