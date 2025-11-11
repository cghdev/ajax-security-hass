from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2
from systems.ajax.protobuf.hub.device import common_fibra_pb2 as _common_fibra_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class MotionProtectFibra(_message.Message):
    __slots__ = (
        "always_active",
        "common_fibra_part",
        "common_part",
        "sensitivity",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MotionProtectFibra.SirenTrigger]
        MOTION: _ClassVar[MotionProtectFibra.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: MotionProtectFibra.SirenTrigger
    MOTION: MotionProtectFibra.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MotionProtectFibra.Subtype]

    NO_SUBTYPE: MotionProtectFibra.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    common_fibra_part: _common_fibra_pb2.CommonFibraPart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        MotionProtectFibra.SirenTrigger
    ]
    sensitivity: int
    always_active: bool
    subtype: MotionProtectFibra.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        common_fibra_part: _common_fibra_pb2.CommonFibraPart | _Mapping | None = ...,
        siren_triggers: _Iterable[MotionProtectFibra.SirenTrigger | str] | None = ...,
        sensitivity: int | None = ...,
        always_active: bool = ...,
        subtype: MotionProtectFibra.Subtype | str | None = ...,
    ) -> None: ...
