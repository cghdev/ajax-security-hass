from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceInstallationCompanyRequest(_message.Message):
    __slots__ = ("company_hex_id", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    company_hex_id: str
    def __init__(
        self, space_id: str | None = ..., company_hex_id: str | None = ...
    ) -> None: ...
