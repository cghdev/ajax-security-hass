from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    accounting_company_pb2 as _accounting_company_pb2,
)
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.hubobject.model.company import (
    company_info_pb2 as _company_info_pb2,
)
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionOwner(_message.Message):
    __slots__ = ("accounting_company", "company", "user")
    class User(_message.Message):
        __slots__ = ("first_name", "images", "last_name", "user_hex_id", "user_role")
        USER_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        USER_ROLE_FIELD_NUMBER: _ClassVar[int]
        user_hex_id: str
        first_name: str
        last_name: str
        images: _image_pb2.Images
        user_role: _user_role_pb2.UserRole
        def __init__(
            self,
            user_hex_id: str | None = ...,
            first_name: str | None = ...,
            last_name: str | None = ...,
            images: _image_pb2.Images | _Mapping | None = ...,
            user_role: _user_role_pb2.UserRole | str | None = ...,
        ) -> None: ...

    USER_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTING_COMPANY_FIELD_NUMBER: _ClassVar[int]
    user: SubscriptionOwner.User
    company: _company_info_pb2.CompanyInfo
    accounting_company: _accounting_company_pb2.AccountingCompany
    def __init__(
        self,
        user: SubscriptionOwner.User | _Mapping | None = ...,
        company: _company_info_pb2.CompanyInfo | _Mapping | None = ...,
        accounting_company: _accounting_company_pb2.AccountingCompany
        | _Mapping
        | None = ...,
    ) -> None: ...
