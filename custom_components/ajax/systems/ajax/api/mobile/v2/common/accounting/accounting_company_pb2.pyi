from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    service_type_pb2 as _service_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AccountingCompany(_message.Message):
    __slots__ = ("companyHexId", "details", "name", "service_type")
    COMPANYHEXID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    companyHexId: str
    name: str
    service_type: _service_type_pb2.ServiceType
    details: CompanyDetails
    def __init__(
        self,
        companyHexId: str | None = ...,
        name: str | None = ...,
        service_type: _service_type_pb2.ServiceType | str | None = ...,
        details: CompanyDetails | _Mapping | None = ...,
    ) -> None: ...

class CompanyContact(_message.Message):
    __slots__ = ("description", "phone_number")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    description: str
    def __init__(
        self, phone_number: str | None = ..., description: str | None = ...
    ) -> None: ...

class CompanyDetails(_message.Message):
    __slots__ = ("contacts", "emails", "logo_url", "web_site_url")
    WEB_SITE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    web_site_url: str
    contacts: _containers.RepeatedCompositeFieldContainer[CompanyContact]
    emails: _containers.RepeatedScalarFieldContainer[str]
    logo_url: str
    def __init__(
        self,
        web_site_url: str | None = ...,
        contacts: _Iterable[CompanyContact | _Mapping] | None = ...,
        emails: _Iterable[str] | None = ...,
        logo_url: str | None = ...,
    ) -> None: ...
