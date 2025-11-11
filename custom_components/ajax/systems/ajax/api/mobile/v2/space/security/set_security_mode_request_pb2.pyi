from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetSecurityModeRequest(_message.Message):
    __slots__ = ("mode", "space_locator")
    class SecurityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SetSecurityModeRequest.SecurityMode]
        REGULAR: _ClassVar[SetSecurityModeRequest.SecurityMode]
        GROUP: _ClassVar[SetSecurityModeRequest.SecurityMode]

    NONE: SetSecurityModeRequest.SecurityMode
    REGULAR: SetSecurityModeRequest.SecurityMode
    GROUP: SetSecurityModeRequest.SecurityMode
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    mode: SetSecurityModeRequest.SecurityMode
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        mode: SetSecurityModeRequest.SecurityMode | str | None = ...,
    ) -> None: ...

class SetSecurityModeResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_wrong_state",
            "permission_denied",
            "security_mode_already_enabled",
            "some_devices_without_groups",
            "space_armed",
            "space_locked",
            "space_not_found",
            "space_without_groups",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_WITHOUT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SOME_DEVICES_WITHOUT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        SECURITY_MODE_ALREADY_ENABLED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_without_groups: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        some_devices_without_groups: _response_pb2.DefaultError
        security_mode_already_enabled: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_without_groups: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            some_devices_without_groups: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            security_mode_already_enabled: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SetSecurityModeResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: SetSecurityModeResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
