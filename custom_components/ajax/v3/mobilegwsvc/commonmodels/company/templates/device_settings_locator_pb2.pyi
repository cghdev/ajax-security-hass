from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceSettingsLocator(_message.Message):
    __slots__ = ("preset_id", "template_id")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PRESET_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    preset_id: str
    def __init__(
        self, template_id: str | None = ..., preset_id: str | None = ...
    ) -> None: ...
