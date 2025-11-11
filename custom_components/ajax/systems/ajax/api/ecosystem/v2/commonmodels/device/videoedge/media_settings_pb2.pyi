from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.commonmodels.device.videoedge import (
    types_pb2 as _types_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ImageSettings(_message.Message):
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
        "noise_reduction",
        "off_illumination",
        "saturation",
        "sharpness",
        "smart_illumination",
        "transform",
        "wdr",
        "white_balance",
        "white_illumination",
    )
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
        off: ImageSettings.BacklightCompensation.OffMode
        on: ImageSettings.BacklightCompensation.OnMode
        def __init__(
            self,
            off: ImageSettings.BacklightCompensation.OffMode | _Mapping | None = ...,
            on: ImageSettings.BacklightCompensation.OnMode | _Mapping | None = ...,
        ) -> None: ...

    class ImageProfile(_message.Message):
        __slots__ = ("type",)
        class ImageProfileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IMAGE_PROFILE_TYPE_UNSPECIFIED: _ClassVar[
                ImageSettings.ImageProfile.ImageProfileType
            ]
            IMAGE_PROFILE_TYPE_NATURAL: _ClassVar[
                ImageSettings.ImageProfile.ImageProfileType
            ]
            IMAGE_PROFILE_TYPE_INSTAMODE: _ClassVar[
                ImageSettings.ImageProfile.ImageProfileType
            ]

        IMAGE_PROFILE_TYPE_UNSPECIFIED: ImageSettings.ImageProfile.ImageProfileType
        IMAGE_PROFILE_TYPE_NATURAL: ImageSettings.ImageProfile.ImageProfileType
        IMAGE_PROFILE_TYPE_INSTAMODE: ImageSettings.ImageProfile.ImageProfileType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: ImageSettings.ImageProfile.ImageProfileType
        def __init__(
            self, type: ImageSettings.ImageProfile.ImageProfileType | str | None = ...
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
        manual: ImageSettings.WhiteBalance.ManualMode
        auto: ImageSettings.WhiteBalance.AutoMode
        def __init__(
            self,
            manual: ImageSettings.WhiteBalance.ManualMode | _Mapping | None = ...,
            auto: ImageSettings.WhiteBalance.AutoMode | _Mapping | None = ...,
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
        off: ImageSettings.WideDynamicRange.OffMode
        on: ImageSettings.WideDynamicRange.OnMode
        def __init__(
            self,
            off: ImageSettings.WideDynamicRange.OffMode | _Mapping | None = ...,
            on: ImageSettings.WideDynamicRange.OnMode | _Mapping | None = ...,
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
            class ExposurePriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                EXPOSURE_PRIORITY_UNSPECIFIED: _ClassVar[
                    ImageSettings.Exposure.AutoMode.ExposurePriority
                ]
                EXPOSURE_PRIORITY_LOW_NOISE: _ClassVar[
                    ImageSettings.Exposure.AutoMode.ExposurePriority
                ]
                EXPOSURE_PRIORITY_FRAME_RATE: _ClassVar[
                    ImageSettings.Exposure.AutoMode.ExposurePriority
                ]

            EXPOSURE_PRIORITY_UNSPECIFIED: (
                ImageSettings.Exposure.AutoMode.ExposurePriority
            )
            EXPOSURE_PRIORITY_LOW_NOISE: (
                ImageSettings.Exposure.AutoMode.ExposurePriority
            )
            EXPOSURE_PRIORITY_FRAME_RATE: (
                ImageSettings.Exposure.AutoMode.ExposurePriority
            )
            class AutoExposurePreset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                AUTO_EXPOSURE_PRESET_UNSPECIFIED: _ClassVar[
                    ImageSettings.Exposure.AutoMode.AutoExposurePreset
                ]
                AUTO_EXPOSURE_PRESET_LESS_NOISE: _ClassVar[
                    ImageSettings.Exposure.AutoMode.AutoExposurePreset
                ]
                AUTO_EXPOSURE_PRESET_BALANCE: _ClassVar[
                    ImageSettings.Exposure.AutoMode.AutoExposurePreset
                ]
                AUTO_EXPOSURE_PRESET_LESS_MOTION_BLUR: _ClassVar[
                    ImageSettings.Exposure.AutoMode.AutoExposurePreset
                ]

            AUTO_EXPOSURE_PRESET_UNSPECIFIED: (
                ImageSettings.Exposure.AutoMode.AutoExposurePreset
            )
            AUTO_EXPOSURE_PRESET_LESS_NOISE: (
                ImageSettings.Exposure.AutoMode.AutoExposurePreset
            )
            AUTO_EXPOSURE_PRESET_BALANCE: (
                ImageSettings.Exposure.AutoMode.AutoExposurePreset
            )
            AUTO_EXPOSURE_PRESET_LESS_MOTION_BLUR: (
                ImageSettings.Exposure.AutoMode.AutoExposurePreset
            )
            PRIORITY_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
            GAIN_RANGE_FIELD_NUMBER: _ClassVar[int]
            IRIS_RANGE_FIELD_NUMBER: _ClassVar[int]
            EXPOSURE_COMPENSATION_FIELD_NUMBER: _ClassVar[int]
            PRESET_FIELD_NUMBER: _ClassVar[int]
            priority: ImageSettings.Exposure.AutoMode.ExposurePriority
            exposure_time_range: _types_pb2.DurationRange
            gain_range: _types_pb2.FloatRange
            iris_range: _types_pb2.FloatRange
            exposure_compensation: int
            preset: ImageSettings.Exposure.AutoMode.AutoExposurePreset
            def __init__(
                self,
                priority: ImageSettings.Exposure.AutoMode.ExposurePriority
                | str
                | None = ...,
                exposure_time_range: _types_pb2.DurationRange | _Mapping | None = ...,
                gain_range: _types_pb2.FloatRange | _Mapping | None = ...,
                iris_range: _types_pb2.FloatRange | _Mapping | None = ...,
                exposure_compensation: int | None = ...,
                preset: ImageSettings.Exposure.AutoMode.AutoExposurePreset
                | str
                | None = ...,
            ) -> None: ...

        MANUAL_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        manual: ImageSettings.Exposure.ManualMode
        auto: ImageSettings.Exposure.AutoMode
        def __init__(
            self,
            manual: ImageSettings.Exposure.ManualMode | _Mapping | None = ...,
            auto: ImageSettings.Exposure.AutoMode | _Mapping | None = ...,
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
                class IrCutFilterAutoBoundaryType(
                    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
                ):
                    __slots__ = ()
                    IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_UNSPECIFIED: _ClassVar[
                        ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                    ]
                    IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_COMMON: _ClassVar[
                        ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                    ]
                    IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_TO_ON: _ClassVar[
                        ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                    ]
                    IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_TO_OFF: _ClassVar[
                        ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                    ]

                IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_UNSPECIFIED: ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_COMMON: ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_TO_ON: ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                IR_CUT_FILTER_AUTO_BOUNDARY_TYPE_TO_OFF: ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                BOUNDARY_TYPE_FIELD_NUMBER: _ClassVar[int]
                BOUNDARY_OFFSET_FIELD_NUMBER: _ClassVar[int]
                RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
                boundary_type: ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                boundary_offset: float
                response_time: _duration_pb2.Duration
                def __init__(
                    self,
                    boundary_type: ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment.IrCutFilterAutoBoundaryType
                    | str
                    | None = ...,
                    boundary_offset: float | None = ...,
                    response_time: _duration_pb2.Duration | _Mapping | None = ...,
                ) -> None: ...

            IRCUT_FILTER_AUTO_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
            ircut_filter_auto_adjustments: _containers.RepeatedCompositeFieldContainer[
                ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment
            ]
            def __init__(
                self,
                ircut_filter_auto_adjustments: _Iterable[
                    ImageSettings.IrCutFilter.AutoMode.IrCutFilterAutoAdjustment
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        AUTO_FIELD_NUMBER: _ClassVar[int]
        on: ImageSettings.IrCutFilter.OnMode
        off: ImageSettings.IrCutFilter.OffMode
        auto: ImageSettings.IrCutFilter.AutoMode
        def __init__(
            self,
            on: ImageSettings.IrCutFilter.OnMode | _Mapping | None = ...,
            off: ImageSettings.IrCutFilter.OffMode | _Mapping | None = ...,
            auto: ImageSettings.IrCutFilter.AutoMode | _Mapping | None = ...,
        ) -> None: ...

    class Transform(_message.Message):
        __slots__ = ("mirror", "rotation")
        class Rotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ROTATION_UNSPECIFIED: _ClassVar[ImageSettings.Transform.Rotation]
            ROTATION_0: _ClassVar[ImageSettings.Transform.Rotation]
            ROTATION_90: _ClassVar[ImageSettings.Transform.Rotation]
            ROTATION_180: _ClassVar[ImageSettings.Transform.Rotation]
            ROTATION_270: _ClassVar[ImageSettings.Transform.Rotation]

        ROTATION_UNSPECIFIED: ImageSettings.Transform.Rotation
        ROTATION_0: ImageSettings.Transform.Rotation
        ROTATION_90: ImageSettings.Transform.Rotation
        ROTATION_180: ImageSettings.Transform.Rotation
        ROTATION_270: ImageSettings.Transform.Rotation
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        MIRROR_FIELD_NUMBER: _ClassVar[int]
        rotation: ImageSettings.Transform.Rotation
        mirror: bool
        def __init__(
            self,
            rotation: ImageSettings.Transform.Rotation | str | None = ...,
            mirror: bool = ...,
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
        auto: ImageSettings.IrIllumination.AutoMode
        manual: ImageSettings.IrIllumination.ManualMode
        def __init__(
            self,
            auto: ImageSettings.IrIllumination.AutoMode | _Mapping | None = ...,
            manual: ImageSettings.IrIllumination.ManualMode | _Mapping | None = ...,
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
        auto: ImageSettings.WhiteIllumination.AutoMode
        manual: ImageSettings.WhiteIllumination.ManualMode
        def __init__(
            self,
            auto: ImageSettings.WhiteIllumination.AutoMode | _Mapping | None = ...,
            manual: ImageSettings.WhiteIllumination.ManualMode | _Mapping | None = ...,
        ) -> None: ...

    class SmartIllumination(_message.Message):
        __slots__ = ("ir_illumination", "white_illumination")
        IR_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
        WHITE_ILLUMINATION_FIELD_NUMBER: _ClassVar[int]
        ir_illumination: ImageSettings.IrIllumination
        white_illumination: ImageSettings.WhiteIllumination
        def __init__(
            self,
            ir_illumination: ImageSettings.IrIllumination | _Mapping | None = ...,
            white_illumination: ImageSettings.WhiteIllumination | _Mapping | None = ...,
        ) -> None: ...

    class ExposureMeteringArea(_message.Message):
        __slots__ = ("predefined",)
        class PredefinedExposureMeteringArea(
            int, metaclass=_enum_type_wrapper.EnumTypeWrapper
        ):
            __slots__ = ()
            PREDEFINED_EXPOSURE_METERING_AREA_UNSPECIFIED: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]
            PREDEFINED_EXPOSURE_METERING_AREA_FULL_FRAME: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]
            PREDEFINED_EXPOSURE_METERING_AREA_TOP: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]
            PREDEFINED_EXPOSURE_METERING_AREA_RIGHT: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]
            PREDEFINED_EXPOSURE_METERING_AREA_BOTTOM: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]
            PREDEFINED_EXPOSURE_METERING_AREA_LEFT: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]
            PREDEFINED_EXPOSURE_METERING_AREA_CENTER: _ClassVar[
                ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            ]

        PREDEFINED_EXPOSURE_METERING_AREA_UNSPECIFIED: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_EXPOSURE_METERING_AREA_FULL_FRAME: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_EXPOSURE_METERING_AREA_TOP: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_EXPOSURE_METERING_AREA_RIGHT: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_EXPOSURE_METERING_AREA_BOTTOM: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_EXPOSURE_METERING_AREA_LEFT: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_EXPOSURE_METERING_AREA_CENTER: (
            ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        )
        PREDEFINED_FIELD_NUMBER: _ClassVar[int]
        predefined: ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
        def __init__(
            self,
            predefined: ImageSettings.ExposureMeteringArea.PredefinedExposureMeteringArea
            | str
            | None = ...,
        ) -> None: ...

    class AntiFlicker(_message.Message):
        __slots__ = ("type",)
        class AntiFlickerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ANTI_FLICKER_TYPE_UNSPECIFIED: _ClassVar[
                ImageSettings.AntiFlicker.AntiFlickerType
            ]
            ANTI_FLICKER_TYPE_DISABLED: _ClassVar[
                ImageSettings.AntiFlicker.AntiFlickerType
            ]
            ANTI_FLICKER_TYPE_50HZ: _ClassVar[ImageSettings.AntiFlicker.AntiFlickerType]
            ANTI_FLICKER_TYPE_60HZ: _ClassVar[ImageSettings.AntiFlicker.AntiFlickerType]

        ANTI_FLICKER_TYPE_UNSPECIFIED: ImageSettings.AntiFlicker.AntiFlickerType
        ANTI_FLICKER_TYPE_DISABLED: ImageSettings.AntiFlicker.AntiFlickerType
        ANTI_FLICKER_TYPE_50HZ: ImageSettings.AntiFlicker.AntiFlickerType
        ANTI_FLICKER_TYPE_60HZ: ImageSettings.AntiFlicker.AntiFlickerType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: ImageSettings.AntiFlicker.AntiFlickerType
        def __init__(
            self, type: ImageSettings.AntiFlicker.AntiFlickerType | str | None = ...
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
        on: ImageSettings.NoiseReduction.OnMode
        off: ImageSettings.NoiseReduction.OffMode
        def __init__(
            self,
            on: ImageSettings.NoiseReduction.OnMode | _Mapping | None = ...,
            off: ImageSettings.NoiseReduction.OffMode | _Mapping | None = ...,
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
    EXPOSURE_METERING_AREA_FIELD_NUMBER: _ClassVar[int]
    ANTI_FLICKER_FIELD_NUMBER: _ClassVar[int]
    NOISE_REDUCTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    brightness: int
    contrast: int
    saturation: int
    sharpness: int
    blc: ImageSettings.BacklightCompensation
    white_balance: ImageSettings.WhiteBalance
    wdr: ImageSettings.WideDynamicRange
    exposure: ImageSettings.Exposure
    ircut_filter: ImageSettings.IrCutFilter
    transform: ImageSettings.Transform
    off_illumination: ImageSettings.OffIllumination
    ir_illumination: ImageSettings.IrIllumination
    white_illumination: ImageSettings.WhiteIllumination
    smart_illumination: ImageSettings.SmartIllumination
    exposure_metering_area: ImageSettings.ExposureMeteringArea
    anti_flicker: ImageSettings.AntiFlicker
    noise_reduction: ImageSettings.NoiseReduction
    image_profile: ImageSettings.ImageProfile
    def __init__(
        self,
        brightness: int | None = ...,
        contrast: int | None = ...,
        saturation: int | None = ...,
        sharpness: int | None = ...,
        blc: ImageSettings.BacklightCompensation | _Mapping | None = ...,
        white_balance: ImageSettings.WhiteBalance | _Mapping | None = ...,
        wdr: ImageSettings.WideDynamicRange | _Mapping | None = ...,
        exposure: ImageSettings.Exposure | _Mapping | None = ...,
        ircut_filter: ImageSettings.IrCutFilter | _Mapping | None = ...,
        transform: ImageSettings.Transform | _Mapping | None = ...,
        off_illumination: ImageSettings.OffIllumination | _Mapping | None = ...,
        ir_illumination: ImageSettings.IrIllumination | _Mapping | None = ...,
        white_illumination: ImageSettings.WhiteIllumination | _Mapping | None = ...,
        smart_illumination: ImageSettings.SmartIllumination | _Mapping | None = ...,
        exposure_metering_area: ImageSettings.ExposureMeteringArea
        | _Mapping
        | None = ...,
        anti_flicker: ImageSettings.AntiFlicker | _Mapping | None = ...,
        noise_reduction: ImageSettings.NoiseReduction | _Mapping | None = ...,
        image_profile: ImageSettings.ImageProfile | _Mapping | None = ...,
    ) -> None: ...

class VideoStreamSettings(_message.Message):
    __slots__ = (
        "bitrate",
        "bitrate_type",
        "codec",
        "enabled",
        "fps",
        "gop_size",
        "resolution",
        "vbr_quality",
    )
    class VideoCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_CODEC_UNSPECIFIED: _ClassVar[VideoStreamSettings.VideoCodec]
        VIDEO_CODEC_H264: _ClassVar[VideoStreamSettings.VideoCodec]
        VIDEO_CODEC_H265: _ClassVar[VideoStreamSettings.VideoCodec]
        VIDEO_CODEC_MJPEG: _ClassVar[VideoStreamSettings.VideoCodec]

    VIDEO_CODEC_UNSPECIFIED: VideoStreamSettings.VideoCodec
    VIDEO_CODEC_H264: VideoStreamSettings.VideoCodec
    VIDEO_CODEC_H265: VideoStreamSettings.VideoCodec
    VIDEO_CODEC_MJPEG: VideoStreamSettings.VideoCodec
    class VideoBitrateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_BITRATE_TYPE_UNSPECIFIED: _ClassVar[VideoStreamSettings.VideoBitrateType]
        VIDEO_BITRATE_TYPE_CBR: _ClassVar[VideoStreamSettings.VideoBitrateType]
        VIDEO_BITRATE_TYPE_VBR: _ClassVar[VideoStreamSettings.VideoBitrateType]

    VIDEO_BITRATE_TYPE_UNSPECIFIED: VideoStreamSettings.VideoBitrateType
    VIDEO_BITRATE_TYPE_CBR: VideoStreamSettings.VideoBitrateType
    VIDEO_BITRATE_TYPE_VBR: VideoStreamSettings.VideoBitrateType
    class VideoResolution(_message.Message):
        __slots__ = ("height", "width")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(
            self, width: int | None = ..., height: int | None = ...
        ) -> None: ...

    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GOP_SIZE_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    VBR_QUALITY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    codec: VideoStreamSettings.VideoCodec
    resolution: VideoStreamSettings.VideoResolution
    bitrate: int
    bitrate_type: VideoStreamSettings.VideoBitrateType
    gop_size: int
    fps: int
    vbr_quality: int
    def __init__(
        self,
        enabled: bool = ...,
        codec: VideoStreamSettings.VideoCodec | str | None = ...,
        resolution: VideoStreamSettings.VideoResolution | _Mapping | None = ...,
        bitrate: int | None = ...,
        bitrate_type: VideoStreamSettings.VideoBitrateType | str | None = ...,
        gop_size: int | None = ...,
        fps: int | None = ...,
        vbr_quality: int | None = ...,
    ) -> None: ...

class AudioSettings(_message.Message):
    __slots__ = ("bitrate", "codec", "enabled", "mic_gain", "mic_volume", "sample_rate")
    class AudioCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_CODEC_UNSPECIFIED: _ClassVar[AudioSettings.AudioCodec]
        AUDIO_CODEC_G711_ULAW: _ClassVar[AudioSettings.AudioCodec]
        AUDIO_CODEC_G711_ALAW: _ClassVar[AudioSettings.AudioCodec]
        AUDIO_CODEC_AAC: _ClassVar[AudioSettings.AudioCodec]
        AUDIO_CODEC_MP2: _ClassVar[AudioSettings.AudioCodec]
        AUDIO_CODEC_G726: _ClassVar[AudioSettings.AudioCodec]
        AUDIO_CODEC_G722: _ClassVar[AudioSettings.AudioCodec]

    AUDIO_CODEC_UNSPECIFIED: AudioSettings.AudioCodec
    AUDIO_CODEC_G711_ULAW: AudioSettings.AudioCodec
    AUDIO_CODEC_G711_ALAW: AudioSettings.AudioCodec
    AUDIO_CODEC_AAC: AudioSettings.AudioCodec
    AUDIO_CODEC_MP2: AudioSettings.AudioCodec
    AUDIO_CODEC_G726: AudioSettings.AudioCodec
    AUDIO_CODEC_G722: AudioSettings.AudioCodec
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    MIC_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MIC_GAIN_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    codec: AudioSettings.AudioCodec
    bitrate: int
    sample_rate: int
    mic_volume: int
    mic_gain: int
    def __init__(
        self,
        enabled: bool = ...,
        codec: AudioSettings.AudioCodec | str | None = ...,
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
