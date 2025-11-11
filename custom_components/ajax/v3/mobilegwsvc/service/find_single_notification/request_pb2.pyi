from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FindSingleNotificationRequest(_message.Message):
    __slots__ = ("notification_id", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    notification_id: str
    def __init__(
        self, space_id: str | None = ..., notification_id: str | None = ...
    ) -> None: ...
