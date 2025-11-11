from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class PendingMember(_message.Message):
    __slots__ = ("email", "sorting_key")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    email: str
    sorting_key: str
    def __init__(
        self, email: str | None = ..., sorting_key: str | None = ...
    ) -> None: ...
