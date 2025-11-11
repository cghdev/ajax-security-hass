from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareIdInfo(_message.Message):
    __slots__ = (
        "device_band",
        "device_hw_version",
        "device_subtype",
        "device_type",
        "fw_version",
    )
    FW_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HW_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BAND_FIELD_NUMBER: _ClassVar[int]
    fw_version: str
    device_type: int
    device_subtype: int
    device_hw_version: str
    device_band: int
    def __init__(
        self,
        fw_version: str | None = ...,
        device_type: int | None = ...,
        device_subtype: int | None = ...,
        device_hw_version: str | None = ...,
        device_band: int | None = ...,
    ) -> None: ...
