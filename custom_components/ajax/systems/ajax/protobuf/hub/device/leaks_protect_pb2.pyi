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

class LeaksProtect(_message.Message):
    __slots__ = (
        "always_active",
        "common_part",
        "leak_detected",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[LeaksProtect.SirenTrigger]
        LEAK: _ClassVar[LeaksProtect.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: LeaksProtect.SirenTrigger
    LEAK: LeaksProtect.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[LeaksProtect.Subtype]

    NO_SUBTYPE: LeaksProtect.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[LeaksProtect.SirenTrigger]
    always_active: bool
    leak_detected: _wrappers_pb2.BoolValue
    subtype: LeaksProtect.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[LeaksProtect.SirenTrigger | str] | None = ...,
        always_active: bool = ...,
        leak_detected: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        subtype: LeaksProtect.Subtype | str | None = ...,
    ) -> None: ...
