from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class RestorePasswordRequest(_message.Message):
    __slots__ = ("email_or_phone", "user_role")
    EMAIL_OR_PHONE_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    email_or_phone: str
    user_role: _user_role_pb2.UserRole
    def __init__(
        self,
        email_or_phone: str | None = ...,
        user_role: _user_role_pb2.UserRole | str | None = ...,
    ) -> None: ...
