from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class HubAddHubRequest(_message.Message):
    __slots__ = ("hub_name", "hub_qr_code")
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    HUB_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    hub_name: str
    hub_qr_code: str
    def __init__(
        self, hub_name: str | None = ..., hub_qr_code: str | None = ...
    ) -> None: ...
