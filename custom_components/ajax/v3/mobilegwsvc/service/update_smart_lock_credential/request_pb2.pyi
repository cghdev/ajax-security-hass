from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSmartLockCredentialRequest(_message.Message):
    __slots__ = ("credential", "device_id", "device_type", "hub_id")
    class SmartLockCredentialToUpdate(_message.Message):
        __slots__ = ("code", "enabled", "id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        enabled: bool
        code: str
        def __init__(
            self,
            id: str | None = ...,
            name: str | None = ...,
            enabled: bool = ...,
            code: str | None = ...,
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    credential: UpdateSmartLockCredentialRequest.SmartLockCredentialToUpdate
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        credential: UpdateSmartLockCredentialRequest.SmartLockCredentialToUpdate
        | _Mapping
        | None = ...,
    ) -> None: ...
