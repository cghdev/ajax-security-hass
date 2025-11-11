from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = (
        "email",
        "end_user_agreement_version",
        "first_name",
        "images",
        "last_name",
        "locale",
        "phone",
        "privacy_notice_version",
        "privacy_policy_version",
        "user_hex_id",
    )
    USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    END_USER_AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_NOTICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    user_hex_id: str
    first_name: str
    last_name: str
    locale: str
    email: str
    phone: str
    images: _image_pb2.Images
    end_user_agreement_version: int
    privacy_policy_version: int
    privacy_notice_version: int
    def __init__(
        self,
        user_hex_id: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        locale: str | None = ...,
        email: str | None = ...,
        phone: str | None = ...,
        images: _image_pb2.Images | _Mapping | None = ...,
        end_user_agreement_version: int | None = ...,
        privacy_policy_version: int | None = ...,
        privacy_notice_version: int | None = ...,
    ) -> None: ...
