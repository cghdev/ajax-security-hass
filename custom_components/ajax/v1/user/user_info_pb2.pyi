from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.common import image_urls_pb2 as _image_urls_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UserInfo(_message.Message):
    __slots__ = (
        "cluster_user_id",
        "email",
        "end_user_agreement_version",
        "first_name",
        "image_urls",
        "last_name",
        "locale",
        "phone",
        "privacy_policy_version",
    )
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    END_USER_AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_VERSION_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    locale: str
    email: str
    phone: str
    image_urls: _image_urls_pb2.ImageUrls
    cluster_user_id: str
    end_user_agreement_version: int
    privacy_policy_version: int
    def __init__(
        self,
        first_name: str | None = ...,
        last_name: str | None = ...,
        locale: str | None = ...,
        email: str | None = ...,
        phone: str | None = ...,
        image_urls: _image_urls_pb2.ImageUrls | _Mapping | None = ...,
        cluster_user_id: str | None = ...,
        end_user_agreement_version: int | None = ...,
        privacy_policy_version: int | None = ...,
    ) -> None: ...
