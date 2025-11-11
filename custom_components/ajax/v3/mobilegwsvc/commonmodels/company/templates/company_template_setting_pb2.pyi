from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import (
    common_arming_part_pb2 as _common_arming_part_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.common.type import (
    device_type_pb2 as _device_type_pb2,
)
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    common_parts_pb2 as _common_parts_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyTemplateSetting(_message.Message):
    __slots__ = (
        "chime",
        "cloud_connection",
        "common_arming_part_settings",
        "company_connection_details",
        "company_connection_type",
        "detection_settings",
        "fan_settings",
        "led_brightness",
        "local_users",
        "media_settings",
        "motion_detection_led_indication",
        "notification_settings",
        "onvif_connection",
        "recording_preferences",
        "ring_button_sound",
        "time_zone",
        "type",
        "video_archive",
        "video_connection_type",
    )
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[CompanyTemplateSetting.Mode]
        MODE_GENERIC: _ClassVar[CompanyTemplateSetting.Mode]
        MODE_PEER_TO_PEER: _ClassVar[CompanyTemplateSetting.Mode]
        MODE_AJAX_SIP: _ClassVar[CompanyTemplateSetting.Mode]

    MODE_UNSPECIFIED: CompanyTemplateSetting.Mode
    MODE_GENERIC: CompanyTemplateSetting.Mode
    MODE_PEER_TO_PEER: CompanyTemplateSetting.Mode
    MODE_AJAX_SIP: CompanyTemplateSetting.Mode
    class CompanyConnectionDetails(_message.Message):
        __slots__ = (
            "address",
            "company_name",
            "company_number",
            "connection_type",
            "port",
            "stun_address",
            "stun_port",
        )
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[
                CompanyTemplateSetting.CompanyConnectionDetails.Mode
            ]
            MODE_GENERIC: _ClassVar[
                CompanyTemplateSetting.CompanyConnectionDetails.Mode
            ]
            MODE_PEER_TO_PEER: _ClassVar[
                CompanyTemplateSetting.CompanyConnectionDetails.Mode
            ]
            MODE_AJAX_SIP: _ClassVar[
                CompanyTemplateSetting.CompanyConnectionDetails.Mode
            ]

        MODE_UNSPECIFIED: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        MODE_GENERIC: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        MODE_PEER_TO_PEER: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        MODE_AJAX_SIP: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
        COMPANY_NUMBER_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        STUN_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        STUN_PORT_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        company_name: str
        company_number: str
        address: str
        port: int
        stun_address: str
        stun_port: int
        connection_type: CompanyTemplateSetting.CompanyConnectionDetails.Mode
        def __init__(
            self,
            company_name: str | None = ...,
            company_number: str | None = ...,
            address: str | None = ...,
            port: int | None = ...,
            stun_address: str | None = ...,
            stun_port: int | None = ...,
            connection_type: CompanyTemplateSetting.CompanyConnectionDetails.Mode
            | str
            | None = ...,
        ) -> None: ...

    TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CONNECTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_USERS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    LED_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    FAN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    ONVIF_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    RECORDING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHIME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_ARMING_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_SOUND_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_LED_INDICATION_FIELD_NUMBER: _ClassVar[int]
    type: _device_type_pb2.DeviceType
    company_connection_details: CompanyTemplateSetting.CompanyConnectionDetails
    company_connection_type: CompanyTemplateSetting.Mode
    video_connection_type: _common_parts_pb2.VideoConnectionTypePart
    video_archive: _common_parts_pb2.VideoArchivePart
    local_users: _common_parts_pb2.VideoLocalUsersPart
    time_zone: _common_parts_pb2.TimeZonePart
    led_brightness: _common_parts_pb2.LogoLedBrightnessPart
    fan_settings: _common_parts_pb2.FanSettingsPart
    cloud_connection: _common_parts_pb2.CloudConnectionPart
    onvif_connection: _common_parts_pb2.OnvifConnectionPart
    recording_preferences: _common_parts_pb2.RecordingPreferencesPart
    media_settings: _common_parts_pb2.MediaSettingsPart
    chime: _common_parts_pb2.ChimePart
    notification_settings: _common_parts_pb2.NotificationSettingsPart
    detection_settings: _common_parts_pb2.DetectionSettingsPart
    common_arming_part_settings: (
        _common_arming_part_pb2.CommonArmingPart.CommonArmingPartSettings
    )
    ring_button_sound: _common_parts_pb2.RingButtonSoundPart
    motion_detection_led_indication: _common_parts_pb2.MotionDetectionLedIndicationPart
    def __init__(
        self,
        type: _device_type_pb2.DeviceType | _Mapping | None = ...,
        company_connection_details: CompanyTemplateSetting.CompanyConnectionDetails
        | _Mapping
        | None = ...,
        company_connection_type: CompanyTemplateSetting.Mode | str | None = ...,
        video_connection_type: _common_parts_pb2.VideoConnectionTypePart
        | _Mapping
        | None = ...,
        video_archive: _common_parts_pb2.VideoArchivePart | _Mapping | None = ...,
        local_users: _common_parts_pb2.VideoLocalUsersPart | _Mapping | None = ...,
        time_zone: _common_parts_pb2.TimeZonePart | _Mapping | None = ...,
        led_brightness: _common_parts_pb2.LogoLedBrightnessPart | _Mapping | None = ...,
        fan_settings: _common_parts_pb2.FanSettingsPart | _Mapping | None = ...,
        cloud_connection: _common_parts_pb2.CloudConnectionPart | _Mapping | None = ...,
        onvif_connection: _common_parts_pb2.OnvifConnectionPart | _Mapping | None = ...,
        recording_preferences: _common_parts_pb2.RecordingPreferencesPart
        | _Mapping
        | None = ...,
        media_settings: _common_parts_pb2.MediaSettingsPart | _Mapping | None = ...,
        chime: _common_parts_pb2.ChimePart | _Mapping | None = ...,
        notification_settings: _common_parts_pb2.NotificationSettingsPart
        | _Mapping
        | None = ...,
        detection_settings: _common_parts_pb2.DetectionSettingsPart
        | _Mapping
        | None = ...,
        common_arming_part_settings: _common_arming_part_pb2.CommonArmingPart.CommonArmingPartSettings
        | _Mapping
        | None = ...,
        ring_button_sound: _common_parts_pb2.RingButtonSoundPart
        | _Mapping
        | None = ...,
        motion_detection_led_indication: _common_parts_pb2.MotionDetectionLedIndicationPart
        | _Mapping
        | None = ...,
    ) -> None: ...
