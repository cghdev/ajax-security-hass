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
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space import (
    source_type_pb2 as _source_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceNotificationSource(_message.Message):
    __slots__ = (
        "id",
        "image_info",
        "member_type",
        "name",
        "room_id",
        "room_name",
        "type",
    )
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.SpaceNotificationSourceType
    id: str
    name: str
    room_id: str
    room_name: str
    member_type: _member_type_pb2.MemberType
    image_info: _source_image_info_pb2.SourceImageInfo
    def __init__(
        self,
        type: _source_type_pb2.SpaceNotificationSourceType | str | None = ...,
        id: str | None = ...,
        name: str | None = ...,
        room_id: str | None = ...,
        room_name: str | None = ...,
        member_type: _member_type_pb2.MemberType | str | None = ...,
        image_info: _source_image_info_pb2.SourceImageInfo | _Mapping | None = ...,
    ) -> None: ...
