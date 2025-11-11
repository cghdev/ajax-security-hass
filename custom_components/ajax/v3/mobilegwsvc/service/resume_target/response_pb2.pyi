from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ResumeTargetResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "illegal_state", "resume_failed")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        RESUME_FAILED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        illegal_state: _response_pb2.Error
        resume_failed: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            illegal_state: _response_pb2.Error | _Mapping | None = ...,
            resume_failed: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ResumeTargetResponse.Success
    failure: ResumeTargetResponse.Failure
    def __init__(
        self,
        success: ResumeTargetResponse.Success | _Mapping | None = ...,
        failure: ResumeTargetResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
