from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import (
    detector_locator_pb2 as _detector_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeSpecificDetectionSettingsRequest(_message.Message):
    __slots__ = ("detector_locator", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    detector_locator: _detector_locator_pb2.DetectorLocator
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        detector_locator: _detector_locator_pb2.DetectorLocator | _Mapping | None = ...,
    ) -> None: ...
