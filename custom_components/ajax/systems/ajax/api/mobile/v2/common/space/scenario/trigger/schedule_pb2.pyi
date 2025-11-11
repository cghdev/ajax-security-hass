from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleTrigger(_message.Message):
    __slots__ = ("days", "time")
    TIME_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    time: _timeofday_pb2.TimeOfDay
    days: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
    def __init__(
        self,
        time: _timeofday_pb2.TimeOfDay | _Mapping | None = ...,
        days: _Iterable[_dayofweek_pb2.DayOfWeek | str] | None = ...,
    ) -> None: ...
