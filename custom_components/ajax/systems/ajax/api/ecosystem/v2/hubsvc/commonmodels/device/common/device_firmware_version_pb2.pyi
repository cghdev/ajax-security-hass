from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    hub_rfm_pb2 as _hub_rfm_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceFirmwareVersion(_message.Message):
    __slots__ = ("hub_rfm", "value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    HUB_RFM_FIELD_NUMBER: _ClassVar[int]
    value: str
    hub_rfm: _hub_rfm_pb2.HubRfm
    def __init__(
        self, value: str | None = ..., hub_rfm: _hub_rfm_pb2.HubRfm | str | None = ...
    ) -> None: ...
