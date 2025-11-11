from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.cloudarchive import (
    fragment_status_pb2 as _fragment_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveMetadataFragmentsContentResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("fragment_content",)
        FRAGMENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        fragment_content: (
            StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent
        )
        def __init__(
            self,
            fragment_content: StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent
            | _Mapping
            | None = ...,
        ) -> None: ...

    class FragmentContent(_message.Message):
        __slots__ = ("content_url", "fragment_id", "status", "tag")
        class Frames(_message.Message):
            __slots__ = ("entries",)
            ENTRIES_FIELD_NUMBER: _ClassVar[int]
            entries: _containers.RepeatedCompositeFieldContainer[
                StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent.Frame
            ]
            def __init__(
                self,
                entries: _Iterable[
                    StreamCloudArchiveMetadataFragmentsContentResponse.FragmentContent.Frame
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class Frame(_message.Message):
            __slots__ = ("data", "timestamp")
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            timestamp: int
            data: bytes
            def __init__(
                self, timestamp: int | None = ..., data: bytes | None = ...
            ) -> None: ...

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

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamCloudArchiveMetadataFragmentsContentResponse.Success
    failure: StreamCloudArchiveMetadataFragmentsContentResponse.Failure
    def __init__(
        self,
        success: StreamCloudArchiveMetadataFragmentsContentResponse.Success
        | _Mapping
        | None = ...,
        failure: StreamCloudArchiveMetadataFragmentsContentResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
