from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class PushTokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUSH_TOKEN_TYPE_UNSPECIFIED: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_REGULAR: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_SANDBOX: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_AOS_FCM: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL_MUTABLE: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL_MUTABLE: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR: _ClassVar[PushTokenType]
    PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR_SANDBOX: _ClassVar[PushTokenType]

PUSH_TOKEN_TYPE_UNSPECIFIED: PushTokenType
PUSH_TOKEN_TYPE_IOS_REGULAR: PushTokenType
PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL: PushTokenType
PUSH_TOKEN_TYPE_IOS_SANDBOX: PushTokenType
PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL: PushTokenType
PUSH_TOKEN_TYPE_AOS_FCM: PushTokenType
PUSH_TOKEN_TYPE_IOS_REGULAR_CRITICAL_MUTABLE: PushTokenType
PUSH_TOKEN_TYPE_IOS_SANDBOX_CRITICAL_MUTABLE: PushTokenType
PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR: PushTokenType
PUSH_TOKEN_TYPE_APPLE_WATCH_REGULAR_SANDBOX: PushTokenType

class UpsertPushTokenRequest(_message.Message):
    __slots__ = (
        "push_token",
        "push_token_type",
        "user_hex_id",
        "user_role",
        "voip_push_token",
    )
    USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    PUSH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PUSH_TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    VOIP_PUSH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_hex_id: str
    user_role: _user_role_pb2.UserRole
    push_token: str
    push_token_type: PushTokenType
    voip_push_token: str
    def __init__(
        self,
        user_hex_id: str | None = ...,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        push_token: str | None = ...,
        push_token_type: PushTokenType | str | None = ...,
        voip_push_token: str | None = ...,
    ) -> None: ...
