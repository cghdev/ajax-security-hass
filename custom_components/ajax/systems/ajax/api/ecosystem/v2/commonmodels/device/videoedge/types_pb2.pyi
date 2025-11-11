from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FloatRange(_message.Message):
    __slots__ = ("max_value", "min_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: float
    max_value: float
    def __init__(
        self, min_value: float | None = ..., max_value: float | None = ...
    ) -> None: ...

class DurationRange(_message.Message):
    __slots__ = ("max_value", "min_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: _duration_pb2.Duration
    max_value: _duration_pb2.Duration
    def __init__(
        self,
        min_value: _duration_pb2.Duration | _Mapping | None = ...,
        max_value: _duration_pb2.Duration | _Mapping | None = ...,
    ) -> None: ...
