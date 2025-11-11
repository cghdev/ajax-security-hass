from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompanyRequest(_message.Message):
    __slots__ = ("company_id", "hub_hex_id")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    hub_hex_id: str
    def __init__(
        self, company_id: str | None = ..., hub_hex_id: str | None = ...
    ) -> None: ...
