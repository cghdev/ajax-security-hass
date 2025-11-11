from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_permission_pb2 as _smart_lock_permission_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockPermissions(_message.Message):
    __slots__ = ("device_id", "permissions", "smart_lock_permissions")
    class PermissionState(_message.Message):
        __slots__ = ("permission", "type")
        class Type(_message.Message):
            __slots__ = ("permanent", "temporary_when_alert_received")
            class Permanent(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            class TemporaryWhenAlertReceived(_message.Message):
                __slots__ = ("duration", "expired_at")
                DURATION_FIELD_NUMBER: _ClassVar[int]
                EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
                duration: _duration_pb2.Duration
                expired_at: _timestamp_pb2.Timestamp
                def __init__(
                    self,
                    duration: _duration_pb2.Duration | _Mapping | None = ...,
                    expired_at: _timestamp_pb2.Timestamp | _Mapping | None = ...,
                ) -> None: ...

            PERMANENT_FIELD_NUMBER: _ClassVar[int]
            TEMPORARY_WHEN_ALERT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
            permanent: SmartLockPermissions.PermissionState.Type.Permanent
            temporary_when_alert_received: (
                SmartLockPermissions.PermissionState.Type.TemporaryWhenAlertReceived
            )
            def __init__(
                self,
                permanent: SmartLockPermissions.PermissionState.Type.Permanent
                | _Mapping
                | None = ...,
                temporary_when_alert_received: SmartLockPermissions.PermissionState.Type.TemporaryWhenAlertReceived
                | _Mapping
                | None = ...,
            ) -> None: ...

        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        permission: _smart_lock_permission_pb2.SmartLockPermission
        type: SmartLockPermissions.PermissionState.Type
        def __init__(
            self,
            permission: _smart_lock_permission_pb2.SmartLockPermission
            | str
            | None = ...,
            type: SmartLockPermissions.PermissionState.Type | _Mapping | None = ...,
        ) -> None: ...

    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    smart_lock_permissions: _containers.RepeatedScalarFieldContainer[
        _smart_lock_permission_pb2.SmartLockPermission
    ]
    permissions: _containers.RepeatedCompositeFieldContainer[
        SmartLockPermissions.PermissionState
    ]
    def __init__(
        self,
        device_id: str | None = ...,
        smart_lock_permissions: _Iterable[
            _smart_lock_permission_pb2.SmartLockPermission | str
        ]
        | None = ...,
        permissions: _Iterable[SmartLockPermissions.PermissionState | _Mapping]
        | None = ...,
    ) -> None: ...
