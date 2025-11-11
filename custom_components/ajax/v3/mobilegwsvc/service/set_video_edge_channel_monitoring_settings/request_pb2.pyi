from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.channel import (
    video_monitoring_state_pb2 as _video_monitoring_state_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeChannelMonitoringSettingsRequest(_message.Message):
    __slots__ = (
        "channel_id",
        "monitoring_state",
        "space_id",
        "video_edge_id",
        "zone_number",
    )
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    zone_number: str
    monitoring_state: _video_monitoring_state_pb2.VideoMonitoringState
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        zone_number: str | None = ...,
        monitoring_state: _video_monitoring_state_pb2.VideoMonitoringState
        | str
        | None = ...,
    ) -> None: ...
