from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_type_pb2 as _video_notification_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeDetectorsEnabledByNotificationTypesRequest(_message.Message):
    __slots__ = ("channel_id", "notification_types", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPES_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    notification_types: _containers.RepeatedScalarFieldContainer[
        _video_notification_type_pb2.VideoNotificationType
    ]
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        notification_types: _Iterable[
            _video_notification_type_pb2.VideoNotificationType | str
        ]
        | None = ...,
    ) -> None: ...
