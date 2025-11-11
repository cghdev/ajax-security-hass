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

class MotionProtectCurtain(_message.Message):
    __slots__ = (
        "always_active",
        "antimasking",
        "common_part",
        "masked",
        "pet_immunity",
        "sensitivity",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionProtectCurtain.SirenTrigger]
        MOTION: _ClassVar[MotionProtectCurtain.SirenTrigger]
        ANTIMASKING: _ClassVar[MotionProtectCurtain.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: MotionProtectCurtain.SirenTrigger
    MOTION: MotionProtectCurtain.SirenTrigger
    ANTIMASKING: MotionProtectCurtain.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionProtectCurtain.Subtype]

    NO_SUBTYPE: MotionProtectCurtain.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PET_IMMUNITY_FIELD_NUMBER: _ClassVar[int]
    ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    MASKED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        MotionProtectCurtain.SirenTrigger
    ]
    sensitivity: int
    always_active: bool
    pet_immunity: bool
    antimasking: bool
    masked: _wrappers_pb2.BoolValue
    subtype: MotionProtectCurtain.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[MotionProtectCurtain.SirenTrigger | str] | None = ...,
        sensitivity: int | None = ...,
        always_active: bool = ...,
        pet_immunity: bool = ...,
        antimasking: bool = ...,
        masked: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        subtype: MotionProtectCurtain.Subtype | str | None = ...,
    ) -> None: ...
