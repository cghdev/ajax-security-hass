from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.scenario import (
    scenario_pb2 as _scenario_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateScenarioRequest(_message.Message):
    __slots__ = ("cases", "enabled", "name", "scenario_id", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    scenario_id: str
    name: str
    enabled: bool
    cases: _containers.RepeatedCompositeFieldContainer[_scenario_pb2.Scenario.Case]
    def __init__(
        self,
        space_id: str | None = ...,
        scenario_id: str | None = ...,
        name: str | None = ...,
        enabled: bool = ...,
        cases: _Iterable[_scenario_pb2.Scenario.Case | _Mapping] | None = ...,
    ) -> None: ...

class UpdateScenarioResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("scenario",)
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        scenario: _scenario_pb2.Scenario
        def __init__(
            self, scenario: _scenario_pb2.Scenario | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "duplicated_name",
            "permission_denied",
            "scenario_not_found",
            "space_armed",
            "space_locked",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        DUPLICATED_NAME_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        duplicated_name: _response_pb2.DefaultError
        scenario_not_found: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            duplicated_name: _response_pb2.DefaultError | _Mapping | None = ...,
            scenario_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UpdateScenarioResponse.Success
    failure: UpdateScenarioResponse.Failure
    def __init__(
        self,
        success: UpdateScenarioResponse.Success | _Mapping | None = ...,
        failure: UpdateScenarioResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
