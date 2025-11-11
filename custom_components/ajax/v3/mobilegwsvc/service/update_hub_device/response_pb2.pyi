from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateHubDeviceResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "device_no_found",
            "hub_offline",
            "hub_wrong_state",
            "permission_denied",
        )
        class HubWrongStateError(_message.Message):
            __slots__ = ("error_cause",)
            ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
            error_cause: _containers.RepeatedCompositeFieldContainer[
                _response_pb2.ErrorCause
            ]
            def __init__(
                self,
                error_cause: _Iterable[_response_pb2.ErrorCause | _Mapping]
                | None = ...,
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NO_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        device_no_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_wrong_state: UpdateHubDeviceResponse.Failure.HubWrongStateError
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            device_no_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: UpdateHubDeviceResponse.Failure.HubWrongStateError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateHubDeviceResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: UpdateHubDeviceResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
