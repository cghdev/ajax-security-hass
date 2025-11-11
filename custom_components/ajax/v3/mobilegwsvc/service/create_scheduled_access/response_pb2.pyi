from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScheduledAccessResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_wrong_state",
            "permission_denied",
            "schedule_limit",
        )
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        permission_denied: _response_pb2.Error
        bad_request: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        schedule_limit: _response_pb2.Error
        def __init__(
            self,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            schedule_limit: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: CreateScheduledAccessResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: CreateScheduledAccessResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
