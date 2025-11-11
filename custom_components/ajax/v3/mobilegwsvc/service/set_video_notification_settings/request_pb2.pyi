from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
import datetime
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_confirm_detection_with_pir_state_pb2 as _video_notification_confirm_detection_with_pir_state_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_monitoring_state_pb2 as _video_notification_monitoring_state_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_object_detection_duration_pb2 as _video_notification_object_detection_duration_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_state_pb2 as _video_notification_state_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_type_pb2 as _video_notification_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoNotificationSettingsRequest(_message.Message):
    __slots__ = (
        "channel_id",
        "notification_settings",
        "space_locator",
        "video_edge_id",
    )
    class NotificationSettings(_message.Message):
        __slots__ = (
            "confirm_detection_with_pir",
            "cooldown_period",
            "line_crossing_changes",
            "monitoring_state",
            "notification_settings_entries",
            "object_detection_duration",
        )
        class NotificationSettingsEntry(_message.Message):
            __slots__ = ("state", "type")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            type: _video_notification_type_pb2.VideoNotificationType
            state: _video_notification_state_pb2.VideoNotificationState
            def __init__(
                self,
                type: _video_notification_type_pb2.VideoNotificationType
                | str
                | None = ...,
                state: _video_notification_state_pb2.VideoNotificationState
                | str
                | None = ...,
            ) -> None: ...

        class LineCrossingNotificationSettingsChange(_message.Message):
            __slots__ = ("rule_id", "state")
            RULE_ID_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            rule_id: int
            state: _video_notification_state_pb2.VideoNotificationState
            def __init__(
                self,
                rule_id: int | None = ...,
                state: _video_notification_state_pb2.VideoNotificationState
                | str
                | None = ...,
            ) -> None: ...

        NOTIFICATION_SETTINGS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
        COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DETECTION_DURATION_FIELD_NUMBER: _ClassVar[int]
        CONFIRM_DETECTION_WITH_PIR_FIELD_NUMBER: _ClassVar[int]
        LINE_CROSSING_CHANGES_FIELD_NUMBER: _ClassVar[int]
        notification_settings_entries: _containers.RepeatedCompositeFieldContainer[
            SetVideoNotificationSettingsRequest.NotificationSettings.NotificationSettingsEntry
        ]
        monitoring_state: (
            _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
        )
        cooldown_period: _duration_pb2.Duration
        object_detection_duration: _video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
        confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
        line_crossing_changes: _containers.RepeatedCompositeFieldContainer[
            SetVideoNotificationSettingsRequest.NotificationSettings.LineCrossingNotificationSettingsChange
        ]
        def __init__(
            self,
            notification_settings_entries: _Iterable[
                SetVideoNotificationSettingsRequest.NotificationSettings.NotificationSettingsEntry
                | _Mapping
            ]
            | None = ...,
            monitoring_state: _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
            | str
            | None = ...,
            cooldown_period: datetime.timedelta
            | _duration_pb2.Duration
            | _Mapping
            | None = ...,
            object_detection_duration: _video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
            | str
            | None = ...,
            confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
            | str
            | None = ...,
            line_crossing_changes: _Iterable[
                SetVideoNotificationSettingsRequest.NotificationSettings.LineCrossingNotificationSettingsChange
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    channel_id: str
    notification_settings: SetVideoNotificationSettingsRequest.NotificationSettings
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        notification_settings: SetVideoNotificationSettingsRequest.NotificationSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
