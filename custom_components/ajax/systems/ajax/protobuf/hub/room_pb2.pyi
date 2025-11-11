from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Room(_message.Message):
    __slots__ = ("id", "image_id", "image_urls", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    id: str
    image_id: str
    name: _name_pb2.Name
    image_urls: _image_urls_pb2.ImageUrls
    def __init__(
        self,
        id: str | None = ...,
        image_id: str | None = ...,
        name: _name_pb2.Name | _Mapping | None = ...,
        image_urls: _image_urls_pb2.ImageUrls | _Mapping | None = ...,
    ) -> None: ...
