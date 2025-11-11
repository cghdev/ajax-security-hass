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

class GlassProtectFibra(_message.Message):
    __slots__ = (
        "always_active",
        "chime_signal",
        "chime_triggers",
        "common_fibra_part",
        "common_part",
        "extra_contact_aware",
        "extra_contact_closed",
        "sensitivity",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[GlassProtectFibra.SirenTrigger]
        EXTRA_CONTACT: _ClassVar[GlassProtectFibra.SirenTrigger]
        GLASS: _ClassVar[GlassProtectFibra.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: GlassProtectFibra.SirenTrigger
    EXTRA_CONTACT: GlassProtectFibra.SirenTrigger
    GLASS: GlassProtectFibra.SirenTrigger
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIME_TRIGGER_INFO: _ClassVar[GlassProtectFibra.ChimeTrigger]
        CHIME_EXTRA_CONTACT: _ClassVar[GlassProtectFibra.ChimeTrigger]

    NO_CHIME_TRIGGER_INFO: GlassProtectFibra.ChimeTrigger
    CHIME_EXTRA_CONTACT: GlassProtectFibra.ChimeTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[GlassProtectFibra.Subtype]

    NO_SUBTYPE: GlassProtectFibra.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_FIBRA_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_CLOSED_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTACT_AWARE_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    common_fibra_part: _common_fibra_pb2.CommonFibraPart
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        GlassProtectFibra.SirenTrigger
    ]
    sensitivity: int
    extra_contact_closed: _wrappers_pb2.BoolValue
    always_active: bool
    extra_contact_aware: bool
    chime_triggers: _containers.RepeatedScalarFieldContainer[
        GlassProtectFibra.ChimeTrigger
    ]
    chime_signal: int
    subtype: GlassProtectFibra.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        common_fibra_part: _common_fibra_pb2.CommonFibraPart | _Mapping | None = ...,
        siren_triggers: _Iterable[GlassProtectFibra.SirenTrigger | str] | None = ...,
        sensitivity: int | None = ...,
        extra_contact_closed: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        always_active: bool = ...,
        extra_contact_aware: bool = ...,
        chime_triggers: _Iterable[GlassProtectFibra.ChimeTrigger | str] | None = ...,
        chime_signal: int | None = ...,
        subtype: GlassProtectFibra.Subtype | str | None = ...,
    ) -> None: ...
