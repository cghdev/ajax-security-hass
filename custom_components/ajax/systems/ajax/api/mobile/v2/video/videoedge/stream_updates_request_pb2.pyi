from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge import (
    video_edge_pb2 as _video_edge_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    archive_pb2 as _archive_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.backupchannel import (
    backup_channel_info_pb2 as _backup_channel_info_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import (
    channel_pb2 as _channel_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.detector import (
    detector_pb2 as _detector_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.diagnostics import (
    diagnostics_settings_pb2 as _diagnostics_settings_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import (
    firmware_pb2 as _firmware_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.leds import leds_pb2 as _leds_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import mcu_pb2 as _mcu_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_pb2 as _media_device_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.network import (
    network_interface_pb2 as _network_interface_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.network import (
    network_pb2 as _network_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.onvif import (
    onvif_info_pb2 as _onvif_info_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import (
    video_edge_space_settings_pb2 as _video_edge_space_settings_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.storage import (
    storage_device_pb2 as _storage_device_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.storage import (
    storage_pb2 as _storage_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.system import (
    system_info_pb2 as _system_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamVideoEdgeUpdatesRequest(_message.Message):
    __slots__ = ("space_locator",)
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self, space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...
    ) -> None: ...

class StreamVideoEdgeUpdatesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "completely_changed",
            "initial_state",
            "installed",
            "partially_changed",
            "uninstalled",
        )
        class InitialState(_message.Message):
            __slots__ = ("video_edges",)
            VIDEO_EDGES_FIELD_NUMBER: _ClassVar[int]
            video_edges: _containers.RepeatedCompositeFieldContainer[
                _video_edge_pb2.VideoEdge
            ]
            def __init__(
                self,
                video_edges: _Iterable[_video_edge_pb2.VideoEdge | _Mapping]
                | None = ...,
            ) -> None: ...

        class Installed(_message.Message):
            __slots__ = ("video_edge",)
            VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
            video_edge: _video_edge_pb2.VideoEdge
            def __init__(
                self, video_edge: _video_edge_pb2.VideoEdge | _Mapping | None = ...
            ) -> None: ...

        class Uninstalled(_message.Message):
            __slots__ = ("video_edge_id",)
            VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
            video_edge_id: str
            def __init__(self, video_edge_id: str | None = ...) -> None: ...

        class CompletelyChanged(_message.Message):
            __slots__ = ("video_edge",)
            VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
            video_edge: _video_edge_pb2.VideoEdge
            def __init__(
                self, video_edge: _video_edge_pb2.VideoEdge | _Mapping | None = ...
            ) -> None: ...

        class PartiallyChanged(_message.Message):
            __slots__ = (
                "archive",
                "backup_channel_info",
                "channel",
                "connection_state",
                "detector",
                "device",
                "diagnostics_settings",
                "firmware",
                "leds",
                "mask",
                "mcu",
                "name",
                "network",
                "network_interface",
                "onvif_info",
                "space_settings",
                "storage",
                "storage_device",
                "system_info",
                "type",
                "video_edge_id",
            )
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NONE: _ClassVar[
                    StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
                ]
                UPDATE: _ClassVar[
                    StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
                ]
                ADD: _ClassVar[
                    StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
                ]
                REMOVE: _ClassVar[
                    StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
                ]

            NONE: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
            UPDATE: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
            ADD: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
            REMOVE: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
            VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_FIELD_NUMBER: _ClassVar[int]
            ARCHIVE_FIELD_NUMBER: _ClassVar[int]
            DETECTOR_FIELD_NUMBER: _ClassVar[int]
            NETWORK_FIELD_NUMBER: _ClassVar[int]
            DIAGNOSTICS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
            CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
            NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
            STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
            FIRMWARE_FIELD_NUMBER: _ClassVar[int]
            LEDS_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            STORAGE_FIELD_NUMBER: _ClassVar[int]
            MCU_FIELD_NUMBER: _ClassVar[int]
            ONVIF_INFO_FIELD_NUMBER: _ClassVar[int]
            SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
            BACKUP_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
            MASK_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            video_edge_id: str
            device: _media_device_pb2.MediaDevice
            channel: _channel_pb2.Channel
            archive: _archive_pb2.Archive
            detector: _detector_pb2.Detector
            network: _network_pb2.Network
            diagnostics_settings: _diagnostics_settings_pb2.DiagnosticsSettings
            system_info: _system_info_pb2.SystemInfo
            connection_state: _video_edge_pb2.ConnectionState
            network_interface: _network_interface_pb2.NetworkInterface
            storage_device: _storage_device_pb2.StorageDevice
            firmware: _firmware_pb2.Firmware
            leds: _leds_pb2.Leds
            name: str
            storage: _storage_pb2.Storage
            mcu: _mcu_pb2.Mcu
            onvif_info: _onvif_info_pb2.OnvifInfo
            space_settings: _video_edge_space_settings_pb2.VideoEdgeSpaceSettings
            backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
            mask: _field_mask_pb2.FieldMask
            type: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
            def __init__(
                self,
                video_edge_id: str | None = ...,
                device: _media_device_pb2.MediaDevice | _Mapping | None = ...,
                channel: _channel_pb2.Channel | _Mapping | None = ...,
                archive: _archive_pb2.Archive | _Mapping | None = ...,
                detector: _detector_pb2.Detector | _Mapping | None = ...,
                network: _network_pb2.Network | _Mapping | None = ...,
                diagnostics_settings: _diagnostics_settings_pb2.DiagnosticsSettings
                | _Mapping
                | None = ...,
                system_info: _system_info_pb2.SystemInfo | _Mapping | None = ...,
                connection_state: _video_edge_pb2.ConnectionState | str | None = ...,
                network_interface: _network_interface_pb2.NetworkInterface
                | _Mapping
                | None = ...,
                storage_device: _storage_device_pb2.StorageDevice
                | _Mapping
                | None = ...,
                firmware: _firmware_pb2.Firmware | _Mapping | None = ...,
                leds: _leds_pb2.Leds | _Mapping | None = ...,
                name: str | None = ...,
                storage: _storage_pb2.Storage | _Mapping | None = ...,
                mcu: _mcu_pb2.Mcu | _Mapping | None = ...,
                onvif_info: _onvif_info_pb2.OnvifInfo | _Mapping | None = ...,
                space_settings: _video_edge_space_settings_pb2.VideoEdgeSpaceSettings
                | _Mapping
                | None = ...,
                backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
                | _Mapping
                | None = ...,
                mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
                type: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged.Type
                | str
                | None = ...,
            ) -> None: ...

        INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
        INSTALLED_FIELD_NUMBER: _ClassVar[int]
        UNINSTALLED_FIELD_NUMBER: _ClassVar[int]
        COMPLETELY_CHANGED_FIELD_NUMBER: _ClassVar[int]
        PARTIALLY_CHANGED_FIELD_NUMBER: _ClassVar[int]
        initial_state: StreamVideoEdgeUpdatesResponse.Success.InitialState
        installed: StreamVideoEdgeUpdatesResponse.Success.Installed
        uninstalled: StreamVideoEdgeUpdatesResponse.Success.Uninstalled
        completely_changed: StreamVideoEdgeUpdatesResponse.Success.CompletelyChanged
        partially_changed: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged
        def __init__(
            self,
            initial_state: StreamVideoEdgeUpdatesResponse.Success.InitialState
            | _Mapping
            | None = ...,
            installed: StreamVideoEdgeUpdatesResponse.Success.Installed
            | _Mapping
            | None = ...,
            uninstalled: StreamVideoEdgeUpdatesResponse.Success.Uninstalled
            | _Mapping
            | None = ...,
            completely_changed: StreamVideoEdgeUpdatesResponse.Success.CompletelyChanged
            | _Mapping
            | None = ...,
            partially_changed: StreamVideoEdgeUpdatesResponse.Success.PartiallyChanged
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamVideoEdgeUpdatesResponse.Success
    failure: StreamVideoEdgeUpdatesResponse.Failure
    def __init__(
        self,
        success: StreamVideoEdgeUpdatesResponse.Success | _Mapping | None = ...,
        failure: StreamVideoEdgeUpdatesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
