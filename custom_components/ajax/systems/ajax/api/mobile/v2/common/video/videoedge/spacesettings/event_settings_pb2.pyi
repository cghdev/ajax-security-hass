from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class EventSettings(_message.Message):
    __slots__ = ("muteConnectionAlarms",)
    MUTECONNECTIONALARMS_FIELD_NUMBER: _ClassVar[int]
    muteConnectionAlarms: bool
    def __init__(self, muteConnectionAlarms: bool = ...) -> None: ...
