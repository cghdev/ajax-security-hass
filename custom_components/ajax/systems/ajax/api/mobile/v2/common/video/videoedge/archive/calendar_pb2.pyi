from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Calendar(_message.Message):
    __slots__ = ("days", "start_day", "tz_map")
    class TzEntry(_message.Message):
        __slots__ = ("day", "offsets")
        DAY_FIELD_NUMBER: _ClassVar[int]
        OFFSETS_FIELD_NUMBER: _ClassVar[int]
        day: _timestamp_pb2.Timestamp
        offsets: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self,
            day: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            offsets: _Iterable[int] | None = ...,
        ) -> None: ...

    START_DAY_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    TZ_MAP_FIELD_NUMBER: _ClassVar[int]
    start_day: _timestamp_pb2.Timestamp
    days: bytes
    tz_map: _containers.RepeatedCompositeFieldContainer[Calendar.TzEntry]
    def __init__(
        self,
        start_day: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        days: bytes | None = ...,
        tz_map: _Iterable[Calendar.TzEntry | _Mapping] | None = ...,
    ) -> None: ...
