from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_appearance_pb2 as _device_appearance_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_label_pb2 as _device_label_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_state_pb2 as _light_device_state_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_status_pb2 as _light_device_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LightDeviceProfile(_message.Message):
    __slots__ = (
        "bypassed",
        "device_appearance",
        "device_color",
        "device_index",
        "device_label",
        "device_marketing_id",
        "group_id",
        "id",
        "interaction_disabled",
        "malfunctions",
        "marketing_device_index",
        "name",
        "room_id",
        "sorting_key",
        "states",
        "statuses",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    MARKETING_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BYPASSED_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MARKETING_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    room_id: str
    group_id: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    malfunctions: int
    states: _containers.RepeatedScalarFieldContainer[
        _light_device_state_pb2.LightDeviceState
    ]
    statuses: _containers.RepeatedCompositeFieldContainer[
        _light_device_status_pb2.LightDeviceStatus
    ]
    sorting_key: str
    device_index: int
    marketing_device_index: int
    bypassed: bool
    interaction_disabled: bool
    device_appearance: _device_appearance_pb2.DeviceAppearance
    device_marketing_id: str
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        room_id: str | None = ...,
        group_id: str | None = ...,
        device_color: _device_color_pb2.DeviceColor | str | None = ...,
        device_label: _device_label_pb2.DeviceLabel | str | None = ...,
        malfunctions: int | None = ...,
        states: _Iterable[_light_device_state_pb2.LightDeviceState | str] | None = ...,
        statuses: _Iterable[_light_device_status_pb2.LightDeviceStatus | _Mapping]
        | None = ...,
        sorting_key: str | None = ...,
        device_index: int | None = ...,
        marketing_device_index: int | None = ...,
        bypassed: bool = ...,
        interaction_disabled: bool = ...,
        device_appearance: _device_appearance_pb2.DeviceAppearance
        | _Mapping
        | None = ...,
        device_marketing_id: str | None = ...,
    ) -> None: ...
