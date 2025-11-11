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

class DoorProtectPlusFibra(_message.Message):
    __slots__ = (
        "accelerometer_aware",
        "accelerometer_tilt_alarm_delay_seconds",
        "accelerometer_tilt_degrees",
        "always_active",
        "chime_signal",
        "chime_triggers",
        "common_fibra_part",
        "common_part",
        "extra_contact_aware",
        "extra_contact_closed",
        "extra_contact_type",
        "ignore_simple_impact",
        "reed_closed",
        "reed_contact_aware",
        "roller_shutter_settings",
        "roller_shutter_supported",
        "shock_sensor_aware",
        "shock_sensor_sensitivity",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[DoorProtectPlusFibra.SirenTrigger]
        REED: _ClassVar[DoorProtectPlusFibra.SirenTrigger]
        EXTRA_CONTACT: _ClassVar[DoorProtectPlusFibra.SirenTrigger]
        TILT: _ClassVar[DoorProtectPlusFibra.SirenTrigger]
        SHOCK: _ClassVar[DoorProtectPlusFibra.SirenTrigger]
        SHUTTER_ALARM: _ClassVar[DoorProtectPlusFibra.SirenTrigger]
        SHUTTER_ONLINE: _ClassVar[DoorProtectPlusFibra.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: DoorProtectPlusFibra.SirenTrigger
    REED: DoorProtectPlusFibra.SirenTrigger
    EXTRA_CONTACT: DoorProtectPlusFibra.SirenTrigger
    TILT: DoorProtectPlusFibra.SirenTrigger
    SHOCK: DoorProtectPlusFibra.SirenTrigger
    SHUTTER_ALARM: DoorProtectPlusFibra.SirenTrigger
    SHUTTER_ONLINE: DoorProtectPlusFibra.SirenTrigger
    class ExtraContactType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA_CONTACT_TYPE_INFO: _ClassVar[DoorProtectPlusFibra.ExtraContactType]
        STANDARD: _ClassVar[DoorProtectPlusFibra.ExtraContactType]
        ROLLER_SHUTTER: _ClassVar[DoorProtectPlusFibra.ExtraContactType]

    NO_EXTRA_CONTACT_TYPE_INFO: DoorProtectPlusFibra.ExtraContactType
    STANDARD: DoorProtectPlusFibra.ExtraContactType
    ROLLER_SHUTTER: DoorProtectPlusFibra.ExtraContactType
    class AccelerometerTiltDegrees(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ACCELEROMETER_TILT_DEGREES_INFO: _ClassVar[
            DoorProtectPlusFibra.AccelerometerTiltDegrees
        ]
        DEG_5: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltDegrees]
        DEG_10: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltDegrees]
        DEG_15: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltDegrees]
        DEG_20: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltDegrees]
        DEG_25: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltDegrees]

    NO_ACCELEROMETER_TILT_DEGREES_INFO: DoorProtectPlusFibra.AccelerometerTiltDegrees
    DEG_5: DoorProtectPlusFibra.AccelerometerTiltDegrees
    DEG_10: DoorProtectPlusFibra.AccelerometerTiltDegrees
    DEG_15: DoorProtectPlusFibra.AccelerometerTiltDegrees
    DEG_20: DoorProtectPlusFibra.AccelerometerTiltDegrees
    DEG_25: DoorProtectPlusFibra.AccelerometerTiltDegrees
    class AccelerometerTiltAlarmDelaySeconds(
        int, metaclass=_enum_type_wrapper.EnumTypeWrapper
    ):
        __slots__ = ()
        NO_ACCELEROMETER_TILT_ALARM_DELAY_SECONDS_INFO: _ClassVar[
            DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
        ]
        SEC_1: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds]
        SEC_2: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds]
        SEC_5: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds]
        SEC_10: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds]
        SEC_30: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds]
        SEC_60: _ClassVar[DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds]

    NO_ACCELEROMETER_TILT_ALARM_DELAY_SECONDS_INFO: (
        DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    )
    SEC_1: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    SEC_2: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    SEC_5: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    SEC_10: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    SEC_30: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    SEC_60: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIME_TRIGGER_INFO: _ClassVar[DoorProtectPlusFibra.ChimeTrigger]
        CHIME_REED: _ClassVar[DoorProtectPlusFibra.ChimeTrigger]
        CHIME_EXTRA_CONTACT: _ClassVar[DoorProtectPlusFibra.ChimeTrigger]

    NO_CHIME_TRIGGER_INFO: DoorProtectPlusFibra.ChimeTrigger
    CHIME_REED: DoorProtectPlusFibra.ChimeTrigger
    CHIME_EXTRA_CONTACT: DoorProtectPlusFibra.ChimeTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[DoorProtectPlusFibra.Subtype]

    NO_SUBTYPE: DoorProtectPlusFibra.Subtype
    class RollerShutterSettings(_message.Message):
        __slots__ = ("count_period", "count_threshold", "roller_shutter_online")
        COUNT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        COUNT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        ROLLER_SHUTTER_ONLINE_FIELD_NUMBER: _ClassVar[int]
        count_period: int
        count_threshold: int
        roller_shutter_online: _wrappers_pb2.BoolValue
        def __init__(
            self,
            count_period: int | None = ...,
            count_threshold: int | None = ...,
            roller_shutter_online: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        ) -> None: ...

    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    REED_CLOSED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_CLOSED_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_AWARE_FIELD_NUMBER: _ClassVar[int]
    REED_CONTACT_AWARE_FIELD_NUMBER: _ClassVar[int]
    SHOCK_SENSOR_AWARE_FIELD_NUMBER: _ClassVar[int]
    SHOCK_SENSOR_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SIMPLE_IMPACT_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_AWARE_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_TILT_DEGREES_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_TILT_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    common_fibra_part: _common_fibra_pb2.CommonFibraPart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        DoorProtectPlusFibra.SirenTrigger
    ]
    reed_closed: _wrappers_pb2.BoolValue
    extra_contact_closed: _wrappers_pb2.BoolValue
    always_active: bool
    extra_contact_aware: bool
    reed_contact_aware: bool
    shock_sensor_aware: bool
    shock_sensor_sensitivity: int
    ignore_simple_impact: bool
    accelerometer_aware: bool
    accelerometer_tilt_degrees: DoorProtectPlusFibra.AccelerometerTiltDegrees
    accelerometer_tilt_alarm_delay_seconds: (
        DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
    )
    extra_contact_type: DoorProtectPlusFibra.ExtraContactType
    roller_shutter_supported: _wrappers_pb2.BoolValue
    roller_shutter_settings: DoorProtectPlusFibra.RollerShutterSettings
    chime_triggers: _containers.RepeatedScalarFieldContainer[
        DoorProtectPlusFibra.ChimeTrigger
    ]
    chime_signal: int
    subtype: DoorProtectPlusFibra.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        common_fibra_part: _common_fibra_pb2.CommonFibraPart | _Mapping | None = ...,
        siren_triggers: _Iterable[DoorProtectPlusFibra.SirenTrigger | str] | None = ...,
        reed_closed: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        extra_contact_closed: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        always_active: bool = ...,
        extra_contact_aware: bool = ...,
        reed_contact_aware: bool = ...,
        shock_sensor_aware: bool = ...,
        shock_sensor_sensitivity: int | None = ...,
        ignore_simple_impact: bool = ...,
        accelerometer_aware: bool = ...,
        accelerometer_tilt_degrees: DoorProtectPlusFibra.AccelerometerTiltDegrees
        | str
        | None = ...,
        accelerometer_tilt_alarm_delay_seconds: DoorProtectPlusFibra.AccelerometerTiltAlarmDelaySeconds
        | str
        | None = ...,
        extra_contact_type: DoorProtectPlusFibra.ExtraContactType | str | None = ...,
        roller_shutter_supported: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        roller_shutter_settings: DoorProtectPlusFibra.RollerShutterSettings
        | _Mapping
        | None = ...,
        chime_triggers: _Iterable[DoorProtectPlusFibra.ChimeTrigger | str] | None = ...,
        chime_signal: int | None = ...,
        subtype: DoorProtectPlusFibra.Subtype | str | None = ...,
    ) -> None: ...
