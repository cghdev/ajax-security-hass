from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    permission_claim_type_pb2 as _permission_claim_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ProPermissionsClaim(_message.Message):
    __slots__ = (
        "hub_hex_id",
        "permissions_type",
        "pro_id",
        "pro_mail",
        "pro_name",
        "request_id",
    )
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    PRO_NAME_FIELD_NUMBER: _ClassVar[int]
    PRO_MAIL_FIELD_NUMBER: _ClassVar[int]
    PRO_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    hub_hex_id: str
    pro_name: str
    pro_mail: str
    pro_id: str
    permissions_type: _permission_claim_type_pb2.PermissionsClaimType
    def __init__(
        self,
        request_id: str | None = ...,
        hub_hex_id: str | None = ...,
        pro_name: str | None = ...,
        pro_mail: str | None = ...,
        pro_id: str | None = ...,
        permissions_type: _permission_claim_type_pb2.PermissionsClaimType
        | _Mapping
        | None = ...,
    ) -> None: ...
