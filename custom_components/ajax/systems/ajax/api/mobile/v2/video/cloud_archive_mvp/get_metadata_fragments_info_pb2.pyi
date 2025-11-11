from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import (
    fragment_info_pb2 as _fragment_info_pb2,
)
from systems.ajax.api.mobile.v2.video.cloud_archive_mvp import (
    tz_entry_pb2 as _tz_entry_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveGetMetadataFragmentsInfoRequest(_message.Message):
    __slots__ = (
        "channel_guid",
        "metadata_type",
        "space_id",
        "ts_range",
        "video_edge_guid",
    )
    VIDEO_EDGE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_guid: str
    channel_guid: str
    metadata_type: str
    ts_range: _types_pb2.TimestampRange
    space_id: str
    def __init__(
        self,
        video_edge_guid: str | None = ...,
        channel_guid: str | None = ...,
        metadata_type: str | None = ...,
        ts_range: _types_pb2.TimestampRange | _Mapping | None = ...,
        space_id: str | None = ...,
    ) -> None: ...

class CloudArchiveGetMetadataFragmentsInfoResponse(_message.Message):
    __slots__ = ("fragments", "tz_map")
    FRAGMENTS_FIELD_NUMBER: _ClassVar[int]
    TZ_MAP_FIELD_NUMBER: _ClassVar[int]
    fragments: _containers.RepeatedCompositeFieldContainer[
        _fragment_info_pb2.CloudArchiveFragmentInfo
    ]
    tz_map: _containers.RepeatedCompositeFieldContainer[
        _tz_entry_pb2.CloudArchiveTzEntry
    ]
    def __init__(
        self,
        fragments: _Iterable[_fragment_info_pb2.CloudArchiveFragmentInfo | _Mapping]
        | None = ...,
        tz_map: _Iterable[_tz_entry_pb2.CloudArchiveTzEntry | _Mapping] | None = ...,
    ) -> None: ...
