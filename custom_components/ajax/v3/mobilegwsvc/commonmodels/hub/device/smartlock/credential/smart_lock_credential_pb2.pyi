from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockCredential(_message.Message):
    __slots__ = ("contactless_key", "enabled", "entry_code", "id", "name")
    class EntryCode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ContactlessKey(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTACTLESS_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    enabled: bool
    entry_code: SmartLockCredential.EntryCode
    contactless_key: SmartLockCredential.ContactlessKey
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        enabled: bool = ...,
        entry_code: SmartLockCredential.EntryCode | _Mapping | None = ...,
        contactless_key: SmartLockCredential.ContactlessKey | _Mapping | None = ...,
    ) -> None: ...
