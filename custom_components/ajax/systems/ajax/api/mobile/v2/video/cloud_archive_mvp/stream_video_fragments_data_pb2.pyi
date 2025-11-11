from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import (
    fragment_error_pb2 as _fragment_error_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveStreamVideoFragmentsDataRequest(_message.Message):
    __slots__ = (
        "channel_guid",
        "enable_presigned_urls_for_fragment_data",
        "enable_presigned_urls_for_fragment_part_data",
        "space_id",
        "stream_type",
        "video_edge_guid",
    )
    VIDEO_EDGE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRESIGNED_URLS_FOR_FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRESIGNED_URLS_FOR_FRAGMENT_PART_DATA_FIELD_NUMBER: _ClassVar[int]
    video_edge_guid: str
    channel_guid: str
    stream_type: _types_pb2.StreamType
    space_id: str
    enable_presigned_urls_for_fragment_data: bool
    enable_presigned_urls_for_fragment_part_data: bool
    def __init__(
        self,
        video_edge_guid: str | None = ...,
        channel_guid: str | None = ...,
        stream_type: _types_pb2.StreamType | str | None = ...,
        space_id: str | None = ...,
        enable_presigned_urls_for_fragment_data: bool = ...,
        enable_presigned_urls_for_fragment_part_data: bool = ...,
    ) -> None: ...

class CloudArchiveStreamVideoFragmentsDataResponse(_message.Message):
    __slots__ = ("fragment_data", "fragment_part_data", "session_id", "tag")
    class CloudArchiveVideoFragmentData(_message.Message):
        __slots__ = ("data", "data_url", "error", "fragment_id")
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

    class CloudArchiveVideoFragmentPartData(_message.Message):
        __slots__ = (
            "data",
            "data_url",
            "data_url_header",
            "error",
            "fragment_id",
            "offset",
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

        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_FIELD_NUMBER: _ClassVar[int]
        DATA_URL_HEADER_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        offset: int
        error: _fragment_error_pb2.FragmentError
        data: bytes
        data_url: str
        data_url_header: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData.Header
        def __init__(
            self,
            fragment_id: int | None = ...,
            offset: int | None = ...,
            error: _fragment_error_pb2.FragmentError | str | None = ...,
            data: bytes | None = ...,
            data_url: str | None = ...,
            data_url_header: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData.Header
            | _Mapping
            | None = ...,
        ) -> None: ...

    TAG_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_PART_DATA_FIELD_NUMBER: _ClassVar[int]
    tag: str
    session_id: str
    fragment_data: (
        CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentData
    )
    fragment_part_data: (
        CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData
    )
    def __init__(
        self,
        tag: str | None = ...,
        session_id: str | None = ...,
        fragment_data: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentData
        | _Mapping
        | None = ...,
        fragment_part_data: CloudArchiveStreamVideoFragmentsDataResponse.CloudArchiveVideoFragmentPartData
        | _Mapping
        | None = ...,
    ) -> None: ...
