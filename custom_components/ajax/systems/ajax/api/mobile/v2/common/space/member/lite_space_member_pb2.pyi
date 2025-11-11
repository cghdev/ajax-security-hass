from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.space.member import (
    space_member_role_pb2 as _space_member_role_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LiteSpaceMember(_message.Message):
    __slots__ = (
        "email",
        "has_privacy_permission",
        "hex_id",
        "id",
        "images",
        "name",
        "role",
        "sorting_key",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_PRIVACY_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    email: str
    role: _space_member_role_pb2.SpaceMemberRole
    images: _image_pb2.Images
    has_privacy_permission: bool
    sorting_key: str
    hex_id: str
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        email: str | None = ...,
        role: _space_member_role_pb2.SpaceMemberRole | str | None = ...,
        images: _image_pb2.Images | _Mapping | None = ...,
        has_privacy_permission: bool = ...,
        sorting_key: str | None = ...,
        hex_id: str | None = ...,
    ) -> None: ...
