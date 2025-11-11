from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.firmware import (
    device_firmware_update_pb2 as _device_firmware_update_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceFirmwareUpdatePart(_message.Message):
    __slots__ = ("capabilities", "device_firmware_update")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[DeviceFirmwareUpdatePart.Capability]
        CAPABILITY_DFU: _ClassVar[DeviceFirmwareUpdatePart.Capability]

    CAPABILITY_UNSPECIFIED: DeviceFirmwareUpdatePart.Capability
    CAPABILITY_DFU: DeviceFirmwareUpdatePart.Capability
    DEVICE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    device_firmware_update: _device_firmware_update_pb2.DeviceFirmwareUpdate
    capabilities: _containers.RepeatedScalarFieldContainer[
        DeviceFirmwareUpdatePart.Capability
    ]
    def __init__(
        self,
        device_firmware_update: _device_firmware_update_pb2.DeviceFirmwareUpdate
        | _Mapping
        | None = ...,
        capabilities: _Iterable[DeviceFirmwareUpdatePart.Capability | str] | None = ...,
    ) -> None: ...
