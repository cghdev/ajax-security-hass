from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)
from systems.ajax.api.mobile.v2.common.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.mobile.v2.common.space.device import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.mobile.v2.common.space.device import (
    device_label_pb2 as _device_label_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubAdditionalInfo(_message.Message):
    __slots__ = ("box_type", "hub_color", "hub_label", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HUB_COLOR_FIELD_NUMBER: _ClassVar[int]
    HUB_LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _object_type_pb2.ObjectType
    hub_color: _device_color_pb2.DeviceColor
    hub_label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    def __init__(
        self,
        type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        hub_color: _device_color_pb2.DeviceColor | str | None = ...,
        hub_label: _device_label_pb2.DeviceLabel | str | None = ...,
        box_type: _hub_box_type_pb2.HubBoxType | str | None = ...,
    ) -> None: ...
