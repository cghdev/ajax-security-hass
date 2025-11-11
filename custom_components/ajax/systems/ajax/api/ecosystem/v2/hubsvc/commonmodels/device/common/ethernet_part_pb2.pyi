from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class EthernetPart(_message.Message):
    __slots__ = (
        "capabilities",
        "ethernet_status",
        "gate",
        "ip",
        "is_dhcp_enabled",
        "is_ethernet_enabled",
        "mac_address",
        "mask",
    )
    class EthernetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ETHERNET_STATUS_UNSPECIFIED: _ClassVar[EthernetPart.EthernetStatus]
        ETHERNET_STATUS_NOT_OK: _ClassVar[EthernetPart.EthernetStatus]
        ETHERNET_STATUS_OK: _ClassVar[EthernetPart.EthernetStatus]

    ETHERNET_STATUS_UNSPECIFIED: EthernetPart.EthernetStatus
    ETHERNET_STATUS_NOT_OK: EthernetPart.EthernetStatus
    ETHERNET_STATUS_OK: EthernetPart.EthernetStatus
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[EthernetPart.Capability]
        CAPABILITY_ETHERNET: _ClassVar[EthernetPart.Capability]

    CAPABILITY_UNSPECIFIED: EthernetPart.Capability
    CAPABILITY_ETHERNET: EthernetPart.Capability
    ETHERNET_STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_ETHERNET_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DHCP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    GATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    ethernet_status: EthernetPart.EthernetStatus
    is_ethernet_enabled: bool
    is_dhcp_enabled: bool
    mac_address: str
    ip: str
    mask: str
    gate: str
    capabilities: _containers.RepeatedScalarFieldContainer[EthernetPart.Capability]
    def __init__(
        self,
        ethernet_status: EthernetPart.EthernetStatus | str | None = ...,
        is_ethernet_enabled: bool = ...,
        is_dhcp_enabled: bool = ...,
        mac_address: str | None = ...,
        ip: str | None = ...,
        mask: str | None = ...,
        gate: str | None = ...,
        capabilities: _Iterable[EthernetPart.Capability | str] | None = ...,
    ) -> None: ...
