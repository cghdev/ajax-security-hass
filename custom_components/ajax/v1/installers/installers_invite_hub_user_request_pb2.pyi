from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class InstallersInviteHubUserRequest(_message.Message):
    __slots__ = ("hub_hex_id", "hub_user_id")
    HUB_USER_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hub_user_id: str
    hub_hex_id: str
    def __init__(
        self, hub_user_id: str | None = ..., hub_hex_id: str | None = ...
    ) -> None: ...
