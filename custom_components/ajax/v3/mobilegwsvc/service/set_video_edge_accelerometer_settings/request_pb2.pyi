from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.system import (
    accelerometer_settings_pb2 as _accelerometer_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeAccelerometerSettingsRequest(_message.Message):
    __slots__ = ("accelerometer_settings", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    accelerometer_settings: _accelerometer_settings_pb2.AccelerometerSettings
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        accelerometer_settings: _accelerometer_settings_pb2.AccelerometerSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
