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

DESCRIPTOR: _descriptor.FileDescriptor

class InstallVideoEdgeRequest(_message.Message):
    __slots__ = (
        "default_channel_group_id",
        "room_id",
        "space_locator",
        "video_edge_id",
        "video_edge_name",
        "video_edge_qr_code",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANNEL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    video_edge_name: str
    room_id: str
    default_channel_group_id: str
    video_edge_qr_code: str
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_id: str | None = ...,
        video_edge_name: str | None = ...,
        room_id: str | None = ...,
        default_channel_group_id: str | None = ...,
        video_edge_qr_code: str | None = ...,
    ) -> None: ...

class InstallVideoEdgeResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("channel_ids", "video_edge_id")
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            video_edge_id: str | None = ...,
            channel_ids: _Iterable[str] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "group_not_found",
            "permission_denied",
            "role_access_required",
            "room_not_found",
            "space_armed",
            "space_locked",
            "space_not_found",
            "video_edge_is_already_installed",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_ALREADY_INSTALLED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        ROLE_ACCESS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_is_already_installed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        group_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        role_access_required: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_is_already_installed: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            room_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            group_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            role_access_required: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InstallVideoEdgeResponse.Success
    failure: InstallVideoEdgeResponse.Failure
    def __init__(
        self,
        success: InstallVideoEdgeResponse.Success | _Mapping | None = ...,
        failure: InstallVideoEdgeResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
