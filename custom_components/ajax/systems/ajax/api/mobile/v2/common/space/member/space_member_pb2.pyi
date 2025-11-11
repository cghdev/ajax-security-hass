from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.space.member import (
    display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    display_member_permissions_pb2 as _display_member_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    group_permissions_pb2 as _group_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    space_member_role_pb2 as _space_member_role_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    space_permissions_pb2 as _space_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    standalone_device_permissions_pb2 as _standalone_device_permissions_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMember(_message.Message):
    __slots__ = (
        "devices_permissions",
        "display_member_notification_preferences",
        "display_member_permissions",
        "email",
        "group_permissions",
        "hex_id",
        "id",
        "images",
        "name",
        "role",
        "sorting_key",
        "space_permissions",
        "user_index",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MEMBER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MEMBER_NOTIFICATION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    space_permissions: _space_permissions_pb2.SpacePermissions
    devices_permissions: _containers.RepeatedCompositeFieldContainer[
        _standalone_device_permissions_pb2.StandaloneDevicePermissions
    ]
    name: str
    email: str
    role: _space_member_role_pb2.SpaceMemberRole
    group_permissions: _containers.RepeatedCompositeFieldContainer[
        _group_permissions_pb2.GroupPermissions
    ]
    display_member_permissions: _display_member_permissions_pb2.DisplayMemberPermissions
    user_index: int
    display_member_notification_preferences: _display_member_notification_preferences_pb2.DisplayMemberNotificationPreferences
    images: _image_pb2.Images
    sorting_key: str
    hex_id: str
    def __init__(
        self,
        id: str | None = ...,
        space_permissions: _space_permissions_pb2.SpacePermissions
        | _Mapping
        | None = ...,
        devices_permissions: _Iterable[
            _standalone_device_permissions_pb2.StandaloneDevicePermissions | _Mapping
        ]
        | None = ...,
        name: str | None = ...,
        email: str | None = ...,
        role: _space_member_role_pb2.SpaceMemberRole | str | None = ...,
        group_permissions: _Iterable[_group_permissions_pb2.GroupPermissions | _Mapping]
        | None = ...,
        display_member_permissions: _display_member_permissions_pb2.DisplayMemberPermissions
        | _Mapping
        | None = ...,
        user_index: int | None = ...,
        display_member_notification_preferences: _display_member_notification_preferences_pb2.DisplayMemberNotificationPreferences
        | _Mapping
        | None = ...,
        images: _image_pb2.Images | _Mapping | None = ...,
        sorting_key: str | None = ...,
        hex_id: str | None = ...,
    ) -> None: ...
