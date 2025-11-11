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

class MotionProtectOutdoor(_message.Message):
    __slots__ = (
        "always_active",
        "antimasking",
        "common_part",
        "externally_powered",
        "masked",
        "sensitivity",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionProtectOutdoor.SirenTrigger]
        MOTION: _ClassVar[MotionProtectOutdoor.SirenTrigger]
        ANTIMASKING: _ClassVar[MotionProtectOutdoor.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: MotionProtectOutdoor.SirenTrigger
    MOTION: MotionProtectOutdoor.SirenTrigger
    ANTIMASKING: MotionProtectOutdoor.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionProtectOutdoor.Subtype]

    NO_SUBTYPE: MotionProtectOutdoor.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ANTIMASKING_FIELD_NUMBER: _ClassVar[int]
    MASKED_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        MotionProtectOutdoor.SirenTrigger
    ]
    sensitivity: int
    always_active: bool
    antimasking: bool
    masked: _wrappers_pb2.BoolValue
    externally_powered: _wrappers_pb2.BoolValue
    subtype: MotionProtectOutdoor.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[MotionProtectOutdoor.SirenTrigger | str] | None = ...,
        sensitivity: int | None = ...,
        always_active: bool = ...,
        antimasking: bool = ...,
        masked: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        externally_powered: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        subtype: MotionProtectOutdoor.Subtype | str | None = ...,
    ) -> None: ...
