from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorInfo(_message.Message):
    __slots__ = ("id", "mail", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    mail: str
    def __init__(
        self, id: str | None = ..., name: str | None = ..., mail: str | None = ...
    ) -> None: ...
