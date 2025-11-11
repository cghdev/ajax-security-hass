from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NewUserSession(_message.Message):
    __slots__ = ("client_os", "device_model", "last_connection_ip", "sessionId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_OS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTION_IP_FIELD_NUMBER: _ClassVar[int]
    sessionId: int
    client_os: str
    device_model: str
    last_connection_ip: str
    def __init__(
        self,
        sessionId: int | None = ...,
        client_os: str | None = ...,
        device_model: str | None = ...,
        last_connection_ip: str | None = ...,
    ) -> None: ...
