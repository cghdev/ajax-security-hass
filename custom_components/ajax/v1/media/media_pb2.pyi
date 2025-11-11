from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v1.common import image_pb2 as _image_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Media(_message.Message):
    __slots__ = ("images", "info")
    class Info(_message.Message):
        __slots__ = ("caption", "category", "facility_id", "id", "image_id")
        class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ROAD_MAP: _ClassVar[Media.Info.Category]
            FLOOR_PLAN: _ClassVar[Media.Info.Category]

        ROAD_MAP: Media.Info.Category
        FLOOR_PLAN: Media.Info.Category
        ID_FIELD_NUMBER: _ClassVar[int]
        FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
        CAPTION_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        id: str
        facility_id: str
        image_id: str
        caption: str
        category: Media.Info.Category
        def __init__(
            self,
            id: str | None = ...,
            facility_id: str | None = ...,
            image_id: str | None = ...,
            caption: str | None = ...,
            category: Media.Info.Category | str | None = ...,
        ) -> None: ...

    INFO_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    info: Media.Info
    images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
    def __init__(
        self,
        info: Media.Info | _Mapping | None = ...,
        images: _Iterable[_image_pb2.Image | _Mapping] | None = ...,
    ) -> None: ...
