from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.company.templates import (
    device_settings_locator_pb2 as _device_settings_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllApplicableDevicesByTemplateRequest(_message.Message):
    __slots__ = ("device_settings_locator", "space_id")
    DEVICE_SETTINGS_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    device_settings_locator: _device_settings_locator_pb2.DeviceSettingsLocator
    space_id: str
    def __init__(
        self,
        device_settings_locator: _device_settings_locator_pb2.DeviceSettingsLocator
        | _Mapping
        | None = ...,
        space_id: str | None = ...,
    ) -> None: ...
