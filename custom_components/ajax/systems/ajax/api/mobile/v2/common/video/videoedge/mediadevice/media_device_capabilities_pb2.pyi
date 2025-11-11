from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class VideoCapabilities(_message.Message):
    __slots__ = (
        "anti_flicker",
        "backlight",
        "blc",
        "exposure",
        "exposure_metering_area",
        "flags",
        "image_profile",
        "ircut_filter_mode",
        "main",
        "noise_reduction",
        "privacy_mask",
        "ptz",
        "sub",
        "transform",
        "wdr",
        "white_balance",
    )
    class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[VideoCapabilities.Flag]
        COMPRESSED_STREAM: _ClassVar[VideoCapabilities.Flag]
        HAVE_SUBSTREAM: _ClassVar[VideoCapabilities.Flag]
        HAVE_ANALYTICS_STREAM: _ClassVar[VideoCapabilities.Flag]
        HAVE_PTZ: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_BITRATE: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_BITRATE_TYPE: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_GOPSIZE: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_FPS: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_QUALITY: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_BRIGHTNESS: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_CONTRAST: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_SATURATION: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_SHARPNESS: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_BACKLIGHT_COMPENSATION: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_WHITE_BALANCE: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_WIDE_DYNAMIC_RANGE: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_EXPOSURE: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_IRCUT_FILTER: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_OSD: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_TRANSFORM: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_IR_ILLUMINATION: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_PRIVACY_MASK: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_EXPOSURE_METERING_AREA: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_ANTI_FLICKER: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_NOISE_REDUCTION: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_BACKLIGHT: _ClassVar[VideoCapabilities.Flag]
        CAN_SET_IMAGE_PROFILE: _ClassVar[VideoCapabilities.Flag]

    NONE: VideoCapabilities.Flag
    COMPRESSED_STREAM: VideoCapabilities.Flag
    HAVE_SUBSTREAM: VideoCapabilities.Flag
    HAVE_ANALYTICS_STREAM: VideoCapabilities.Flag
    HAVE_PTZ: VideoCapabilities.Flag
    CAN_SET_BITRATE: VideoCapabilities.Flag
    CAN_SET_BITRATE_TYPE: VideoCapabilities.Flag
    CAN_SET_GOPSIZE: VideoCapabilities.Flag
    CAN_SET_FPS: VideoCapabilities.Flag
    CAN_SET_QUALITY: VideoCapabilities.Flag
    CAN_SET_BRIGHTNESS: VideoCapabilities.Flag
    CAN_SET_CONTRAST: VideoCapabilities.Flag
    CAN_SET_SATURATION: VideoCapabilities.Flag
    CAN_SET_SHARPNESS: VideoCapabilities.Flag
    CAN_SET_BACKLIGHT_COMPENSATION: VideoCapabilities.Flag
    CAN_SET_WHITE_BALANCE: VideoCapabilities.Flag
    CAN_SET_WIDE_DYNAMIC_RANGE: VideoCapabilities.Flag
    CAN_SET_EXPOSURE: VideoCapabilities.Flag
    CAN_SET_IRCUT_FILTER: VideoCapabilities.Flag
    CAN_SET_OSD: VideoCapabilities.Flag
    CAN_SET_TRANSFORM: VideoCapabilities.Flag
    CAN_SET_IR_ILLUMINATION: VideoCapabilities.Flag
    CAN_SET_PRIVACY_MASK: VideoCapabilities.Flag
    CAN_SET_EXPOSURE_METERING_AREA: VideoCapabilities.Flag
    CAN_SET_ANTI_FLICKER: VideoCapabilities.Flag
    CAN_SET_NOISE_REDUCTION: VideoCapabilities.Flag
    CAN_SET_BACKLIGHT: VideoCapabilities.Flag
    CAN_SET_IMAGE_PROFILE: VideoCapabilities.Flag
    class NoiseReduction(_message.Message):
        __slots__ = ("midpoint_level_supported",)
        MIDPOINT_LEVEL_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        midpoint_level_supported: bool
        def __init__(self, midpoint_level_supported: bool = ...) -> None: ...

    class ImageProfile(_message.Message):
        __slots__ = ("types",)
        TYPES_FIELD_NUMBER: _ClassVar[int]
        types: _containers.RepeatedScalarFieldContainer[_types_pb2.ImageProfileType]
        def __init__(
            self, types: _Iterable[_types_pb2.ImageProfileType | str] | None = ...
        ) -> None: ...

    class Backlight(_message.Message):
        __slots__ = (
            "ir_illumination_mode",
            "off_illumination_mode",
            "smart_illumination_mode",
            "white_illumination_mode",
        )
        class OffIlluminationMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class IrIlluminationMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class WhiteIlluminationMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class SmartIlluminationMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        OFF_ILLUMINATION_MODE_FIELD_NUMBER: _ClassVar[int]
        IR_ILLUMINATION_MODE_FIELD_NUMBER: _ClassVar[int]
        WHITE_ILLUMINATION_MODE_FIELD_NUMBER: _ClassVar[int]
        SMART_ILLUMINATION_MODE_FIELD_NUMBER: _ClassVar[int]
        off_illumination_mode: VideoCapabilities.Backlight.OffIlluminationMode
        ir_illumination_mode: VideoCapabilities.Backlight.IrIlluminationMode
        white_illumination_mode: VideoCapabilities.Backlight.WhiteIlluminationMode
        smart_illumination_mode: VideoCapabilities.Backlight.SmartIlluminationMode
        def __init__(
            self,
            off_illumination_mode: VideoCapabilities.Backlight.OffIlluminationMode
            | _Mapping
            | None = ...,
            ir_illumination_mode: VideoCapabilities.Backlight.IrIlluminationMode
            | _Mapping
            | None = ...,
            white_illumination_mode: VideoCapabilities.Backlight.WhiteIlluminationMode
            | _Mapping
            | None = ...,
            smart_illumination_mode: VideoCapabilities.Backlight.SmartIlluminationMode
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Stream(_message.Message):
        __slots__ = (
            "bitrate_range",
            "codecs",
            "fps_range",
            "gop_size_range",
            "quality_range",
            "resolutions",
        )
        RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
        CODECS_FIELD_NUMBER: _ClassVar[int]
        FPS_RANGE_FIELD_NUMBER: _ClassVar[int]
        GOP_SIZE_RANGE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_RANGE_FIELD_NUMBER: _ClassVar[int]
        QUALITY_RANGE_FIELD_NUMBER: _ClassVar[int]
        resolutions: _containers.RepeatedCompositeFieldContainer[
            _types_pb2.VideoResolution
        ]
        codecs: _containers.RepeatedScalarFieldContainer[_types_pb2.VideoCodec]
        fps_range: _types_pb2.UInt32Range
        gop_size_range: _types_pb2.UInt32Range
        bitrate_range: _types_pb2.UInt32Range
        quality_range: _types_pb2.UInt32Range
        def __init__(
            self,
            resolutions: _Iterable[_types_pb2.VideoResolution | _Mapping] | None = ...,
            codecs: _Iterable[_types_pb2.VideoCodec | str] | None = ...,
            fps_range: _types_pb2.UInt32Range | _Mapping | None = ...,
            gop_size_range: _types_pb2.UInt32Range | _Mapping | None = ...,
            bitrate_range: _types_pb2.UInt32Range | _Mapping | None = ...,
            quality_range: _types_pb2.UInt32Range | _Mapping | None = ...,
        ) -> None: ...

    class BacklightCompensation(_message.Message):
        __slots__ = ("level_range",)
        LEVEL_RANGE_FIELD_NUMBER: _ClassVar[int]
        level_range: _types_pb2.FloatRange
        def __init__(
            self, level_range: _types_pb2.FloatRange | _Mapping | None = ...
        ) -> None: ...

    class WhiteBalance(_message.Message):
        __slots__ = ("auto", "manual")
        class AutoMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class ManualMode(_message.Message):
            __slots__ = ("blue_gain_range", "red_gain_range")
            RED_GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            BLUE_GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            red_gain_range: _types_pb2.FloatRange
            blue_gain_range: _types_pb2.FloatRange
            def __init__(
                self,
                red_gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
                blue_gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
            ) -> None: ...

        AUTO_FIELD_NUMBER: _ClassVar[int]
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        auto: VideoCapabilities.WhiteBalance.AutoMode
        manual: VideoCapabilities.WhiteBalance.ManualMode
        def __init__(
            self,
            auto: VideoCapabilities.WhiteBalance.AutoMode | _Mapping | None = ...,
            manual: VideoCapabilities.WhiteBalance.ManualMode | _Mapping | None = ...,
        ) -> None: ...

    class WideDynamicRange(_message.Message):
        __slots__ = ("level_range",)
        LEVEL_RANGE_FIELD_NUMBER: _ClassVar[int]
        level_range: _types_pb2.FloatRange
        def __init__(
            self, level_range: _types_pb2.FloatRange | _Mapping | None = ...
        ) -> None: ...

    class Exposure(_message.Message):
        __slots__ = ("auto", "manual", "shutter_speed")
        class ManualMode(_message.Message):
            __slots__ = ("exposure_time_range", "gain_range", "iris_range")
            EXPOSURE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            IRIS_RANGE_FIELD_NUMBER: _ClassVar[int]
            exposure_time_range: _types_pb2.DurationRange
            gain_range: _types_pb2.FloatRange
            iris_range: _types_pb2.FloatRange
            def __init__(
                self,
                exposure_time_range: _types_pb2.DurationRange | _Mapping | None = ...,
                gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
                iris_range: _types_pb2.FloatRange | _Mapping | None = ...,
            ) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = (
                "exposure_compensation_range",
                "max_exposure_time_range",
                "max_gain_range",
                "max_iris_range",
                "min_exposure_time_range",
                "min_gain_range",
                "min_iris_range",
                "presets",
                "priorities",
            )
            PRIORITIES_FIELD_NUMBER: _ClassVar[int]
            MIN_EXPOSURE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            MAX_EXPOSURE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            MIN_GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            MAX_GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            MIN_IRIS_RANGE_FIELD_NUMBER: _ClassVar[int]
            MAX_IRIS_RANGE_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_COMPENSATION_RANGE_FIELD_NUMBER: _ClassVar[int]
            PRESETS_FIELD_NUMBER: _ClassVar[int]
            priorities: _containers.RepeatedScalarFieldContainer[
                _types_pb2.ExposurePriority
            ]
            min_exposure_time_range: _types_pb2.DurationRange
            max_exposure_time_range: _types_pb2.DurationRange
            min_gain_range: _types_pb2.FloatRange
            max_gain_range: _types_pb2.FloatRange
            min_iris_range: _types_pb2.FloatRange
            max_iris_range: _types_pb2.FloatRange
            exposure_compensation_range: _types_pb2.Int32Range
            presets: _containers.RepeatedScalarFieldContainer[
                _types_pb2.AutoExposurePreset
            ]
            def __init__(
                self,
                priorities: _Iterable[_types_pb2.ExposurePriority | str] | None = ...,
                min_exposure_time_range: _types_pb2.DurationRange
                | _Mapping
                | None = ...,
                max_exposure_time_range: _types_pb2.DurationRange
                | _Mapping
                | None = ...,
                min_gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
                max_gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
                min_iris_range: _types_pb2.FloatRange | _Mapping | None = ...,
                max_iris_range: _types_pb2.FloatRange | _Mapping | None = ...,
                exposure_compensation_range: _types_pb2.Int32Range
                | _Mapping
                | None = ...,
                presets: _Iterable[_types_pb2.AutoExposurePreset | str] | None = ...,
            ) -> None: ...

        MANUAL_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        SHUTTER_SPEED_FIELD_NUMBER: _ClassVar[int]
        manual: VideoCapabilities.Exposure.ManualMode
        auto: VideoCapabilities.Exposure.AutoMode
        shutter_speed: _containers.RepeatedCompositeFieldContainer[
            _types_pb2.ShutterSpeed
        ]
        def __init__(
            self,
            manual: VideoCapabilities.Exposure.ManualMode | _Mapping | None = ...,
            auto: VideoCapabilities.Exposure.AutoMode | _Mapping | None = ...,
            shutter_speed: _Iterable[_types_pb2.ShutterSpeed | _Mapping] | None = ...,
        ) -> None: ...

    class IrCutFilterMode(_message.Message):
        __slots__ = ("auto", "off", "on")
        class OnMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class AutoMode(_message.Message):
            __slots__ = ("boundary_offset", "boundary_types", "response_time_range")
            BOUNDARY_TYPES_FIELD_NUMBER: _ClassVar[int]
            BOUNDARY_OFFSET_FIELD_NUMBER: _ClassVar[int]
            RESPONSE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            boundary_types: _containers.RepeatedScalarFieldContainer[
                _types_pb2.IrCutFilterAutoBoundaryType
            ]
            boundary_offset: bool
            response_time_range: _types_pb2.DurationRange
            def __init__(
                self,
                boundary_types: _Iterable[_types_pb2.IrCutFilterAutoBoundaryType | str]
                | None = ...,
                boundary_offset: bool = ...,
                response_time_range: _types_pb2.DurationRange | _Mapping | None = ...,
            ) -> None: ...

        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        on: VideoCapabilities.IrCutFilterMode.OnMode
        off: VideoCapabilities.IrCutFilterMode.OffMode
        auto: VideoCapabilities.IrCutFilterMode.AutoMode
        def __init__(
            self,
            on: VideoCapabilities.IrCutFilterMode.OnMode | _Mapping | None = ...,
            off: VideoCapabilities.IrCutFilterMode.OffMode | _Mapping | None = ...,
            auto: VideoCapabilities.IrCutFilterMode.AutoMode | _Mapping | None = ...,
        ) -> None: ...

    class Ptz(_message.Message):
        __slots__ = ("flags", "max_presets")
        class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[VideoCapabilities.Ptz.Flag]
            CAN_PANTILT: _ClassVar[VideoCapabilities.Ptz.Flag]
            CAN_ZOOM: _ClassVar[VideoCapabilities.Ptz.Flag]
            CAN_FOCUS: _ClassVar[VideoCapabilities.Ptz.Flag]
            HAVE_HOME_POSITION: _ClassVar[VideoCapabilities.Ptz.Flag]

        UNSPECIFIED: VideoCapabilities.Ptz.Flag
        CAN_PANTILT: VideoCapabilities.Ptz.Flag
        CAN_ZOOM: VideoCapabilities.Ptz.Flag
        CAN_FOCUS: VideoCapabilities.Ptz.Flag
        HAVE_HOME_POSITION: VideoCapabilities.Ptz.Flag
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        MAX_PRESETS_FIELD_NUMBER: _ClassVar[int]
        flags: _containers.RepeatedScalarFieldContainer[VideoCapabilities.Ptz.Flag]
        max_presets: int
        def __init__(
            self,
            flags: _Iterable[VideoCapabilities.Ptz.Flag | str] | None = ...,
            max_presets: int | None = ...,
        ) -> None: ...

    class Transform(_message.Message):
        __slots__ = ("performer", "rotations")
        class Performer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PERFORMER_UNSPECIFIED: _ClassVar[VideoCapabilities.Transform.Performer]
            PERFORMER_DEVICE: _ClassVar[VideoCapabilities.Transform.Performer]
            PERFORMER_CLIENT: _ClassVar[VideoCapabilities.Transform.Performer]

        PERFORMER_UNSPECIFIED: VideoCapabilities.Transform.Performer
        PERFORMER_DEVICE: VideoCapabilities.Transform.Performer
        PERFORMER_CLIENT: VideoCapabilities.Transform.Performer
        ROTATIONS_FIELD_NUMBER: _ClassVar[int]
        PERFORMER_FIELD_NUMBER: _ClassVar[int]
        rotations: _containers.RepeatedScalarFieldContainer[_types_pb2.Rotation]
        performer: VideoCapabilities.Transform.Performer
        def __init__(
            self,
            rotations: _Iterable[_types_pb2.Rotation | str] | None = ...,
            performer: VideoCapabilities.Transform.Performer | str | None = ...,
        ) -> None: ...

    class PrivacyMaskOptions(_message.Message):
        __slots__ = (
            "color_options",
            "max_masks",
            "max_points_per_mask",
            "rectangle_only",
            "single_color_only",
            "types",
        )
        MAX_MASKS_FIELD_NUMBER: _ClassVar[int]
        MAX_POINTS_PER_MASK_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        COLOR_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        RECTANGLE_ONLY_FIELD_NUMBER: _ClassVar[int]
        SINGLE_COLOR_ONLY_FIELD_NUMBER: _ClassVar[int]
        max_masks: int
        max_points_per_mask: int
        types: _containers.RepeatedScalarFieldContainer[_types_pb2.PrivacyMaskType]
        color_options: _containers.RepeatedCompositeFieldContainer[_types_pb2.Color]
        rectangle_only: bool
        single_color_only: bool
        def __init__(
            self,
            max_masks: int | None = ...,
            max_points_per_mask: int | None = ...,
            types: _Iterable[_types_pb2.PrivacyMaskType | str] | None = ...,
            color_options: _Iterable[_types_pb2.Color | _Mapping] | None = ...,
            rectangle_only: bool = ...,
            single_color_only: bool = ...,
        ) -> None: ...

    class ExposureMeteringArea(_message.Message):
        __slots__ = ("predefined_exposure_metering_areas",)
        PREDEFINED_EXPOSURE_METERING_AREAS_FIELD_NUMBER: _ClassVar[int]
        predefined_exposure_metering_areas: _containers.RepeatedScalarFieldContainer[
            _types_pb2.PredefinedExposureMeteringArea
        ]
        def __init__(
            self,
            predefined_exposure_metering_areas: _Iterable[
                _types_pb2.PredefinedExposureMeteringArea | str
            ]
            | None = ...,
        ) -> None: ...

    class AntiFlicker(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: _containers.RepeatedScalarFieldContainer[_types_pb2.AntiFlickerType]
        def __init__(
            self, type: _Iterable[_types_pb2.AntiFlickerType | str] | None = ...
        ) -> None: ...

    FLAGS_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    BLC_FIELD_NUMBER: _ClassVar[int]
    WHITE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    WDR_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_FIELD_NUMBER: _ClassVar[int]
    IRCUT_FILTER_MODE_FIELD_NUMBER: _ClassVar[int]
    PTZ_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_MASK_FIELD_NUMBER: _ClassVar[int]
    EXPOSURE_METERING_AREA_FIELD_NUMBER: _ClassVar[int]
    ANTI_FLICKER_FIELD_NUMBER: _ClassVar[int]
    BACKLIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    NOISE_REDUCTION_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.RepeatedScalarFieldContainer[VideoCapabilities.Flag]
    main: VideoCapabilities.Stream
    sub: VideoCapabilities.Stream
    blc: VideoCapabilities.BacklightCompensation
    white_balance: VideoCapabilities.WhiteBalance
    wdr: VideoCapabilities.WideDynamicRange
    exposure: VideoCapabilities.Exposure
    ircut_filter_mode: VideoCapabilities.IrCutFilterMode
    ptz: VideoCapabilities.Ptz
    transform: VideoCapabilities.Transform
    privacy_mask: VideoCapabilities.PrivacyMaskOptions
    exposure_metering_area: VideoCapabilities.ExposureMeteringArea
    anti_flicker: VideoCapabilities.AntiFlicker
    backlight: VideoCapabilities.Backlight
    image_profile: VideoCapabilities.ImageProfile
    noise_reduction: VideoCapabilities.NoiseReduction
    def __init__(
        self,
        flags: _Iterable[VideoCapabilities.Flag | str] | None = ...,
        main: VideoCapabilities.Stream | _Mapping | None = ...,
        sub: VideoCapabilities.Stream | _Mapping | None = ...,
        blc: VideoCapabilities.BacklightCompensation | _Mapping | None = ...,
        white_balance: VideoCapabilities.WhiteBalance | _Mapping | None = ...,
        wdr: VideoCapabilities.WideDynamicRange | _Mapping | None = ...,
        exposure: VideoCapabilities.Exposure | _Mapping | None = ...,
        ircut_filter_mode: VideoCapabilities.IrCutFilterMode | _Mapping | None = ...,
        ptz: VideoCapabilities.Ptz | _Mapping | None = ...,
        transform: VideoCapabilities.Transform | _Mapping | None = ...,
        privacy_mask: VideoCapabilities.PrivacyMaskOptions | _Mapping | None = ...,
        exposure_metering_area: VideoCapabilities.ExposureMeteringArea
        | _Mapping
        | None = ...,
        anti_flicker: VideoCapabilities.AntiFlicker | _Mapping | None = ...,
        backlight: VideoCapabilities.Backlight | _Mapping | None = ...,
        image_profile: VideoCapabilities.ImageProfile | _Mapping | None = ...,
        noise_reduction: VideoCapabilities.NoiseReduction | _Mapping | None = ...,
    ) -> None: ...

class AudioCapabilities(_message.Message):
    __slots__ = ("encodings", "flags", "num_audio_channels")
    class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[AudioCapabilities.Flag]
        COMPRESSED_STREAM: _ClassVar[AudioCapabilities.Flag]
        CAN_SET_BITRATE: _ClassVar[AudioCapabilities.Flag]
        CAN_SET_SAMPLE_RATE: _ClassVar[AudioCapabilities.Flag]
        CAN_SET_MIC_VOLUME: _ClassVar[AudioCapabilities.Flag]
        CAN_SET_MIC_GAIN: _ClassVar[AudioCapabilities.Flag]

    NONE: AudioCapabilities.Flag
    COMPRESSED_STREAM: AudioCapabilities.Flag
    CAN_SET_BITRATE: AudioCapabilities.Flag
    CAN_SET_SAMPLE_RATE: AudioCapabilities.Flag
    CAN_SET_MIC_VOLUME: AudioCapabilities.Flag
    CAN_SET_MIC_GAIN: AudioCapabilities.Flag
    class Encoding(_message.Message):
        __slots__ = ("bitrates", "codec", "sample_rates")
        CODEC_FIELD_NUMBER: _ClassVar[int]
        BITRATES_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_RATES_FIELD_NUMBER: _ClassVar[int]
        codec: _types_pb2.AudioCodec
        bitrates: _containers.RepeatedScalarFieldContainer[int]
        sample_rates: _containers.RepeatedScalarFieldContainer[int]
        def __init__(
            self,
            codec: _types_pb2.AudioCodec | str | None = ...,
            bitrates: _Iterable[int] | None = ...,
            sample_rates: _Iterable[int] | None = ...,
        ) -> None: ...

    FLAGS_FIELD_NUMBER: _ClassVar[int]
    ENCODINGS_FIELD_NUMBER: _ClassVar[int]
    NUM_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.RepeatedScalarFieldContainer[AudioCapabilities.Flag]
    encodings: _containers.RepeatedCompositeFieldContainer[AudioCapabilities.Encoding]
    num_audio_channels: int
    def __init__(
        self,
        flags: _Iterable[AudioCapabilities.Flag | str] | None = ...,
        encodings: _Iterable[AudioCapabilities.Encoding | _Mapping] | None = ...,
        num_audio_channels: int | None = ...,
    ) -> None: ...

class AudioOutputCapabilities(_message.Message):
    __slots__ = ("flags",)
    class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[AudioOutputCapabilities.Flag]
        CAN_SET_VOLUME: _ClassVar[AudioOutputCapabilities.Flag]

    NONE: AudioOutputCapabilities.Flag
    CAN_SET_VOLUME: AudioOutputCapabilities.Flag
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.RepeatedScalarFieldContainer[AudioOutputCapabilities.Flag]
    def __init__(
        self, flags: _Iterable[AudioOutputCapabilities.Flag | str] | None = ...
    ) -> None: ...

class ChannelCapabilities(_message.Message):
    __slots__ = ("audio", "audio_output", "channel_id", "video")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    video: VideoCapabilities
    audio: AudioCapabilities
    audio_output: AudioOutputCapabilities
    def __init__(
        self,
        channel_id: str | None = ...,
        video: VideoCapabilities | _Mapping | None = ...,
        audio: AudioCapabilities | _Mapping | None = ...,
        audio_output: AudioOutputCapabilities | _Mapping | None = ...,
    ) -> None: ...

class MediaDeviceCapabilities(_message.Message):
    __slots__ = ("channels", "flags")
    class Flag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[MediaDeviceCapabilities.Flag]
        HAVE_MOTION_DETECTOR: _ClassVar[MediaDeviceCapabilities.Flag]
        HAVE_SOUND_DETECTOR: _ClassVar[MediaDeviceCapabilities.Flag]
        SKIP_INITIAL_SETUP: _ClassVar[MediaDeviceCapabilities.Flag]

    NONE: MediaDeviceCapabilities.Flag
    HAVE_MOTION_DETECTOR: MediaDeviceCapabilities.Flag
    HAVE_SOUND_DETECTOR: MediaDeviceCapabilities.Flag
    SKIP_INITIAL_SETUP: MediaDeviceCapabilities.Flag
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.RepeatedScalarFieldContainer[MediaDeviceCapabilities.Flag]
    channels: _containers.RepeatedCompositeFieldContainer[ChannelCapabilities]
    def __init__(
        self,
        flags: _Iterable[MediaDeviceCapabilities.Flag | str] | None = ...,
        channels: _Iterable[ChannelCapabilities | _Mapping] | None = ...,
    ) -> None: ...
