from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.hubobject.model.company import (
    company_info_pb2 as _company_info_pb2,
)
from v3.mobilegwsvc.commonmodels.company import (
    company_provided_service_pb2 as _company_provided_service_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LiteSpaceCompany(_message.Message):
    __slots__ = (
        "company_info",
        "company_provided_services",
        "hub_user_index",
        "sorting_key",
        "space_member_id",
    )
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_PROVIDED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    company_info: _company_info_pb2.CompanyInfo
    space_member_id: str
    hub_user_index: int
    sorting_key: str
    company_provided_services: _containers.RepeatedScalarFieldContainer[
        _company_provided_service_pb2.CompanyProvidedService
    ]
    def __init__(
        self,
        company_info: _company_info_pb2.CompanyInfo | _Mapping | None = ...,
        space_member_id: str | None = ...,
        hub_user_index: int | None = ...,
        sorting_key: str | None = ...,
        company_provided_services: _Iterable[
            _company_provided_service_pb2.CompanyProvidedService | str
        ]
        | None = ...,
    ) -> None: ...
