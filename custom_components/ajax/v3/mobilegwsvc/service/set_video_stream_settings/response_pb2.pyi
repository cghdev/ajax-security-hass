from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoStreamSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "device_setup_in_progress",
            "device_unavailable",
            "permission_denied",
            "space_armed",
            "space_not_found",
            "stream_settings_not_found",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        STREAM_SETTINGS_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SETUP_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        stream_settings_not_found: _response_pb2.Error
        device_unavailable: _response_pb2.Error
        device_setup_in_progress: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
            stream_settings_not_found: _response_pb2.Error | _Mapping | None = ...,
            device_unavailable: _response_pb2.Error | _Mapping | None = ...,
            device_setup_in_progress: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SetVideoStreamSettingsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: SetVideoStreamSettingsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
