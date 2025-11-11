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

class FindAllScenariosRequest(_message.Message):
    __slots__ = ("space_id",)
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: str | None = ...) -> None: ...

class FindAllScenariosResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("scenarios",)
        SCENARIOS_FIELD_NUMBER: _ClassVar[int]
        scenarios: _containers.RepeatedCompositeFieldContainer[_scenario_pb2.Scenario]
        def __init__(
            self, scenarios: _Iterable[_scenario_pb2.Scenario | _Mapping] | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllScenariosResponse.Success
    failure: FindAllScenariosResponse.Failure
    def __init__(
        self,
        success: FindAllScenariosResponse.Success | _Mapping | None = ...,
        failure: FindAllScenariosResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
