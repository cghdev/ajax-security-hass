from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Name(_message.Message):
    __slots__ = ("alias", "name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    name: str
    alias: str
    def __init__(self, name: str | None = ..., alias: str | None = ...) -> None: ...
