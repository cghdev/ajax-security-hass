from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class UserDeleteVerificationRequest(_message.Message):
    __slots__ = ("email_token", "phone_token")
    PHONE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phone_token: str
    email_token: str
    def __init__(
        self, phone_token: str | None = ..., email_token: str | None = ...
    ) -> None: ...
