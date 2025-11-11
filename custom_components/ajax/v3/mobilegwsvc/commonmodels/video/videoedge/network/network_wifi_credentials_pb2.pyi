from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkWifiCredentials(_message.Message):
    __slots__ = ("none", "psk")
    class PSK(_message.Message):
        __slots__ = ("password",)
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        password: str
        def __init__(self, password: str | None = ...) -> None: ...

    NONE_FIELD_NUMBER: _ClassVar[int]
    PSK_FIELD_NUMBER: _ClassVar[int]
    none: _empty_pb2.Empty
    psk: NetworkWifiCredentials.PSK
    def __init__(
        self,
        none: _empty_pb2.Empty | _Mapping | None = ...,
        psk: NetworkWifiCredentials.PSK | _Mapping | None = ...,
    ) -> None: ...
