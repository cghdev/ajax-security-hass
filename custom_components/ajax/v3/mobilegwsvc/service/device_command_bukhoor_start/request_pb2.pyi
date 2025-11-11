from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandBukhoorStartRequest(_message.Message):
    __slots__ = ("hub_id", "number_of_seconds_for_bukhoor")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_SECONDS_FOR_BUKHOOR_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    number_of_seconds_for_bukhoor: int
    def __init__(
        self, hub_id: str | None = ..., number_of_seconds_for_bukhoor: int | None = ...
    ) -> None: ...
