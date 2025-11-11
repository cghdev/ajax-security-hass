from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenarioResource(_message.Message):
    __slots__ = ("channel_metadata", "scenario_name", "trigger_time")
    class ChannelAlarmFrameMetadata(_message.Message):
        __slots__ = ("channel_id", "channel_name", "frames_ready", "room_name")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAMES_READY_FIELD_NUMBER: _ClassVar[int]
        channel_id: str
        channel_name: str
        room_name: str
        frames_ready: int
        def __init__(
            self,
            channel_id: str | None = ...,
            channel_name: str | None = ...,
            room_name: str | None = ...,
            frames_ready: int | None = ...,
        ) -> None: ...

    SCENARIO_NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    scenario_name: str
    trigger_time: _timestamp_pb2.Timestamp
    channel_metadata: _containers.RepeatedCompositeFieldContainer[
        VideoScenarioResource.ChannelAlarmFrameMetadata
    ]
    def __init__(
        self,
        scenario_name: str | None = ...,
        trigger_time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        channel_metadata: _Iterable[
            VideoScenarioResource.ChannelAlarmFrameMetadata | _Mapping
        ]
        | None = ...,
    ) -> None: ...
