from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import (
    image_analysis_mode_pb2 as _image_analysis_mode_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeMotionDetectionImageAnalysisModeRequest(_message.Message):
    __slots__ = ("channel_id", "image_analysis_mode", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ANALYSIS_MODE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    image_analysis_mode: _image_analysis_mode_pb2.ImageAnalysisMode
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        image_analysis_mode: _image_analysis_mode_pb2.ImageAnalysisMode
        | str
        | None = ...,
    ) -> None: ...
