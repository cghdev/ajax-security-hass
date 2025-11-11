from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class HubGroupPermission(_message.Message):
    __slots__ = ("group_id", "permissions")
    class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_PERMISSION_INFO: _ClassVar[HubGroupPermission.Permission]
        ARM: _ClassVar[HubGroupPermission.Permission]
        DISARM: _ClassVar[HubGroupPermission.Permission]

    NO_PERMISSION_INFO: HubGroupPermission.Permission
    ARM: HubGroupPermission.Permission
    DISARM: HubGroupPermission.Permission
    class Permissions(_message.Message):
        __slots__ = ("permissions",)
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        permissions: _containers.RepeatedScalarFieldContainer[
            HubGroupPermission.Permission
        ]
        def __init__(
            self,
            permissions: _Iterable[HubGroupPermission.Permission | str] | None = ...,
        ) -> None: ...

    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    permissions: HubGroupPermission.Permissions
    def __init__(
        self,
        group_id: str | None = ...,
        permissions: HubGroupPermission.Permissions | _Mapping | None = ...,
    ) -> None: ...

class HubGroupPermissions(_message.Message):
    __slots__ = ("hubGroupPermissions",)
    HUBGROUPPERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    hubGroupPermissions: _containers.RepeatedCompositeFieldContainer[HubGroupPermission]
    def __init__(
        self, hubGroupPermissions: _Iterable[HubGroupPermission | _Mapping] | None = ...
    ) -> None: ...
