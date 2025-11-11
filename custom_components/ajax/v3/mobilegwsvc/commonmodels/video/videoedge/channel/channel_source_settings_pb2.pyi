from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.videoedge import (
    video_edge_pb2 as _video_edge_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    archive_pb2 as _archive_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import (
    channel_pb2 as _channel_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelSourceSettings(_message.Message):
    __slots__ = ("nvr_source_settings",)
    NVR_SOURCE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    nvr_source_settings: NvrSourceSettings
    def __init__(
        self, nvr_source_settings: NvrSourceSettings | _Mapping | None = ...
    ) -> None: ...

class NvrSourceSettings(_message.Message):
    __slots__ = (
        "channel_id",
        "channel_states",
        "media_device_id",
        "record_mode",
        "record_policy",
        "storage_devices",
        "video_edge_connection_state",
        "video_edge_id",
        "video_edge_name",
    )
    class StorageDevice(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STATES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    channel_id: str
    video_edge_name: str
    video_edge_connection_state: _video_edge_pb2.ConnectionState
    record_mode: _archive_pb2.RecordMode
    record_policy: _archive_pb2.RecordPolicy
    storage_devices: _containers.RepeatedCompositeFieldContainer[
        NvrSourceSettings.StorageDevice
    ]
    channel_states: _containers.RepeatedScalarFieldContainer[_channel_pb2.ChannelState]
    media_device_id: str
    def __init__(
        self,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        video_edge_name: str | None = ...,
        video_edge_connection_state: _video_edge_pb2.ConnectionState | str | None = ...,
        record_mode: _archive_pb2.RecordMode | str | None = ...,
        record_policy: _archive_pb2.RecordPolicy | str | None = ...,
        storage_devices: _Iterable[NvrSourceSettings.StorageDevice | _Mapping]
        | None = ...,
        channel_states: _Iterable[_channel_pb2.ChannelState | str] | None = ...,
        media_device_id: str | None = ...,
    ) -> None: ...
