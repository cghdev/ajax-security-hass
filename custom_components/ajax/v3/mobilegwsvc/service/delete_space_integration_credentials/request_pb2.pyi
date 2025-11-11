from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSpaceIntegrationCredentialsRequest(_message.Message):
    __slots__ = ("credentials_id",)
    CREDENTIALS_ID_FIELD_NUMBER: _ClassVar[int]
    credentials_id: str
    def __init__(self, credentials_id: str | None = ...) -> None: ...
