from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteDeviceFromHubRequest(_message.Message):
    __slots__ = ("device_id", "hub_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    def __init__(
        self, hub_id: str | None = ..., device_id: str | None = ...
    ) -> None: ...
