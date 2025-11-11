from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.video.videoedge.about import (
    about_pb2 as _about_pb2,
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

class ConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[ConnectionState]
    OFFLINE: _ClassVar[ConnectionState]
    ONLINE: _ClassVar[ConnectionState]

NONE: ConnectionState
OFFLINE: ConnectionState
ONLINE: ConnectionState

class VideoEdge(_message.Message):
    __slots__ = (
        "about",
        "archive",
        "backup_channel_info",
        "channels",
        "connection_state",
        "detectors",
        "devices",
        "diagnostics_settings",
        "firmware",
        "guid",
        "leds",
        "mcu",
        "name",
        "network",
        "network_interfaces",
        "onvif_info",
        "space_settings",
        "storage",
        "storage_devices",
        "system_info",
    )
    GUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    LEDS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    MCU_FIELD_NUMBER: _ClassVar[int]
    ONVIF_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    guid: str
    name: str
    connection_state: ConnectionState
    archive: _archive_pb2.Archive
    devices: _containers.RepeatedCompositeFieldContainer[_media_device_pb2.MediaDevice]
    channels: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    detectors: _containers.RepeatedCompositeFieldContainer[_detector_pb2.Detector]
    network: _network_pb2.Network
    diagnostics_settings: _diagnostics_settings_pb2.DiagnosticsSettings
    system_info: _system_info_pb2.SystemInfo
    network_interfaces: _containers.RepeatedCompositeFieldContainer[
        _network_interface_pb2.NetworkInterface
    ]
    storage_devices: _containers.RepeatedCompositeFieldContainer[
        _storage_device_pb2.StorageDevice
    ]
    firmware: _firmware_pb2.Firmware
    about: _about_pb2.About
    leds: _leds_pb2.Leds
    storage: _storage_pb2.Storage
    mcu: _mcu_pb2.Mcu
    onvif_info: _onvif_info_pb2.OnvifInfo
    space_settings: _video_edge_space_settings_pb2.VideoEdgeSpaceSettings
    backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
    def __init__(
        self,
        guid: str | None = ...,
        name: str | None = ...,
        connection_state: ConnectionState | str | None = ...,
        archive: _archive_pb2.Archive | _Mapping | None = ...,
        devices: _Iterable[_media_device_pb2.MediaDevice | _Mapping] | None = ...,
        channels: _Iterable[_channel_pb2.Channel | _Mapping] | None = ...,
        detectors: _Iterable[_detector_pb2.Detector | _Mapping] | None = ...,
        network: _network_pb2.Network | _Mapping | None = ...,
        diagnostics_settings: _diagnostics_settings_pb2.DiagnosticsSettings
        | _Mapping
        | None = ...,
        system_info: _system_info_pb2.SystemInfo | _Mapping | None = ...,
        network_interfaces: _Iterable[
            _network_interface_pb2.NetworkInterface | _Mapping
        ]
        | None = ...,
        storage_devices: _Iterable[_storage_device_pb2.StorageDevice | _Mapping]
        | None = ...,
        firmware: _firmware_pb2.Firmware | _Mapping | None = ...,
        about: _about_pb2.About | _Mapping | None = ...,
        leds: _leds_pb2.Leds | _Mapping | None = ...,
        storage: _storage_pb2.Storage | _Mapping | None = ...,
        mcu: _mcu_pb2.Mcu | _Mapping | None = ...,
        onvif_info: _onvif_info_pb2.OnvifInfo | _Mapping | None = ...,
        space_settings: _video_edge_space_settings_pb2.VideoEdgeSpaceSettings
        | _Mapping
        | None = ...,
        backup_channel_info: _backup_channel_info_pb2.BackupChannelInfo
        | _Mapping
        | None = ...,
    ) -> None: ...
