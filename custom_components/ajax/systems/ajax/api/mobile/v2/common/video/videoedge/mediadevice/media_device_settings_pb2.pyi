from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectionSettings(_message.Message):
    __slots__ = ("address", "password", "port", "username")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: str
    username: str
    password: str
    def __init__(
        self,
        address: str | None = ...,
        port: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
    ) -> None: ...

class VideoSettings(_message.Message):
    __slots__ = (
        "anti_flicker",
        "blc",
        "brightness",
        "contrast",
        "exposure",
        "exposure_metering_area",
        "image_profile",
        "ir_illumination",
        "ircut_filter",
        "main",
        "noise_reduction",
        "off_illumination",
        "privacy_masks",
        "saturation",
        "sharpness",
        "smart_illumination",
        "sub",
        "transform",
        "wdr",
        "white_balance",
        "white_illumination",
    )
    class ImageProfile(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _types_pb2.ImageProfileType
        def __init__(
            self, type: _types_pb2.ImageProfileType | str | None = ...
        ) -> None: ...

    class BacklightCompensation(_message.Message):
        __slots__ = ("off", "on")
        class OnMode(_message.Message):
            __slots__ = ("level",)
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            level: float
            def __init__(self, level: float | None = ...) -> None: ...

        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        OFF_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        off: VideoSettings.BacklightCompensation.OffMode
        on: VideoSettings.BacklightCompensation.OnMode
        def __init__(
            self,
            off: VideoSettings.BacklightCompensation.OffMode | _Mapping | None = ...,
            on: VideoSettings.BacklightCompensation.OnMode | _Mapping | None = ...,
        ) -> None: ...

    class WhiteBalance(_message.Message):
        __slots__ = ("auto", "manual")
        class ManualMode(_message.Message):
            __slots__ = ("blue_gain", "red_gain")
            RED_GAIN_FIELD_NUMBER: _ClassVar[int]
            BLUE_GAIN_FIELD_NUMBER: _ClassVar[int]
            red_gain: float
            blue_gain: float
            def __init__(
                self, red_gain: float | None = ..., blue_gain: float | None = ...
            ) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        MANUAL_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        manual: VideoSettings.WhiteBalance.ManualMode
        auto: VideoSettings.WhiteBalance.AutoMode
        def __init__(
            self,
            manual: VideoSettings.WhiteBalance.ManualMode | _Mapping | None = ...,
            auto: VideoSettings.WhiteBalance.AutoMode | _Mapping | None = ...,
        ) -> None: ...

    class WideDynamicRange(_message.Message):
        __slots__ = ("off", "on")
        class OnMode(_message.Message):
            __slots__ = ("level",)
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            level: float
            def __init__(self, level: float | None = ...) -> None: ...

        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        OFF_FIELD_NUMBER: _ClassVar[int]
        ON_FIELD_NUMBER: _ClassVar[int]
        off: VideoSettings.WideDynamicRange.OffMode
        on: VideoSettings.WideDynamicRange.OnMode
        def __init__(
            self,
            off: VideoSettings.WideDynamicRange.OffMode | _Mapping | None = ...,
            on: VideoSettings.WideDynamicRange.OnMode | _Mapping | None = ...,
        ) -> None: ...

    class Exposure(_message.Message):
        __slots__ = ("auto", "manual")
        class ManualMode(_message.Message):
            __slots__ = ("exposure_time", "gain", "iris")
            EXPOSURE_TIME_FIELD_NUMBER: _ClassVar[int]
            GAIN_FIELD_NUMBER: _ClassVar[int]
            IRIS_FIELD_NUMBER: _ClassVar[int]
            exposure_time: _duration_pb2.Duration
            gain: float
            iris: float
            def __init__(
                self,
                exposure_time: _duration_pb2.Duration | _Mapping | None = ...,
                gain: float | None = ...,
                iris: float | None = ...,
            ) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = (
                "exposure_compensation",
                "exposure_time_range",
                "gain_range",
                "iris_range",
                "preset",
                "priority",
            )
            PRIORITY_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            IRIS_RANGE_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_COMPENSATION_FIELD_NUMBER: _ClassVar[int]
            PRESET_FIELD_NUMBER: _ClassVar[int]
            priority: _types_pb2.ExposurePriority
            exposure_time_range: _types_pb2.DurationRange
            gain_range: _types_pb2.FloatRange
            iris_range: _types_pb2.FloatRange
            exposure_compensation: int
            preset: _types_pb2.AutoExposurePreset
            def __init__(
                self,
                priority: _types_pb2.ExposurePriority | str | None = ...,
                exposure_time_range: _types_pb2.DurationRange | _Mapping | None = ...,
                gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
                iris_range: _types_pb2.FloatRange | _Mapping | None = ...,
                exposure_compensation: int | None = ...,
                preset: _types_pb2.AutoExposurePreset | str | None = ...,
            ) -> None: ...

        MANUAL_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        manual: VideoSettings.Exposure.ManualMode
        auto: VideoSettings.Exposure.AutoMode
        def __init__(
            self,
            manual: VideoSettings.Exposure.ManualMode | _Mapping | None = ...,
            auto: VideoSettings.Exposure.AutoMode | _Mapping | None = ...,
        ) -> None: ...

    class IrCutFilter(_message.Message):
        __slots__ = ("auto", "off", "on")
        class OnMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = ("ircut_filter_auto_adjustments",)
            class IrCutFilterAutoAdjustment(_message.Message):
                __slots__ = ("boundary_offset", "boundary_type", "response_time")
                BOUNDARY_TYPE_FIELD_NUMBER: _ClassVar[int]
                BOUNDARY_OFFSET_FIELD_NUMBER: _ClassVar[int]
                RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
                boundary_type: _types_pb2.IrCutFilterAutoBoundaryType
                boundary_offset: float
                response_time: _duration_pb2.Duration
                def __init__(
                    self,
                    boundary_type: _types_pb2.IrCutFilterAutoBoundaryType
                    | str
                    | None = ...,
                    boundary_offset: float | None = ...,
                    response_time: _duration_pb2.Duration | _Mapping | None = ...,
                ) -> None: ...

            IRCUT_FILTER_AUTO_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
            ircut_filter_auto_adjustments: _containers.RepeatedCompositeFieldContainer[
                VideoSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment
            ]
            def __init__(
                self,
                ircut_filter_auto_adjustments: _Iterable[
                    VideoSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        on: VideoSettings.IrCutFilter.OnMode
        off: VideoSettings.IrCutFilter.OffMode
        auto: VideoSettings.IrCutFilter.AutoMode
        def __init__(
            self,
            on: VideoSettings.IrCutFilter.OnMode | _Mapping | None = ...,
            off: VideoSettings.IrCutFilter.OffMode | _Mapping | None = ...,
            auto: VideoSettings.IrCutFilter.AutoMode | _Mapping | None = ...,
        ) -> None: ...

    class Stream(_message.Message):
        __slots__ = (
            "bitrate",
            "bitrate_type",
            "codec",
            "codec_extradata",
            "enabled",
            "fps",
            "gop_size",
            "quality",
            "resolution",
        )
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CODEC_FIELD_NUMBER: _ClassVar[int]
        CODEC_EXTRADATA_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        BITRATE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        GOP_SIZE_FIELD_NUMBER: _ClassVar[int]
        FPS_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        codec: _types_pb2.VideoCodec
        codec_extradata: bytes
        resolution: _types_pb2.VideoResolution
        bitrate: int
        bitrate_type: _types_pb2.VideoBitrateType
        gop_size: int
        fps: int
        quality: int
        def __init__(
            self,
            enabled: bool = ...,
            codec: _types_pb2.VideoCodec | str | None = ...,
            codec_extradata: bytes | None = ...,
            resolution: _types_pb2.VideoResolution | _Mapping | None = ...,
            bitrate: int | None = ...,
            bitrate_type: _types_pb2.VideoBitrateType | str | None = ...,
            gop_size: int | None = ...,
            fps: int | None = ...,
            quality: int | None = ...,
        ) -> None: ...

    class Transform(_message.Message):
        __slots__ = ("mirror", "rotation")
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        MIRROR_FIELD_NUMBER: _ClassVar[int]
        rotation: _types_pb2.Rotation
        mirror: bool
        def __init__(
            self, rotation: _types_pb2.Rotation | str | None = ..., mirror: bool = ...
        ) -> None: ...

    class OffIllumination(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class IrIllumination(_message.Message):
        __slots__ = ("auto", "manual")
        class ManualMode(_message.Message):
            __slots__ = ("power_level",)
            POWER_LEVEL_FIELD_NUMBER: _ClassVar[int]
            power_level: int
            def __init__(self, power_level: int | None = ...) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        AUTO_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        auto: VideoSettings.IrIllumination.AutoMode
        manual: VideoSettings.IrIllumination.ManualMode
        def __init__(
            self,
            auto: VideoSettings.IrIllumination.AutoMode | _Mapping | None = ...,
            manual: VideoSettings.IrIllumination.ManualMode | _Mapping | None = ...,
        ) -> None: ...

    class WhiteIllumination(_message.Message):
        __slots__ = ("auto", "manual")
        class ManualMode(_message.Message):
            __slots__ = ("power_level",)
            POWER_LEVEL_FIELD_NUMBER: _ClassVar[int]
            power_level: int
            def __init__(self, power_level: int | None = ...) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = ("max_power_level",)
            MAX_POWER_LEVEL_FIELD_NUMBER: _ClassVar[int]
            max_power_level: int
            def __init__(self, max_power_level: int | None = ...) -> None: ...

        AUTO_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        auto: VideoSettings.WhiteIllumination.AutoMode
        manual: VideoSettings.WhiteIllumination.ManualMode
        def __init__(
            self,
            auto: VideoSettings.WhiteIllumination.AutoMode | _Mapping | None = ...,
            manual: VideoSettings.WhiteIllumination.ManualMode | _Mapping | None = ...,
        ) -> None: ...

    class SmartIllumination(_message.Message):
        __slots__ = ("ir_illumination", "white_illumination")
        IR_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
        WHITE_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
        ir_illumination: VideoSettings.IrIllumination
        white_illumination: VideoSettings.WhiteIllumination
        def __init__(
            self,
            ir_illumination: VideoSettings.IrIllumination | _Mapping | None = ...,
            white_illumination: VideoSettings.WhiteIllumination | _Mapping | None = ...,
        ) -> None: ...

    class PrivacyMasks(_message.Message):
        __slots__ = ("entries",)
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[VideoSettings.PrivacyMask]
        def __init__(
            self, entries: _Iterable[VideoSettings.PrivacyMask | _Mapping] | None = ...
        ) -> None: ...

    class PrivacyMask(_message.Message):
        __slots__ = ("color", "enabled", "polygon", "type")
        class Polygon(_message.Message):
            __slots__ = ("points",)
            POINTS_FIELD_NUMBER: _ClassVar[int]
            points: _containers.RepeatedCompositeFieldContainer[_types_pb2.Point2i]
            def __init__(
                self, points: _Iterable[_types_pb2.Point2i | _Mapping] | None = ...
            ) -> None: ...

        ENABLED_FIELD_NUMBER: _ClassVar[int]
        POLYGON_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        polygon: VideoSettings.PrivacyMask.Polygon
        type: _types_pb2.PrivacyMaskType
        color: _types_pb2.Color
        def __init__(
            self,
            enabled: bool = ...,
            polygon: VideoSettings.PrivacyMask.Polygon | _Mapping | None = ...,
            type: _types_pb2.PrivacyMaskType | str | None = ...,
            color: _types_pb2.Color | _Mapping | None = ...,
        ) -> None: ...

    class ExposureMeteringArea(_message.Message):
        __slots__ = ("predefined",)
        PREDEFINED_FIELD_NUMBER: _ClassVar[int]
        predefined: _types_pb2.PredefinedExposureMeteringArea
        def __init__(
            self,
            predefined: _types_pb2.PredefinedExposureMeteringArea | str | None = ...,
        ) -> None: ...

    class AntiFlicker(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _types_pb2.AntiFlickerType
        def __init__(
            self, type: _types_pb2.AntiFlickerType | str | None = ...
        ) -> None: ...

    class NoiseReduction(_message.Message):
        __slots__ = ("off", "on")
        class OnMode(_message.Message):
            __slots__ = ("level", "midpoint_level")
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            MIDPOINT_LEVEL_FIELD_NUMBER: _ClassVar[int]
            level: int
            midpoint_level: int
            def __init__(
                self, level: int | None = ..., midpoint_level: int | None = ...
            ) -> None: ...

        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        on: VideoSettings.NoiseReduction.OnMode
        off: VideoSettings.NoiseReduction.OffMode
        def __init__(
            self,
            on: VideoSettings.NoiseReduction.OnMode | _Mapping | None = ...,
            off: VideoSettings.NoiseReduction.OffMode | _Mapping | None = ...,
        ) -> None: ...

    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    CONTRAST_FIELD_NUMBER: _ClassVar[int]
    SATURATION_FIELD_NUMBER: _ClassVar[int]
    SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    BLC_FIELD_NUMBER: _ClassVar[int]
    WHITE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    WDR_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    IRCUT_FILTER_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    OFF_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    IR_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    WHITE_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    SMART_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_MASKS_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_METERING_AREA_FIELD_NUMBER: _ClassVar[int]
    ANTI_FLICKER_FIELD_NUMBER: _ClassVar[int]
    NOISE_REDUCTION_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    brightness: int
    contrast: int
    saturation: int
    sharpness: int
    blc: VideoSettings.BacklightCompensation
    white_balance: VideoSettings.WhiteBalance
    wdr: VideoSettings.WideDynamicRange
    exposure: VideoSettings.Exposure
    ircut_filter: VideoSettings.IrCutFilter
    transform: VideoSettings.Transform
    off_illumination: VideoSettings.OffIllumination
    ir_illumination: VideoSettings.IrIllumination
    white_illumination: VideoSettings.WhiteIllumination
    smart_illumination: VideoSettings.SmartIllumination
    privacy_masks: VideoSettings.PrivacyMasks
    exposure_metering_area: VideoSettings.ExposureMeteringArea
    anti_flicker: VideoSettings.AntiFlicker
    noise_reduction: VideoSettings.NoiseReduction
    main: VideoSettings.Stream
    sub: VideoSettings.Stream
    image_profile: VideoSettings.ImageProfile
    def __init__(
        self,
        brightness: int | None = ...,
        contrast: int | None = ...,
        saturation: int | None = ...,
        sharpness: int | None = ...,
        blc: VideoSettings.BacklightCompensation | _Mapping | None = ...,
        white_balance: VideoSettings.WhiteBalance | _Mapping | None = ...,
        wdr: VideoSettings.WideDynamicRange | _Mapping | None = ...,
        exposure: VideoSettings.Exposure | _Mapping | None = ...,
        ircut_filter: VideoSettings.IrCutFilter | _Mapping | None = ...,
        transform: VideoSettings.Transform | _Mapping | None = ...,
        off_illumination: VideoSettings.OffIllumination | _Mapping | None = ...,
        ir_illumination: VideoSettings.IrIllumination | _Mapping | None = ...,
        white_illumination: VideoSettings.WhiteIllumination | _Mapping | None = ...,
        smart_illumination: VideoSettings.SmartIllumination | _Mapping | None = ...,
        privacy_masks: VideoSettings.PrivacyMasks | _Mapping | None = ...,
        exposure_metering_area: VideoSettings.ExposureMeteringArea
        | _Mapping
        | None = ...,
        anti_flicker: VideoSettings.AntiFlicker | _Mapping | None = ...,
        noise_reduction: VideoSettings.NoiseReduction | _Mapping | None = ...,
        main: VideoSettings.Stream | _Mapping | None = ...,
        sub: VideoSettings.Stream | _Mapping | None = ...,
        image_profile: VideoSettings.ImageProfile | _Mapping | None = ...,
    ) -> None: ...

class AudioSettings(_message.Message):
    __slots__ = (
        "bitrate",
        "codec",
        "codec_extradata",
        "enabled",
        "mic_gain",
        "mic_volume",
        "sample_rate",
    )
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    CODEC_EXTRADATA_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    MIC_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MIC_GAIN_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    codec: _types_pb2.AudioCodec
    codec_extradata: bytes
    bitrate: int
    sample_rate: int
    mic_volume: int
    mic_gain: int
    def __init__(
        self,
        enabled: bool = ...,
        codec: _types_pb2.AudioCodec | str | None = ...,
        codec_extradata: bytes | None = ...,
        bitrate: int | None = ...,
        sample_rate: int | None = ...,
        mic_volume: int | None = ...,
        mic_gain: int | None = ...,
    ) -> None: ...

class AudioOutputSettings(_message.Message):
    __slots__ = ("volume",)
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    volume: int
    def __init__(self, volume: int | None = ...) -> None: ...

class ChannelSettings(_message.Message):
    __slots__ = ("audio", "audio_output", "channel_id", "video")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    video: VideoSettings
    audio: AudioSettings
    audio_output: AudioOutputSettings
    def __init__(
        self,
        channel_id: str | None = ...,
        video: VideoSettings | _Mapping | None = ...,
        audio: AudioSettings | _Mapping | None = ...,
        audio_output: AudioOutputSettings | _Mapping | None = ...,
    ) -> None: ...

class MediaDeviceSettings(_message.Message):
    __slots__ = ("channels",)
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[ChannelSettings]
    def __init__(
        self, channels: _Iterable[ChannelSettings | _Mapping] | None = ...
    ) -> None: ...
