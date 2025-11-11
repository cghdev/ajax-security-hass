from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSmartLockCredentialRequest(_message.Message):
    __slots__ = ("credential_id", "device_id", "device_type", "hub_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    credential_id: str
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        credential_id: str | None = ...,
    ) -> None: ...
