from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeDetectorsEnabledRequest(_message.Message):
    __slots__ = ("detectors", "space_id", "video_edge_id")
    class DetectorEnabled(_message.Message):
        __slots__ = ("detector_id", "enabled")
        DETECTOR_ID_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        detector_id: str
        enabled: bool
        def __init__(
            self, detector_id: str | None = ..., enabled: bool = ...
        ) -> None: ...

    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    detectors: _containers.RepeatedCompositeFieldContainer[
        SetVideoEdgeDetectorsEnabledRequest.DetectorEnabled
    ]
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        detectors: _Iterable[
            SetVideoEdgeDetectorsEnabledRequest.DetectorEnabled | _Mapping
        ]
        | None = ...,
    ) -> None: ...
