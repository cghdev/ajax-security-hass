from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class HubLogEvent(_message.Message):
    __slots__ = ("id", "video_scenario_triggered")
    ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    id: str
    video_scenario_triggered: VideoScenarioTriggeredEvent
    def __init__(
        self,
        id: str | None = ...,
        video_scenario_triggered: VideoScenarioTriggeredEvent | _Mapping | None = ...,
    ) -> None: ...

class VideoScenarioTriggeredEvent(_message.Message):
    __slots__ = ("channel_gifs", "scenario_name", "triggered_time")
    class ChannelGif(_message.Message):
        __slots__ = (
            "channel_guid",
            "channel_name",
            "frames",
            "room_name",
            "video_edge_id",
        )
        CHANNEL_GUID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAMES_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        channel_guid: str
        channel_name: str
        room_name: str
        frames: _containers.RepeatedScalarFieldContainer[str]
        video_edge_id: str
        def __init__(
            self,
            channel_guid: str | None = ...,
            channel_name: str | None = ...,
            room_name: str | None = ...,
            frames: _Iterable[str] | None = ...,
            video_edge_id: str | None = ...,
        ) -> None: ...

    SCENARIO_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GIFS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_TIME_FIELD_NUMBER: _ClassVar[int]
    scenario_name: str
    channel_gifs: _containers.RepeatedCompositeFieldContainer[
        VideoScenarioTriggeredEvent.ChannelGif
    ]
    triggered_time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        scenario_name: str | None = ...,
        channel_gifs: _Iterable[VideoScenarioTriggeredEvent.ChannelGif | _Mapping]
        | None = ...,
        triggered_time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...
