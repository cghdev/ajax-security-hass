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

class CombiProtectFibra(_message.Message):
    __slots__ = (
        "common_fibra_part",
        "common_part",
        "glass_break_detected",
        "glass_break_sensitivity",
        "glass_break_sensor_always_active",
        "glass_break_sensor_aware",
        "motion_detected",
        "motion_sensitivity",
        "motion_sensor_always_active",
        "motion_sensor_aware",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[CombiProtectFibra.SirenTrigger]
        MOTION: _ClassVar[CombiProtectFibra.SirenTrigger]
        GLASS: _ClassVar[CombiProtectFibra.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: CombiProtectFibra.SirenTrigger
    MOTION: CombiProtectFibra.SirenTrigger
    GLASS: CombiProtectFibra.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[CombiProtectFibra.Subtype]

    NO_SUBTYPE: CombiProtectFibra.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_AWARE_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_SENSOR_AWARE_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_SENSOR_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    common_fibra_part: _common_fibra_pb2.CommonFibraPart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        CombiProtectFibra.SirenTrigger
    ]
    motion_sensor_aware: bool
    glass_break_sensor_aware: bool
    motion_sensitivity: int
    glass_break_sensitivity: int
    motion_sensor_always_active: bool
    glass_break_sensor_always_active: bool
    motion_detected: _wrappers_pb2.BoolValue
    glass_break_detected: _wrappers_pb2.BoolValue
    subtype: CombiProtectFibra.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        common_fibra_part: _common_fibra_pb2.CommonFibraPart | _Mapping | None = ...,
        siren_triggers: _Iterable[CombiProtectFibra.SirenTrigger | str] | None = ...,
        motion_sensor_aware: bool = ...,
        glass_break_sensor_aware: bool = ...,
        motion_sensitivity: int | None = ...,
        glass_break_sensitivity: int | None = ...,
        motion_sensor_always_active: bool = ...,
        glass_break_sensor_always_active: bool = ...,
        motion_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        glass_break_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        subtype: CombiProtectFibra.Subtype | str | None = ...,
    ) -> None: ...
