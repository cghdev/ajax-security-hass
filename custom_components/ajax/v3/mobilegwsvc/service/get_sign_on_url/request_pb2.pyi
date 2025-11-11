from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class GetSignOnUrlRequest(_message.Message):
    __slots__ = ("client_device_id", "email", "relay_state")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RELAY_STATE_FIELD_NUMBER: _ClassVar[int]
    email: str
    client_device_id: str
    relay_state: str
    def __init__(
        self,
        email: str | None = ...,
        client_device_id: str | None = ...,
        relay_state: str | None = ...,
    ) -> None: ...
