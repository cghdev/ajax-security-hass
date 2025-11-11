from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.about import (
    about_pb2 as _about_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeAdditionalInfo(_message.Message):
    __slots__ = ("color", "type")
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    color: _about_pb2.About.Color
    type: _about_pb2.About.Type
    def __init__(
        self,
        color: _about_pb2.About.Color | str | None = ...,
        type: _about_pb2.About.Type | str | None = ...,
    ) -> None: ...
