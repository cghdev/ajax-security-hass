from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshSmartLocksResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "smart_lock_not_found",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        smart_lock_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            smart_lock_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RefreshSmartLocksResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: RefreshSmartLocksResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
