from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyForMonitoringWithAccountNumberRequest(_message.Message):
    __slots__ = ("account_number", "company_hex_id", "hub_hex_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    company_hex_id: str
    account_number: str
    def __init__(
        self,
        hub_hex_id: str | None = ...,
        company_hex_id: str | None = ...,
        account_number: str | None = ...,
    ) -> None: ...

class ApplyForMonitoringWithAccountNumberResponse(_message.Message):
    __slots__ = ("error", "success")
    class Failure(_message.Message):
        __slots__ = (
            "account_number_invalid",
            "cannot_apply_on_locked_hub",
            "hub_users_limit_exceeded",
            "message",
            "permission_denied",
            "request_timeout",
        )
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        CANNOT_APPLY_ON_LOCKED_HUB_FIELD_NUMBER: _ClassVar[int]
        HUB_USERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_INVALID_FIELD_NUMBER: _ClassVar[int]
        message: str
        request_timeout: _response_pb2.DefaultError
        cannot_apply_on_locked_hub: _response_pb2.DefaultError
        hub_users_limit_exceeded: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        account_number_invalid: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            request_timeout: _response_pb2.DefaultError | _Mapping | None = ...,
            cannot_apply_on_locked_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_users_limit_exceeded: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            account_number_invalid: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    error: ApplyForMonitoringWithAccountNumberResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        error: ApplyForMonitoringWithAccountNumberResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
