from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import (
    channel_pb2 as _channel_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.cloudarchive import (
    cloud_archive_pb2 as _cloud_archive_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import (
    app_settings_pb2 as _app_settings_pb2,
)
from v3.mobilegwsvc.service.stream_video_player import (
    player_channel_pb2 as _player_channel_pb2,
)
from v3.mobilegwsvc.service.stream_video_player import (
    player_detector_pb2 as _player_detector_pb2,
)
from v3.mobilegwsvc.service.stream_video_player import (
    player_storage_device_pb2 as _player_storage_device_pb2,
)
from v3.mobilegwsvc.service.stream_video_player import (
    player_video_edge_pb2 as _player_video_edge_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Updates(_message.Message):
    __slots__ = ("updates",)
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[Update]
    def __init__(self, updates: _Iterable[Update | _Mapping] | None = ...) -> None: ...

class Update(_message.Message):
    __slots__ = (
        "app_settings_updated",
        "channel_added",
        "channel_audio_settings_updated",
        "channel_media_device_info_added",
        "channel_media_device_info_removed",
        "channel_video_settings_updated",
        "cloud_archive_updated",
        "detector_added",
        "detector_removed",
        "detector_state_updated",
        "storage_device_added",
        "storage_device_removed",
        "timezone_updated",
        "video_edge_id",
        "video_edge_installed",
        "video_edge_updated",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_UPDATED_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_UPDATED_FIELD_NUMBER: _ClassVar[int]
    APP_SETTINGS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ADDED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MEDIA_DEVICE_INFO_ADDED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MEDIA_DEVICE_INFO_REMOVED_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_ADDED_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_STATE_UPDATED_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_REMOVED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_REMOVED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_VIDEO_SETTINGS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_AUDIO_SETTINGS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_UPDATED_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    video_edge_installed: VideoEdgeInstalled
    video_edge_updated: VideoEdgeUpdated
    timezone_updated: TimezoneUpdated
    app_settings_updated: AppSettingsUpdated
    channel_added: ChannelAdded
    channel_media_device_info_added: ChannelMediaDeviceInfoAdded
    channel_media_device_info_removed: ChannelMediaDeviceInfoRemoved
    detector_added: DetectorAdded
    detector_state_updated: DetectorStateUpdated
    detector_removed: DetectorRemoved
    storage_device_added: StorageDeviceAdded
    storage_device_removed: StorageDeviceRemoved
    channel_video_settings_updated: ChannelVideoSettingsUpdated
    channel_audio_settings_updated: ChannelAudioSettingsUpdated
    cloud_archive_updated: CloudArchiveUpdated
    def __init__(
        self,
        video_edge_id: str | None = ...,
        video_edge_installed: VideoEdgeInstalled | _Mapping | None = ...,
        video_edge_updated: VideoEdgeUpdated | _Mapping | None = ...,
        timezone_updated: TimezoneUpdated | _Mapping | None = ...,
        app_settings_updated: AppSettingsUpdated | _Mapping | None = ...,
        channel_added: ChannelAdded | _Mapping | None = ...,
        channel_media_device_info_added: ChannelMediaDeviceInfoAdded
        | _Mapping
        | None = ...,
        channel_media_device_info_removed: ChannelMediaDeviceInfoRemoved
        | _Mapping
        | None = ...,
        detector_added: DetectorAdded | _Mapping | None = ...,
        detector_state_updated: DetectorStateUpdated | _Mapping | None = ...,
        detector_removed: DetectorRemoved | _Mapping | None = ...,
        storage_device_added: StorageDeviceAdded | _Mapping | None = ...,
        storage_device_removed: StorageDeviceRemoved | _Mapping | None = ...,
        channel_video_settings_updated: ChannelVideoSettingsUpdated
        | _Mapping
        | None = ...,
        channel_audio_settings_updated: ChannelAudioSettingsUpdated
        | _Mapping
        | None = ...,
        cloud_archive_updated: CloudArchiveUpdated | _Mapping | None = ...,
    ) -> None: ...

class VideoEdgeInstalled(_message.Message):
    __slots__ = ("video_edge",)
    VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
    video_edge: _player_video_edge_pb2.PlayerVideoEdge
    def __init__(
        self, video_edge: _player_video_edge_pb2.PlayerVideoEdge | _Mapping | None = ...
    ) -> None: ...

class VideoEdgeUpdated(_message.Message):
    __slots__ = ("video_edge",)
    VIDEO_EDGE_FIELD_NUMBER: _ClassVar[int]
    video_edge: _player_video_edge_pb2.PlayerVideoEdge
    def __init__(
        self, video_edge: _player_video_edge_pb2.PlayerVideoEdge | _Mapping | None = ...
    ) -> None: ...

class TimezoneUpdated(_message.Message):
    __slots__ = ("timezone_id",)
    TIMEZONE_ID_FIELD_NUMBER: _ClassVar[int]
    timezone_id: str
    def __init__(self, timezone_id: str | None = ...) -> None: ...

class AppSettingsUpdated(_message.Message):
    __slots__ = ("app_settings",)
    APP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    app_settings: _app_settings_pb2.AppSettings
    def __init__(
        self, app_settings: _app_settings_pb2.AppSettings | _Mapping | None = ...
    ) -> None: ...

class ChannelAdded(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _player_channel_pb2.PlayerChannel
    def __init__(
        self, channel: _player_channel_pb2.PlayerChannel | _Mapping | None = ...
    ) -> None: ...

class ChannelMediaDeviceInfoAdded(_message.Message):
    __slots__ = ("channel_id", "media_device_info")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    media_device_info: _channel_pb2.MediaDeviceInfo
    def __init__(
        self,
        channel_id: str | None = ...,
        media_device_info: _channel_pb2.MediaDeviceInfo | _Mapping | None = ...,
    ) -> None: ...

class ChannelMediaDeviceInfoRemoved(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: str | None = ...) -> None: ...

class DetectorAdded(_message.Message):
    __slots__ = ("detector",)
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    detector: _player_detector_pb2.PlayerDetector
    def __init__(
        self, detector: _player_detector_pb2.PlayerDetector | _Mapping | None = ...
    ) -> None: ...

class DetectorStateUpdated(_message.Message):
    __slots__ = ("detector_id", "enabled")
    DETECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    detector_id: str
    enabled: bool
    def __init__(self, detector_id: str | None = ..., enabled: bool = ...) -> None: ...

class DetectorRemoved(_message.Message):
    __slots__ = ("detector_id",)
    DETECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    detector_id: str
    def __init__(self, detector_id: str | None = ...) -> None: ...

class StorageDeviceAdded(_message.Message):
    __slots__ = ("storage_device",)
    STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    storage_device: _player_storage_device_pb2.PlayerStorageDevice
    def __init__(
        self,
        storage_device: _player_storage_device_pb2.PlayerStorageDevice
        | _Mapping
        | None = ...,
    ) -> None: ...

class StorageDeviceRemoved(_message.Message):
    __slots__ = ("storage_device_id",)
    STORAGE_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    storage_device_id: str
    def __init__(self, storage_device_id: str | None = ...) -> None: ...

class ChannelVideoSettingsUpdated(_message.Message):
    __slots__ = ("channel_id_on_media_device", "media_device_id", "video_settings")
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    media_device_id: str
    channel_id_on_media_device: str
    video_settings: _player_channel_pb2.PlayerChannel.VideoSettings
    def __init__(
        self,
        media_device_id: str | None = ...,
        channel_id_on_media_device: str | None = ...,
        video_settings: _player_channel_pb2.PlayerChannel.VideoSettings
        | _Mapping
        | None = ...,
    ) -> None: ...

class ChannelAudioSettingsUpdated(_message.Message):
    __slots__ = ("audio_settings", "channel_id_on_media_device", "media_device_id")
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    media_device_id: str
    channel_id_on_media_device: str
    audio_settings: _player_channel_pb2.PlayerChannel.AudioSettings
    def __init__(
        self,
        media_device_id: str | None = ...,
        channel_id_on_media_device: str | None = ...,
        audio_settings: _player_channel_pb2.PlayerChannel.AudioSettings
        | _Mapping
        | None = ...,
    ) -> None: ...

class CloudArchiveUpdated(_message.Message):
    __slots__ = ("channel_id", "cloud_archive")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    cloud_archive: _cloud_archive_pb2.CloudArchive
    def __init__(
        self,
        channel_id: str | None = ...,
        cloud_archive: _cloud_archive_pb2.CloudArchive | _Mapping | None = ...,
    ) -> None: ...
