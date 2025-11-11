from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LoginByTotpRequest(_message.Message):
    __slots__ = ("email", "request_id", "totp", "user_role")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    TOTP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    user_role: _user_role_pb2.UserRole
    totp: str
    request_id: str
    def __init__(
        self,
        email: str | None = ...,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        totp: str | None = ...,
        request_id: str | None = ...,
    ) -> None: ...
