from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from systems.ajax.protobuf.hub.device import common_fibra_pb2 as _common_fibra_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreetSirenFibra(_message.Message):
    __slots__ = (
        "alarm_duration",
        "alert_if_moved",
        "associated_group_id",
        "beep_on_arm_disarm",
        "beep_on_arm_disarm_v2",
        "beep_on_delay",
        "beep_on_delay_v2",
        "beep_volume_level",
        "blink_while_armed",
        "buzzer_state",
        "chimes_enabled",
        "common_fibra_part",
        "common_part",
        "externally_powered",
        "post_alarm_indication_enabled",
        "siren_volume_level",
        "subtype",
    )
    class ArmedLightIndication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ARMED_LIGHT_INDICATION_INFO: _ClassVar[StreetSirenFibra.ArmedLightIndication]
        OFF_ARMED_LIGHT_INDICATION: _ClassVar[StreetSirenFibra.ArmedLightIndication]
        BLINK_ARMED_LIGHT_INDICATION: _ClassVar[StreetSirenFibra.ArmedLightIndication]
        CONSTANT_ON_ARMED_LIGHT_INDICATION: _ClassVar[
            StreetSirenFibra.ArmedLightIndication
        ]

    NO_ARMED_LIGHT_INDICATION_INFO: StreetSirenFibra.ArmedLightIndication
    OFF_ARMED_LIGHT_INDICATION: StreetSirenFibra.ArmedLightIndication
    BLINK_ARMED_LIGHT_INDICATION: StreetSirenFibra.ArmedLightIndication
    CONSTANT_ON_ARMED_LIGHT_INDICATION: StreetSirenFibra.ArmedLightIndication
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_BUZZER_STATE_INFO: _ClassVar[StreetSirenFibra.BuzzerState]
        OFF_BUZZER_STATE: _ClassVar[StreetSirenFibra.BuzzerState]
        ON_BUZZER_STATE: _ClassVar[StreetSirenFibra.BuzzerState]
        WAIT_START_BUZZER_STATE: _ClassVar[StreetSirenFibra.BuzzerState]
        WAIT_STOP_BUZZER_STATE: _ClassVar[StreetSirenFibra.BuzzerState]

    NOT_BUZZER_STATE_INFO: StreetSirenFibra.BuzzerState
    OFF_BUZZER_STATE: StreetSirenFibra.BuzzerState
    ON_BUZZER_STATE: StreetSirenFibra.BuzzerState
    WAIT_START_BUZZER_STATE: StreetSirenFibra.BuzzerState
    WAIT_STOP_BUZZER_STATE: StreetSirenFibra.BuzzerState
    class SirenVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_VOLUME_LEVEL_INFO: _ClassVar[StreetSirenFibra.SirenVolumeLevel]
        VERY_LOUD_SIREN_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.SirenVolumeLevel]
        LOUD_SIREN_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.SirenVolumeLevel]
        QUIET_SIREN_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.SirenVolumeLevel]
        DISABLED_SIREN_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.SirenVolumeLevel]

    NO_SIREN_VOLUME_LEVEL_INFO: StreetSirenFibra.SirenVolumeLevel
    VERY_LOUD_SIREN_VOLUME_LEVEL: StreetSirenFibra.SirenVolumeLevel
    LOUD_SIREN_VOLUME_LEVEL: StreetSirenFibra.SirenVolumeLevel
    QUIET_SIREN_VOLUME_LEVEL: StreetSirenFibra.SirenVolumeLevel
    DISABLED_SIREN_VOLUME_LEVEL: StreetSirenFibra.SirenVolumeLevel
    class BeepVolumeLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_VOLUME_LEVEL_INFO: _ClassVar[StreetSirenFibra.BeepVolumeLevel]
        VERY_LOUD_BEEP_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.BeepVolumeLevel]
        LOUD_BEEP_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.BeepVolumeLevel]
        QUIET_BEEP_VOLUME_LEVEL: _ClassVar[StreetSirenFibra.BeepVolumeLevel]

    NO_BEEP_VOLUME_LEVEL_INFO: StreetSirenFibra.BeepVolumeLevel
    VERY_LOUD_BEEP_VOLUME_LEVEL: StreetSirenFibra.BeepVolumeLevel
    LOUD_BEEP_VOLUME_LEVEL: StreetSirenFibra.BeepVolumeLevel
    QUIET_BEEP_VOLUME_LEVEL: StreetSirenFibra.BeepVolumeLevel
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_ARM_DISARM_INFO: _ClassVar[StreetSirenFibra.BeepOnArmDisarm]
        BEEP_ON_ARM: _ClassVar[StreetSirenFibra.BeepOnArmDisarm]
        BEEP_ON_DISARM: _ClassVar[StreetSirenFibra.BeepOnArmDisarm]
        BEEP_ON_NIGHT_ARM: _ClassVar[StreetSirenFibra.BeepOnArmDisarm]
        BEEP_ON_NIGHT_DISARM: _ClassVar[StreetSirenFibra.BeepOnArmDisarm]

    NO_BEEP_ON_ARM_DISARM_INFO: StreetSirenFibra.BeepOnArmDisarm
    BEEP_ON_ARM: StreetSirenFibra.BeepOnArmDisarm
    BEEP_ON_DISARM: StreetSirenFibra.BeepOnArmDisarm
    BEEP_ON_NIGHT_ARM: StreetSirenFibra.BeepOnArmDisarm
    BEEP_ON_NIGHT_DISARM: StreetSirenFibra.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_DELAY_INFO: _ClassVar[StreetSirenFibra.BeepOnDelay]
        BEEP_ON_ARM_DELAY: _ClassVar[StreetSirenFibra.BeepOnDelay]
        BEEP_ON_DISARM_DELAY: _ClassVar[StreetSirenFibra.BeepOnDelay]
        BEEP_ON_NIGHT_ARM_DELAY: _ClassVar[StreetSirenFibra.BeepOnDelay]
        BEEP_ON_NIGHT_DISARM_DELAY: _ClassVar[StreetSirenFibra.BeepOnDelay]

    NO_BEEP_ON_DELAY_INFO: StreetSirenFibra.BeepOnDelay
    BEEP_ON_ARM_DELAY: StreetSirenFibra.BeepOnDelay
    BEEP_ON_DISARM_DELAY: StreetSirenFibra.BeepOnDelay
    BEEP_ON_NIGHT_ARM_DELAY: StreetSirenFibra.BeepOnDelay
    BEEP_ON_NIGHT_DISARM_DELAY: StreetSirenFibra.BeepOnDelay
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[StreetSirenFibra.Subtype]

    NO_SUBTYPE: StreetSirenFibra.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_DURATION_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_V2_FIELD_NUMBER: _ClassVar[int]
    BLINK_WHILE_ARMED_FIELD_NUMBER: _ClassVar[int]
    ALERT_IF_MOVED_FIELD_NUMBER: _ClassVar[int]
    SIREN_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    BUZZER_STATE_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_V2_FIELD_NUMBER: _ClassVar[int]
    BEEP_VOLUME_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHIMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    common_fibra_part: _common_fibra_pb2.CommonFibraPart
    alarm_duration: int
    beep_on_arm_disarm: bool
    beep_on_arm_disarm_v2: _containers.RepeatedScalarFieldContainer[
        StreetSirenFibra.BeepOnArmDisarm
    ]
    blink_while_armed: StreetSirenFibra.ArmedLightIndication
    alert_if_moved: bool
    siren_volume_level: StreetSirenFibra.SirenVolumeLevel
    externally_powered: _wrappers_pb2.BoolValue
    buzzer_state: StreetSirenFibra.BuzzerState
    beep_on_delay: bool
    beep_on_delay_v2: _containers.RepeatedScalarFieldContainer[
        StreetSirenFibra.BeepOnDelay
    ]
    beep_volume_level: StreetSirenFibra.BeepVolumeLevel
    associated_group_id: str
    chimes_enabled: bool
    post_alarm_indication_enabled: bool
    subtype: StreetSirenFibra.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        common_fibra_part: _common_fibra_pb2.CommonFibraPart | _Mapping | None = ...,
        alarm_duration: int | None = ...,
        beep_on_arm_disarm: bool = ...,
        beep_on_arm_disarm_v2: _Iterable[StreetSirenFibra.BeepOnArmDisarm | str]
        | None = ...,
        blink_while_armed: StreetSirenFibra.ArmedLightIndication | str | None = ...,
        alert_if_moved: bool = ...,
        siren_volume_level: StreetSirenFibra.SirenVolumeLevel | str | None = ...,
        externally_powered: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        buzzer_state: StreetSirenFibra.BuzzerState | str | None = ...,
        beep_on_delay: bool = ...,
        beep_on_delay_v2: _Iterable[StreetSirenFibra.BeepOnDelay | str] | None = ...,
        beep_volume_level: StreetSirenFibra.BeepVolumeLevel | str | None = ...,
        associated_group_id: str | None = ...,
        chimes_enabled: bool = ...,
        post_alarm_indication_enabled: bool = ...,
        subtype: StreetSirenFibra.Subtype | str | None = ...,
    ) -> None: ...
