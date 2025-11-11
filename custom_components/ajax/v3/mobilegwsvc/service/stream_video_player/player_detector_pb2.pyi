from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.detector import (
    detector_pb2 as _detector_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerDetector(_message.Message):
    __slots__ = ("channel_id", "detector_type", "enabled", "id")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    channel_id: str
    detector_type: _detector_pb2.DetectorType
    enabled: bool
    def __init__(
        self,
        id: str | None = ...,
        channel_id: str | None = ...,
        detector_type: _detector_pb2.DetectorType | str | None = ...,
        enabled: bool = ...,
    ) -> None: ...
