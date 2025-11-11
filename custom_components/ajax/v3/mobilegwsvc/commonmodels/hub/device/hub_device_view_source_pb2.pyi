from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    custom_alarm_type_pb2 as _custom_alarm_type_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_appearance_pb2 as _device_appearance_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_label_pb2 as _device_label_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    yavir_access_control_type_pb2 as _yavir_access_control_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubDeviceViewSource(_message.Message):
    __slots__ = (
        "custom_alarm_type",
        "device_appearance_type",
        "device_color",
        "device_hex_id",
        "device_label",
        "device_type",
        "name",
        "room_hex_id",
        "room_name",
        "yavir_access_control_type",
    )
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    YAVIR_ACCESS_CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APPEARANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    device_type: _object_type_pb2.ObjectType
    device_hex_id: str
    name: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    yavir_access_control_type: _yavir_access_control_type_pb2.YavirAccessControlType
    custom_alarm_type: _custom_alarm_type_pb2.CustomAlarmType
    device_appearance_type: _device_appearance_pb2.DeviceAppearance.DeviceAppearanceType
    room_hex_id: str
    room_name: str
    def __init__(
        self,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        device_hex_id: str | None = ...,
        name: str | None = ...,
        device_color: _device_color_pb2.DeviceColor | str | None = ...,
        device_label: _device_label_pb2.DeviceLabel | str | None = ...,
        yavir_access_control_type: _yavir_access_control_type_pb2.YavirAccessControlType
        | str
        | None = ...,
        custom_alarm_type: _custom_alarm_type_pb2.CustomAlarmType | str | None = ...,
        device_appearance_type: _device_appearance_pb2.DeviceAppearance.DeviceAppearanceType
        | str
        | None = ...,
        room_hex_id: str | None = ...,
        room_name: str | None = ...,
    ) -> None: ...
