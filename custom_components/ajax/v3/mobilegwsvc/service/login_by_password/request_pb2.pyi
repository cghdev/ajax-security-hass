from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LoginByPasswordRequest(_message.Message):
    __slots__ = ("email", "password_sha256_hash", "user_role")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    email: str
    password_sha256_hash: str
    user_role: _user_role_pb2.UserRole
    def __init__(
        self,
        email: str | None = ...,
        password_sha256_hash: str | None = ...,
        user_role: _user_role_pb2.UserRole | str | None = ...,
    ) -> None: ...
