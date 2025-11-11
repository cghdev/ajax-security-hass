from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.videoedge.detector import (
    detector_pb2 as _detector_pb2,
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

class VideoNotificationSettings(_message.Message):
    __slots__ = (
        "confirm_detection_with_pir",
        "cooldown_period",
        "detection_type_enabled_states",
        "enabled_detector_types",
        "line_crossing_settings",
        "monitoring_state",
        "notification_settings_entries",
        "object_detection_duration",
    )
    class NotificationStateEntry(_message.Message):
        __slots__ = ("detector_type", "state", "type")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        DETECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _video_notification_type_pb2.VideoNotificationType
        state: _video_notification_state_pb2.VideoNotificationState
        detector_type: _detector_pb2.DetectorType
        def __init__(
            self,
            type: _video_notification_type_pb2.VideoNotificationType | str | None = ...,
            state: _video_notification_state_pb2.VideoNotificationState
            | str
            | None = ...,
            detector_type: _detector_pb2.DetectorType | str | None = ...,
        ) -> None: ...

    class LineCrossingNotificationSettings(_message.Message):
        __slots__ = ("enabled_rules", "notification_state_entries")
        NOTIFICATION_STATE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        ENABLED_RULES_FIELD_NUMBER: _ClassVar[int]
        notification_state_entries: _containers.RepeatedCompositeFieldContainer[
            VideoNotificationSettings.LineCrossingNotificationState
        ]
        enabled_rules: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self,
            notification_state_entries: _Iterable[
                VideoNotificationSettings.LineCrossingNotificationState | _Mapping
            ]
            | None = ...,
            enabled_rules: _Iterable[int] | None = ...,
        ) -> None: ...

    class LineCrossingNotificationState(_message.Message):
        __slots__ = ("rule_id", "rule_name", "state")
        RULE_ID_FIELD_NUMBER: _ClassVar[int]
        RULE_NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        rule_id: int
        rule_name: str
        state: _video_notification_state_pb2.VideoNotificationState
        def __init__(
            self,
            rule_id: int | None = ...,
            rule_name: str | None = ...,
            state: _video_notification_state_pb2.VideoNotificationState
            | str
            | None = ...,
        ) -> None: ...

    class DetectionTypeEnabledState(_message.Message):
        __slots__ = ("detection_type", "enabled")
        DETECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        detection_type: _video_notification_type_pb2.VideoNotificationType
        enabled: bool
        def __init__(
            self,
            detection_type: _video_notification_type_pb2.VideoNotificationType
            | str
            | None = ...,
            enabled: bool = ...,
        ) -> None: ...

    NOTIFICATION_SETTINGS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    ENABLED_DETECTOR_TYPES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DETECTION_WITH_PIR_FIELD_NUMBER: _ClassVar[int]
    DETECTION_TYPE_ENABLED_STATES_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    notification_settings_entries: _containers.RepeatedCompositeFieldContainer[
        VideoNotificationSettings.NotificationStateEntry
    ]
    monitoring_state: (
        _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
    )
    cooldown_period: _duration_pb2.Duration
    enabled_detector_types: _containers.RepeatedScalarFieldContainer[
        _detector_pb2.DetectorType
    ]
    object_detection_duration: _video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
    confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
    detection_type_enabled_states: _containers.RepeatedCompositeFieldContainer[
        VideoNotificationSettings.DetectionTypeEnabledState
    ]
    line_crossing_settings: VideoNotificationSettings.LineCrossingNotificationSettings
    def __init__(
        self,
        notification_settings_entries: _Iterable[
            VideoNotificationSettings.NotificationStateEntry | _Mapping
        ]
        | None = ...,
        monitoring_state: _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
        | str
        | None = ...,
        cooldown_period: _duration_pb2.Duration | _Mapping | None = ...,
        enabled_detector_types: _Iterable[_detector_pb2.DetectorType | str]
        | None = ...,
        object_detection_duration: _video_notification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
        | str
        | None = ...,
        confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
        | str
        | None = ...,
        detection_type_enabled_states: _Iterable[
            VideoNotificationSettings.DetectionTypeEnabledState | _Mapping
        ]
        | None = ...,
        line_crossing_settings: VideoNotificationSettings.LineCrossingNotificationSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
