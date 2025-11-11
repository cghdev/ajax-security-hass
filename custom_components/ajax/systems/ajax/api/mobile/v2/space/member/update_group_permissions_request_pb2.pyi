from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    group_permissions_pb2 as _group_permissions_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberGroupPermissionsRequest(_message.Message):
    __slots__ = ("space_locator", "space_members_group_permissions")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBERS_GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    space_members_group_permissions: _containers.RepeatedCompositeFieldContainer[
        SpaceMemberGroupPermissions
    ]
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        space_members_group_permissions: _Iterable[
            SpaceMemberGroupPermissions | _Mapping
        ]
        | None = ...,
    ) -> None: ...

class SpaceMemberGroupPermissions(_message.Message):
    __slots__ = ("group_permissions", "space_member_id")
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_member_id: str
    group_permissions: _containers.RepeatedCompositeFieldContainer[
        _group_permissions_pb2.GroupPermissions
    ]
    def __init__(
        self,
        space_member_id: str | None = ...,
        group_permissions: _Iterable[_group_permissions_pb2.GroupPermissions | _Mapping]
        | None = ...,
    ) -> None: ...

class UpdateSpaceMemberGroupPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "group_not_found",
            "hub_error",
            "hub_is_offline",
            "hub_wrong_state",
            "member_not_found",
            "permission_denied",
            "space_armed",
            "space_locked",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        member_not_found: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        hub_is_offline: _response_pb2.DefaultError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            member_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            group_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSpaceMemberGroupPermissionsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: UpdateSpaceMemberGroupPermissionsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
