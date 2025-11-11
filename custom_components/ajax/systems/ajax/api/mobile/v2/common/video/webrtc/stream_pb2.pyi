from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import (
    channel_pb2 as _channel_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Stream(_message.Message):
    __slots__ = (
        "archive",
        "channel_guid",
        "dcp_tag",
        "device_info",
        "filter",
        "id",
        "live",
        "type",
    )
    class Live(_message.Message):
        __slots__ = ("input_rtc_stream_id", "use_ptz")
        INPUT_RTC_STREAM_ID_FIELD_NUMBER: _ClassVar[int]
        USE_PTZ_FIELD_NUMBER: _ClassVar[int]
        input_rtc_stream_id: str
        use_ptz: bool
        def __init__(
            self, input_rtc_stream_id: str | None = ..., use_ptz: bool = ...
        ) -> None: ...

    class Archive(_message.Message):
        __slots__ = ("group_id", "pos_update_interval", "ts_range")
        TS_RANGE_FIELD_NUMBER: _ClassVar[int]
        POS_UPDATE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ts_range: _types_pb2.TimestampRange
        pos_update_interval: _duration_pb2.Duration
        group_id: str
        def __init__(
            self,
            ts_range: _types_pb2.TimestampRange | _Mapping | None = ...,
            pos_update_interval: _duration_pb2.Duration | _Mapping | None = ...,
            group_id: str | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    DCP_TAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_guid: str
    device_info: _channel_pb2.MediaDeviceInfo
    dcp_tag: int
    type: _types_pb2.StreamType
    filter: _containers.RepeatedCompositeFieldContainer[_types_pb2.FrameTypeId]
    live: Stream.Live
    archive: Stream.Archive
    def __init__(
        self,
        id: str | None = ...,
        channel_guid: str | None = ...,
        device_info: _channel_pb2.MediaDeviceInfo | _Mapping | None = ...,
        dcp_tag: int | None = ...,
        type: _types_pb2.StreamType | str | None = ...,
        filter: _Iterable[_types_pb2.FrameTypeId | _Mapping] | None = ...,
        live: Stream.Live | _Mapping | None = ...,
        archive: Stream.Archive | _Mapping | None = ...,
    ) -> None: ...
