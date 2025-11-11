from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import (
    firmware_version_pb2 as _firmware_version_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeFirmwareId(_message.Message):
    __slots__ = ("firmware_version", "platform_name", "product_type")
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    product_type: str
    platform_name: str
    firmware_version: _firmware_version_pb2.FirmwareVersion
    def __init__(
        self,
        product_type: str | None = ...,
        platform_name: str | None = ...,
        firmware_version: _firmware_version_pb2.FirmwareVersion | _Mapping | None = ...,
    ) -> None: ...
