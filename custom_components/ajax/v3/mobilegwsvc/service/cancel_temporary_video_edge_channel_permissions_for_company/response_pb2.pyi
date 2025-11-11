from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CancelTemporaryVideoEdgeChannelPermissionsForCompanyResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "company_not_found",
            "permission_denied",
            "space_armed",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        COMPANY_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        company_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            company_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CancelTemporaryVideoEdgeChannelPermissionsForCompanyResponse.Success
    failure: CancelTemporaryVideoEdgeChannelPermissionsForCompanyResponse.Failure
    def __init__(
        self,
        success: CancelTemporaryVideoEdgeChannelPermissionsForCompanyResponse.Success
        | _Mapping
        | None = ...,
        failure: CancelTemporaryVideoEdgeChannelPermissionsForCompanyResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
