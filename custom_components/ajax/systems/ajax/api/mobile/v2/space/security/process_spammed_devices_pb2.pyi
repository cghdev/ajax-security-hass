from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.device import (
    hub_device_pb2 as _hub_device_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessSpammedDevicesRequest(_message.Message):
    __slots__ = ("space_id", "spammed_hub_devices")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAMMED_HUB_DEVICES_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    spammed_hub_devices: _containers.RepeatedCompositeFieldContainer[
        _hub_device_pb2.HubDevice
    ]
    def __init__(
        self,
        space_id: str | None = ...,
        spammed_hub_devices: _Iterable[_hub_device_pb2.HubDevice | _Mapping]
        | None = ...,
    ) -> None: ...

class ProcessSpammedDevicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "already_in_the_requested_security_state",
            "another_transition_is_in_progress",
            "bad_request",
            "bypass_failed",
            "hub_busy",
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
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_ALLOWED_TO_PERFORM_COMMAND_FIELD_NUMBER: _ClassVar[int]
        BYPASS_FAILED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        another_transition_is_in_progress: _response_pb2.DefaultError
        already_in_the_requested_security_state: _response_pb2.DefaultError
        illegal_space_security_mode: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        space_locked: _response_pb2.SpaceLockedError
        hub_not_allowed_to_perform_command: _response_pb2.DefaultError
        bypass_failed: _response_pb2.DefaultError
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
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            hub_not_allowed_to_perform_command: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            bypass_failed: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: ProcessSpammedDevicesResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: ProcessSpammedDevicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
