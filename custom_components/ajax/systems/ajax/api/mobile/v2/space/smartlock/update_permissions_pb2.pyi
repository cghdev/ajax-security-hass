from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_device_permissions_pb2 as _smart_lock_device_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_permission_pb2 as _smart_lock_permission_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockPermissionsRequest(_message.Message):
    __slots__ = ("assignee_space_member_id", "smart_lock_id", "space_id", "updates")
    class Update(_message.Message):
        __slots__ = ("enabled", "permission", "type")
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        permission: _smart_lock_permission_pb2.SmartLockPermission
        enabled: bool
        type: (
            _smart_lock_device_permissions_pb2.SmartLockPermissions.PermissionState.Type
        )
        def __init__(
            self,
            permission: _smart_lock_permission_pb2.SmartLockPermission
            | str
            | None = ...,
            enabled: bool = ...,
            type: _smart_lock_device_permissions_pb2.SmartLockPermissions.PermissionState.Type
            | _Mapping
            | None = ...,
        ) -> None: ...

    ASSIGNEE_SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    assignee_space_member_id: str
    space_id: str
    smart_lock_id: str
    updates: _containers.RepeatedCompositeFieldContainer[
        UpdateSmartLockPermissionsRequest.Update
    ]
    def __init__(
        self,
        assignee_space_member_id: str | None = ...,
        space_id: str | None = ...,
        smart_lock_id: str | None = ...,
        updates: _Iterable[UpdateSmartLockPermissionsRequest.Update | _Mapping]
        | None = ...,
    ) -> None: ...

class UpdateSmartLockPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "member_not_found",
            "message",
            "permission_denied",
            "smart_lock_not_found",
            "space_armed",
            "space_not_found",
        )
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        smart_lock_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        member_not_found: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            smart_lock_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            member_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSmartLockPermissionsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: UpdateSmartLockPermissionsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
