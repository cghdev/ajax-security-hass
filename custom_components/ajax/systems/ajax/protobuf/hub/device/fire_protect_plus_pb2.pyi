from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FireProtectPlus(_message.Message):
    __slots__ = (
        "always_active",
        "backup_battery_charge_ok",
        "backup_battery_inserted",
        "buzzer_state",
        "camera_malfunction",
        "co_alarm_detected",
        "co_alarms_enabled",
        "common_part",
        "high_temperature_alarms_enabled",
        "high_temperature_diff_detected",
        "siren_triggers",
        "smoke_alarm_detected",
        "smoke_camera_dusty",
        "subtype",
        "temperature_alarm_detected",
        "temperature_diff_detection_enabled",
    )
    class BuzzerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFF: _ClassVar[FireProtectPlus.BuzzerState]
        ON: _ClassVar[FireProtectPlus.BuzzerState]

    OFF: FireProtectPlus.BuzzerState
    ON: FireProtectPlus.BuzzerState
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[FireProtectPlus.SirenTrigger]
        TEMPERATURE: _ClassVar[FireProtectPlus.SirenTrigger]
        TEMPERATURE_DIFF: _ClassVar[FireProtectPlus.SirenTrigger]
        SMOKE: _ClassVar[FireProtectPlus.SirenTrigger]
        CO: _ClassVar[FireProtectPlus.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: FireProtectPlus.SirenTrigger
    TEMPERATURE: FireProtectPlus.SirenTrigger
    TEMPERATURE_DIFF: FireProtectPlus.SirenTrigger
    SMOKE: FireProtectPlus.SirenTrigger
    CO: FireProtectPlus.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[FireProtectPlus.Subtype]

    NO_SUBTYPE: FireProtectPlus.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SMOKE_ALARM_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_ALARM_DETECTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_BATTERY_INSERTED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_BATTERY_CHARGE_OK_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_DIFF_DETECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAMERA_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    SMOKE_CAMERA_DUSTY_FIELD_NUMBER: _ClassVar[int]
    HIGH_TEMPERATURE_ALARMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HIGH_TEMPERATURE_DIFF_DETECTED_FIELD_NUMBER: _ClassVar[int]
    BUZZER_STATE_FIELD_NUMBER: _ClassVar[int]
    CO_ALARMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CO_ALARM_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        FireProtectPlus.SirenTrigger
    ]
    smoke_alarm_detected: _wrappers_pb2.BoolValue
    temperature_alarm_detected: _wrappers_pb2.BoolValue
    backup_battery_inserted: _wrappers_pb2.BoolValue
    backup_battery_charge_ok: _wrappers_pb2.BoolValue
    always_active: bool
    temperature_diff_detection_enabled: bool
    camera_malfunction: _wrappers_pb2.BoolValue
    smoke_camera_dusty: _wrappers_pb2.BoolValue
    high_temperature_alarms_enabled: bool
    high_temperature_diff_detected: _wrappers_pb2.BoolValue
    buzzer_state: FireProtectPlus.BuzzerState
    co_alarms_enabled: bool
    co_alarm_detected: _wrappers_pb2.BoolValue
    subtype: FireProtectPlus.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[FireProtectPlus.SirenTrigger | str] | None = ...,
        smoke_alarm_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        temperature_alarm_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        backup_battery_inserted: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        backup_battery_charge_ok: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        always_active: bool = ...,
        temperature_diff_detection_enabled: bool = ...,
        camera_malfunction: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        smoke_camera_dusty: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        high_temperature_alarms_enabled: bool = ...,
        high_temperature_diff_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        buzzer_state: FireProtectPlus.BuzzerState | str | None = ...,
        co_alarms_enabled: bool = ...,
        co_alarm_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        subtype: FireProtectPlus.Subtype | str | None = ...,
    ) -> None: ...
