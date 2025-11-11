from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetVaelsysCameraTokenResponse(_message.Message):
    __slots__ = ("error", "success")
    class Success(_message.Message):
        __slots__ = ("external_user_id", "token")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_USER_ID_FIELD_NUMBER: _ClassVar[int]
        token: str
        external_user_id: str
        def __init__(
            self, token: str | None = ..., external_user_id: str | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(
            self, bad_request: _response_pb2.Error | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetVaelsysCameraTokenResponse.Success
    error: GetVaelsysCameraTokenResponse.Failure
    def __init__(
        self,
        success: GetVaelsysCameraTokenResponse.Success | _Mapping | None = ...,
        error: GetVaelsysCameraTokenResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
