from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyForMonitoringRequest(_message.Message):
    __slots__ = ("company_hex_id", "hub_hex_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    company_hex_id: str
    def __init__(
        self, hub_hex_id: str | None = ..., company_hex_id: str | None = ...
    ) -> None: ...
