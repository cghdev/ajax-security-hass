from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LiteAccount(_message.Message):
    __slots__ = (
        "email",
        "end_user_agreement_version",
        "first_name",
        "last_name",
        "locale",
        "privacy_notice_version",
        "privacy_policy_version",
        "user_hex_id",
        "user_role",
    )
    USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    END_USER_AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_NOTICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    user_hex_id: str
    user_role: _user_role_pb2.UserRole
    first_name: str
    last_name: str
    locale: str
    end_user_agreement_version: int
    privacy_policy_version: int
    email: str
    privacy_notice_version: int
    def __init__(
        self,
        user_hex_id: str | None = ...,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        locale: str | None = ...,
        end_user_agreement_version: int | None = ...,
        privacy_policy_version: int | None = ...,
        email: str | None = ...,
        privacy_notice_version: int | None = ...,
    ) -> None: ...
