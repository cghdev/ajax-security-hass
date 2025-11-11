from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from ajax.svep.v1 import network_interface_pb2 as _network_interface_pb2
from ajax.svep.v1 import network_pb2 as _network_pb2
from ajax.video.v1.types import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConfigurationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NCS_NONE: _ClassVar[NetworkConfigurationState]
    NCS_OK: _ClassVar[NetworkConfigurationState]
    NCS_FAILED: _ClassVar[NetworkConfigurationState]

class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    E_OTHER: _ClassVar[Error]
    E_UNKNOWN: _ClassVar[Error]
    E_UNIMPLEMENTED: _ClassVar[Error]
    E_INVALID_STATE: _ClassVar[Error]
    E_NETWORK_INTERFACE_NOT_FOUND: _ClassVar[Error]
    E_NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS: _ClassVar[Error]
    E_NETWORK_INTERFACE_INVALID_REQUEST: _ClassVar[Error]

NCS_NONE: NetworkConfigurationState
NCS_OK: NetworkConfigurationState
NCS_FAILED: NetworkConfigurationState
E_OTHER: Error
E_UNKNOWN: Error
E_UNIMPLEMENTED: Error
E_INVALID_STATE: Error
E_NETWORK_INTERFACE_NOT_FOUND: Error
E_NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS: Error
E_NETWORK_INTERFACE_INVALID_REQUEST: Error

class ClientMsg(_message.Message):
    __slots__ = ("encrypted_msg", "sec1", "sec2")
    SEC1_FIELD_NUMBER: _ClassVar[int]
    SEC2_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_MSG_FIELD_NUMBER: _ClassVar[int]
    sec1: Sec1Request
    sec2: Sec2Request
    encrypted_msg: EncryptedMsg
    def __init__(
        self,
        sec1: Sec1Request | _Mapping | None = ...,
        sec2: Sec2Request | _Mapping | None = ...,
        encrypted_msg: EncryptedMsg | _Mapping | None = ...,
    ) -> None: ...

class ServerMsg(_message.Message):
    __slots__ = ("encrypted_msg", "sec1", "sec2")
    SEC1_FIELD_NUMBER: _ClassVar[int]
    SEC2_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_MSG_FIELD_NUMBER: _ClassVar[int]
    sec1: Sec1Response
    sec2: Sec2Response
    encrypted_msg: EncryptedMsg
    def __init__(
        self,
        sec1: Sec1Response | _Mapping | None = ...,
        sec2: Sec2Response | _Mapping | None = ...,
        encrypted_msg: EncryptedMsg | _Mapping | None = ...,
    ) -> None: ...

class Sec1Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Sec1Response(_message.Message):
    __slots__ = ("cert", "nonce")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    nonce: str
    cert: str
    def __init__(self, nonce: str | None = ..., cert: str | None = ...) -> None: ...

class Sec2Request(_message.Message):
    __slots__ = ("encrypted_key", "encrypted_key_signature", "hash_algorithm")
    HASH_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    hash_algorithm: _types_pb2.CryptoHashAlgorithm
    encrypted_key: bytes
    encrypted_key_signature: bytes
    def __init__(
        self,
        hash_algorithm: _types_pb2.CryptoHashAlgorithm | str | None = ...,
        encrypted_key: bytes | None = ...,
        encrypted_key_signature: bytes | None = ...,
    ) -> None: ...

class Sec2Response(_message.Message):
    __slots__ = ("is_ok",)
    IS_OK_FIELD_NUMBER: _ClassVar[int]
    is_ok: bool
    def __init__(self, is_ok: bool = ...) -> None: ...

class EncryptedMsg(_message.Message):
    __slots__ = ("data", "iv", "tag")
    DATA_FIELD_NUMBER: _ClassVar[int]
    IV_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    iv: bytes
    tag: bytes
    def __init__(
        self, data: bytes | None = ..., iv: bytes | None = ..., tag: bytes | None = ...
    ) -> None: ...

class ClientSecMsg(_message.Message):
    __slots__ = (
        "hello",
        "network_update_configuration",
        "network_wifi_scan",
        "ping",
        "seq_no",
    )
    SEQ_NO_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UPDATE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_WIFI_SCAN_FIELD_NUMBER: _ClassVar[int]
    seq_no: int
    hello: HelloRequest
    ping: PingRequest
    network_update_configuration: NetworkUpdateConfigurationRequest
    network_wifi_scan: NetworkWifiScanRequest
    def __init__(
        self,
        seq_no: int | None = ...,
        hello: HelloRequest | _Mapping | None = ...,
        ping: PingRequest | _Mapping | None = ...,
        network_update_configuration: NetworkUpdateConfigurationRequest
        | _Mapping
        | None = ...,
        network_wifi_scan: NetworkWifiScanRequest | _Mapping | None = ...,
    ) -> None: ...

class ServerSecMsg(_message.Message):
    __slots__ = (
        "change",
        "error",
        "hello",
        "network_configuration_state",
        "network_update_configuration",
        "network_wifi_scan",
        "ping",
        "seq_no",
    )
    SEQ_NO_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIGURATION_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UPDATE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_WIFI_SCAN_FIELD_NUMBER: _ClassVar[int]
    seq_no: int
    change: StateChange
    network_configuration_state: NetworkConfigurationState
    error: Error
    hello: HelloResponse
    ping: PingResponse
    network_update_configuration: NetworkUpdateConfigurationResponse
    network_wifi_scan: NetworkWifiScanResponse
    def __init__(
        self,
        seq_no: int | None = ...,
        change: StateChange | _Mapping | None = ...,
        network_configuration_state: NetworkConfigurationState | str | None = ...,
        error: Error | str | None = ...,
        hello: HelloResponse | _Mapping | None = ...,
        ping: PingResponse | _Mapping | None = ...,
        network_update_configuration: NetworkUpdateConfigurationResponse
        | _Mapping
        | None = ...,
        network_wifi_scan: NetworkWifiScanResponse | _Mapping | None = ...,
    ) -> None: ...

class StateChange(_message.Message):
    __slots__ = ("mask", "network", "network_interface", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[StateChange.Type]
        UPDATE: _ClassVar[StateChange.Type]
        ADD: _ClassVar[StateChange.Type]
        REMOVE: _ClassVar[StateChange.Type]

    NONE: StateChange.Type
    UPDATE: StateChange.Type
    ADD: StateChange.Type
    REMOVE: StateChange.Type
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    network: _network_pb2.Network
    network_interface: _network_interface_pb2.NetworkInterface
    mask: _field_mask_pb2.FieldMask
    type: StateChange.Type
    def __init__(
        self,
        network: _network_pb2.Network | _Mapping | None = ...,
        network_interface: _network_interface_pb2.NetworkInterface
        | _Mapping
        | None = ...,
        mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        type: StateChange.Type | str | None = ...,
    ) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: Snapshot
    def __init__(self, snapshot: Snapshot | _Mapping | None = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkUpdateConfigurationRequest(_message.Message):
    __slots__ = (
        "configuration_timeout",
        "desired_configuration",
        "network_interface_guid",
        "wifi",
    )
    class Wifi(_message.Message):
        __slots__ = ("credentials", "enabled")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        credentials: _network_interface_pb2.NetworkWifiCredentials
        def __init__(
            self,
            enabled: bool = ...,
            credentials: _network_interface_pb2.NetworkWifiCredentials
            | _Mapping
            | None = ...,
        ) -> None: ...

    NETWORK_INTERFACE_GUID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    network_interface_guid: str
    desired_configuration: _network_interface_pb2.NetworkConfiguration
    wifi: NetworkUpdateConfigurationRequest.Wifi
    configuration_timeout: _duration_pb2.Duration
    def __init__(
        self,
        network_interface_guid: str | None = ...,
        desired_configuration: _network_interface_pb2.NetworkConfiguration
        | _Mapping
        | None = ...,
        wifi: NetworkUpdateConfigurationRequest.Wifi | _Mapping | None = ...,
        configuration_timeout: _duration_pb2.Duration | _Mapping | None = ...,
    ) -> None: ...

class NetworkUpdateConfigurationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkWifiScanRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NetworkWifiScanResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ("network", "network_interfaces")
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    network: _network_pb2.Network
    network_interfaces: _containers.RepeatedCompositeFieldContainer[
        _network_interface_pb2.NetworkInterface
    ]
    def __init__(
        self,
        network: _network_pb2.Network | _Mapping | None = ...,
        network_interfaces: _Iterable[
            _network_interface_pb2.NetworkInterface | _Mapping
        ]
        | None = ...,
    ) -> None: ...
