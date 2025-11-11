from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METHOD_UNSPECIFIED: _ClassVar[Method]
    METHOD_OFF: _ClassVar[Method]
    METHOD_DHCP: _ClassVar[Method]
    METHOD_MANUAL: _ClassVar[Method]

METHOD_UNSPECIFIED: Method
METHOD_OFF: Method
METHOD_DHCP: Method
METHOD_MANUAL: Method

class IpAddress(_message.Message):
    __slots__ = ("v4", "v6")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    v4: IpAddressV4
    v6: IpAddressV6
    def __init__(
        self,
        v4: IpAddressV4 | _Mapping | None = ...,
        v6: IpAddressV6 | _Mapping | None = ...,
    ) -> None: ...

class IpAddressV4(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: int | None = ...) -> None: ...

class IpAddressV6(_message.Message):
    __slots__ = ("data", "scope_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    scope_id: int
    def __init__(
        self, data: bytes | None = ..., scope_id: int | None = ...
    ) -> None: ...

class NetworkConfiguration(_message.Message):
    __slots__ = ("name_servers", "v4", "v6")
    V4_FIELD_NUMBER: _ClassVar[int]
    V6_FIELD_NUMBER: _ClassVar[int]
    NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
    v4: NetworkConfigurationIPv4
    v6: NetworkConfigurationIPv6
    name_servers: _containers.RepeatedCompositeFieldContainer[IpAddress]
    def __init__(
        self,
        v4: NetworkConfigurationIPv4 | _Mapping | None = ...,
        v6: NetworkConfigurationIPv6 | _Mapping | None = ...,
        name_servers: _Iterable[IpAddress | _Mapping] | None = ...,
    ) -> None: ...

class NetworkConfigurationIPv4(_message.Message):
    __slots__ = ("address", "gateway", "method", "netmask")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: Method
    address: IpAddressV4
    netmask: IpAddressV4
    gateway: IpAddressV4
    def __init__(
        self,
        method: Method | str | None = ...,
        address: IpAddressV4 | _Mapping | None = ...,
        netmask: IpAddressV4 | _Mapping | None = ...,
        gateway: IpAddressV4 | _Mapping | None = ...,
    ) -> None: ...

class NetworkConfigurationIPv6(_message.Message):
    __slots__ = ("address", "gateway", "method", "prefix_length")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    method: Method
    address: IpAddressV6
    prefix_length: int
    gateway: IpAddressV6
    def __init__(
        self,
        method: Method | str | None = ...,
        address: IpAddressV6 | _Mapping | None = ...,
        prefix_length: int | None = ...,
        gateway: IpAddressV6 | _Mapping | None = ...,
    ) -> None: ...
