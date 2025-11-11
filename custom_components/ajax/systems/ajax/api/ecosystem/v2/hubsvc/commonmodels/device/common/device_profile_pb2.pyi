from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_appearance_pb2 as _device_appearance_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_firmware_update_part_pb2 as _device_firmware_update_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_firmware_version_pb2 as _device_firmware_version_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_label_pb2 as _device_label_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceProfile(_message.Message):
    __slots__ = (
        "device_appearance",
        "device_color",
        "device_firmware_update",
        "device_firmware_version",
        "device_label",
        "device_location",
        "device_profile_settings",
        "displayed_id",
        "group_id",
        "id",
        "marketing_device_index",
        "name",
        "room_id",
    )
    class DeviceProfileSettings(_message.Message):
        __slots__ = ("device_location", "name")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        name: str
        device_location: str
        def __init__(
            self, name: str | None = ..., device_location: str | None = ...
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROFILE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    MARKETING_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    displayed_id: str
    device_profile_settings: DeviceProfile.DeviceProfileSettings
    device_appearance: _device_appearance_pb2.DeviceAppearance
    marketing_device_index: int
    room_id: str
    group_id: str
    device_firmware_version: _device_firmware_version_pb2.DeviceFirmwareVersion
    device_firmware_update: _device_firmware_update_part_pb2.DeviceFirmwareUpdatePart
    device_location: str
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        device_color: _device_color_pb2.DeviceColor | str | None = ...,
        device_label: _device_label_pb2.DeviceLabel | str | None = ...,
        displayed_id: str | None = ...,
        device_profile_settings: DeviceProfile.DeviceProfileSettings
        | _Mapping
        | None = ...,
        device_appearance: _device_appearance_pb2.DeviceAppearance
        | _Mapping
        | None = ...,
        marketing_device_index: int | None = ...,
        room_id: str | None = ...,
        group_id: str | None = ...,
        device_firmware_version: _device_firmware_version_pb2.DeviceFirmwareVersion
        | _Mapping
        | None = ...,
        device_firmware_update: _device_firmware_update_part_pb2.DeviceFirmwareUpdatePart
        | _Mapping
        | None = ...,
        device_location: str | None = ...,
    ) -> None: ...
