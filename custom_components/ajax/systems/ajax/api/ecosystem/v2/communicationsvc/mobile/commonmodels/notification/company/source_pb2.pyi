from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    member_type_pb2 as _member_type_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    source_image_info_pb2 as _source_image_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company import (
    source_type_pb2 as _source_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyNotificationSource(_message.Message):
    __slots__ = ("id", "image_info", "member_type", "name", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.CompanyNotificationSourceType
    id: str
    name: str
    image_info: _source_image_info_pb2.SourceImageInfo
    member_type: _member_type_pb2.MemberType
    def __init__(
        self,
        type: _source_type_pb2.CompanyNotificationSourceType | str | None = ...,
        id: str | None = ...,
        name: str | None = ...,
        image_info: _source_image_info_pb2.SourceImageInfo | _Mapping | None = ...,
        member_type: _member_type_pb2.MemberType | str | None = ...,
    ) -> None: ...
