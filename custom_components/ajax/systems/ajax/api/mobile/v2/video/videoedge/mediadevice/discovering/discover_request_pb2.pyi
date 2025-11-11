from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.about import (
    about_pb2 as _about_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_pb2 as _media_device_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice.discovering import (
    discovery_address_pb2 as _discovery_address_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoverMediaDevicesRequest(_message.Message):
    __slots__ = ("filter", "space_locator", "video_edge_id")
    class Filter(_message.Message):
        __slots__ = ("protocols",)
        PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
        protocols: _containers.RepeatedScalarFieldContainer[
            _media_device_pb2.MediaDeviceProtocol
        ]
        def __init__(
            self,
            protocols: _Iterable[_media_device_pb2.MediaDeviceProtocol | str]
            | None = ...,
        ) -> None: ...

    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    filter: DiscoverMediaDevicesRequest.Filter
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        filter: DiscoverMediaDevicesRequest.Filter | _Mapping | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class DiscoverMediaDevicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "device_added",
            "device_removed",
            "device_updated",
            "instant_discovering_result",
            "unknown",
        )
        INSTANT_DISCOVERING_RESULT_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_REMOVED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_UPDATED_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        instant_discovering_result: (
            DiscoverMediaDevicesResponse.InstantDiscoveringResult
        )
        device_added: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        device_removed: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        device_updated: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        unknown: _empty_pb2.Empty
        def __init__(
            self,
            instant_discovering_result: DiscoverMediaDevicesResponse.InstantDiscoveringResult
            | _Mapping
            | None = ...,
            device_added: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
            | _Mapping
            | None = ...,
            device_removed: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
            | _Mapping
            | None = ...,
            device_updated: DiscoverMediaDevicesResponse.DiscoveredMediaDevice
            | _Mapping
            | None = ...,
            unknown: _empty_pb2.Empty | _Mapping | None = ...,
        ) -> None: ...

    class InstantDiscoveringResult(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[
            DiscoverMediaDevicesResponse.DiscoveredMediaDevice
        ]
        def __init__(
            self,
            devices: _Iterable[
                DiscoverMediaDevicesResponse.DiscoveredMediaDevice | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class DiscoveredMediaDevice(_message.Message):
        __slots__ = (
            "addresses",
            "already_added",
            "already_added_new",
            "available_to_add",
            "model",
            "name",
            "uuid",
            "vendor",
            "video_edge_info",
        )
        UUID_FIELD_NUMBER: _ClassVar[int]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        ALREADY_ADDED_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_INFO_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_TO_ADD_FIELD_NUMBER: _ClassVar[int]
        ALREADY_ADDED_NEW_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        vendor: str
        model: str
        addresses: _containers.RepeatedCompositeFieldContainer[
            _discovery_address_pb2.DiscoveryAddress
        ]
        already_added: bool
        name: str
        video_edge_info: DiscoverMediaDevicesResponse.DiscoveredVideoEdgeInfo
        available_to_add: DiscoverMediaDevicesResponse.AvailableToAdd
        already_added_new: DiscoverMediaDevicesResponse.AlreadyAdded
        def __init__(
            self,
            uuid: str | None = ...,
            vendor: str | None = ...,
            model: str | None = ...,
            addresses: _Iterable[_discovery_address_pb2.DiscoveryAddress | _Mapping]
            | None = ...,
            already_added: bool = ...,
            name: str | None = ...,
            video_edge_info: DiscoverMediaDevicesResponse.DiscoveredVideoEdgeInfo
            | _Mapping
            | None = ...,
            available_to_add: DiscoverMediaDevicesResponse.AvailableToAdd
            | _Mapping
            | None = ...,
            already_added_new: DiscoverMediaDevicesResponse.AlreadyAdded
            | _Mapping
            | None = ...,
        ) -> None: ...

    class AvailableToAdd(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class AlreadyAdded(_message.Message):
        __slots__ = ("available_channel_ids_on_media_device", "media_device_id")
        MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_CHANNEL_IDS_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
        media_device_id: str
        available_channel_ids_on_media_device: _containers.RepeatedScalarFieldContainer[
            str
        ]
        def __init__(
            self,
            media_device_id: str | None = ...,
            available_channel_ids_on_media_device: _Iterable[str] | None = ...,
        ) -> None: ...

    class DiscoveredVideoEdgeInfo(_message.Message):
        __slots__ = (
            "channels",
            "color",
            "group_id",
            "installed",
            "room_id",
            "type",
            "video_edge_id",
        )
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INSTALLED_FIELD_NUMBER: _ClassVar[int]
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        type: _about_pb2.About.Type
        installed: bool
        room_id: str
        group_id: str
        channels: _containers.RepeatedCompositeFieldContainer[
            DiscoverMediaDevicesResponse.AvailableChannel
        ]
        color: _about_pb2.About.Color
        def __init__(
            self,
            video_edge_id: str | None = ...,
            type: _about_pb2.About.Type | str | None = ...,
            installed: bool = ...,
            room_id: str | None = ...,
            group_id: str | None = ...,
            channels: _Iterable[
                DiscoverMediaDevicesResponse.AvailableChannel | _Mapping
            ]
            | None = ...,
            color: _about_pb2.About.Color | str | None = ...,
        ) -> None: ...

    class AvailableChannel(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: str | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "role_access_required",
            "space_armed",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        ROLE_ACCESS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        role_access_required: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            role_access_required: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DiscoverMediaDevicesResponse.Success
    failure: DiscoverMediaDevicesResponse.Failure
    def __init__(
        self,
        success: DiscoverMediaDevicesResponse.Success | _Mapping | None = ...,
        failure: DiscoverMediaDevicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
