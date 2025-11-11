from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.member import (
    display_member_permissions_pb2 as _display_member_permissions_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberPermissionsRequest(_message.Message):
    __slots__ = ("member_id", "space_id", "update")
    class PermissionsUpdate(_message.Message):
        __slots__ = (
            "hub_permission_extended_patch",
            "hub_permission_patch",
            "space_permission_patch",
        )
        class HubPermissionPatch(_message.Message):
            __slots__ = ("enabled", "permission")
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            permission: _display_member_permissions_pb2.DisplaySpaceMemberHubPermission
            enabled: bool
            def __init__(
                self,
                permission: _display_member_permissions_pb2.DisplaySpaceMemberHubPermission
                | str
                | None = ...,
                enabled: bool = ...,
            ) -> None: ...

        class SpacePermissionPatch(_message.Message):
            __slots__ = ("enabled", "permission")
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            permission: (
                _display_member_permissions_pb2.DisplaySpaceMemberSpacePermission
            )
            enabled: bool
            def __init__(
                self,
                permission: _display_member_permissions_pb2.DisplaySpaceMemberSpacePermission
                | str
                | None = ...,
                enabled: bool = ...,
            ) -> None: ...

        class HubPermissionExtendedPatch(_message.Message):
            __slots__ = ("enabled", "permission")
            PERMISSION_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            permission: (
                _display_member_permissions_pb2.DisplaySpaceMemberHubPermissionExtended
            )
            enabled: bool
            def __init__(
                self,
                permission: _display_member_permissions_pb2.DisplaySpaceMemberHubPermissionExtended
                | str
                | None = ...,
                enabled: bool = ...,
            ) -> None: ...

        SPACE_PERMISSION_PATCH_FIELD_NUMBER: _ClassVar[int]
        HUB_PERMISSION_PATCH_FIELD_NUMBER: _ClassVar[int]
        HUB_PERMISSION_EXTENDED_PATCH_FIELD_NUMBER: _ClassVar[int]
        space_permission_patch: _containers.RepeatedCompositeFieldContainer[
            UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.SpacePermissionPatch
        ]
        hub_permission_patch: _containers.RepeatedCompositeFieldContainer[
            UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionPatch
        ]
        hub_permission_extended_patch: _containers.RepeatedCompositeFieldContainer[
            UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionExtendedPatch
        ]
        def __init__(
            self,
            space_permission_patch: _Iterable[
                UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.SpacePermissionPatch
                | _Mapping
            ]
            | None = ...,
            hub_permission_patch: _Iterable[
                UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionPatch
                | _Mapping
            ]
            | None = ...,
            hub_permission_extended_patch: _Iterable[
                UpdateSpaceMemberPermissionsRequest.PermissionsUpdate.HubPermissionExtendedPatch
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    member_id: str
    update: UpdateSpaceMemberPermissionsRequest.PermissionsUpdate
    def __init__(
        self,
        space_id: str | None = ...,
        member_id: str | None = ...,
        update: UpdateSpaceMemberPermissionsRequest.PermissionsUpdate
        | _Mapping
        | None = ...,
    ) -> None: ...

class UpdateSpaceMemberPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateSpaceMemberPermissionsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: UpdateSpaceMemberPermissionsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
