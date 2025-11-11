from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    connection_status_pb2 as _connection_status_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_signal_level_pb2 as _device_signal_level_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceTelemetry(_message.Message):
    __slots__ = ("connection_status", "device_signal_level")
    DEVICE_SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    device_signal_level: _device_signal_level_pb2.DeviceSignalLevel
    connection_status: _connection_status_pb2.ConnectionStatus
    def __init__(
        self,
        device_signal_level: _device_signal_level_pb2.DeviceSignalLevel
        | str
        | None = ...,
        connection_status: _connection_status_pb2.ConnectionStatus | str | None = ...,
    ) -> None: ...
