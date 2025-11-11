from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.hub.device.common import (
    device_radio_test_type_pb2 as _device_radio_test_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamRadioTestRequest(_message.Message):
    __slots__ = ("device_id", "hub_id", "type")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    type: _device_radio_test_type_pb2.DeviceRadioTestType
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        type: _device_radio_test_type_pb2.DeviceRadioTestType | str | None = ...,
    ) -> None: ...
