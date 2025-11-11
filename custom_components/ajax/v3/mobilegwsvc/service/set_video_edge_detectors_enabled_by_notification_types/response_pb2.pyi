from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeDetectorsEnabledByNotificationTypesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "permission_denied",
            "some_detectors_failed_to_update",
            "space_armed",
            "space_not_found",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SOME_DETECTORS_FAILED_TO_UPDATE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        space_not_found: _response_pb2.Error
        some_detectors_failed_to_update: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            some_detectors_failed_to_update: _response_pb2.Error
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SetVideoEdgeDetectorsEnabledByNotificationTypesResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: SetVideoEdgeDetectorsEnabledByNotificationTypesResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
