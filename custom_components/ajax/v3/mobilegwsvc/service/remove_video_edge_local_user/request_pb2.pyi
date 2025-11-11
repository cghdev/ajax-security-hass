from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveVideoEdgeLocalUserRequest(_message.Message):
    __slots__ = ("name", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    name: str
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        name: str | None = ...,
    ) -> None: ...
