from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSmartLockCredentialResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "cannot_delete_last_credential",
            "command_not_performed",
            "delivered_was_already_performed",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_wrong_state",
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
        CANNOT_DELETE_LAST_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        hub_offline: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        command_not_performed: _response_pb2.Error
        delivered_was_already_performed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        object_not_found: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        cannot_delete_last_credential: _response_pb2.Error
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
            cannot_delete_last_credential: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSmartLockCredentialResponse.Success
    failure: DeleteSmartLockCredentialResponse.Failure
    def __init__(
        self,
        success: DeleteSmartLockCredentialResponse.Success | _Mapping | None = ...,
        failure: DeleteSmartLockCredentialResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
