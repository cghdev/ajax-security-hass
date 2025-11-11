from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import (
    channel_pb2 as _channel_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeChannelSmartBacklightTriggerSettingsRequest(_message.Message):
    __slots__ = (
        "channel_id",
        "smart_backlight_trigger_settings",
        "space_id",
        "video_edge_id",
    )
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_BACKLIGHT_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    smart_backlight_trigger_settings: _channel_pb2.SmartBacklightTriggerSettings
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        smart_backlight_trigger_settings: _channel_pb2.SmartBacklightTriggerSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
