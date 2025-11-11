from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AskVideoEdgeDirectConnectAccessRequest(_message.Message):
    __slots__ = (
        "access_protocol",
        "crypto_cipher_algorithm",
        "crypto_hash_algorithm",
        "nonce",
        "space_locator",
        "video_edge_certificate",
        "video_edge_id",
    )
    class AccessProtocol(_message.Message):
        __slots__ = ("bluetooth", "wi_fi")
        BLUETOOTH_FIELD_NUMBER: _ClassVar[int]
        WI_FI_FIELD_NUMBER: _ClassVar[int]
        bluetooth: AskVideoEdgeDirectConnectAccessRequest.Bluetooth
        wi_fi: AskVideoEdgeDirectConnectAccessRequest.WiFi
        def __init__(
            self,
            bluetooth: AskVideoEdgeDirectConnectAccessRequest.Bluetooth
            | _Mapping
            | None = ...,
            wi_fi: AskVideoEdgeDirectConnectAccessRequest.WiFi | _Mapping | None = ...,
        ) -> None: ...

    class Bluetooth(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class WiFi(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CIPHER_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ACCESS_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_certificate: str
    video_edge_id: str
    nonce: str
    crypto_cipher_algorithm: _types_pb2.CryptoCipherAlgorithm
    crypto_hash_algorithm: _types_pb2.CryptoHashAlgorithm
    access_protocol: AskVideoEdgeDirectConnectAccessRequest.AccessProtocol
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_certificate: str | None = ...,
        video_edge_id: str | None = ...,
        nonce: str | None = ...,
        crypto_cipher_algorithm: _types_pb2.CryptoCipherAlgorithm | str | None = ...,
        crypto_hash_algorithm: _types_pb2.CryptoHashAlgorithm | str | None = ...,
        access_protocol: AskVideoEdgeDirectConnectAccessRequest.AccessProtocol
        | _Mapping
        | None = ...,
    ) -> None: ...
