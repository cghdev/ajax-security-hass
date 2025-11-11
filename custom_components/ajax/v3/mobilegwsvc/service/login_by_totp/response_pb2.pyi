from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.auth import login_response_pb2 as _login_response_pb2
from v3.mobilegwsvc.commonmodels.account import lite_account_pb2 as _lite_account_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LoginByTotpResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("lite_account", "pro_login_response", "session_token")
        SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        LITE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PRO_LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        session_token: bytes
        lite_account: _lite_account_pb2.LiteAccount
        pro_login_response: _login_response_pb2.LoginResponse
        def __init__(
            self,
            session_token: bytes | None = ...,
            lite_account: _lite_account_pb2.LiteAccount | _Mapping | None = ...,
            pro_login_response: _login_response_pb2.LoginResponse
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "account_locked",
            "account_not_confirmed",
            "bad_request",
            "invalid_totp",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NOT_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        INVALID_TOTP_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        account_not_confirmed: _response_pb2.Error
        account_locked: _response_pb2.Error
        invalid_totp: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            account_not_confirmed: _response_pb2.Error | _Mapping | None = ...,
            account_locked: _response_pb2.Error | _Mapping | None = ...,
            invalid_totp: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: LoginByTotpResponse.Success
    failure: LoginByTotpResponse.Failure
    def __init__(
        self,
        success: LoginByTotpResponse.Success | _Mapping | None = ...,
        failure: LoginByTotpResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
