from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_transmission_power_mode_pb2 as _device_transmission_power_mode_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTransmissionPowerModePart(_message.Message):
    __slots__ = ("device_transmission_power_mode",)
    class DeviceTransmissionPowerModePartSettings(_message.Message):
        __slots__ = ("device_transmission_power_mode",)
        DEVICE_TRANSMISSION_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
        device_transmission_power_mode: (
            _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
        )
        def __init__(
            self,
            device_transmission_power_mode: _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
            | str
            | None = ...,
        ) -> None: ...

    DEVICE_TRANSMISSION_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    device_transmission_power_mode: (
        _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
    )
    def __init__(
        self,
        device_transmission_power_mode: _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
        | str
        | None = ...,
    ) -> None: ...
