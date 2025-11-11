from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.video import (
    types_pb2 as _types_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoArchiveExportCompletedMedia(_message.Message):
    __slots__ = ("recordings",)
    class VideoExportedRecording(_message.Message):
        __slots__ = ("codec", "file_name", "start_timestamp", "timezone_offset", "url")
        CODEC_FIELD_NUMBER: _ClassVar[int]
        START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        codec: _types_pb2.VideoCodec
        start_timestamp: _timestamp_pb2.Timestamp
        timezone_offset: _duration_pb2.Duration
        url: str
        file_name: str
        def __init__(
            self,
            codec: _types_pb2.VideoCodec | str | None = ...,
            start_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            timezone_offset: _duration_pb2.Duration | _Mapping | None = ...,
            url: str | None = ...,
            file_name: str | None = ...,
        ) -> None: ...

    RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    recordings: _containers.RepeatedCompositeFieldContainer[
        VideoArchiveExportCompletedMedia.VideoExportedRecording
    ]
    def __init__(
        self,
        recordings: _Iterable[
            VideoArchiveExportCompletedMedia.VideoExportedRecording | _Mapping
        ]
        | None = ...,
    ) -> None: ...
