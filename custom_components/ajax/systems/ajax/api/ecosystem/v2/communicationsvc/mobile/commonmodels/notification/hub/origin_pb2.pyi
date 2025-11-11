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

class HubOrigin(_message.Message):
    __slots__ = ("box_type", "color", "hex_id", "label", "name", "type")
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    name: str
    color: _device_color_pb2.DeviceColor
    type: _hub_type_pb2.HubType
    label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    def __init__(
        self,
        hex_id: str | None = ...,
        name: str | None = ...,
        color: _device_color_pb2.DeviceColor | str | None = ...,
        type: _hub_type_pb2.HubType | str | None = ...,
        label: _device_label_pb2.DeviceLabel | str | None = ...,
        box_type: _hub_box_type_pb2.HubBoxType | str | None = ...,
    ) -> None: ...
