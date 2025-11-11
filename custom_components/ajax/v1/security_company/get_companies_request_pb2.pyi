from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompaniesRequest(_message.Message):
    __slots__ = ("country_code", "hub_hex_id")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    hub_hex_id: str
    def __init__(
        self, country_code: str | None = ..., hub_hex_id: str | None = ...
    ) -> None: ...
