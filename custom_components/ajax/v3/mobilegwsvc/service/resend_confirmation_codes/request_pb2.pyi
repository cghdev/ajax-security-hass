from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import (
    phone_validation_type_pb2 as _phone_validation_type_pb2,
)
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ResendConfirmationCodesRequest(_message.Message):
    __slots__ = ("email", "phone_number", "phone_validation_type", "user_role")
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    email: str
    phone_number: str
    phone_validation_type: _phone_validation_type_pb2.PhoneValidationType
    def __init__(
        self,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        email: str | None = ...,
        phone_number: str | None = ...,
        phone_validation_type: _phone_validation_type_pb2.PhoneValidationType
        | str
        | None = ...,
    ) -> None: ...
