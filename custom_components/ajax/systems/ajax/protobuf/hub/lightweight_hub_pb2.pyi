from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2
from systems.ajax.protobuf.hub.device import hub_device_pb2 as _hub_device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LightweightHub(_message.Message):
    __slots__ = (
        "color",
        "firmware",
        "groups_enabled",
        "id",
        "image_urls",
        "name",
        "online",
        "state",
        "state_with_groups",
        "subtype",
        "warnings_total_count",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_WITH_GROUPS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    groups_enabled: bool
    state: _hub_device_pb2.HubDevice.State
    state_with_groups: _hub_device_pb2.HubDevice.StateWithGroups
    image_urls: _image_urls_pb2.ImageUrls
    online: _wrappers_pb2.BoolValue
    color: _hub_device_pb2.HubDevice.Color
    subtype: _hub_device_pb2.HubDevice.Subtype
    warnings_total_count: _wrappers_pb2.Int32Value
    firmware: _hub_device_pb2.HubDevice.Firmware
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        groups_enabled: bool = ...,
        state: _hub_device_pb2.HubDevice.State | str | None = ...,
        state_with_groups: _hub_device_pb2.HubDevice.StateWithGroups | str | None = ...,
        image_urls: _image_urls_pb2.ImageUrls | _Mapping | None = ...,
        online: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        color: _hub_device_pb2.HubDevice.Color | str | None = ...,
        subtype: _hub_device_pb2.HubDevice.Subtype | str | None = ...,
        warnings_total_count: _wrappers_pb2.Int32Value | _Mapping | None = ...,
        firmware: _hub_device_pb2.HubDevice.Firmware | _Mapping | None = ...,
    ) -> None: ...
