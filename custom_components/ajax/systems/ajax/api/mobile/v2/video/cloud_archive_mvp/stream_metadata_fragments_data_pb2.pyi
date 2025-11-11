from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import (
    fragment_error_pb2 as _fragment_error_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveStreamMetadataFragmentsDataRequest(_message.Message):
    __slots__ = (
        "channel_guid",
        "enable_presigned_urls_for_fragment_data",
        "metadata_type",
        "space_id",
        "video_edge_guid",
    )
    VIDEO_EDGE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRESIGNED_URLS_FOR_FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    video_edge_guid: str
    channel_guid: str
    metadata_type: str
    space_id: str
    enable_presigned_urls_for_fragment_data: bool
    def __init__(
        self,
        video_edge_guid: str | None = ...,
        channel_guid: str | None = ...,
        metadata_type: str | None = ...,
        space_id: str | None = ...,
        enable_presigned_urls_for_fragment_data: bool = ...,
    ) -> None: ...

class CloudArchiveStreamMetadataFragmentsDataResponse(_message.Message):
    __slots__ = ("fragment_data", "session_id", "tag")
    class CloudArchiveMetadataFragmentData(_message.Message):
        __slots__ = ("data", "data_url", "error", "fragment_id")
        class Frames(_message.Message):
            __slots__ = ("entries",)
            ENTRIES_FIELD_NUMBER: _ClassVar[int]
            entries: _containers.RepeatedCompositeFieldContainer[
                CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData.Frame
            ]
            def __init__(
                self,
                entries: _Iterable[
                    CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData.Frame
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class Frame(_message.Message):
            __slots__ = ("data", "ts")
            TS_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            ts: int
            data: bytes
            def __init__(
                self, ts: int | None = ..., data: bytes | None = ...
            ) -> None: ...

        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        error: _fragment_error_pb2.FragmentError
        data: bytes
        data_url: str
        def __init__(
            self,
            fragment_id: int | None = ...,
            error: _fragment_error_pb2.FragmentError | str | None = ...,
            data: bytes | None = ...,
            data_url: str | None = ...,
        ) -> None: ...

    TAG_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    tag: str
    session_id: str
    fragment_data: (
        CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData
    )
    def __init__(
        self,
        tag: str | None = ...,
        session_id: str | None = ...,
        fragment_data: CloudArchiveStreamMetadataFragmentsDataResponse.CloudArchiveMetadataFragmentData
        | _Mapping
        | None = ...,
    ) -> None: ...
