from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmNewAccountRequest(_message.Message):
    __slots__ = ("email", "email_token", "phone_token", "user_role")
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    email: str
    phone_token: str
    email_token: str
    def __init__(
        self,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        email: str | None = ...,
        phone_token: str | None = ...,
        email_token: str | None = ...,
    ) -> None: ...
