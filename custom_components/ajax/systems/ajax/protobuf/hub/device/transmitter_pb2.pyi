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

class Transmitter(_message.Message):
    __slots__ = (
        "accelerometer_aware",
        "chime_signal",
        "chime_triggers",
        "common_part",
        "custom_alarm_type",
        "external_contact_alarm_mode",
        "external_contact_always_active",
        "external_contact_state_mode",
        "external_contact_triggered",
        "external_device_power_supply_mode",
        "external_device_tamper_state_mode",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[Transmitter.SirenTrigger]
        EXTRA_CONTACT: _ClassVar[Transmitter.SirenTrigger]
        ACCELERATION: _ClassVar[Transmitter.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: Transmitter.SirenTrigger
    EXTRA_CONTACT: Transmitter.SirenTrigger
    ACCELERATION: Transmitter.SirenTrigger
    class ContactStateMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CONTACT_STATE_MODE_INFO: _ClassVar[Transmitter.ContactStateMode]
        NO: _ClassVar[Transmitter.ContactStateMode]
        NC: _ClassVar[Transmitter.ContactStateMode]

    NO_CONTACT_STATE_MODE_INFO: Transmitter.ContactStateMode
    NO: Transmitter.ContactStateMode
    NC: Transmitter.ContactStateMode
    class ExternalContactAlarmMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_ALARM_MODE_INFO: _ClassVar[
            Transmitter.ExternalContactAlarmMode
        ]
        BISTABLE: _ClassVar[Transmitter.ExternalContactAlarmMode]
        IMPULSE: _ClassVar[Transmitter.ExternalContactAlarmMode]

    NO_EXTERNAL_CONTACT_ALARM_MODE_INFO: Transmitter.ExternalContactAlarmMode
    BISTABLE: Transmitter.ExternalContactAlarmMode
    IMPULSE: Transmitter.ExternalContactAlarmMode
    class PowerSupplyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_POWER_SUPPLY_MODE_INFO: _ClassVar[Transmitter.PowerSupplyMode]
        ALWAYS_DISABLED: _ClassVar[Transmitter.PowerSupplyMode]
        DISABLED_IF_HUB_DISARMED: _ClassVar[Transmitter.PowerSupplyMode]
        ALWAYS_ENABLED: _ClassVar[Transmitter.PowerSupplyMode]

    NO_POWER_SUPPLY_MODE_INFO: Transmitter.PowerSupplyMode
    ALWAYS_DISABLED: Transmitter.PowerSupplyMode
    DISABLED_IF_HUB_DISARMED: Transmitter.PowerSupplyMode
    ALWAYS_ENABLED: Transmitter.PowerSupplyMode
    class CustomAlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CUSTOM_ALARM_TYPE: _ClassVar[Transmitter.CustomAlarmType]
        BURGLARY: _ClassVar[Transmitter.CustomAlarmType]
        FIRE: _ClassVar[Transmitter.CustomAlarmType]
        MEDICAL: _ClassVar[Transmitter.CustomAlarmType]
        PANIC: _ClassVar[Transmitter.CustomAlarmType]
        GAS: _ClassVar[Transmitter.CustomAlarmType]

    NO_CUSTOM_ALARM_TYPE: Transmitter.CustomAlarmType
    BURGLARY: Transmitter.CustomAlarmType
    FIRE: Transmitter.CustomAlarmType
    MEDICAL: Transmitter.CustomAlarmType
    PANIC: Transmitter.CustomAlarmType
    GAS: Transmitter.CustomAlarmType
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIME_TRIGGER_INFO: _ClassVar[Transmitter.ChimeTrigger]
        CHIME_EXTRA_CONTACT: _ClassVar[Transmitter.ChimeTrigger]

    NO_CHIME_TRIGGER_INFO: Transmitter.ChimeTrigger
    CHIME_EXTRA_CONTACT: Transmitter.ChimeTrigger
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[Transmitter.Subtype]

    NO_SUBTYPE: Transmitter.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_STATE_MODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALARM_MODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_TAMPER_STATE_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_AWARE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEVICE_POWER_SUPPLY_MODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[Transmitter.SirenTrigger]
    external_contact_state_mode: Transmitter.ContactStateMode
    external_contact_always_active: bool
    external_contact_triggered: _wrappers_pb2.BoolValue
    external_contact_alarm_mode: Transmitter.ExternalContactAlarmMode
    external_device_tamper_state_mode: Transmitter.ContactStateMode
    accelerometer_aware: bool
    external_device_power_supply_mode: Transmitter.PowerSupplyMode
    custom_alarm_type: Transmitter.CustomAlarmType
    chime_triggers: _containers.RepeatedScalarFieldContainer[Transmitter.ChimeTrigger]
    chime_signal: int
    subtype: Transmitter.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[Transmitter.SirenTrigger | str] | None = ...,
        external_contact_state_mode: Transmitter.ContactStateMode | str | None = ...,
        external_contact_always_active: bool = ...,
        external_contact_triggered: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        external_contact_alarm_mode: Transmitter.ExternalContactAlarmMode
        | str
        | None = ...,
        external_device_tamper_state_mode: Transmitter.ContactStateMode
        | str
        | None = ...,
        accelerometer_aware: bool = ...,
        external_device_power_supply_mode: Transmitter.PowerSupplyMode
        | str
        | None = ...,
        custom_alarm_type: Transmitter.CustomAlarmType | str | None = ...,
        chime_triggers: _Iterable[Transmitter.ChimeTrigger | str] | None = ...,
        chime_signal: int | None = ...,
        subtype: Transmitter.Subtype | str | None = ...,
    ) -> None: ...
