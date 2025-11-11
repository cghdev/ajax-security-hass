from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmUserDeletionRequest(_message.Message):
    __slots__ = ("email_otp_code", "phone_otp_code")
    PHONE_OTP_CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_OTP_CODE_FIELD_NUMBER: _ClassVar[int]
    phone_otp_code: str
    email_otp_code: str
    def __init__(
        self, phone_otp_code: str | None = ..., email_otp_code: str | None = ...
    ) -> None: ...

class ConfirmUserDeletionResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = ("otp_code_invalid", "user_not_found")
        OTP_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
        USER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        otp_code_invalid: _response_pb2.DefaultError
        user_not_found: _response_pb2.DefaultError
        def __init__(
            self,
            otp_code_invalid: _response_pb2.DefaultError | _Mapping | None = ...,
            user_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: ConfirmUserDeletionResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: ConfirmUserDeletionResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
