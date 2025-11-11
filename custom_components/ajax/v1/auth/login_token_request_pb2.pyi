from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class LoginTokenRequest(_message.Message):
    __slots__ = ("login", "machine_id", "token")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    login: str
    token: str
    machine_id: str
    def __init__(
        self,
        login: str | None = ...,
        token: str | None = ...,
        machine_id: str | None = ...,
    ) -> None: ...
