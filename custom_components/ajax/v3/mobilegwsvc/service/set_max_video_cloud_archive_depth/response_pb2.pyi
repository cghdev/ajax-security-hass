from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SetMaxVideoCloudArchiveDepthResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("cloud_archive_depth",)
        CLOUD_ARCHIVE_DEPTH_FIELD_NUMBER: _ClassVar[int]
        cloud_archive_depth: _duration_pb2.Duration
        def __init__(
            self, cloud_archive_depth: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "cloud_archive_not_found",
            "max_cloud_archive_depth_limit_exceeded",
            "permission_denied",
            "space_armed",
            "space_not_found",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        MAX_CLOUD_ARCHIVE_DEPTH_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        cloud_archive_not_found: _response_pb2.Error
        max_cloud_archive_depth_limit_exceeded: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            cloud_archive_not_found: _response_pb2.Error | _Mapping | None = ...,
            max_cloud_archive_depth_limit_exceeded: _response_pb2.Error
            | _Mapping
            | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetMaxVideoCloudArchiveDepthResponse.Success
    failure: SetMaxVideoCloudArchiveDepthResponse.Failure
    def __init__(
        self,
        success: SetMaxVideoCloudArchiveDepthResponse.Success | _Mapping | None = ...,
        failure: SetMaxVideoCloudArchiveDepthResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
