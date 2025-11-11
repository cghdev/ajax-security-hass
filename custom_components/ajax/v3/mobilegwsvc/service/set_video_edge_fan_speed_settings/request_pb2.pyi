from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.system import (
    fan_speed_settings_pb2 as _fan_speed_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeFanSpeedSettingsRequest(_message.Message):
    __slots__ = ("fan_speed_settings", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    FAN_SPEED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    fan_speed_settings: _fan_speed_settings_pb2.FanSpeedSettings
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        fan_speed_settings: _fan_speed_settings_pb2.FanSpeedSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
