from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class RequestedVideoChannelData(_message.Message):
    __slots__ = ("channel_id", "channel_name", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    channel_name: str
    def __init__(
        self,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        channel_name: str | None = ...,
    ) -> None: ...
