from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class LineCrossedData(_message.Message):
    __slots__ = ("rule_id", "rule_name")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    rule_id: int
    rule_name: str
    def __init__(
        self, rule_id: int | None = ..., rule_name: str | None = ...
    ) -> None: ...
