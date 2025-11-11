from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2_1
from systems.ajax.api.mobile.v2.common.space.security.group import (
    group_pb2 as _group_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableFollowedGroupsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("groups",)
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
        def __init__(
            self, groups: _Iterable[_group_pb2.Group | _Mapping] | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_armed", "space_locked")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_locked: _response_pb2_1.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            space_locked: _response_pb2_1.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAvailableFollowedGroupsResponse.Success
    failure: GetAvailableFollowedGroupsResponse.Failure
    def __init__(
        self,
        success: GetAvailableFollowedGroupsResponse.Success | _Mapping | None = ...,
        failure: GetAvailableFollowedGroupsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
