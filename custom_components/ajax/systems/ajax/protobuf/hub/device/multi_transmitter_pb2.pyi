from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class MultiTransmitter(_message.Message):
    __slots__ = (
        "battery_broken",
        "battery_charging",
        "common_part",
        "external_fire_notifiers_power_broken",
        "external_power",
        "external_sensor_power_broken",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[MultiTransmitter.SirenTrigger]
        SHORT_CIRCUIT: _ClassVar[MultiTransmitter.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: MultiTransmitter.SirenTrigger
    SHORT_CIRCUIT: MultiTransmitter.SirenTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[MultiTransmitter.Subtype]

    NO_SUBTYPE: MultiTransmitter.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SENSOR_POWER_BROKEN_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGING_FIELD_NUMBER: _ClassVar[int]
    BATTERY_BROKEN_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_FIRE_NOTIFIERS_POWER_BROKEN_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    external_power: bool
    external_sensor_power_broken: bool
    battery_charging: bool
    battery_broken: bool
    external_fire_notifiers_power_broken: bool
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        MultiTransmitter.SirenTrigger
    ]
    subtype: MultiTransmitter.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        external_power: bool = ...,
        external_sensor_power_broken: bool = ...,
        battery_charging: bool = ...,
        battery_broken: bool = ...,
        external_fire_notifiers_power_broken: bool = ...,
        siren_triggers: _Iterable[MultiTransmitter.SirenTrigger | str] | None = ...,
        subtype: MultiTransmitter.Subtype | str | None = ...,
    ) -> None: ...
