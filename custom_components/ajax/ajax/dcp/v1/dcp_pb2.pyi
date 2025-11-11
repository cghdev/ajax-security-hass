from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from ajax.dcp.v1 import archive_pb2 as _archive_pb2
from ajax.dcp.v1 import ptz_pb2 as _ptz_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CompressionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CM_UNKNOWN: _ClassVar[CompressionMethod]
    CM_GZIP: _ClassVar[CompressionMethod]

class VideoStreamingQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VSQ_UNKNOWN: _ClassVar[VideoStreamingQuality]
    VSQ_HIGH: _ClassVar[VideoStreamingQuality]
    VSQ_MEDIUM: _ClassVar[VideoStreamingQuality]
    VSQ_LOW: _ClassVar[VideoStreamingQuality]

CM_UNKNOWN: CompressionMethod
CM_GZIP: CompressionMethod
VSQ_UNKNOWN: VideoStreamingQuality
VSQ_HIGH: VideoStreamingQuality
VSQ_MEDIUM: VideoStreamingQuality
VSQ_LOW: VideoStreamingQuality

class ClientMsg(_message.Message):
    __slots__ = (
        "archive_change_range",
        "archive_multi_play_range",
        "archive_pause",
        "archive_play",
        "archive_play_range",
        "archive_reopen",
        "archive_seek",
        "hello",
        "ptz_focus",
        "ptz_move",
        "ptz_stop",
        "ptz_zoom",
        "sync_marker",
        "tag",
    )
    class Hello(_message.Message):
        __slots__ = ("supported_compression_methods",)
        SUPPORTED_COMPRESSION_METHODS_FIELD_NUMBER: _ClassVar[int]
        supported_compression_methods: _containers.RepeatedScalarFieldContainer[
            CompressionMethod
        ]
        def __init__(
            self,
            supported_compression_methods: _Iterable[CompressionMethod | str]
            | None = ...,
        ) -> None: ...

    TAG_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_REOPEN_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_SEEK_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PLAY_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PLAY_RANGE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_CHANGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PAUSE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_MULTI_PLAY_RANGE_FIELD_NUMBER: _ClassVar[int]
    PTZ_MOVE_FIELD_NUMBER: _ClassVar[int]
    PTZ_ZOOM_FIELD_NUMBER: _ClassVar[int]
    PTZ_FOCUS_FIELD_NUMBER: _ClassVar[int]
    PTZ_STOP_FIELD_NUMBER: _ClassVar[int]
    SYNC_MARKER_FIELD_NUMBER: _ClassVar[int]
    tag: int
    hello: ClientMsg.Hello
    archive_reopen: _archive_pb2.ArchiveReopen
    archive_seek: _archive_pb2.ArchiveSeek
    archive_play: _archive_pb2.ArchivePlay
    archive_play_range: _archive_pb2.ArchivePlayRange
    archive_change_range: _archive_pb2.ArchiveChangeRange
    archive_pause: _archive_pb2.ArchivePause
    archive_multi_play_range: _archive_pb2.ArchiveMultiPlayRange
    ptz_move: _ptz_pb2.PtzMove
    ptz_zoom: _ptz_pb2.PtzZoom
    ptz_focus: _ptz_pb2.PtzFocus
    ptz_stop: _ptz_pb2.PtzStop
    sync_marker: int
    def __init__(
        self,
        tag: int | None = ...,
        hello: ClientMsg.Hello | _Mapping | None = ...,
        archive_reopen: _archive_pb2.ArchiveReopen | _Mapping | None = ...,
        archive_seek: _archive_pb2.ArchiveSeek | _Mapping | None = ...,
        archive_play: _archive_pb2.ArchivePlay | _Mapping | None = ...,
        archive_play_range: _archive_pb2.ArchivePlayRange | _Mapping | None = ...,
        archive_change_range: _archive_pb2.ArchiveChangeRange | _Mapping | None = ...,
        archive_pause: _archive_pb2.ArchivePause | _Mapping | None = ...,
        archive_multi_play_range: _archive_pb2.ArchiveMultiPlayRange
        | _Mapping
        | None = ...,
        ptz_move: _ptz_pb2.PtzMove | _Mapping | None = ...,
        ptz_zoom: _ptz_pb2.PtzZoom | _Mapping | None = ...,
        ptz_focus: _ptz_pb2.PtzFocus | _Mapping | None = ...,
        ptz_stop: _ptz_pb2.PtzStop | _Mapping | None = ...,
        sync_marker: int | None = ...,
    ) -> None: ...

class ServerMsg(_message.Message):
    __slots__ = (
        "archive_status",
        "archive_timeline",
        "compressed",
        "frame_data",
        "hello",
        "quality_report",
        "sync_marker",
        "tag",
    )
    class Hello(_message.Message):
        __slots__ = ("supports_archive_reopen",)
        SUPPORTS_ARCHIVE_REOPEN_FIELD_NUMBER: _ClassVar[int]
        supports_archive_reopen: bool
        def __init__(self, supports_archive_reopen: bool = ...) -> None: ...

    class Compressed(_message.Message):
        __slots__ = ("data", "method")
        METHOD_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        method: CompressionMethod
        data: bytes
        def __init__(
            self, method: CompressionMethod | str | None = ..., data: bytes | None = ...
        ) -> None: ...

    class Uncompressed(_message.Message):
        __slots__ = ("archive_timeline", "frame_data")
        FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
        ARCHIVE_TIMELINE_FIELD_NUMBER: _ClassVar[int]
        frame_data: FrameData
        archive_timeline: _archive_pb2.ArchiveTimeline
        def __init__(
            self,
            frame_data: FrameData | _Mapping | None = ...,
            archive_timeline: _archive_pb2.ArchiveTimeline | _Mapping | None = ...,
        ) -> None: ...

    TAG_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_REPORT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    SYNC_MARKER_FIELD_NUMBER: _ClassVar[int]
    tag: int
    hello: ServerMsg.Hello
    frame_data: FrameData
    archive_status: _archive_pb2.ArchivePlayerStatus
    archive_timeline: _archive_pb2.ArchiveTimeline
    quality_report: QualityReport
    compressed: ServerMsg.Compressed
    sync_marker: int
    def __init__(
        self,
        tag: int | None = ...,
        hello: ServerMsg.Hello | _Mapping | None = ...,
        frame_data: FrameData | _Mapping | None = ...,
        archive_status: _archive_pb2.ArchivePlayerStatus | _Mapping | None = ...,
        archive_timeline: _archive_pb2.ArchiveTimeline | _Mapping | None = ...,
        quality_report: QualityReport | _Mapping | None = ...,
        compressed: ServerMsg.Compressed | _Mapping | None = ...,
        sync_marker: int | None = ...,
    ) -> None: ...

class Frame(_message.Message):
    __slots__ = ("data", "ts", "type")
    TS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    type: str
    data: bytes
    def __init__(
        self,
        ts: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        type: str | None = ...,
        data: bytes | None = ...,
    ) -> None: ...

class FrameData(_message.Message):
    __slots__ = ("frames",)
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[Frame]
    def __init__(self, frames: _Iterable[Frame | _Mapping] | None = ...) -> None: ...

class QualityReport(_message.Message):
    __slots__ = ("video_streaming_quality",)
    VIDEO_STREAMING_QUALITY_FIELD_NUMBER: _ClassVar[int]
    video_streaming_quality: VideoStreamingQuality
    def __init__(
        self, video_streaming_quality: VideoStreamingQuality | str | None = ...
    ) -> None: ...
