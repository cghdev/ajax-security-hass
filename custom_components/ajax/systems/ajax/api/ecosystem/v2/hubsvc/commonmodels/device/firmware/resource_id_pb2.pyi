from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceId(_message.Message):
    __slots__ = ("firmware_id",)
    class FirmwareId(_message.Message):
        __slots__ = (
            "device_hardware_version",
            "device_object_subtype",
            "device_object_type",
            "firmware_band_type",
            "firmware_version",
        )
        DEVICE_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_OBJECT_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_BAND_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        device_object_type: int
        device_object_subtype: int
        device_hardware_version: str
        firmware_band_type: int
        firmware_version: str
        def __init__(
            self,
            device_object_type: int | None = ...,
            device_object_subtype: int | None = ...,
            device_hardware_version: str | None = ...,
            firmware_band_type: int | None = ...,
            firmware_version: str | None = ...,
        ) -> None: ...

    FIRMWARE_ID_FIELD_NUMBER: _ClassVar[int]
    firmware_id: ResourceId.FirmwareId
    def __init__(
        self, firmware_id: ResourceId.FirmwareId | _Mapping | None = ...
    ) -> None: ...
