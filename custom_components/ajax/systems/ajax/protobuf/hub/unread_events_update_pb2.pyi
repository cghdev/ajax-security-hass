from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class UnreadEventsUpdate(_message.Message):
    __slots__ = ("event_count", "hub_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    event_count: int
    def __init__(
        self, hub_id: str | None = ..., event_count: int | None = ...
    ) -> None: ...
