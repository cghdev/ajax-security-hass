from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER: _ClassVar[UserRole]
    PRO: _ClassVar[UserRole]
    COMPANY: _ClassVar[UserRole]

USER: UserRole
PRO: UserRole
COMPANY: UserRole

class LoginRequest(_message.Message):
    __slots__ = ("login", "password", "user_role")
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    login: str
    password: str
    user_role: UserRole
    def __init__(
        self,
        login: str | None = ...,
        password: str | None = ...,
        user_role: UserRole | str | None = ...,
    ) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "user_id",
        "user_role",
    )
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_role: UserRole
    email: str
    first_name: str
    last_name: str
    phone_number: str
    def __init__(
        self,
        user_id: str | None = ...,
        user_role: UserRole | str | None = ...,
        email: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        phone_number: str | None = ...,
    ) -> None: ...
