from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.localuser import (
    local_user_pb2 as _local_user_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeLocalUsersResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("local_users",)
        LOCAL_USERS_FIELD_NUMBER: _ClassVar[int]
        local_users: _containers.RepeatedCompositeFieldContainer[
            _local_user_pb2.LocalUser
        ]
        def __init__(
            self,
            local_users: _Iterable[_local_user_pb2.LocalUser | _Mapping] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "command_not_supported",
            "permission_denied",
            "space_armed",
            "space_not_found",
            "video_edge_is_offline",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        command_not_supported: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
            command_not_supported: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoEdgeLocalUsersResponse.Success
    failure: GetVideoEdgeLocalUsersResponse.Failure
    def __init__(
        self,
        success: GetVideoEdgeLocalUsersResponse.Success | _Mapping | None = ...,
        failure: GetVideoEdgeLocalUsersResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
