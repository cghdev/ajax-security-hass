from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdateFinishedData(_message.Message):
    __slots__ = ("firmware_id",)
    class VideoEdgeFirmwareId(_message.Message):
        __slots__ = ("firmware_version", "platform_name", "product_type")
        class FirmwareVersion(_message.Message):
            __slots__ = ("extra", "major", "minor")
            MAJOR_FIELD_NUMBER: _ClassVar[int]
            MINOR_FIELD_NUMBER: _ClassVar[int]
            EXTRA_FIELD_NUMBER: _ClassVar[int]
            major: int
            minor: int
            extra: str
            def __init__(
                self,
                major: int | None = ...,
                minor: int | None = ...,
                extra: str | None = ...,
            ) -> None: ...

        PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        product_type: str
        platform_name: str
        firmware_version: FirmwareUpdateFinishedData.VideoEdgeFirmwareId.FirmwareVersion
        def __init__(
            self,
            product_type: str | None = ...,
            platform_name: str | None = ...,
            firmware_version: FirmwareUpdateFinishedData.VideoEdgeFirmwareId.FirmwareVersion
            | _Mapping
            | None = ...,
        ) -> None: ...

    FIRMWARE_ID_FIELD_NUMBER: _ClassVar[int]
    firmware_id: FirmwareUpdateFinishedData.VideoEdgeFirmwareId
    def __init__(
        self,
        firmware_id: FirmwareUpdateFinishedData.VideoEdgeFirmwareId
        | _Mapping
        | None = ...,
    ) -> None: ...
