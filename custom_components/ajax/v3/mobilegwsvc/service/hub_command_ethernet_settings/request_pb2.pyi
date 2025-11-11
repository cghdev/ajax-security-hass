from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommandEthernetSettingsRequest(_message.Message):
    __slots__ = ("dhcp", "dns", "gate", "hub_id", "ip", "mask")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DHCP_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    GATE_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    dhcp: bool
    ip: str
    mask: str
    gate: str
    dns: str
    def __init__(
        self,
        hub_id: str | None = ...,
        dhcp: bool = ...,
        ip: str | None = ...,
        mask: str | None = ...,
        gate: str | None = ...,
        dns: str | None = ...,
    ) -> None: ...
