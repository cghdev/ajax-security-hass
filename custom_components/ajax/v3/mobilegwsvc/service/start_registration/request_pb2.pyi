from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.type import (
    phone_validation_type_pb2 as _phone_validation_type_pb2,
)
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StartRegistrationRequest(_message.Message):
    __slots__ = (
        "company_name",
        "company_website",
        "email",
        "first_name",
        "last_name",
        "locale",
        "news_subscription",
        "password",
        "phone_number",
        "phone_validation_type",
        "recaptcha_site_key",
        "recaptcha_token",
        "user_role",
    )
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PHONE_VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NEWS_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_SITE_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_WEBSITE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    user_role: _user_role_pb2.UserRole
    email: str
    phone_number: str
    first_name: str
    last_name: str
    password: str
    phone_validation_type: _phone_validation_type_pb2.PhoneValidationType
    locale: str
    news_subscription: bool
    recaptcha_token: str
    recaptcha_site_key: str
    company_website: str
    company_name: str
    def __init__(
        self,
        user_role: _user_role_pb2.UserRole | str | None = ...,
        email: str | None = ...,
        phone_number: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        password: str | None = ...,
        phone_validation_type: _phone_validation_type_pb2.PhoneValidationType
        | str
        | None = ...,
        locale: str | None = ...,
        news_subscription: bool = ...,
        recaptcha_token: str | None = ...,
        recaptcha_site_key: str | None = ...,
        company_website: str | None = ...,
        company_name: str | None = ...,
    ) -> None: ...
