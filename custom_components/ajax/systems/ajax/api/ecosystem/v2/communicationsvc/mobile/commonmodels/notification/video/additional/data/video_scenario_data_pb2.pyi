from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenarioData(_message.Message):
    __slots__ = ("channel_metadata",)
    class FramesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FRAMES_STATUS_UNKNOWN: _ClassVar[VideoScenarioData.FramesStatus]
        FRAMES_STATUS_IN_PROGRESS: _ClassVar[VideoScenarioData.FramesStatus]
        FRAMES_STATUS_READY: _ClassVar[VideoScenarioData.FramesStatus]

    FRAMES_STATUS_UNKNOWN: VideoScenarioData.FramesStatus
    FRAMES_STATUS_IN_PROGRESS: VideoScenarioData.FramesStatus
    FRAMES_STATUS_READY: VideoScenarioData.FramesStatus
    class ChannelAlarmFrameMetadata(_message.Message):
        __slots__ = (
            "channel_id",
            "channel_name",
            "frames_ready",
            "frames_status",
            "room_name",
            "video_edge_id",
        )
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAMES_READY_FIELD_NUMBER: _ClassVar[int]
        FRAMES_STATUS_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_id: str
        channel_name: str
        room_name: str
        frames_ready: int
        frames_status: VideoScenarioData.FramesStatus
        def __init__(
            self,
            video_edge_id: str | None = ...,
            channel_id: str | None = ...,
            channel_name: str | None = ...,
            room_name: str | None = ...,
            frames_ready: int | None = ...,
            frames_status: VideoScenarioData.FramesStatus | str | None = ...,
        ) -> None: ...

    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    channel_metadata: _containers.RepeatedCompositeFieldContainer[
        VideoScenarioData.ChannelAlarmFrameMetadata
    ]
    def __init__(
        self,
        channel_metadata: _Iterable[
            VideoScenarioData.ChannelAlarmFrameMetadata | _Mapping
        ]
        | None = ...,
    ) -> None: ...
