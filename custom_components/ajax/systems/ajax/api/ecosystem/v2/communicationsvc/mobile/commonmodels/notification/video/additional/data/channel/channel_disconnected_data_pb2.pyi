from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelDisconnectedData(_message.Message):
    __slots__ = ("channel_id", "channel_name")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    channel_name: str
    def __init__(
        self, channel_id: str | None = ..., channel_name: str | None = ...
    ) -> None: ...
