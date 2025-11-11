from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    permission_claim_type_pb2 as _permission_claim_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ProPermissionsClaimResponse(_message.Message):
    __slots__ = (
        "hub_hex_id",
        "permissions_type",
        "pro_id",
        "pro_mail",
        "pro_name",
        "request_id",
        "user_id",
        "user_mail",
        "user_name",
    )
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    PRO_NAME_FIELD_NUMBER: _ClassVar[int]
    PRO_MAIL_FIELD_NUMBER: _ClassVar[int]
    PRO_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_MAIL_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_TYPE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    hub_hex_id: str
    pro_name: str
    pro_mail: str
    pro_id: str
    user_id: str
    user_mail: str
    user_name: str
    permissions_type: _permission_claim_type_pb2.PermissionsClaimType
    def __init__(
        self,
        request_id: str | None = ...,
        hub_hex_id: str | None = ...,
        pro_name: str | None = ...,
        pro_mail: str | None = ...,
        pro_id: str | None = ...,
        user_id: str | None = ...,
        user_mail: str | None = ...,
        user_name: str | None = ...,
        permissions_type: _permission_claim_type_pb2.PermissionsClaimType
        | _Mapping
        | None = ...,
    ) -> None: ...
