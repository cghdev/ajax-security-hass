from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_pb2 as _smart_lock_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AddSmartLockByExternalIdRequest(_message.Message):
    __slots__ = (
        "external_smart_lock_id",
        "group_id",
        "name",
        "room_id",
        "space_id",
        "type",
    )
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    room_id: str
    external_smart_lock_id: str
    type: _smart_lock_pb2.SmartLockType
    name: str
    group_id: str
    def __init__(
        self,
        space_id: str | None = ...,
        room_id: str | None = ...,
        external_smart_lock_id: str | None = ...,
        type: _smart_lock_pb2.SmartLockType | str | None = ...,
        name: str | None = ...,
        group_id: str | None = ...,
    ) -> None: ...

class AddSmartLockByExternalIdResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "external_service_access_denied",
            "group_not_found",
            "members_limit_exceeded",
            "permission_denied",
            "room_not_found",
            "smart_lock_already_added_by_another_space_member",
            "smart_lock_not_found",
            "smart_lock_offline",
            "smart_lock_without_group",
            "space_armed",
            "space_not_found",
        )
        EXTERNAL_SERVICE_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_ALREADY_ADDED_BY_ANOTHER_SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_WITHOUT_GROUP_FIELD_NUMBER: _ClassVar[int]
        external_service_access_denied: _response_pb2.DefaultError
        bad_request: _response_pb2.DefaultError
        smart_lock_not_found: _response_pb2.DefaultError
        smart_lock_already_added_by_another_space_member: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        smart_lock_offline: _response_pb2.DefaultError
        members_limit_exceeded: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        smart_lock_without_group: _response_pb2.DefaultError
        def __init__(
            self,
            external_service_access_denied: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            smart_lock_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            smart_lock_already_added_by_another_space_member: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            room_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            smart_lock_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            members_limit_exceeded: _response_pb2.DefaultError | _Mapping | None = ...,
            group_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            smart_lock_without_group: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: AddSmartLockByExternalIdResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: AddSmartLockByExternalIdResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
