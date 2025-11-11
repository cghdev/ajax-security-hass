from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    source_image_info_pb2 as _source_image_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import (
    source_type_pb2 as _source_type_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import (
    video_edge_type_pb2 as _video_edge_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoNotificationSource(_message.Message):
    __slots__ = (
        "device_color",
        "id",
        "image_info",
        "name",
        "room_hex_id",
        "room_name",
        "type",
        "video_edge_type",
    )
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.VideoNotificationSourceType
    id: str
    name: str
    room_hex_id: str
    room_name: str
    device_color: _device_color_pb2.DeviceColor
    video_edge_type: _video_edge_type_pb2.VideoEdgeType
    image_info: _source_image_info_pb2.SourceImageInfo
    def __init__(
        self,
        type: _source_type_pb2.VideoNotificationSourceType | str | None = ...,
        id: str | None = ...,
        name: str | None = ...,
        room_hex_id: str | None = ...,
        room_name: str | None = ...,
        device_color: _device_color_pb2.DeviceColor | str | None = ...,
        video_edge_type: _video_edge_type_pb2.VideoEdgeType | str | None = ...,
        image_info: _source_image_info_pb2.SourceImageInfo | _Mapping | None = ...,
    ) -> None: ...
