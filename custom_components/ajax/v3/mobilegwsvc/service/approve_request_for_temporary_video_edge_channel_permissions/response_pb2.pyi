from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveRequestForTemporaryVideoEdgeChannelPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "request_cannot_be_approved",
            "request_expired",
            "request_not_found",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        REQUEST_EXPIRED_FIELD_NUMBER: _ClassVar[int]
        REQUEST_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        REQUEST_CANNOT_BE_APPROVED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        request_expired: _response_pb2.Error
        request_not_found: _response_pb2.Error
        request_cannot_be_approved: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            request_expired: _response_pb2.Error | _Mapping | None = ...,
            request_not_found: _response_pb2.Error | _Mapping | None = ...,
            request_cannot_be_approved: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ApproveRequestForTemporaryVideoEdgeChannelPermissionsResponse.Success
    failure: ApproveRequestForTemporaryVideoEdgeChannelPermissionsResponse.Failure
    def __init__(
        self,
        success: ApproveRequestForTemporaryVideoEdgeChannelPermissionsResponse.Success
        | _Mapping
        | None = ...,
        failure: ApproveRequestForTemporaryVideoEdgeChannelPermissionsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
