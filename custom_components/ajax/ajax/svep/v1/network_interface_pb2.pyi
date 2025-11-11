from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from ajax.video.v1.types import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NS_NONE: _ClassVar[NetworkState]
    NS_OFFLINE: _ClassVar[NetworkState]
    NS_CONFIGURING: _ClassVar[NetworkState]
    NS_ONLINE: _ClassVar[NetworkState]

class NetworkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NE_OTHER: _ClassVar[NetworkError]
    NE_OK: _ClassVar[NetworkError]
    NE_OUT_OF_RANGE: _ClassVar[NetworkError]
    NE_PIN_MISSING: _ClassVar[NetworkError]
    NE_DHCP_FAILED: _ClassVar[NetworkError]
    NE_CONNECT_FAILED: _ClassVar[NetworkError]
    NE_LOGIN_FAILED: _ClassVar[NetworkError]
    NE_AUTH_FAILED: _ClassVar[NetworkError]
    NE_INVALID_KEY: _ClassVar[NetworkError]
    NE_BLOCKED: _ClassVar[NetworkError]

class NetworkWifiSecurity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NWS_OTHER: _ClassVar[NetworkWifiSecurity]
    NWS_NONE: _ClassVar[NetworkWifiSecurity]
    NWS_WEP: _ClassVar[NetworkWifiSecurity]
    NWS_PSK: _ClassVar[NetworkWifiSecurity]
    NWS_IEEE8021X: _ClassVar[NetworkWifiSecurity]
    NWS_WPS: _ClassVar[NetworkWifiSecurity]

NS_NONE: NetworkState
NS_OFFLINE: NetworkState
NS_CONFIGURING: NetworkState
NS_ONLINE: NetworkState
NE_OTHER: NetworkError
NE_OK: NetworkError
NE_OUT_OF_RANGE: NetworkError
NE_PIN_MISSING: NetworkError
NE_DHCP_FAILED: NetworkError
NE_CONNECT_FAILED: NetworkError
NE_LOGIN_FAILED: NetworkError
NE_AUTH_FAILED: NetworkError
NE_INVALID_KEY: NetworkError
NE_BLOCKED: NetworkError
NWS_OTHER: NetworkWifiSecurity
NWS_NONE: NetworkWifiSecurity
NWS_WEP: NetworkWifiSecurity
NWS_PSK: NetworkWifiSecurity
NWS_IEEE8021X: NetworkWifiSecurity
NWS_WPS: NetworkWifiSecurity

class NetworkInterface(_message.Message):
    __slots__ = (
        "configuration",
        "desired_configuration",
        "enabled",
        "ethernet",
        "guid",
        "mac_address",
        "name",
        "stats",
        "status",
        "wifi",
    )
    class Ethernet(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Wifi(_message.Message):
        __slots__ = ("credentials", "security", "signal_strength")
        SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        SECURITY_FIELD_NUMBER: _ClassVar[int]
        CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        signal_strength: int
        security: _containers.RepeatedScalarFieldContainer[NetworkWifiSecurity]
        credentials: NetworkWifiCredentials
        def __init__(
            self,
            signal_strength: int | None = ...,
            security: _Iterable[NetworkWifiSecurity | str] | None = ...,
            credentials: NetworkWifiCredentials | _Mapping | None = ...,
        ) -> None: ...

    class Stats(_message.Message):
        __slots__ = (
            "rx_bytes",
            "rx_dropped",
            "rx_errors",
            "tx_bytes",
            "tx_dropped",
            "tx_errors",
        )
        TX_BYTES_FIELD_NUMBER: _ClassVar[int]
        RX_BYTES_FIELD_NUMBER: _ClassVar[int]
        TX_ERRORS_FIELD_NUMBER: _ClassVar[int]
        RX_ERRORS_FIELD_NUMBER: _ClassVar[int]
        TX_DROPPED_FIELD_NUMBER: _ClassVar[int]
        RX_DROPPED_FIELD_NUMBER: _ClassVar[int]
        tx_bytes: int
        rx_bytes: int
        tx_errors: int
        rx_errors: int
        tx_dropped: int
        rx_dropped: int
        def __init__(
            self,
            tx_bytes: int | None = ...,
            rx_bytes: int | None = ...,
            tx_errors: int | None = ...,
            rx_errors: int | None = ...,
            tx_dropped: int | None = ...,
            rx_dropped: int | None = ...,
        ) -> None: ...

    GUID_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    guid: str
    mac_address: _types_pb2.MacAddress
    enabled: bool
    ethernet: NetworkInterface.Ethernet
    wifi: NetworkInterface.Wifi
    name: str
    status: NetworkStatus
    desired_configuration: NetworkConfiguration
    configuration: NetworkConfiguration
    stats: NetworkInterface.Stats
    def __init__(
        self,
        guid: str | None = ...,
        mac_address: _types_pb2.MacAddress | _Mapping | None = ...,
        enabled: bool = ...,
        ethernet: NetworkInterface.Ethernet | _Mapping | None = ...,
        wifi: NetworkInterface.Wifi | _Mapping | None = ...,
        name: str | None = ...,
        status: NetworkStatus | _Mapping | None = ...,
        desired_configuration: NetworkConfiguration | _Mapping | None = ...,
        configuration: NetworkConfiguration | _Mapping | None = ...,
        stats: NetworkInterface.Stats | _Mapping | None = ...,
    ) -> None: ...

class NetworkStatus(_message.Message):
    __slots__ = ("error", "state")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: NetworkState
    error: NetworkError
    def __init__(
        self,
        state: NetworkState | str | None = ...,
        error: NetworkError | str | None = ...,
    ) -> None: ...

class NetworkConfiguration(_message.Message):
    __slots__ = ("name_servers", "v4", "v6")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
    v4: NetworkConfigurationIPv4
    v6: NetworkConfigurationIPv6
    name_servers: _containers.RepeatedCompositeFieldContainer[_types_pb2.IpAddress]
    def __init__(
        self,
        v4: NetworkConfigurationIPv4 | _Mapping | None = ...,
        v6: NetworkConfigurationIPv6 | _Mapping | None = ...,
        name_servers: _Iterable[_types_pb2.IpAddress | _Mapping] | None = ...,
    ) -> None: ...

class NetworkConfigurationIPv4(_message.Message):
    __slots__ = ("address", "gateway", "method", "netmask")
    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[NetworkConfigurationIPv4.Method]
        OFF: _ClassVar[NetworkConfigurationIPv4.Method]
        DHCP: _ClassVar[NetworkConfigurationIPv4.Method]
        MANUAL: _ClassVar[NetworkConfigurationIPv4.Method]

    NONE: NetworkConfigurationIPv4.Method
    OFF: NetworkConfigurationIPv4.Method
    DHCP: NetworkConfigurationIPv4.Method
    MANUAL: NetworkConfigurationIPv4.Method
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: NetworkConfigurationIPv4.Method
    address: _types_pb2.IpAddressV4
    netmask: _types_pb2.IpAddressV4
    gateway: _types_pb2.IpAddressV4
    def __init__(
        self,
        method: NetworkConfigurationIPv4.Method | str | None = ...,
        address: _types_pb2.IpAddressV4 | _Mapping | None = ...,
        netmask: _types_pb2.IpAddressV4 | _Mapping | None = ...,
        gateway: _types_pb2.IpAddressV4 | _Mapping | None = ...,
    ) -> None: ...

class NetworkConfigurationIPv6(_message.Message):
    __slots__ = ("address", "gateway", "method", "prefix_length")
    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[NetworkConfigurationIPv6.Method]
        OFF: _ClassVar[NetworkConfigurationIPv6.Method]
        AUTO: _ClassVar[NetworkConfigurationIPv6.Method]
        MANUAL: _ClassVar[NetworkConfigurationIPv6.Method]

    NONE: NetworkConfigurationIPv6.Method
    OFF: NetworkConfigurationIPv6.Method
    AUTO: NetworkConfigurationIPv6.Method
    MANUAL: NetworkConfigurationIPv6.Method
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: NetworkConfigurationIPv6.Method
    address: _types_pb2.IpAddressV6
    prefix_length: int
    gateway: _types_pb2.IpAddressV6
    def __init__(
        self,
        method: NetworkConfigurationIPv6.Method | str | None = ...,
        address: _types_pb2.IpAddressV6 | _Mapping | None = ...,
        prefix_length: int | None = ...,
        gateway: _types_pb2.IpAddressV6 | _Mapping | None = ...,
    ) -> None: ...

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
