from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCrossZoneResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("cross_zone_id",)
        CROSS_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
        cross_zone_id: str
        def __init__(self, cross_zone_id: str | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_busy",
            "hub_error",
            "hub_not_found",
            "hub_offline",
            "hub_wrong_state",
            "illegal_argument",
            "object_limit_exceeded",
            "permission_denied",
            "request_timeout",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        OBJECT_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        object_limit_exceeded: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        request_timeout: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_error: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_wrong_state: _response_pb2.HubWrongStateError
        hub_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            object_limit_exceeded: _response_pb2.Error | _Mapping | None = ...,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            request_timeout: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateCrossZoneResponse.Success
    failure: CreateCrossZoneResponse.Failure
    def __init__(
        self,
        success: CreateCrossZoneResponse.Success | _Mapping | None = ...,
        failure: CreateCrossZoneResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
