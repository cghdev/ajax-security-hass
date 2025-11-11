from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshSmartLocksRequest(_message.Message):
    __slots__ = ("smart_lock_ids", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_IDS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self, space_id: str | None = ..., smart_lock_ids: _Iterable[str] | None = ...
    ) -> None: ...
