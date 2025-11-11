from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockCredentialResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "cannot_disable_last_credential",
            "code_not_unique",
            "command_not_performed",
            "delivered_was_already_performed",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_wrong_state",
            "name_not_unique",
            "object_not_found",
            "permission_denied",
        )
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        DELIVERED_WAS_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        OBJECT_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        CODE_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        NAME_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        CANNOT_DISABLE_LAST_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        hub_offline: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        command_not_performed: _response_pb2.Error
        delivered_was_already_performed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        object_not_found: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        code_not_unique: _response_pb2.Error
        name_not_unique: _response_pb2.Error
        cannot_disable_last_credential: _response_pb2.Error
        hub_error: _response_pb2.Error
        bad_request: _response_pb2.Error
        def __init__(
            self,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            command_not_performed: _response_pb2.Error | _Mapping | None = ...,
            delivered_was_already_performed: _response_pb2.Error
            | _Mapping
            | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            object_not_found: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            code_not_unique: _response_pb2.Error | _Mapping | None = ...,
            name_not_unique: _response_pb2.Error | _Mapping | None = ...,
            cannot_disable_last_credential: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UpdateSmartLockCredentialResponse.Success
    failure: UpdateSmartLockCredentialResponse.Failure
    def __init__(
        self,
        success: UpdateSmartLockCredentialResponse.Success | _Mapping | None = ...,
        failure: UpdateSmartLockCredentialResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
