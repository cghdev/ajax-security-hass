from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CheckIsCaptchaRequiredForNumberRequest(_message.Message):
    __slots__ = ("phone_number",)
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    def __init__(self, phone_number: str | None = ...) -> None: ...
