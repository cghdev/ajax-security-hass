from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.scenario import (
    alarm_source_pb2 as _alarm_source_pb2,
)
from systems.ajax.api.mobile.v2.common.video.scenario import (
    alarm_sources_condition_pb2 as _alarm_sources_condition_pb2,
)
from systems.ajax.api.mobile.v2.common.video.scenario import (
    target_video_edge_pb2 as _target_video_edge_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoScenario(_message.Message):
    __slots__ = (
        "alarm_sources",
        "alarm_sources_condition",
        "enabled",
        "id",
        "monitoring_state",
        "name",
        "targets",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    enabled: bool
    name: str
    alarm_sources: _containers.RepeatedCompositeFieldContainer[
        _alarm_source_pb2.AlarmSource
    ]
    alarm_sources_condition: _alarm_sources_condition_pb2.AlarmSourcesCondition
    targets: _containers.RepeatedCompositeFieldContainer[
        _target_video_edge_pb2.TargetVideoEdge
    ]
    monitoring_state: _target_video_edge_pb2.MonitoringState
    def __init__(
        self,
        id: str | None = ...,
        enabled: bool = ...,
        name: str | None = ...,
        alarm_sources: _Iterable[_alarm_source_pb2.AlarmSource | _Mapping] | None = ...,
        alarm_sources_condition: _alarm_sources_condition_pb2.AlarmSourcesCondition
        | _Mapping
        | None = ...,
        targets: _Iterable[_target_video_edge_pb2.TargetVideoEdge | _Mapping]
        | None = ...,
        monitoring_state: _target_video_edge_pb2.MonitoringState | str | None = ...,
    ) -> None: ...
