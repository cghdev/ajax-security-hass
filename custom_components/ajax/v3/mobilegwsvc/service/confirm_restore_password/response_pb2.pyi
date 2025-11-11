from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmRestorePasswordResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("account_locked", "bad_request", "invalid_confirmation_token")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        INVALID_CONFIRMATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        account_locked: _response_pb2.Error
        invalid_confirmation_token: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            account_locked: _response_pb2.Error | _Mapping | None = ...,
            invalid_confirmation_token: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ConfirmRestorePasswordResponse.Success
    failure: ConfirmRestorePasswordResponse.Failure
    def __init__(
        self,
        success: ConfirmRestorePasswordResponse.Success | _Mapping | None = ...,
        failure: ConfirmRestorePasswordResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
