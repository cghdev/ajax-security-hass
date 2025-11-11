from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Storage(_message.Message):
    __slots__ = ("num_ports", "temperature_threshold")
    TEMPERATURE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NUM_PORTS_FIELD_NUMBER: _ClassVar[int]
    temperature_threshold: int
    num_ports: int
    def __init__(
        self, temperature_threshold: int | None = ..., num_ports: int | None = ...
    ) -> None: ...
