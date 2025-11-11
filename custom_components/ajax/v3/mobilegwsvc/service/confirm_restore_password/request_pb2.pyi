from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmRestorePasswordRequest(_message.Message):
    __slots__ = (
        "email_or_phone",
        "mail_token",
        "new_password_sha256_hash",
        "phone_token",
        "user_role",
    )
    EMAIL_OR_PHONE_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    PHONE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_SHA256_HASH_FIELD_NUMBER: _ClassVar[int]
    email_or_phone: str
    user_role: _user_role_pb2.UserRole
    phone_token: str
    mail_token: str
    new_password_sha256_hash: str
    def __init__(
        self,
        email_or_phone: str | None = ...,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        phone_token: str | None = ...,
        mail_token: str | None = ...,
        new_password_sha256_hash: str | None = ...,
    ) -> None: ...
