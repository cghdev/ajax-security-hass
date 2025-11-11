from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMemberInfo(_message.Message):
    __slots__ = ("name", "space_member_id")
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    space_member_id: str
    name: str
    def __init__(
        self, space_member_id: str | None = ..., name: str | None = ...
    ) -> None: ...
