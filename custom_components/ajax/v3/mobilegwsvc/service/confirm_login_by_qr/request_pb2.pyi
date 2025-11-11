from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ConfirmLoginByQrRequest(_message.Message):
    __slots__ = ("qr_session_key",)
    QR_SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    qr_session_key: bytes
    def __init__(self, qr_session_key: bytes | None = ...) -> None: ...
