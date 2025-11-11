from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.spacesettings import (
    app_settings_pb2 as _app_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetHideShortDisconnectsOnVideoEdgeTimelineRequest(_message.Message):
    __slots__ = ("hide_short_disconnects_on_timeline", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    HIDE_SHORT_DISCONNECTS_ON_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    hide_short_disconnects_on_timeline: _app_settings_pb2.HideShortDisconnectsOnTimeline
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        hide_short_disconnects_on_timeline: _app_settings_pb2.HideShortDisconnectsOnTimeline
        | str
        | None = ...,
    ) -> None: ...
