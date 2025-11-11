from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    device_label_pb2 as _device_label_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    hub_box_type_pb2 as _hub_box_type_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    hub_type_pb2 as _hub_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubInfo(_message.Message):
    __slots__ = ("box_type", "color", "device_label", "hub_type")
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    HUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    hub_type: _hub_type_pb2.HubType
    def __init__(
        self,
        color: _device_color_pb2.DeviceColor | str | None = ...,
        device_label: _device_label_pb2.DeviceLabel | str | None = ...,
        box_type: _hub_box_type_pb2.HubBoxType | str | None = ...,
        hub_type: _hub_type_pb2.HubType | str | None = ...,
    ) -> None: ...
