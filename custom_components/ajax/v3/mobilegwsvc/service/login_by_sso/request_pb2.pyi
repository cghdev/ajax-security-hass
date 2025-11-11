from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class LoginBySsoRequest(_message.Message):
    __slots__ = ("client_device_id", "company_id", "email", "relay_state", "request_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RELAY_STATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    client_device_id: str
    relay_state: str
    request_id: str
    company_id: str
    def __init__(
        self,
        email: str | None = ...,
        client_device_id: str | None = ...,
        relay_state: str | None = ...,
        request_id: str | None = ...,
        company_id: str | None = ...,
    ) -> None: ...
