from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeOnvifUserAuthEnabledRequest(_message.Message):
    __slots__ = ("enabled", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    enabled: bool
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        enabled: bool = ...,
    ) -> None: ...
