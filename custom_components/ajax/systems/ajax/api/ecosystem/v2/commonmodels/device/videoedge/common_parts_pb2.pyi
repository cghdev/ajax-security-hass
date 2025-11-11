from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    alert_with_siren_pb2 as _alert_with_siren_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    detector_settings_pb2 as _detector_settings_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    fan_speed_settings_pb2 as _fan_speed_settings_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    local_user_permissions_pb2 as _local_user_permissions_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    max_ring_depth_pb2 as _max_ring_depth_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    media_settings_pb2 as _media_settings_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    network_pb2 as _network_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    notification_event_type_pb2 as _notification_event_type_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    onvif_user_role_pb2 as _onvif_user_role_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    video_nofification_object_detection_duration_pb2 as _video_nofification_object_detection_duration_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    video_notification_confirm_detection_with_pir_state_pb2 as _video_notification_confirm_detection_with_pir_state_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    video_notification_monitoring_state_pb2 as _video_notification_monitoring_state_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    video_notification_state_pb2 as _video_notification_state_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    video_notificaton_type_pb2 as _video_notificaton_type_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge.archive import (
    record_mode_pb2 as _record_mode_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge.archive import (
    record_policy_pb2 as _record_policy_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoConnectionTypePart(_message.Message):
    __slots__ = ("ethernet",)
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    ethernet: _network_pb2.NetworkConfiguration
    def __init__(
        self, ethernet: _network_pb2.NetworkConfiguration | _Mapping | None = ...
    ) -> None: ...

class VideoArchivePart(_message.Message):
    __slots__ = ("max_ring_depth",)
    MAX_RING_DEPTH_FIELD_NUMBER: _ClassVar[int]
    max_ring_depth: _max_ring_depth_pb2.MaxRingDepth
    def __init__(
        self, max_ring_depth: _max_ring_depth_pb2.MaxRingDepth | str | None = ...
    ) -> None: ...

class VideoLocalUsersPart(_message.Message):
    __slots__ = ("users",)
    class VideoLocalUser(_message.Message):
        __slots__ = ("name", "password", "permissions")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        password: str
        permissions: _local_user_permissions_pb2.LocalUserPermissions
        def __init__(
            self,
            name: str | None = ...,
            password: str | None = ...,
            permissions: _local_user_permissions_pb2.LocalUserPermissions
            | _Mapping
            | None = ...,
        ) -> None: ...

    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[
        VideoLocalUsersPart.VideoLocalUser
    ]
    def __init__(
        self,
        users: _Iterable[VideoLocalUsersPart.VideoLocalUser | _Mapping] | None = ...,
    ) -> None: ...

class TimeZonePart(_message.Message):
    __slots__ = ("time_zone_id",)
    TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    time_zone_id: str
    def __init__(self, time_zone_id: str | None = ...) -> None: ...

class LogoLedBrightnessPart(_message.Message):
    __slots__ = ("brightness",)
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    brightness: int
    def __init__(self, brightness: int | None = ...) -> None: ...

class RingButtonSoundPart(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class FanSettingsPart(_message.Message):
    __slots__ = ("fan_speed_settings",)
    FAN_SPEED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    fan_speed_settings: _fan_speed_settings_pb2.FanSpeedSettings
    def __init__(
        self,
        fan_speed_settings: _fan_speed_settings_pb2.FanSpeedSettings
        | _Mapping
        | None = ...,
    ) -> None: ...

class CloudConnectionPart(_message.Message):
    __slots__ = (
        "connection_failure_alarm_delay",
        "mute_connection_alarms",
        "server_ping_interval",
    )
    SERVER_PING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FAILURE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    MUTE_CONNECTION_ALARMS_FIELD_NUMBER: _ClassVar[int]
    server_ping_interval: _duration_pb2.Duration
    connection_failure_alarm_delay: _duration_pb2.Duration
    mute_connection_alarms: bool
    def __init__(
        self,
        server_ping_interval: _duration_pb2.Duration | _Mapping | None = ...,
        connection_failure_alarm_delay: _duration_pb2.Duration | _Mapping | None = ...,
        mute_connection_alarms: bool = ...,
    ) -> None: ...

class OnvifConnectionPart(_message.Message):
    __slots__ = (
        "onvif_http_port",
        "onvif_user_auth_enabled",
        "rtsp_http_port",
        "users",
    )
    class OnvifUser(_message.Message):
        __slots__ = ("password", "role", "username")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: str
        role: _onvif_user_role_pb2.OnvifUserRole
        def __init__(
            self,
            username: str | None = ...,
            password: str | None = ...,
            role: _onvif_user_role_pb2.OnvifUserRole | str | None = ...,
        ) -> None: ...

    ONVIF_USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ONVIF_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    RTSP_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    onvif_user_auth_enabled: bool
    onvif_http_port: int
    rtsp_http_port: int
    users: _containers.RepeatedCompositeFieldContainer[OnvifConnectionPart.OnvifUser]
    def __init__(
        self,
        onvif_user_auth_enabled: bool = ...,
        onvif_http_port: int | None = ...,
        rtsp_http_port: int | None = ...,
        users: _Iterable[OnvifConnectionPart.OnvifUser | _Mapping] | None = ...,
    ) -> None: ...

class ChimePart(_message.Message):
    __slots__ = ("digital", "mechanical", "off", "siren_mode")
    class OffMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MechanicalMode(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(
            self, duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    class DigitalMode(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(
            self, duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    class SirenMode(_message.Message):
        __slots__ = ("chime_signal",)
        CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
        chime_signal: int
        def __init__(self, chime_signal: int | None = ...) -> None: ...

    OFF_FIELD_NUMBER: _ClassVar[int]
    MECHANICAL_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_FIELD_NUMBER: _ClassVar[int]
    SIREN_MODE_FIELD_NUMBER: _ClassVar[int]
    off: ChimePart.OffMode
    mechanical: ChimePart.MechanicalMode
    digital: ChimePart.DigitalMode
    siren_mode: ChimePart.SirenMode
    def __init__(
        self,
        off: ChimePart.OffMode | _Mapping | None = ...,
        mechanical: ChimePart.MechanicalMode | _Mapping | None = ...,
        digital: ChimePart.DigitalMode | _Mapping | None = ...,
        siren_mode: ChimePart.SirenMode | _Mapping | None = ...,
    ) -> None: ...

class RecordingPreferencesPart(_message.Message):
    __slots__ = ("cloud_archive_source", "nvr_source", "primary_source")
    class RecordingPreference(_message.Message):
        __slots__ = (
            "cooldown_interval",
            "record_duration",
            "record_mode",
            "record_policy",
        )
        RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
        RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
        RECORD_DURATION_FIELD_NUMBER: _ClassVar[int]
        COOLDOWN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        record_mode: _record_mode_pb2.RecordMode
        record_policy: _record_policy_pb2.RecordPolicy
        record_duration: _duration_pb2.Duration
        cooldown_interval: _duration_pb2.Duration
        def __init__(
            self,
            record_mode: _record_mode_pb2.RecordMode | str | None = ...,
            record_policy: _record_policy_pb2.RecordPolicy | str | None = ...,
            record_duration: _duration_pb2.Duration | _Mapping | None = ...,
            cooldown_interval: _duration_pb2.Duration | _Mapping | None = ...,
        ) -> None: ...

    PRIMARY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NVR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ARCHIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    primary_source: RecordingPreferencesPart.RecordingPreference
    nvr_source: RecordingPreferencesPart.RecordingPreference
    cloud_archive_source: RecordingPreferencesPart.RecordingPreference
    def __init__(
        self,
        primary_source: RecordingPreferencesPart.RecordingPreference
        | _Mapping
        | None = ...,
        nvr_source: RecordingPreferencesPart.RecordingPreference
        | _Mapping
        | None = ...,
        cloud_archive_source: RecordingPreferencesPart.RecordingPreference
        | _Mapping
        | None = ...,
    ) -> None: ...

class NotificationSettingsPart(_message.Message):
    __slots__ = (
        "confirm_detection_with_pir",
        "cooldown_period",
        "monitoring_state",
        "object_detection_duration",
        "settings",
    )
    class NotificationSettingsEntry(_message.Message):
        __slots__ = ("alert_with_siren", "notification_event_type", "state", "type")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ALERT_WITH_SIREN_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        type: _video_notificaton_type_pb2.VideoNotificationType
        alert_with_siren: _alert_with_siren_pb2.AlertWithSiren
        notification_event_type: _notification_event_type_pb2.NotificationEventType
        state: _video_notification_state_pb2.VideoNotificationState
        def __init__(
            self,
            type: _video_notificaton_type_pb2.VideoNotificationType | str | None = ...,
            alert_with_siren: _alert_with_siren_pb2.AlertWithSiren | str | None = ...,
            notification_event_type: _notification_event_type_pb2.NotificationEventType
            | str
            | None = ...,
            state: _video_notification_state_pb2.VideoNotificationState
            | str
            | None = ...,
        ) -> None: ...

    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DETECTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DETECTION_WITH_PIR_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[
        NotificationSettingsPart.NotificationSettingsEntry
    ]
    cooldown_period: _duration_pb2.Duration
    monitoring_state: (
        _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
    )
    object_detection_duration: _video_nofification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
    confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
    def __init__(
        self,
        settings: _Iterable[
            NotificationSettingsPart.NotificationSettingsEntry | _Mapping
        ]
        | None = ...,
        cooldown_period: _duration_pb2.Duration | _Mapping | None = ...,
        monitoring_state: _video_notification_monitoring_state_pb2.VideoNotificationMonitoringState
        | str
        | None = ...,
        object_detection_duration: _video_nofification_object_detection_duration_pb2.VideoNotificationObjectDetectionDuration
        | str
        | None = ...,
        confirm_detection_with_pir: _video_notification_confirm_detection_with_pir_state_pb2.VideoNotificationConfirmDetectionWithPirState
        | str
        | None = ...,
    ) -> None: ...

class DetectionSettingsPart(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[
        _detector_settings_pb2.DetectorSettings
    ]
    def __init__(
        self,
        settings: _Iterable[_detector_settings_pb2.DetectorSettings | _Mapping]
        | None = ...,
    ) -> None: ...

class MediaSettingsPart(_message.Message):
    __slots__ = (
        "audio_output_settings",
        "audio_settings",
        "image_settings",
        "mainstream_video_stream_settings",
        "substream_video_stream_settings",
    )
    IMAGE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAINSTREAM_VIDEO_STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SUBSTREAM_VIDEO_STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    image_settings: _media_settings_pb2.ImageSettings
    mainstream_video_stream_settings: _media_settings_pb2.VideoStreamSettings
    substream_video_stream_settings: _media_settings_pb2.VideoStreamSettings
    audio_settings: _media_settings_pb2.AudioSettings
    audio_output_settings: _media_settings_pb2.AudioOutputSettings
    def __init__(
        self,
        image_settings: _media_settings_pb2.ImageSettings | _Mapping | None = ...,
        mainstream_video_stream_settings: _media_settings_pb2.VideoStreamSettings
        | _Mapping
        | None = ...,
        substream_video_stream_settings: _media_settings_pb2.VideoStreamSettings
        | _Mapping
        | None = ...,
        audio_settings: _media_settings_pb2.AudioSettings | _Mapping | None = ...,
        audio_output_settings: _media_settings_pb2.AudioOutputSettings
        | _Mapping
        | None = ...,
    ) -> None: ...

class MotionDetectionLedIndicationPart(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class RingButtonBellPart(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...
