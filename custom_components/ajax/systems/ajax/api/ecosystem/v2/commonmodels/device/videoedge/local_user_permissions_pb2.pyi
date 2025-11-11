from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class LocalUserPermissions(_message.Message):
    __slots__ = ("admin", "operator")
    class LocalUserChannelPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCAL_USER_CHANNEL_PERMISSION_UNSPECIFIED: _ClassVar[
            LocalUserPermissions.LocalUserChannelPermission
        ]
        LOCAL_USER_CHANNEL_PERMISSION_VIEW_LIVE_STREAM: _ClassVar[
            LocalUserPermissions.LocalUserChannelPermission
        ]
        LOCAL_USER_CHANNEL_PERMISSION_VIEW_ARCHIVE: _ClassVar[
            LocalUserPermissions.LocalUserChannelPermission
        ]
        LOCAL_USER_CHANNEL_PERMISSION_PTZ: _ClassVar[
            LocalUserPermissions.LocalUserChannelPermission
        ]
        LOCAL_USER_CHANNEL_PERMISSION_SOUND: _ClassVar[
            LocalUserPermissions.LocalUserChannelPermission
        ]
        LOCAL_USER_CHANNEL_PERMISSION_EXPORT_ARCHIVE: _ClassVar[
            LocalUserPermissions.LocalUserChannelPermission
        ]

    LOCAL_USER_CHANNEL_PERMISSION_UNSPECIFIED: (
        LocalUserPermissions.LocalUserChannelPermission
    )
    LOCAL_USER_CHANNEL_PERMISSION_VIEW_LIVE_STREAM: (
        LocalUserPermissions.LocalUserChannelPermission
    )
    LOCAL_USER_CHANNEL_PERMISSION_VIEW_ARCHIVE: (
        LocalUserPermissions.LocalUserChannelPermission
    )
    LOCAL_USER_CHANNEL_PERMISSION_PTZ: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_SOUND: LocalUserPermissions.LocalUserChannelPermission
    LOCAL_USER_CHANNEL_PERMISSION_EXPORT_ARCHIVE: (
        LocalUserPermissions.LocalUserChannelPermission
    )
    class LocalUserAdminRole(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class LocalUserOperatorRole(_message.Message):
        __slots__ = ("channel_ids", "channel_permissions")
        CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        channel_ids: _containers.RepeatedScalarFieldContainer[str]
        channel_permissions: _containers.RepeatedScalarFieldContainer[
            LocalUserPermissions.LocalUserChannelPermission
        ]
        def __init__(
            self,
            channel_ids: _Iterable[str] | None = ...,
            channel_permissions: _Iterable[
                LocalUserPermissions.LocalUserChannelPermission | str
            ]
            | None = ...,
        ) -> None: ...

    ADMIN_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    admin: LocalUserPermissions.LocalUserAdminRole
    operator: LocalUserPermissions.LocalUserOperatorRole
    def __init__(
        self,
        admin: LocalUserPermissions.LocalUserAdminRole | _Mapping | None = ...,
        operator: LocalUserPermissions.LocalUserOperatorRole | _Mapping | None = ...,
    ) -> None: ...
