from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    notification_event_type_pb2 as _notification_event_type_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_alert_with_siren_pb2 as _video_notification_alert_with_siren_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_type_pb2 as _video_notification_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoNotificationAlertSettingsRequest(_message.Message):
    __slots__ = (
        "alert_with_siren",
        "channel_id",
        "line_crossing_rule_id",
        "notification_event_type",
        "space_id",
        "type",
        "video_edge_id",
    )
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSING_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_WITH_SIREN_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    type: _video_notification_type_pb2.VideoNotificationType
    line_crossing_rule_id: int
    alert_with_siren: _video_notification_alert_with_siren_pb2.AlertWithSiren
    notification_event_type: _notification_event_type_pb2.NotificationEventType
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        type: _video_notification_type_pb2.VideoNotificationType | str | None = ...,
        line_crossing_rule_id: int | None = ...,
        alert_with_siren: _video_notification_alert_with_siren_pb2.AlertWithSiren
        | str
        | None = ...,
        notification_event_type: _notification_event_type_pb2.NotificationEventType
        | str
        | None = ...,
    ) -> None: ...
