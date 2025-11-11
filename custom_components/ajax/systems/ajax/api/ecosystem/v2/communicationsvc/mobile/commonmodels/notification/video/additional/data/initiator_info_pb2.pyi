from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorInfo(_message.Message):
    __slots__ = ("initiator_id", "initiator_name")
    INITIATOR_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    initiator_id: str
    initiator_name: str
    def __init__(
        self, initiator_id: str | None = ..., initiator_name: str | None = ...
    ) -> None: ...
