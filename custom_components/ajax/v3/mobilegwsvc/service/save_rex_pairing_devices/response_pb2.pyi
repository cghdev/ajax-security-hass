from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SaveRexPairingDevicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_busy",
            "hub_offline",
            "hub_wrong_state",
            "permission_denied",
            "rex_offline",
            "wrong_parameters",
        )
        class RexOfflineError(_message.Message):
            __slots__ = ("rex_name",)
            REX_NAME_FIELD_NUMBER: _ClassVar[int]
            rex_name: str
            def __init__(self, rex_name: str | None = ...) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        REX_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        WRONG_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_wrong_state: _response_pb2.HubWrongStateError
        rex_offline: SaveRexPairingDevicesResponse.Failure.RexOfflineError
        wrong_parameters: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            rex_offline: SaveRexPairingDevicesResponse.Failure.RexOfflineError
            | _Mapping
            | None = ...,
            wrong_parameters: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: SaveRexPairingDevicesResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: SaveRexPairingDevicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
