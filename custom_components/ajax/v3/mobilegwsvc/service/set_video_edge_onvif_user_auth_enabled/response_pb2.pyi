from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import (
    onvif_settings_pb2 as _onvif_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeOnvifUserAuthEnabledResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("settings",)
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        settings: _onvif_settings_pb2.OnvifSettings
        def __init__(
            self, settings: _onvif_settings_pb2.OnvifSettings | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "space_armed",
            "space_not_found",
            "unimplemented_video_edge_command",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
            unimplemented_video_edge_command: _response_pb2.Error
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetVideoEdgeOnvifUserAuthEnabledResponse.Success
    failure: SetVideoEdgeOnvifUserAuthEnabledResponse.Failure
    def __init__(
        self,
        success: SetVideoEdgeOnvifUserAuthEnabledResponse.Success
        | _Mapping
        | None = ...,
        failure: SetVideoEdgeOnvifUserAuthEnabledResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
