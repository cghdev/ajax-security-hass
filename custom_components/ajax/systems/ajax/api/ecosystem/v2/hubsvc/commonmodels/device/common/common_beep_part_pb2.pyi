from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    patch_type_pb2 as _patch_type_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    progress_annunciation_thresholds_pb2 as _progress_annunciation_thresholds_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CommonBeepPart(_message.Message):
    __slots__ = (
        "beep_config",
        "beep_on_arm_disarm",
        "beep_on_delay",
        "beep_volume_level",
        "capabilities",
        "chimes",
        "progress_annunciation_thresholds",
        "volume_level_capabilities",
    )
    class Chimes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHIMES_UNSPECIFIED: _ClassVar[CommonBeepPart.Chimes]
        CHIMES_DISABLED: _ClassVar[CommonBeepPart.Chimes]
        CHIMES_ENABLED: _ClassVar[CommonBeepPart.Chimes]

    CHIMES_UNSPECIFIED: CommonBeepPart.Chimes
    CHIMES_DISABLED: CommonBeepPart.Chimes
    CHIMES_ENABLED: CommonBeepPart.Chimes
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEEP_ON_ARM_DISARM_UNSPECIFIED: _ClassVar[CommonBeepPart.BeepOnArmDisarm]
        BEEP_ON_ARM_DISARM_ARM: _ClassVar[CommonBeepPart.BeepOnArmDisarm]
        BEEP_ON_ARM_DISARM_DISARM: _ClassVar[CommonBeepPart.BeepOnArmDisarm]
        BEEP_ON_ARM_DISARM_NIGHT_ARM: _ClassVar[CommonBeepPart.BeepOnArmDisarm]
        BEEP_ON_ARM_DISARM_NIGHT_DISARM: _ClassVar[CommonBeepPart.BeepOnArmDisarm]
        BEEP_ON_ARM_DISARM_ABORT_WINDOW: _ClassVar[CommonBeepPart.BeepOnArmDisarm]
        BEEP_ON_ARM_DISARM_CANCEL_WINDOW: _ClassVar[CommonBeepPart.BeepOnArmDisarm]

    BEEP_ON_ARM_DISARM_UNSPECIFIED: CommonBeepPart.BeepOnArmDisarm
    BEEP_ON_ARM_DISARM_ARM: CommonBeepPart.BeepOnArmDisarm
    BEEP_ON_ARM_DISARM_DISARM: CommonBeepPart.BeepOnArmDisarm
    BEEP_ON_ARM_DISARM_NIGHT_ARM: CommonBeepPart.BeepOnArmDisarm
    BEEP_ON_ARM_DISARM_NIGHT_DISARM: CommonBeepPart.BeepOnArmDisarm
    BEEP_ON_ARM_DISARM_ABORT_WINDOW: CommonBeepPart.BeepOnArmDisarm
    BEEP_ON_ARM_DISARM_CANCEL_WINDOW: CommonBeepPart.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEEP_ON_DELAY_UNSPECIFIED: _ClassVar[CommonBeepPart.BeepOnDelay]
        BEEP_ON_DELAY_ARM: _ClassVar[CommonBeepPart.BeepOnDelay]
        BEEP_ON_DELAY_DISARM: _ClassVar[CommonBeepPart.BeepOnDelay]
        BEEP_ON_DELAY_NIGHT_ARM: _ClassVar[CommonBeepPart.BeepOnDelay]
        BEEP_ON_DELAY_NIGHT_DISARM: _ClassVar[CommonBeepPart.BeepOnDelay]

    BEEP_ON_DELAY_UNSPECIFIED: CommonBeepPart.BeepOnDelay
    BEEP_ON_DELAY_ARM: CommonBeepPart.BeepOnDelay
    BEEP_ON_DELAY_DISARM: CommonBeepPart.BeepOnDelay
    BEEP_ON_DELAY_NIGHT_ARM: CommonBeepPart.BeepOnDelay
    BEEP_ON_DELAY_NIGHT_DISARM: CommonBeepPart.BeepOnDelay
    class BeepVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEEP_VOLUME_LEVEL_UNSPECIFIED: _ClassVar[CommonBeepPart.BeepVolumeLevel]
        BEEP_VOLUME_LEVEL_VERY_LOUD: _ClassVar[CommonBeepPart.BeepVolumeLevel]
        BEEP_VOLUME_LEVEL_LOUD: _ClassVar[CommonBeepPart.BeepVolumeLevel]
        BEEP_VOLUME_LEVEL_QUIET: _ClassVar[CommonBeepPart.BeepVolumeLevel]
        BEEP_VOLUME_LEVEL_VERY_QUIET: _ClassVar[CommonBeepPart.BeepVolumeLevel]

    BEEP_VOLUME_LEVEL_UNSPECIFIED: CommonBeepPart.BeepVolumeLevel
    BEEP_VOLUME_LEVEL_VERY_LOUD: CommonBeepPart.BeepVolumeLevel
    BEEP_VOLUME_LEVEL_LOUD: CommonBeepPart.BeepVolumeLevel
    BEEP_VOLUME_LEVEL_QUIET: CommonBeepPart.BeepVolumeLevel
    BEEP_VOLUME_LEVEL_VERY_QUIET: CommonBeepPart.BeepVolumeLevel
    class BeepConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BEEP_CONFIG_UNSPECIFIED: _ClassVar[CommonBeepPart.BeepConfig]
        BEEP_CONFIG_SILENT_ENTRY_DELAY_ENABLED: _ClassVar[CommonBeepPart.BeepConfig]

    BEEP_CONFIG_UNSPECIFIED: CommonBeepPart.BeepConfig
    BEEP_CONFIG_SILENT_ENTRY_DELAY_ENABLED: CommonBeepPart.BeepConfig
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[CommonBeepPart.Capability]
        CAPABILITY_SEPARATE_BEEP_SETTING: _ClassVar[CommonBeepPart.Capability]
        CAPABILITY_DELAY_BEEP: _ClassVar[CommonBeepPart.Capability]
        CAPABILITY_FAST_BEEP: _ClassVar[CommonBeepPart.Capability]
        CAPABILITY_BEEP_VOLUME: _ClassVar[CommonBeepPart.Capability]
        CAPABILITY_BEEP_CHIMES: _ClassVar[CommonBeepPart.Capability]

    CAPABILITY_UNSPECIFIED: CommonBeepPart.Capability
    CAPABILITY_SEPARATE_BEEP_SETTING: CommonBeepPart.Capability
    CAPABILITY_DELAY_BEEP: CommonBeepPart.Capability
    CAPABILITY_FAST_BEEP: CommonBeepPart.Capability
    CAPABILITY_BEEP_VOLUME: CommonBeepPart.Capability
    CAPABILITY_BEEP_CHIMES: CommonBeepPart.Capability
    class CommonBeepPartSettings(_message.Message):
        __slots__ = (
            "beep_config",
            "beep_on_arm_disarm",
            "beep_on_delay",
            "beep_volume_level",
            "chimes",
            "progress_annunciation_thresholds",
        )
        class BeepOnArmDisarmPatch(_message.Message):
            __slots__ = ("beep_on_arm_disarm", "type")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
            type: _patch_type_pb2.PatchType
            beep_on_arm_disarm: CommonBeepPart.BeepOnArmDisarm
            def __init__(
                self,
                type: _patch_type_pb2.PatchType | str | None = ...,
                beep_on_arm_disarm: CommonBeepPart.BeepOnArmDisarm | str | None = ...,
            ) -> None: ...

        class BeepOnDelayPatch(_message.Message):
            __slots__ = ("beep_on_delay", "type")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
            type: _patch_type_pb2.PatchType
            beep_on_delay: CommonBeepPart.BeepOnDelay
            def __init__(
                self,
                type: _patch_type_pb2.PatchType | str | None = ...,
                beep_on_delay: CommonBeepPart.BeepOnDelay | str | None = ...,
            ) -> None: ...

        class BeepConfigPatch(_message.Message):
            __slots__ = ("beep_config", "type")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            BEEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
            type: _patch_type_pb2.PatchType
            beep_config: CommonBeepPart.BeepConfig
            def __init__(
                self,
                type: _patch_type_pb2.PatchType | str | None = ...,
                beep_config: CommonBeepPart.BeepConfig | str | None = ...,
            ) -> None: ...

        BEEP_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
        CHIMES_FIELD_NUMBER: _ClassVar[int]
        BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
        BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
        BEEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_ANNUNCIATION_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        beep_volume_level: CommonBeepPart.BeepVolumeLevel
        chimes: CommonBeepPart.Chimes
        beep_on_arm_disarm: _containers.RepeatedCompositeFieldContainer[
            CommonBeepPart.CommonBeepPartSettings.BeepOnArmDisarmPatch
        ]
        beep_on_delay: _containers.RepeatedCompositeFieldContainer[
            CommonBeepPart.CommonBeepPartSettings.BeepOnDelayPatch
        ]
        beep_config: _containers.RepeatedCompositeFieldContainer[
            CommonBeepPart.CommonBeepPartSettings.BeepConfigPatch
        ]
        progress_annunciation_thresholds: _progress_annunciation_thresholds_pb2.ProgressAnnunciationThreshold.ProgressAnnunciationThresholdSettings
        def __init__(
            self,
            beep_volume_level: CommonBeepPart.BeepVolumeLevel | str | None = ...,
            chimes: CommonBeepPart.Chimes | str | None = ...,
            beep_on_arm_disarm: _Iterable[
                CommonBeepPart.CommonBeepPartSettings.BeepOnArmDisarmPatch | _Mapping
            ]
            | None = ...,
            beep_on_delay: _Iterable[
                CommonBeepPart.CommonBeepPartSettings.BeepOnDelayPatch | _Mapping
            ]
            | None = ...,
            beep_config: _Iterable[
                CommonBeepPart.CommonBeepPartSettings.BeepConfigPatch | _Mapping
            ]
            | None = ...,
            progress_annunciation_thresholds: _progress_annunciation_thresholds_pb2.ProgressAnnunciationThreshold.ProgressAnnunciationThresholdSettings
            | _Mapping
            | None = ...,
        ) -> None: ...

    BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
    BEEP_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BEEP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CHIMES_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_ANNUNCIATION_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_LEVEL_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    beep_on_arm_disarm: _containers.RepeatedScalarFieldContainer[
        CommonBeepPart.BeepOnArmDisarm
    ]
    beep_on_delay: _containers.RepeatedScalarFieldContainer[CommonBeepPart.BeepOnDelay]
    beep_volume_level: CommonBeepPart.BeepVolumeLevel
    beep_config: _containers.RepeatedScalarFieldContainer[CommonBeepPart.BeepConfig]
    chimes: CommonBeepPart.Chimes
    progress_annunciation_thresholds: (
        _progress_annunciation_thresholds_pb2.ProgressAnnunciationThreshold
    )
    volume_level_capabilities: _containers.RepeatedScalarFieldContainer[
        CommonBeepPart.BeepVolumeLevel
    ]
    capabilities: _containers.RepeatedScalarFieldContainer[CommonBeepPart.Capability]
    def __init__(
        self,
        beep_on_arm_disarm: _Iterable[CommonBeepPart.BeepOnArmDisarm | str]
        | None = ...,
        beep_on_delay: _Iterable[CommonBeepPart.BeepOnDelay | str] | None = ...,
        beep_volume_level: CommonBeepPart.BeepVolumeLevel | str | None = ...,
        beep_config: _Iterable[CommonBeepPart.BeepConfig | str] | None = ...,
        chimes: CommonBeepPart.Chimes | str | None = ...,
        progress_annunciation_thresholds: _progress_annunciation_thresholds_pb2.ProgressAnnunciationThreshold
        | _Mapping
        | None = ...,
        volume_level_capabilities: _Iterable[CommonBeepPart.BeepVolumeLevel | str]
        | None = ...,
        capabilities: _Iterable[CommonBeepPart.Capability | str] | None = ...,
    ) -> None: ...
