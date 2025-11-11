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
    video_scenario_pb2 as _video_scenario_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetAllScenariosRequest(_message.Message):
    __slots__ = ("space_locator",)
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self, space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...
    ) -> None: ...

class GetAllScenariosResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("scenario",)
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        scenario: _containers.RepeatedCompositeFieldContainer[
            _video_scenario_pb2.VideoScenario
        ]
        def __init__(
            self,
            scenario: _Iterable[_video_scenario_pb2.VideoScenario | _Mapping]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "space_armed",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAllScenariosResponse.Success
    failure: GetAllScenariosResponse.Failure
    def __init__(
        self,
        success: GetAllScenariosResponse.Success | _Mapping | None = ...,
        failure: GetAllScenariosResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
