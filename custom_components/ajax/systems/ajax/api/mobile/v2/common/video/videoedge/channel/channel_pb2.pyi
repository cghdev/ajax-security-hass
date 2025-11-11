from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.about import (
    about_pb2 as _about_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    archive_pb2 as _archive_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    calendar_pb2 as _calendar_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.cloudarchive import (
    cloud_archive_pb2 as _cloud_archive_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.spacesettings import (
    channel_space_settings_pb2 as _channel_space_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CS_NONE: _ClassVar[ChannelState]
    ONLINE: _ClassVar[ChannelState]
    RECORDING: _ClassVar[ChannelState]
    HAVE_ARCHIVE: _ClassVar[ChannelState]
    HAVE_DETECTION: _ClassVar[ChannelState]
    HAVE_MOTION: _ClassVar[ChannelState]
    HAVE_SOUND: _ClassVar[ChannelState]
    HAVE_ALARM: _ClassVar[ChannelState]
    HAVE_OBJECTS: _ClassVar[ChannelState]
    FLICKERING: _ClassVar[ChannelState]
    HAVE_PIR_MOTION: _ClassVar[ChannelState]
    HAVE_RING: _ClassVar[ChannelState]

CS_NONE: ChannelState
ONLINE: ChannelState
RECORDING: ChannelState
HAVE_ARCHIVE: ChannelState
HAVE_DETECTION: ChannelState
HAVE_MOTION: ChannelState
HAVE_SOUND: ChannelState
HAVE_ALARM: ChannelState
HAVE_OBJECTS: ChannelState
FLICKERING: ChannelState
HAVE_PIR_MOTION: ChannelState
HAVE_RING: ChannelState

class Channel(_message.Message):
    __slots__ = (
        "calendar",
        "channel_preview",
        "cloud_archive",
        "device_info",
        "group_id",
        "guid",
        "info",
        "record_mode",
        "record_policy",
        "room_id",
        "smart_backlight_trigger_settings",
        "source_aliases",
        "space_settings",
        "state",
        "zombie",
    )
    GUID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    ZOMBIE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    SMART_BACKLIGHT_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ALIASES_FIELD_NUMBER: _ClassVar[int]
    guid: str
    device_info: MediaDeviceInfo
    info: ChannelInfo
    state: _containers.RepeatedScalarFieldContainer[ChannelState]
    record_mode: _archive_pb2.RecordMode
    channel_preview: ChannelPreview
    calendar: _calendar_pb2.Calendar
    record_policy: _archive_pb2.RecordPolicy
    zombie: bool
    cloud_archive: _cloud_archive_pb2.CloudArchive
    smart_backlight_trigger_settings: SmartBacklightTriggerSettings
    room_id: str
    group_id: str
    space_settings: _channel_space_settings_pb2.ChannelSpaceSettings
    source_aliases: SourceAliases
    def __init__(
        self,
        guid: str | None = ...,
        device_info: MediaDeviceInfo | _Mapping | None = ...,
        info: ChannelInfo | _Mapping | None = ...,
        state: _Iterable[ChannelState | str] | None = ...,
        record_mode: _archive_pb2.RecordMode | str | None = ...,
        channel_preview: ChannelPreview | _Mapping | None = ...,
        calendar: _calendar_pb2.Calendar | _Mapping | None = ...,
        record_policy: _archive_pb2.RecordPolicy | str | None = ...,
        zombie: bool = ...,
        cloud_archive: _cloud_archive_pb2.CloudArchive | _Mapping | None = ...,
        smart_backlight_trigger_settings: SmartBacklightTriggerSettings
        | _Mapping
        | None = ...,
        room_id: str | None = ...,
        group_id: str | None = ...,
        space_settings: _channel_space_settings_pb2.ChannelSpaceSettings
        | _Mapping
        | None = ...,
        source_aliases: SourceAliases | _Mapping | None = ...,
    ) -> None: ...

class MediaDeviceInfo(_message.Message):
    __slots__ = ("channel_id", "media_device_guid")
    MEDIA_DEVICE_GUID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    media_device_guid: str
    channel_id: str
    def __init__(
        self, media_device_guid: str | None = ..., channel_id: str | None = ...
    ) -> None: ...

class ChannelInfo(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: str | None = ...) -> None: ...

class ChannelPreview(_message.Message):
    __slots__ = ("created_at", "image_url")
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        image_url: str | None = ...,
        created_at: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...

class SourceAliases(_message.Message):
    __slots__ = ("sources",)
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[VideoSource]
    def __init__(
        self, sources: _Iterable[VideoSource | _Mapping] | None = ...
    ) -> None: ...

class VideoSource(_message.Message):
    __slots__ = ("cloud_archive_source", "nvr_source", "primary_source")
    PRIMARY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NVR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    primary_source: PrimarySource
    nvr_source: NvrSource
    cloud_archive_source: CloudArchiveSource
    def __init__(
        self,
        primary_source: PrimarySource | _Mapping | None = ...,
        nvr_source: NvrSource | _Mapping | None = ...,
        cloud_archive_source: CloudArchiveSource | _Mapping | None = ...,
    ) -> None: ...

class PrimarySource(_message.Message):
    __slots__ = ("channel_id", "color", "type", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    type: _about_pb2.About.Type
    color: _about_pb2.About.Color
    def __init__(
        self,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        type: _about_pb2.About.Type | str | None = ...,
        color: _about_pb2.About.Color | str | None = ...,
    ) -> None: ...

class NvrSource(_message.Message):
    __slots__ = ("channel_id", "type", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    type: _about_pb2.About.Type
    def __init__(
        self,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        type: _about_pb2.About.Type | str | None = ...,
    ) -> None: ...

class CloudArchiveSource(_message.Message):
    __slots__ = ("channel_id", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    def __init__(
        self, video_edge_id: str | None = ..., channel_id: str | None = ...
    ) -> None: ...

class SmartBacklightTriggerTypeSettings(_message.Message):
    __slots__ = ("enabled", "motion", "object")
    class Motion(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Object(_message.Message):
        __slots__ = ("object_class",)
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        object_class: _types_pb2.ObjectClass
        def __init__(
            self, object_class: _types_pb2.ObjectClass | str | None = ...
        ) -> None: ...

    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MOTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    motion: SmartBacklightTriggerTypeSettings.Motion
    object: SmartBacklightTriggerTypeSettings.Object
    def __init__(
        self,
        enabled: bool = ...,
        motion: SmartBacklightTriggerTypeSettings.Motion | _Mapping | None = ...,
        object: SmartBacklightTriggerTypeSettings.Object | _Mapping | None = ...,
    ) -> None: ...

class SmartBacklightTriggerSettings(_message.Message):
    __slots__ = ("smart_backlight_trigger_types",)
    SMART_BACKLIGHT_TRIGGER_TYPES_FIELD_NUMBER: _ClassVar[int]
    smart_backlight_trigger_types: _containers.RepeatedCompositeFieldContainer[
        SmartBacklightTriggerTypeSettings
    ]
    def __init__(
        self,
        smart_backlight_trigger_types: _Iterable[
            SmartBacklightTriggerTypeSettings | _Mapping
        ]
        | None = ...,
    ) -> None: ...
