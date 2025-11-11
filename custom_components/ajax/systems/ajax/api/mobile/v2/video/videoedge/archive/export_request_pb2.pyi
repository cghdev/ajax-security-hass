from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ExportArchiveRequest(_message.Message):
    __slots__ = (
        "channel_id",
        "export_ranges",
        "space_locator",
        "stream_type",
        "video_edge_id",
        "video_source_type",
        "with_audio",
        "with_figures",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    WITH_AUDIO_FIELD_NUMBER: _ClassVar[int]
    WITH_FIGURES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    export_ranges: _containers.RepeatedCompositeFieldContainer[
        _types_pb2.TimestampRange
    ]
    stream_type: _types_pb2.StreamType
    with_audio: bool
    with_figures: bool
    video_source_type: _types_pb2.VideoSourceType
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        export_ranges: _Iterable[_types_pb2.TimestampRange | _Mapping] | None = ...,
        stream_type: _types_pb2.StreamType | str | None = ...,
        with_audio: bool = ...,
        with_figures: bool = ...,
        video_source_type: _types_pb2.VideoSourceType | str | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class ExportArchiveResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("export_id",)
        EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
        export_id: str
        def __init__(self, export_id: str | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "archive_out_of_requested_time_range",
            "bad_request",
            "channel_not_found",
            "cloud_archive_not_found",
            "exports_limit_exceeded",
            "permission_denied",
            "too_many_parallel_exports",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        class ExportsLimitExceededError(_message.Message):
            __slots__ = ("timeout",)
            TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            timeout: _duration_pb2.Duration
            def __init__(
                self, timeout: _duration_pb2.Duration | _Mapping | None = ...
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        TOO_MANY_PARALLEL_EXPORTS_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_OUT_OF_REQUESTED_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        EXPORTS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        channel_not_found: _response_pb2.DefaultError
        too_many_parallel_exports: _response_pb2.DefaultError
        archive_out_of_requested_time_range: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        cloud_archive_not_found: _response_pb2.DefaultError
        exports_limit_exceeded: ExportArchiveResponse.Failure.ExportsLimitExceededError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            channel_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            too_many_parallel_exports: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            archive_out_of_requested_time_range: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            cloud_archive_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            exports_limit_exceeded: ExportArchiveResponse.Failure.ExportsLimitExceededError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ExportArchiveResponse.Success
    failure: ExportArchiveResponse.Failure
    def __init__(
        self,
        success: ExportArchiveResponse.Success | _Mapping | None = ...,
        failure: ExportArchiveResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
