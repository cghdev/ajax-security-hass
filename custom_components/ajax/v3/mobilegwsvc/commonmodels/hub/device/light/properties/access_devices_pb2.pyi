from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class AccessDevices(_message.Message):
    __slots__ = ("quantity",)
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    def __init__(self, quantity: int | None = ...) -> None: ...
