from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space.member import (
    space_permission_pb2 as _space_permission_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SpacePermissions(_message.Message):
    __slots__ = ("expiredAt", "has_system_settings_permissions", "permissions")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_SYSTEM_SETTINGS_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXPIREDAT_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[
        _space_permission_pb2.SpacePermission
    ]
    has_system_settings_permissions: bool
    expiredAt: _timestamp_pb2.Timestamp
    def __init__(
        self,
        permissions: _Iterable[_space_permission_pb2.SpacePermission | str]
        | None = ...,
        has_system_settings_permissions: bool = ...,
        expiredAt: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...
