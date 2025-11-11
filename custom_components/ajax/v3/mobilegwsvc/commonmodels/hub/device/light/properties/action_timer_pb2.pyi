from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ActionTimer(_message.Message):
    __slots__ = ("pending", "ticking")
    class Ticking(_message.Message):
        __slots__ = ("end_timestamp",)
        END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        end_timestamp: _timestamp_pb2.Timestamp
        def __init__(
            self, end_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...
        ) -> None: ...

    class Pending(_message.Message):
        __slots__ = ("period_seconds",)
        PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
        period_seconds: int
        def __init__(self, period_seconds: int | None = ...) -> None: ...

    TICKING_FIELD_NUMBER: _ClassVar[int]
    PENDING_FIELD_NUMBER: _ClassVar[int]
    ticking: ActionTimer.Ticking
    pending: ActionTimer.Pending
    def __init__(
        self,
        ticking: ActionTimer.Ticking | _Mapping | None = ...,
        pending: ActionTimer.Pending | _Mapping | None = ...,
    ) -> None: ...
