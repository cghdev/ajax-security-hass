from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common import strings_pb2 as _strings_pb2
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company import (
    phod_devices_rights_feasibility_pb2 as _phod_devices_rights_feasibility_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyInfo(_message.Message):
    __slots__ = (
        "available_in",
        "cobranded_status",
        "emails",
        "hex_id",
        "logo",
        "name",
        "phod_devices_company_rights_feasibility",
        "phones",
        "web_page_url",
    )
    class CobrandedStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COBRANDED_STATUS_UNSPECIFIED: _ClassVar[CompanyInfo.CobrandedStatus]
        COBRANDED_STATUS_ON: _ClassVar[CompanyInfo.CobrandedStatus]
        COBRANDED_STATUS_OFF: _ClassVar[CompanyInfo.CobrandedStatus]

    COBRANDED_STATUS_UNSPECIFIED: CompanyInfo.CobrandedStatus
    COBRANDED_STATUS_ON: CompanyInfo.CobrandedStatus
    COBRANDED_STATUS_OFF: CompanyInfo.CobrandedStatus
    class PhoneNumber(_message.Message):
        __slots__ = ("number", "phone_description")
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        PHONE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        number: _wrappers_pb2.StringValue
        phone_description: _wrappers_pb2.StringValue
        def __init__(
            self,
            number: _wrappers_pb2.StringValue | _Mapping | None = ...,
            phone_description: _wrappers_pb2.StringValue | _Mapping | None = ...,
        ) -> None: ...

    class PhoneNumbers(_message.Message):
        __slots__ = ("phoneNumbers",)
        PHONENUMBERS_FIELD_NUMBER: _ClassVar[int]
        phoneNumbers: _containers.RepeatedCompositeFieldContainer[
            CompanyInfo.PhoneNumber
        ]
        def __init__(
            self,
            phoneNumbers: _Iterable[CompanyInfo.PhoneNumber | _Mapping] | None = ...,
        ) -> None: ...

    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    WEB_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_IN_FIELD_NUMBER: _ClassVar[int]
    PHOD_DEVICES_COMPANY_RIGHTS_FEASIBILITY_FIELD_NUMBER: _ClassVar[int]
    COBRANDED_STATUS_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    name: _wrappers_pb2.StringValue
    logo: _image_pb2.Images
    emails: _strings_pb2.Strings
    phones: CompanyInfo.PhoneNumbers
    web_page_url: _wrappers_pb2.StringValue
    available_in: _strings_pb2.Strings
    phod_devices_company_rights_feasibility: (
        _phod_devices_rights_feasibility_pb2.PhodDevicesRightsFeasibility
    )
    cobranded_status: CompanyInfo.CobrandedStatus
    def __init__(
        self,
        hex_id: str | None = ...,
        name: _wrappers_pb2.StringValue | _Mapping | None = ...,
        logo: _image_pb2.Images | _Mapping | None = ...,
        emails: _strings_pb2.Strings | _Mapping | None = ...,
        phones: CompanyInfo.PhoneNumbers | _Mapping | None = ...,
        web_page_url: _wrappers_pb2.StringValue | _Mapping | None = ...,
        available_in: _strings_pb2.Strings | _Mapping | None = ...,
        phod_devices_company_rights_feasibility: _phod_devices_rights_feasibility_pb2.PhodDevicesRightsFeasibility
        | str
        | None = ...,
        cobranded_status: CompanyInfo.CobrandedStatus | str | None = ...,
    ) -> None: ...
