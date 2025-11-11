from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video import (
    duration_option_pb2 as _duration_option_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetMaxVideoCloudArchiveDepthRequest(_message.Message):
    __slots__ = ("channel_id", "max_cloud_archive_depth", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_CLOUD_ARCHIVE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    max_cloud_archive_depth: _duration_option_pb2.DurationOption
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        max_cloud_archive_depth: _duration_option_pb2.DurationOption | str | None = ...,
    ) -> None: ...
