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

class DualCurtainOutdoor(_message.Message):
    __slots__ = (
        "common_part",
        "left_fade_antimasking",
        "left_motion_allowed",
        "left_motion_always_active",
        "left_motion_antimasking",
        "left_motion_detected",
        "left_motion_masked",
        "left_motion_sensitivity",
        "logging_enabled",
        "right_fade_antimasking",
        "right_motion_allowed",
        "right_motion_always_active",
        "right_motion_antimasking",
        "right_motion_detected",
        "right_motion_masked",
        "right_motion_sensitivity",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[DualCurtainOutdoor.SirenTrigger]
        LEFT_MOTION: _ClassVar[DualCurtainOutdoor.SirenTrigger]
        RIGHT_MOTION: _ClassVar[DualCurtainOutdoor.SirenTrigger]
        LEFT_ANTIMASKING: _ClassVar[DualCurtainOutdoor.SirenTrigger]
        RIGHT_ANTIMASKING: _ClassVar[DualCurtainOutdoor.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: DualCurtainOutdoor.SirenTrigger
    LEFT_MOTION: DualCurtainOutdoor.SirenTrigger
    RIGHT_MOTION: DualCurtainOutdoor.SirenTrigger
    LEFT_ANTIMASKING: DualCurtainOutdoor.SirenTrigger
    RIGHT_ANTIMASKING: DualCurtainOutdoor.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[DualCurtainOutdoor.Subtype]

    NO_SUBTYPE: DualCurtainOutdoor.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    LEFT_MOTION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    RIGHT_MOTION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    LEFT_MOTION_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    RIGHT_MOTION_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    LEFT_MOTION_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    RIGHT_MOTION_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LEFT_MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    RIGHT_MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    LEFT_MOTION_ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    RIGHT_MOTION_ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    LEFT_MOTION_MASKED_FIELD_NUMBER: _ClassVar[int]
    RIGHT_MOTION_MASKED_FIELD_NUMBER: _ClassVar[int]
    LEFT_FADE_ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FADE_ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    LOGGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        DualCurtainOutdoor.SirenTrigger
    ]
    left_motion_allowed: bool
    right_motion_allowed: bool
    left_motion_sensitivity: int
    right_motion_sensitivity: int
    left_motion_always_active: bool
    right_motion_always_active: bool
    left_motion_detected: bool
    right_motion_detected: bool
    left_motion_antimasking: bool
    right_motion_antimasking: bool
    left_motion_masked: _wrappers_pb2.BoolValue
    right_motion_masked: _wrappers_pb2.BoolValue
    left_fade_antimasking: int
    right_fade_antimasking: int
    logging_enabled: bool
    subtype: DualCurtainOutdoor.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[DualCurtainOutdoor.SirenTrigger | str] | None = ...,
        left_motion_allowed: bool = ...,
        right_motion_allowed: bool = ...,
        left_motion_sensitivity: int | None = ...,
        right_motion_sensitivity: int | None = ...,
        left_motion_always_active: bool = ...,
        right_motion_always_active: bool = ...,
        left_motion_detected: bool = ...,
        right_motion_detected: bool = ...,
        left_motion_antimasking: bool = ...,
        right_motion_antimasking: bool = ...,
        left_motion_masked: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        right_motion_masked: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        left_fade_antimasking: int | None = ...,
        right_fade_antimasking: int | None = ...,
        logging_enabled: bool = ...,
        subtype: DualCurtainOutdoor.Subtype | str | None = ...,
    ) -> None: ...
