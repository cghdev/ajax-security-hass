from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AskBluetoothDirectConnectAccessRequest(_message.Message):
    __slots__ = (
        "crypto_cipher_algorithm",
        "crypto_hash_algorithm",
        "nonce",
        "space_locator",
        "video_edge_certificate",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CIPHER_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_certificate: str
    nonce: str
    crypto_cipher_algorithm: _types_pb2.CryptoCipherAlgorithm
    crypto_hash_algorithm: _types_pb2.CryptoHashAlgorithm
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_certificate: str | None = ...,
        nonce: str | None = ...,
        crypto_cipher_algorithm: _types_pb2.CryptoCipherAlgorithm | str | None = ...,
        crypto_hash_algorithm: _types_pb2.CryptoHashAlgorithm | str | None = ...,
    ) -> None: ...

class AskBluetoothDirectConnectAccessResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("encrypted_key", "encrypted_key_signature", "raw_key")
        RAW_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_KEY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        raw_key: bytes
        encrypted_key: bytes
        encrypted_key_signature: bytes
        def __init__(
            self,
            raw_key: bytes | None = ...,
            encrypted_key: bytes | None = ...,
            encrypted_key_signature: bytes | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "space_not_disarmed",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_DISARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_not_disarmed: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_disarmed: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AskBluetoothDirectConnectAccessResponse.Success
    failure: AskBluetoothDirectConnectAccessResponse.Failure
    def __init__(
        self,
        success: AskBluetoothDirectConnectAccessResponse.Success
        | _Mapping
        | None = ...,
        failure: AskBluetoothDirectConnectAccessResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
