from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.cloudarchive import (
    fragment_status_pb2 as _fragment_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveVideoFragmentsContentResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("fragment_content", "fragment_part_content", "init")
        FRAGMENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_PART_CONTENT_FIELD_NUMBER: _ClassVar[int]
        INIT_FIELD_NUMBER: _ClassVar[int]
        fragment_content: (
            StreamCloudArchiveVideoFragmentsContentResponse.FragmentContent
        )
        fragment_part_content: (
            StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent
        )
        init: StreamCloudArchiveVideoFragmentsContentResponse.Init
        def __init__(
            self,
            fragment_content: StreamCloudArchiveVideoFragmentsContentResponse.FragmentContent
            | _Mapping
            | None = ...,
            fragment_part_content: StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent
            | _Mapping
            | None = ...,
            init: StreamCloudArchiveVideoFragmentsContentResponse.Init
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Init(_message.Message):
        __slots__ = ("playback_duration_interval",)
        PLAYBACK_DURATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        playback_duration_interval: _duration_pb2.Duration
        def __init__(
            self,
            playback_duration_interval: _duration_pb2.Duration | _Mapping | None = ...,
        ) -> None: ...

    class FragmentContent(_message.Message):
        __slots__ = ("content_url", "fragment_id", "status", "tag")
        TAG_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        tag: str
        fragment_id: int
        status: _fragment_status_pb2.FragmentStatus
        content_url: str
        def __init__(
            self,
            tag: str | None = ...,
            fragment_id: int | None = ...,
            status: _fragment_status_pb2.FragmentStatus | str | None = ...,
            content_url: str | None = ...,
        ) -> None: ...

    class FragmentPartContent(_message.Message):
        __slots__ = (
            "content_url",
            "content_url_headers",
            "fragment_id",
            "offset",
            "status",
            "tag",
        )
        class Header(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: str | None = ..., value: str | None = ...
            ) -> None: ...

        TAG_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_URL_HEADERS_FIELD_NUMBER: _ClassVar[int]
        tag: str
        fragment_id: int
        offset: int
        status: _fragment_status_pb2.FragmentStatus
        content_url: str
        content_url_headers: _containers.RepeatedCompositeFieldContainer[
            StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent.Header
        ]
        def __init__(
            self,
            tag: str | None = ...,
            fragment_id: int | None = ...,
            offset: int | None = ...,
            status: _fragment_status_pb2.FragmentStatus | str | None = ...,
            content_url: str | None = ...,
            content_url_headers: _Iterable[
                StreamCloudArchiveVideoFragmentsContentResponse.FragmentPartContent.Header
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "cloud_archive_not_found",
            "permission_denied",
            "playback_limit_exceeded",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        playback_limit_exceeded: _response_pb2.Error
        cloud_archive_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            playback_limit_exceeded: _response_pb2.Error | _Mapping | None = ...,
            cloud_archive_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamCloudArchiveVideoFragmentsContentResponse.Success
    failure: StreamCloudArchiveVideoFragmentsContentResponse.Failure
    def __init__(
        self,
        success: StreamCloudArchiveVideoFragmentsContentResponse.Success
        | _Mapping
        | None = ...,
        failure: StreamCloudArchiveVideoFragmentsContentResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
