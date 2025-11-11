from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ArmSpaceRequest(_message.Message):
    __slots__ = ("ignore_alarms", "space_locator")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ALARMS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    ignore_alarms: bool
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        ignore_alarms: bool = ...,
    ) -> None: ...

class ArmSpaceResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "action_is_limited_in_empty_space",
            "already_in_the_requested_security_state",
            "another_transition_is_in_progress",
            "bad_request",
            "hub_alarm_reset_required",
            "hub_blocked_by_service_provider",
            "hub_busy",
            "hub_detected_malfunctions",
            "hub_not_allowed_to_perform_command",
            "hub_offline",
            "illegal_space_security_mode",
            "permission_denied",
            "space_locked",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        ANOTHER_TRANSITION_IS_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        ALREADY_IN_THE_REQUESTED_SECURITY_STATE_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_SPACE_SECURITY_MODE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_BLOCKED_BY_SERVICE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
        HUB_ALARM_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        HUB_DETECTED_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        ACTION_IS_LIMITED_IN_EMPTY_SPACE_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_ALLOWED_TO_PERFORM_COMMAND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        another_transition_is_in_progress: _response_pb2.DefaultError
        already_in_the_requested_security_state: _response_pb2.DefaultError
        illegal_space_security_mode: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_blocked_by_service_provider: _response_pb2.DefaultError
        hub_alarm_reset_required: _response_pb2.DefaultError
        hub_detected_malfunctions: _response_pb2.HubDetectedMalfunctionsError
        space_locked: _response_pb2.SpaceLockedError
        action_is_limited_in_empty_space: _response_pb2.DefaultError
        hub_not_allowed_to_perform_command: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            another_transition_is_in_progress: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            already_in_the_requested_security_state: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            illegal_space_security_mode: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_blocked_by_service_provider: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_alarm_reset_required: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_detected_malfunctions: _response_pb2.HubDetectedMalfunctionsError
            | _Mapping
            | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
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
    failure: ArmSpaceResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: ArmSpaceResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
