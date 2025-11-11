from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class PressPanicButtonRequest(_message.Message):
    __slots__ = ("location", "space_locator")
    class Location(_message.Message):
        __slots__ = ("horizontalAccuracy", "latitude", "longitude", "speed", "time")
        LATITUDE_FIELD_NUMBER: _ClassVar[int]
        LONGITUDE_FIELD_NUMBER: _ClassVar[int]
        HORIZONTALACCURACY_FIELD_NUMBER: _ClassVar[int]
        SPEED_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        latitude: float
        longitude: float
        horizontalAccuracy: float
        speed: float
        time: int
        def __init__(
            self,
            latitude: float | None = ...,
            longitude: float | None = ...,
            horizontalAccuracy: float | None = ...,
            speed: float | None = ...,
            time: int | None = ...,
        ) -> None: ...

    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    location: PressPanicButtonRequest.Location
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        location: PressPanicButtonRequest.Location | _Mapping | None = ...,
    ) -> None: ...

class PressPanicButtonResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "action_is_limited_in_empty_space",
            "bad_request",
            "hub_not_allowed_to_perform_command",
            "permissions_denied",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ACTION_IS_LIMITED_IN_EMPTY_SPACE_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_ALLOWED_TO_PERFORM_COMMAND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permissions_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        action_is_limited_in_empty_space: _response_pb2.DefaultError
        hub_not_allowed_to_perform_command: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permissions_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            action_is_limited_in_empty_space: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_not_allowed_to_perform_command: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: PressPanicButtonResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: PressPanicButtonResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
