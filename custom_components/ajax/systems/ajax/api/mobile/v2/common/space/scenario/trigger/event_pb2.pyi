from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import (
    qualifier_pb2 as _qualifier_pb2_1_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.smartlock import (
    qualifier_pb2 as _qualifier_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.space import (
    qualifier_pb2 as _qualifier_pb2_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.video import (
    qualifier_pb2 as _qualifier_pb2_1_1,
)

DESCRIPTOR: _descriptor.FileDescriptor

class EventTrigger(_message.Message):
    __slots__ = ("condition", "sources")
    class EventSource(_message.Message):
        __slots__ = ("hub_device", "smart_lock", "space", "video_edge")
        class Space(_message.Message):
            __slots__ = ("events",)
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            events: _containers.RepeatedCompositeFieldContainer[
                _qualifier_pb2_1.SpaceEventQualifier
            ]
            def __init__(
                self,
                events: _Iterable[_qualifier_pb2_1.SpaceEventQualifier | _Mapping]
                | None = ...,
            ) -> None: ...

        class HubDevice(_message.Message):
            __slots__ = ("events", "hub_id", "id")
            ID_FIELD_NUMBER: _ClassVar[int]
            HUB_ID_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            id: str
            hub_id: str
            events: _containers.RepeatedCompositeFieldContainer[
                _qualifier_pb2_1_1_1.HubEventQualifier
            ]
            def __init__(
                self,
                id: str | None = ...,
                hub_id: str | None = ...,
                events: _Iterable[_qualifier_pb2_1_1_1.HubEventQualifier | _Mapping]
                | None = ...,
            ) -> None: ...

        class VideoEdge(_message.Message):
            __slots__ = ("channel_id", "events", "id")
            ID_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            events: _containers.RepeatedCompositeFieldContainer[
                _qualifier_pb2_1_1.VideoEventQualifier
            ]
            channel_id: str
            def __init__(
                self,
                id: str | None = ...,
                events: _Iterable[_qualifier_pb2_1_1.VideoEventQualifier | _Mapping]
                | None = ...,
                channel_id: str | None = ...,
            ) -> None: ...

        class SmartLock(_message.Message):
            __slots__ = ("events", "id")
            ID_FIELD_NUMBER: _ClassVar[int]
            EVENTS_FIELD_NUMBER: _ClassVar[int]
            id: str
            events: _containers.RepeatedCompositeFieldContainer[
                _qualifier_pb2.SmartLockEventQualifier
            ]
            def __init__(
                self,
                id: str | None = ...,
                events: _Iterable[_qualifier_pb2.SmartLockEventQualifier | _Mapping]
                | None = ...,
            ) -> None: ...

        SPACE_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
        space: EventTrigger.EventSource.Space
        hub_device: EventTrigger.EventSource.HubDevice
        video_edge: EventTrigger.EventSource.VideoEdge
        smart_lock: EventTrigger.EventSource.SmartLock
        def __init__(
            self,
            space: EventTrigger.EventSource.Space | _Mapping | None = ...,
            hub_device: EventTrigger.EventSource.HubDevice | _Mapping | None = ...,
            video_edge: EventTrigger.EventSource.VideoEdge | _Mapping | None = ...,
            smart_lock: EventTrigger.EventSource.SmartLock | _Mapping | None = ...,
        ) -> None: ...

    class EventCondition(_message.Message):
        __slots__ = ("all", "any")
        class Any(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class All(_message.Message):
            __slots__ = ("max_actuating_time",)
            MAX_ACTUATING_TIME_FIELD_NUMBER: _ClassVar[int]
            max_actuating_time: _duration_pb2.Duration
            def __init__(
                self, max_actuating_time: _duration_pb2.Duration | _Mapping | None = ...
            ) -> None: ...

        ANY_FIELD_NUMBER: _ClassVar[int]
        ALL_FIELD_NUMBER: _ClassVar[int]
        any: EventTrigger.EventCondition.Any
        all: EventTrigger.EventCondition.All
        def __init__(
            self,
            any: EventTrigger.EventCondition.Any | _Mapping | None = ...,
            all: EventTrigger.EventCondition.All | _Mapping | None = ...,
        ) -> None: ...

    SOURCES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[EventTrigger.EventSource]
    condition: EventTrigger.EventCondition
    def __init__(
        self,
        sources: _Iterable[EventTrigger.EventSource | _Mapping] | None = ...,
        condition: EventTrigger.EventCondition | _Mapping | None = ...,
    ) -> None: ...
