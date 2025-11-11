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

class VideoEdgeInSpaceInfo(_message.Message):
    __slots__ = ("color", "id", "name", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: _video_edge_type_pb2.VideoEdgeType
    color: _device_color_pb2.DeviceColor
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        type: _video_edge_type_pb2.VideoEdgeType | str | None = ...,
        color: _device_color_pb2.DeviceColor | str | None = ...,
    ) -> None: ...
