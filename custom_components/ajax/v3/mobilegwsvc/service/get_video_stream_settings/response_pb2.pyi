from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_capabilities_pb2 as _media_device_capabilities_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_settings_pb2 as _media_device_settings_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video import (
    setting_availability_mode_pb2 as _setting_availability_mode_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoStreamSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class SettingsLimitationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SETTINGS_LIMITATION_MODE_UNSPECIFIED: _ClassVar[
            GetVideoStreamSettingsResponse.SettingsLimitationMode
        ]
        SETTINGS_LIMITATION_MODE_NOT_LIMITED: _ClassVar[
            GetVideoStreamSettingsResponse.SettingsLimitationMode
        ]
        SETTINGS_LIMITATION_MODE_LIMITED_BY_EXTRA_SERVICES: _ClassVar[
            GetVideoStreamSettingsResponse.SettingsLimitationMode
        ]

    SETTINGS_LIMITATION_MODE_UNSPECIFIED: (
        GetVideoStreamSettingsResponse.SettingsLimitationMode
    )
    SETTINGS_LIMITATION_MODE_NOT_LIMITED: (
        GetVideoStreamSettingsResponse.SettingsLimitationMode
    )
    SETTINGS_LIMITATION_MODE_LIMITED_BY_EXTRA_SERVICES: (
        GetVideoStreamSettingsResponse.SettingsLimitationMode
    )
    class Success(_message.Message):
        __slots__ = (
            "main_availability",
            "main_limitations",
            "main_settings",
            "settings_limitation_mode",
            "sub_availability",
            "sub_limitations",
            "sub_settings",
        )
        MAIN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SUB_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        MAIN_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        SUB_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        MAIN_LIMITATIONS_FIELD_NUMBER: _ClassVar[int]
        SUB_LIMITATIONS_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_LIMITATION_MODE_FIELD_NUMBER: _ClassVar[int]
        main_settings: _media_device_settings_pb2.VideoSettings.Stream
        sub_settings: _media_device_settings_pb2.VideoSettings.Stream
        main_availability: (
            GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability
        )
        sub_availability: GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability
        main_limitations: _media_device_capabilities_pb2.VideoCapabilities.Stream
        sub_limitations: _media_device_capabilities_pb2.VideoCapabilities.Stream
        settings_limitation_mode: GetVideoStreamSettingsResponse.SettingsLimitationMode
        def __init__(
            self,
            main_settings: _media_device_settings_pb2.VideoSettings.Stream
            | _Mapping
            | None = ...,
            sub_settings: _media_device_settings_pb2.VideoSettings.Stream
            | _Mapping
            | None = ...,
            main_availability: GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability
            | _Mapping
            | None = ...,
            sub_availability: GetVideoStreamSettingsResponse.VideoStreamSettingsAvailability
            | _Mapping
            | None = ...,
            main_limitations: _media_device_capabilities_pb2.VideoCapabilities.Stream
            | _Mapping
            | None = ...,
            sub_limitations: _media_device_capabilities_pb2.VideoCapabilities.Stream
            | _Mapping
            | None = ...,
            settings_limitation_mode: GetVideoStreamSettingsResponse.SettingsLimitationMode
            | str
            | None = ...,
        ) -> None: ...

    class VideoStreamSettingsAvailability(_message.Message):
        __slots__ = (
            "bitrate",
            "bitrate_type",
            "codec",
            "fps",
            "gop_size",
            "quality",
            "resolution",
        )
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        CODEC_FIELD_NUMBER: _ClassVar[int]
        FPS_FIELD_NUMBER: _ClassVar[int]
        BITRATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_FIELD_NUMBER: _ClassVar[int]
        GOP_SIZE_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        resolution: _setting_availability_mode_pb2.SettingAvailabilityMode
        codec: _setting_availability_mode_pb2.SettingAvailabilityMode
        fps: _setting_availability_mode_pb2.SettingAvailabilityMode
        bitrate_type: _setting_availability_mode_pb2.SettingAvailabilityMode
        bitrate: _setting_availability_mode_pb2.SettingAvailabilityMode
        gop_size: _setting_availability_mode_pb2.SettingAvailabilityMode
        quality: _setting_availability_mode_pb2.SettingAvailabilityMode
        def __init__(
            self,
            resolution: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
            codec: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
            fps: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
            bitrate_type: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
            bitrate: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
            gop_size: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
            quality: _setting_availability_mode_pb2.SettingAvailabilityMode
            | str
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "permission_denied",
            "space_not_found",
            "stream_settings_not_found",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        STREAM_SETTINGS_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        stream_settings_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
            stream_settings_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoStreamSettingsResponse.Success
    failure: GetVideoStreamSettingsResponse.Failure
    def __init__(
        self,
        success: GetVideoStreamSettingsResponse.Success | _Mapping | None = ...,
        failure: GetVideoStreamSettingsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
