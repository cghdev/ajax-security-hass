from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFramesMedia(_message.Message):
    __slots__ = ("frames",)
    class VideoFrameMedia(_message.Message):
        __slots__ = ("timestamp", "url")
        URL_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        url: str
        timestamp: _timestamp_pb2.Timestamp
        def __init__(
            self,
            url: str | None = ...,
            timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        ) -> None: ...

    FRAMES_FIELD_NUMBER: _ClassVar[int]
    frames: _containers.RepeatedCompositeFieldContainer[
        VideoFramesMedia.VideoFrameMedia
    ]
    def __init__(
        self,
        frames: _Iterable[VideoFramesMedia.VideoFrameMedia | _Mapping] | None = ...,
    ) -> None: ...
