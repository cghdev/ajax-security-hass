from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import (
    qualifier_pb2 as _qualifier_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    source_image_info_pb2 as _source_image_info_pb2,
)
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
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    source_pb2 as _source_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TroubledDevices(_message.Message):
    __slots__ = ("hub_info", "troubled_devices", "troubled_followed_groups")
    class TroubledDevice(_message.Message):
        __slots__ = ("device", "troubled_alarm")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        TROUBLED_ALARM_FIELD_NUMBER: _ClassVar[int]
        device: _source_pb2.HubNotificationSource
        troubled_alarm: _qualifier_pb2.HubEventQualifier
        def __init__(
            self,
            device: _source_pb2.HubNotificationSource | _Mapping | None = ...,
            troubled_alarm: _qualifier_pb2.HubEventQualifier | _Mapping | None = ...,
        ) -> None: ...

    class TroubledFollowedGroup(_message.Message):
        __slots__ = ("id", "image_info", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        image_info: _source_image_info_pb2.SourceImageInfo
        def __init__(
            self,
            id: str | None = ...,
            name: str | None = ...,
            image_info: _source_image_info_pb2.SourceImageInfo | _Mapping | None = ...,
        ) -> None: ...

    class HubInfo(_message.Message):
        __slots__ = ("box_type", "color", "hex_id", "label", "name", "type")
        HEX_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        hex_id: str
        name: str
        color: _device_color_pb2.DeviceColor
        type: _hub_type_pb2.HubType
        box_type: _hub_box_type_pb2.HubBoxType
        label: _device_label_pb2.DeviceLabel
        def __init__(
            self,
            hex_id: str | None = ...,
            name: str | None = ...,
            color: _device_color_pb2.DeviceColor | str | None = ...,
            type: _hub_type_pb2.HubType | str | None = ...,
            box_type: _hub_box_type_pb2.HubBoxType | str | None = ...,
            label: _device_label_pb2.DeviceLabel | str | None = ...,
        ) -> None: ...

    TROUBLED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    HUB_INFO_FIELD_NUMBER: _ClassVar[int]
    TROUBLED_FOLLOWED_GROUPS_FIELD_NUMBER: _ClassVar[int]
    troubled_devices: _containers.RepeatedCompositeFieldContainer[
        TroubledDevices.TroubledDevice
    ]
    hub_info: TroubledDevices.HubInfo
    troubled_followed_groups: _containers.RepeatedCompositeFieldContainer[
        TroubledDevices.TroubledFollowedGroup
    ]
    def __init__(
        self,
        troubled_devices: _Iterable[TroubledDevices.TroubledDevice | _Mapping]
        | None = ...,
        hub_info: TroubledDevices.HubInfo | _Mapping | None = ...,
        troubled_followed_groups: _Iterable[
            TroubledDevices.TroubledFollowedGroup | _Mapping
        ]
        | None = ...,
    ) -> None: ...
