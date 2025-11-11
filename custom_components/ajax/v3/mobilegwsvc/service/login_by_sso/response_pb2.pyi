from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.auth import login_response_pb2 as _login_response_pb2
from v1.user import user_company_pb2 as _user_company_pb2
from v3.mobilegwsvc.commonmodels.account import lite_account_pb2 as _lite_account_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LoginBySsoResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("company_list", "login_response", "sign_on_url_response")
        class SignOnUrlResponse(_message.Message):
            __slots__ = ("request_id", "sign_on_url")
            SIGN_ON_URL_FIELD_NUMBER: _ClassVar[int]
            REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
            sign_on_url: str
            request_id: str
            def __init__(
                self, sign_on_url: str | None = ..., request_id: str | None = ...
            ) -> None: ...

        class LoginResponse(_message.Message):
            __slots__ = (
                "a911_session_token",
                "lite_account",
                "pro_login_response",
                "user_company",
                "user_id",
                "user_session_token",
            )
            USER_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            LITE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
            USER_ID_FIELD_NUMBER: _ClassVar[int]
            A911_SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            USER_COMPANY_FIELD_NUMBER: _ClassVar[int]
            PRO_LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
            user_session_token: bytes
            lite_account: _lite_account_pb2.LiteAccount
            user_id: str
            a911_session_token: str
            user_company: _user_company_pb2.UserCompany
            pro_login_response: _login_response_pb2.LoginResponse
            def __init__(
                self,
                user_session_token: bytes | None = ...,
                lite_account: _lite_account_pb2.LiteAccount | _Mapping | None = ...,
                user_id: str | None = ...,
                a911_session_token: str | None = ...,
                user_company: _user_company_pb2.UserCompany | _Mapping | None = ...,
                pro_login_response: _login_response_pb2.LoginResponse
                | _Mapping
                | None = ...,
            ) -> None: ...

        SIGN_ON_URL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        LOGIN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        COMPANY_LIST_FIELD_NUMBER: _ClassVar[int]
        sign_on_url_response: LoginBySsoResponse.Success.SignOnUrlResponse
        login_response: LoginBySsoResponse.Success.LoginResponse
        company_list: LoginBySsoResponse.CompanyList
        def __init__(
            self,
            sign_on_url_response: LoginBySsoResponse.Success.SignOnUrlResponse
            | _Mapping
            | None = ...,
            login_response: LoginBySsoResponse.Success.LoginResponse
            | _Mapping
            | None = ...,
            company_list: LoginBySsoResponse.CompanyList | _Mapping | None = ...,
        ) -> None: ...

    class CompanyList(_message.Message):
        __slots__ = ("companies",)
        COMPANIES_FIELD_NUMBER: _ClassVar[int]
        companies: _containers.RepeatedCompositeFieldContainer[
            _user_company_pb2.UserCompany
        ]
        def __init__(
            self,
            companies: _Iterable[_user_company_pb2.UserCompany | _Mapping] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "account_locked",
            "account_not_confirmed",
            "bad_request",
            "sso_config_not_found",
            "unauthenticated",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SSO_CONFIG_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        UNAUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NOT_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        sso_config_not_found: _response_pb2.Error
        unauthenticated: _response_pb2.Error
        account_not_confirmed: _response_pb2.Error
        account_locked: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            sso_config_not_found: _response_pb2.Error | _Mapping | None = ...,
            unauthenticated: _response_pb2.Error | _Mapping | None = ...,
            account_not_confirmed: _response_pb2.Error | _Mapping | None = ...,
            account_locked: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: LoginBySsoResponse.Success
    failure: LoginBySsoResponse.Failure
    def __init__(
        self,
        success: LoginBySsoResponse.Success | _Mapping | None = ...,
        failure: LoginBySsoResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
