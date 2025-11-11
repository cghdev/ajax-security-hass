from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import (
    video_edge_type_pb2 as _video_edge_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeInfo(_message.Message):
    __slots__ = ("color", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    type: _video_edge_type_pb2.VideoEdgeType
    color: _device_color_pb2.DeviceColor
    def __init__(
        self,
        type: _video_edge_type_pb2.VideoEdgeType | str | None = ...,
        color: _device_color_pb2.DeviceColor | str | None = ...,
    ) -> None: ...
