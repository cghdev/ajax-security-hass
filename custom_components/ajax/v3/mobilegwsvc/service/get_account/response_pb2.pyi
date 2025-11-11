from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.account import account_pb2 as _account_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetAccountResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("account",)
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        account: _account_pb2.Account
        def __init__(
            self, account: _account_pb2.Account | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAccountResponse.Success
    failure: GetAccountResponse.Failure
    def __init__(
        self,
        success: GetAccountResponse.Success | _Mapping | None = ...,
        failure: GetAccountResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
