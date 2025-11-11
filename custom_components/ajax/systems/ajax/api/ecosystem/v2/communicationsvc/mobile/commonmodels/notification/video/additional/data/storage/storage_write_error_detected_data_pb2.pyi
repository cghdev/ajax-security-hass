from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.storage import (
    storage_device_port_number_pb2 as _storage_device_port_number_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StorageWriteErrorDetectedData(_message.Message):
    __slots__ = ("storage_device_port_number", "storage_id")
    STORAGE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    storage_id: str
    storage_device_port_number: _storage_device_port_number_pb2.StorageDevicePortNumber
    def __init__(
        self,
        storage_id: str | None = ...,
        storage_device_port_number: _storage_device_port_number_pb2.StorageDevicePortNumber
        | _Mapping
        | None = ...,
    ) -> None: ...
