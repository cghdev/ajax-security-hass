from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company.additional.data import (
    permission_claim_type_pb2 as _permission_claim_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyPermissionsClaimRequest(_message.Message):
    __slots__ = ("company_mail", "company_name", "permissions_type", "request_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_MAIL_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    company_name: str
    company_mail: str
    permissions_type: _permission_claim_type_pb2.PermissionsClaimType
    def __init__(
        self,
        request_id: str | None = ...,
        company_name: str | None = ...,
        company_mail: str | None = ...,
        permissions_type: _permission_claim_type_pb2.PermissionsClaimType
        | _Mapping
        | None = ...,
    ) -> None: ...
