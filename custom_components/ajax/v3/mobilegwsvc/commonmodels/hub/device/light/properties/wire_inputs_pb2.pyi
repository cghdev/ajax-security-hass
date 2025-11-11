from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class WireInputs(_message.Message):
    __slots__ = ("is_malfunction", "quantity")
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    IS_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    is_malfunction: bool
    def __init__(
        self, quantity: int | None = ..., is_malfunction: bool = ...
    ) -> None: ...
