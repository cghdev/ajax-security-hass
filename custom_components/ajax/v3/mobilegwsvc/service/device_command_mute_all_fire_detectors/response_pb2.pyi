from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandMuteAllFireDetectorsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "command_not_performed",
            "delivered_was_already_performed",
            "hub_busy",
            "hub_offline",
            "hub_wrong_state",
            "permission_denied",
            "unknown_command",
        )
        UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        DELIVERED_WAS_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        unknown_command: _response_pb2.Error
        command_not_performed: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        delivered_was_already_performed: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        def __init__(
            self,
            unknown_command: _response_pb2.Error | _Mapping | None = ...,
            command_not_performed: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            delivered_was_already_performed: _response_pb2.Error
            | _Mapping
            | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeviceCommandMuteAllFireDetectorsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: DeviceCommandMuteAllFireDetectorsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
