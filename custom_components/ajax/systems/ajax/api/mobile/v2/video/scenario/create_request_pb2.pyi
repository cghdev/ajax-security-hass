from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.scenario import (
    alarm_source_pb2 as _alarm_source_pb2,
)
from systems.ajax.api.mobile.v2.common.video.scenario import (
    alarm_sources_condition_pb2 as _alarm_sources_condition_pb2,
)
from systems.ajax.api.mobile.v2.common.video.scenario import (
    target_video_edge_pb2 as _target_video_edge_pb2,
)
from systems.ajax.api.mobile.v2.common.video.scenario import (
    video_scenario_pb2 as _video_scenario_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScenarioRequest(_message.Message):
    __slots__ = (
        "alarm_sources",
        "alarm_sources_condition",
        "monitoring_state",
        "name",
        "space_locator",
        "targets",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
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
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        name: str | None = ...,
        alarm_sources: _Iterable[_alarm_source_pb2.AlarmSource | _Mapping] | None = ...,
        alarm_sources_condition: _alarm_sources_condition_pb2.AlarmSourcesCondition
        | _Mapping
        | None = ...,
        targets: _Iterable[_target_video_edge_pb2.TargetVideoEdge | _Mapping]
        | None = ...,
        monitoring_state: _target_video_edge_pb2.MonitoringState | str | None = ...,
    ) -> None: ...

class CreateScenarioResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("scenario",)
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        scenario: _video_scenario_pb2.VideoScenario
        def __init__(
            self, scenario: _video_scenario_pb2.VideoScenario | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "duplicated_name",
            "empty_source_list",
            "hub_not_found",
            "invalid_channel_state",
            "permission_denied",
            "source_not_found",
            "space_armed",
            "space_locked",
            "space_not_found",
            "target_channel_list_is_empty",
            "target_channel_not_found",
            "target_video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        EMPTY_SOURCE_LIST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SOURCE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        TARGET_CHANNEL_LIST_IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
        TARGET_VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        TARGET_CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        INVALID_CHANNEL_STATE_FIELD_NUMBER: _ClassVar[int]
        DUPLICATED_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        empty_source_list: _response_pb2.DefaultError
        hub_not_found: _response_pb2.DefaultError
        source_not_found: _response_pb2.DefaultError
        target_channel_list_is_empty: _response_pb2.DefaultError
        target_video_edge_not_found: _response_pb2.DefaultError
        target_channel_not_found: _response_pb2.DefaultError
        invalid_channel_state: _response_pb2.DefaultError
        duplicated_name: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            empty_source_list: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            source_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            target_channel_list_is_empty: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            target_video_edge_not_found: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            target_channel_not_found: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            invalid_channel_state: _response_pb2.DefaultError | _Mapping | None = ...,
            duplicated_name: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateScenarioResponse.Success
    failure: CreateScenarioResponse.Failure
    def __init__(
        self,
        success: CreateScenarioResponse.Success | _Mapping | None = ...,
        failure: CreateScenarioResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
