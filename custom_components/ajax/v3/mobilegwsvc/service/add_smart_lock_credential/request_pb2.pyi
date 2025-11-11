from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AddSmartLockCredentialRequest(_message.Message):
    __slots__ = ("credential", "device_id", "device_type", "hub_id")
    class SmartLockCredentialToAdd(_message.Message):
        __slots__ = ("contactless_key", "entry_code", "name")
        class EntryCode(_message.Message):
            __slots__ = ("code",)
            CODE_FIELD_NUMBER: _ClassVar[int]
            code: str
            def __init__(self, code: str | None = ...) -> None: ...

        class ContactlessKey(_message.Message):
            __slots__ = ("code",)
            CODE_FIELD_NUMBER: _ClassVar[int]
            code: str
            def __init__(self, code: str | None = ...) -> None: ...

        NAME_FIELD_NUMBER: _ClassVar[int]
        ENTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        CONTACTLESS_KEY_FIELD_NUMBER: _ClassVar[int]
        name: str
        entry_code: AddSmartLockCredentialRequest.SmartLockCredentialToAdd.EntryCode
        contactless_key: (
            AddSmartLockCredentialRequest.SmartLockCredentialToAdd.ContactlessKey
        )
        def __init__(
            self,
            name: str | None = ...,
            entry_code: AddSmartLockCredentialRequest.SmartLockCredentialToAdd.EntryCode
            | _Mapping
            | None = ...,
            contactless_key: AddSmartLockCredentialRequest.SmartLockCredentialToAdd.ContactlessKey
            | _Mapping
            | None = ...,
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    credential: AddSmartLockCredentialRequest.SmartLockCredentialToAdd
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        credential: AddSmartLockCredentialRequest.SmartLockCredentialToAdd
        | _Mapping
        | None = ...,
    ) -> None: ...
