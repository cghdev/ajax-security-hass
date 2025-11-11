from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityCompanyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_STATE: _ClassVar[SecurityCompanyStatus]
    PENDING_APPROVAL: _ClassVar[SecurityCompanyStatus]
    APPROVED: _ClassVar[SecurityCompanyStatus]
    PENDING_REMOVAL: _ClassVar[SecurityCompanyStatus]

NO_STATE: SecurityCompanyStatus
PENDING_APPROVAL: SecurityCompanyStatus
APPROVED: SecurityCompanyStatus
PENDING_REMOVAL: SecurityCompanyStatus

class SecurityCompany(_message.Message):
    __slots__ = ("data", "details")
    DATA_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    data: SecurityCompanyData
    details: SecurityCompanyDetails
    def __init__(
        self,
        data: SecurityCompanyData | _Mapping | None = ...,
        details: SecurityCompanyDetails | _Mapping | None = ...,
    ) -> None: ...

class SecurityCompanyPreview(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: SecurityCompanyData
    def __init__(self, data: SecurityCompanyData | _Mapping | None = ...) -> None: ...

class SecurityCompanyData(_message.Message):
    __slots__ = (
        "account_number_required_status",
        "hub_user_index",
        "id",
        "logo_url",
        "monitoring_status",
        "name",
    )
    class AccountNumberRequiredStatus(
        int, metaclass=_enum_type_wrapper.EnumTypeWrapper
    ):
        __slots__ = ()
        ACCOUNT_NUMBER_REQUIRED_STATUS_UNSPECIFIED: _ClassVar[
            SecurityCompanyData.AccountNumberRequiredStatus
        ]
        ACCOUNT_NUMBER_REQUIRED_STATUS_REQUIRED: _ClassVar[
            SecurityCompanyData.AccountNumberRequiredStatus
        ]
        ACCOUNT_NUMBER_REQUIRED_STATUS_NOT_REQUIRED: _ClassVar[
            SecurityCompanyData.AccountNumberRequiredStatus
        ]

    ACCOUNT_NUMBER_REQUIRED_STATUS_UNSPECIFIED: (
        SecurityCompanyData.AccountNumberRequiredStatus
    )
    ACCOUNT_NUMBER_REQUIRED_STATUS_REQUIRED: (
        SecurityCompanyData.AccountNumberRequiredStatus
    )
    ACCOUNT_NUMBER_REQUIRED_STATUS_NOT_REQUIRED: (
        SecurityCompanyData.AccountNumberRequiredStatus
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATUS_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_REQUIRED_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    logo_url: str
    monitoring_status: SecurityCompanyStatus
    hub_user_index: int
    account_number_required_status: SecurityCompanyData.AccountNumberRequiredStatus
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        logo_url: str | None = ...,
        monitoring_status: SecurityCompanyStatus | str | None = ...,
        hub_user_index: int | None = ...,
        account_number_required_status: SecurityCompanyData.AccountNumberRequiredStatus
        | str
        | None = ...,
    ) -> None: ...

class SecurityCompanyContact(_message.Message):
    __slots__ = ("description", "phone_number")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    description: str
    def __init__(
        self, phone_number: str | None = ..., description: str | None = ...
    ) -> None: ...

class SecurityCompanyLocation(_message.Message):
    __slots__ = ("country_code",)
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    def __init__(self, country_code: str | None = ...) -> None: ...

class SecurityCompanyDetails(_message.Message):
    __slots__ = ("contacts", "description", "emails", "locations", "web_site_url")
    WEB_SITE_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    web_site_url: str
    description: str
    locations: _containers.RepeatedCompositeFieldContainer[SecurityCompanyLocation]
    contacts: _containers.RepeatedCompositeFieldContainer[SecurityCompanyContact]
    emails: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        web_site_url: str | None = ...,
        description: str | None = ...,
        locations: _Iterable[SecurityCompanyLocation | _Mapping] | None = ...,
        contacts: _Iterable[SecurityCompanyContact | _Mapping] | None = ...,
        emails: _Iterable[str] | None = ...,
    ) -> None: ...
