from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmSourcesCondition(_message.Message):
    __slots__ = ("all", "any")
    class AnySource(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class AllSources(_message.Message):
        __slots__ = ("max_actuating_time",)
        MAX_ACTUATING_TIME_FIELD_NUMBER: _ClassVar[int]
        max_actuating_time: _duration_pb2.Duration
        def __init__(
            self, max_actuating_time: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    ANY_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    any: AlarmSourcesCondition.AnySource
    all: AlarmSourcesCondition.AllSources
    def __init__(
        self,
        any: AlarmSourcesCondition.AnySource | _Mapping | None = ...,
        all: AlarmSourcesCondition.AllSources | _Mapping | None = ...,
    ) -> None: ...
