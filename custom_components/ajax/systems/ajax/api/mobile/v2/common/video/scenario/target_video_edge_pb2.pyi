from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class MonitoringState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[MonitoringState]
    ARMED: _ClassVar[MonitoringState]
    ALWAYS: _ClassVar[MonitoringState]

UNKNOWN: MonitoringState
ARMED: MonitoringState
ALWAYS: MonitoringState

class TargetVideoEdge(_message.Message):
    __slots__ = ("channels", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channels: _containers.RepeatedCompositeFieldContainer[TargetChannel]
    def __init__(
        self,
        video_edge_id: str | None = ...,
        channels: _Iterable[TargetChannel | _Mapping] | None = ...,
    ) -> None: ...

class TargetChannel(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: str | None = ...) -> None: ...
