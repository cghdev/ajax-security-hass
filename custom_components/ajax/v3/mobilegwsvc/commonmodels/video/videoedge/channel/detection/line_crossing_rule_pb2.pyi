from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.detection import (
    line_crossing_direction_pb2 as _line_crossing_direction_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LineCrossingRule(_message.Message):
    __slots__ = ("direction", "enabled", "id", "name", "object_classes", "points")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLASSES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    enabled: bool
    points: _containers.RepeatedCompositeFieldContainer[_types_pb2.Point2f]
    direction: _line_crossing_direction_pb2.LineCrossingDirection
    object_classes: _containers.RepeatedScalarFieldContainer[_types_pb2.ObjectClass]
    def __init__(
        self,
        id: int | None = ...,
        name: str | None = ...,
        enabled: bool = ...,
        points: _Iterable[_types_pb2.Point2f | _Mapping] | None = ...,
        direction: _line_crossing_direction_pb2.LineCrossingDirection
        | str
        | None = ...,
        object_classes: _Iterable[_types_pb2.ObjectClass | str] | None = ...,
    ) -> None: ...
