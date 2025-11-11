from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeNetworkConfigurationRequest(_message.Message):
    __slots__ = (
        "dns",
        "ip_configuration_v4",
        "network_interface_id",
        "space_id",
        "video_edge_id",
    )
    class IpConfigurationV4(_message.Message):
        __slots__ = ("dhcp", "static")
        class DhcpConfigurationV4(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class StaticConfigurationV4(_message.Message):
            __slots__ = ("address", "gateway", "netmask")
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            NETMASK_FIELD_NUMBER: _ClassVar[int]
            GATEWAY_FIELD_NUMBER: _ClassVar[int]
            address: _types_pb2.IpAddressV4
            netmask: _types_pb2.IpAddressV4
            gateway: _types_pb2.IpAddressV4
            def __init__(
                self,
                address: _types_pb2.IpAddressV4 | _Mapping | None = ...,
                netmask: _types_pb2.IpAddressV4 | _Mapping | None = ...,
                gateway: _types_pb2.IpAddressV4 | _Mapping | None = ...,
            ) -> None: ...

        DHCP_FIELD_NUMBER: _ClassVar[int]
        STATIC_FIELD_NUMBER: _ClassVar[int]
        dhcp: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.DhcpConfigurationV4
        static: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.StaticConfigurationV4
        def __init__(
            self,
            dhcp: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.DhcpConfigurationV4
            | _Mapping
            | None = ...,
            static: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4.StaticConfigurationV4
            | _Mapping
            | None = ...,
        ) -> None: ...

    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIGURATION_V4_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    network_interface_id: str
    ip_configuration_v4: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4
    dns: _containers.RepeatedCompositeFieldContainer[_types_pb2.IpAddress]
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        network_interface_id: str | None = ...,
        ip_configuration_v4: SetVideoEdgeNetworkConfigurationRequest.IpConfigurationV4
        | _Mapping
        | None = ...,
        dns: _Iterable[_types_pb2.IpAddress | _Mapping] | None = ...,
    ) -> None: ...
