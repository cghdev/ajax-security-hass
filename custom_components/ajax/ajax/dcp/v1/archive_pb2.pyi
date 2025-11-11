from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from ajax.video.v1.types import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ArchiveReopen(_message.Message):
    __slots__ = ("filter", "is_export", "new_tag", "ts_range", "type")
    NEW_TAG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    IS_EXPORT_FIELD_NUMBER: _ClassVar[int]
    new_tag: int
    type: _types_pb2.StreamType
    filter: _containers.RepeatedCompositeFieldContainer[_types_pb2.FrameTypeId]
    ts_range: _types_pb2.TimestampRange
    is_export: bool
    def __init__(
        self,
        new_tag: int | None = ...,
        type: _types_pb2.StreamType | str | None = ...,
        filter: _Iterable[_types_pb2.FrameTypeId | _Mapping] | None = ...,
        ts_range: _types_pb2.TimestampRange | _Mapping | None = ...,
        is_export: bool = ...,
    ) -> None: ...

class ArchiveSeek(_message.Message):
    __slots__ = ("economy", "ts")
    TS_FIELD_NUMBER: _ClassVar[int]
    ECONOMY_FIELD_NUMBER: _ClassVar[int]
    ts: _timestamp_pb2.Timestamp
    economy: bool
    def __init__(
        self, ts: _timestamp_pb2.Timestamp | _Mapping | None = ..., economy: bool = ...
    ) -> None: ...

class ArchivePlay(_message.Message):
    __slots__ = ("speed",)
    SPEED_FIELD_NUMBER: _ClassVar[int]
    speed: float
    def __init__(self, speed: float | None = ...) -> None: ...

class ArchivePlayRange(_message.Message):
    __slots__ = ("loop", "speed", "ts_range")
    SPEED_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    speed: float
    ts_range: _types_pb2.TimestampRange
    loop: bool
    def __init__(
        self,
        speed: float | None = ...,
        ts_range: _types_pb2.TimestampRange | _Mapping | None = ...,
        loop: bool = ...,
    ) -> None: ...

class ArchiveChangeRange(_message.Message):
    __slots__ = ("loop", "ts_range")
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    LOOP_FIELD_NUMBER: _ClassVar[int]
    ts_range: _types_pb2.TimestampRange
    loop: bool
    def __init__(
        self,
        ts_range: _types_pb2.TimestampRange | _Mapping | None = ...,
        loop: bool = ...,
    ) -> None: ...

class ArchivePause(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArchiveMultiPlayRange(_message.Message):
    __slots__ = ("ranges",)
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[_types_pb2.SparseRange]
    def __init__(
        self, ranges: _Iterable[_types_pb2.SparseRange | _Mapping] | None = ...
    ) -> None: ...

class ArchivePlayerStatus(_message.Message):
    __slots__ = ("pos", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PS_NONE: _ClassVar[ArchivePlayerStatus.State]
        PS_PLAYING: _ClassVar[ArchivePlayerStatus.State]
        PS_PAUSED: _ClassVar[ArchivePlayerStatus.State]

    PS_NONE: ArchivePlayerStatus.State
    PS_PLAYING: ArchivePlayerStatus.State
    PS_PAUSED: ArchivePlayerStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    state: ArchivePlayerStatus.State
    pos: _timestamp_pb2.Timestamp
    def __init__(
        self,
        state: ArchivePlayerStatus.State | str | None = ...,
        pos: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class ArchiveTimeline(_message.Message):
    __slots__ = ("seconds", "ts_range", "tz_map", "update_type")
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ArchiveTimeline.UpdateType]
        MERGE: _ClassVar[ArchiveTimeline.UpdateType]
        REPLACE: _ClassVar[ArchiveTimeline.UpdateType]

    NONE: ArchiveTimeline.UpdateType
    MERGE: ArchiveTimeline.UpdateType
    REPLACE: ArchiveTimeline.UpdateType
    class TzEntry(_message.Message):
        __slots__ = ("ts", "tz_offset")
        TS_FIELD_NUMBER: _ClassVar[int]
        TZ_OFFSET_FIELD_NUMBER: _ClassVar[int]
        ts: _timestamp_pb2.Timestamp
        tz_offset: _duration_pb2.Duration
        def __init__(
            self,
            ts: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            tz_offset: _duration_pb2.Duration | _Mapping | None = ...,
        ) -> None: ...

    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TS_RANGE_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    TZ_MAP_FIELD_NUMBER: _ClassVar[int]
    update_type: ArchiveTimeline.UpdateType
    ts_range: _types_pb2.TimestampRange
    seconds: bytes
    tz_map: _containers.RepeatedCompositeFieldContainer[ArchiveTimeline.TzEntry]
    def __init__(
        self,
        update_type: ArchiveTimeline.UpdateType | str | None = ...,
        ts_range: _types_pb2.TimestampRange | _Mapping | None = ...,
        seconds: bytes | None = ...,
        tz_map: _Iterable[ArchiveTimeline.TzEntry | _Mapping] | None = ...,
    ) -> None: ...
