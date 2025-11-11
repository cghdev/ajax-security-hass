from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandManageLinesPowerSupplyResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_request_already_performed",
            "hub_unknown_command",
            "hub_wrong_state",
            "permission_denied",
        )
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_REQUEST_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        hub_offline: _response_pb2.Error
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_unknown_command: _response_pb2.Error
        hub_error: _response_pb2.Error
        hub_request_already_performed: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_wrong_state: _response_pb2.HubWrongStateError
        def __init__(
            self,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_unknown_command: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            hub_request_already_performed: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeviceCommandManageLinesPowerSupplyResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: DeviceCommandManageLinesPowerSupplyResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
