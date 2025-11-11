from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_id_pb2 as _image_id_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateAccountProfileRequest(_message.Message):
    __slots__ = ("first_name", "image", "last_name", "locale")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    locale: str
    image: _image_id_pb2.ImageIdValue
    def __init__(
        self,
        first_name: str | None = ...,
        last_name: str | None = ...,
        locale: str | None = ...,
        image: _image_id_pb2.ImageIdValue | _Mapping | None = ...,
    ) -> None: ...
