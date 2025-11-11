from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class WireInput(_message.Message):
    __slots__ = (
        "alarm_delay_seconds",
        "apply_delays_to_night_mode",
        "arm_delay_seconds",
        "bypass_mode",
        "chime_signal",
        "chime_triggers",
        "cms_device_index",
        "external_contact_alarm_mode",
        "external_contact_always_active",
        "external_contact_mode",
        "external_contact_state",
        "group_id",
        "id",
        "is_bypass_mode",
        "name",
        "night_mode_arm",
        "perimeter_alarm_delay_seconds",
        "perimeter_arm_delay_seconds",
        "room_id",
        "service_problems",
        "siren_triggers",
        "tampered",
        "verifies_alarm",
        "wire_input_type",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[WireInput.SirenTrigger]
        EXTRA_CONTACT: _ClassVar[WireInput.SirenTrigger]
        SHORT_CIRCUIT: _ClassVar[WireInput.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: WireInput.SirenTrigger
    EXTRA_CONTACT: WireInput.SirenTrigger
    SHORT_CIRCUIT: WireInput.SirenTrigger
    class ExternalContactMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_MODE_INFO: _ClassVar[WireInput.ExternalContactMode]
        DISABLED: _ClassVar[WireInput.ExternalContactMode]
        NORMALLY_OPEN: _ClassVar[WireInput.ExternalContactMode]
        NORMALLY_CLOSED: _ClassVar[WireInput.ExternalContactMode]
        NORMALLY_CLOSED_R: _ClassVar[WireInput.ExternalContactMode]
        NORMALLY_OPEN_R: _ClassVar[WireInput.ExternalContactMode]

    NO_EXTERNAL_CONTACT_MODE_INFO: WireInput.ExternalContactMode
    DISABLED: WireInput.ExternalContactMode
    NORMALLY_OPEN: WireInput.ExternalContactMode
    NORMALLY_CLOSED: WireInput.ExternalContactMode
    NORMALLY_CLOSED_R: WireInput.ExternalContactMode
    NORMALLY_OPEN_R: WireInput.ExternalContactMode
    class ExternalContactState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_STATE: _ClassVar[WireInput.ExternalContactState]
        BROKEN: _ClassVar[WireInput.ExternalContactState]
        NORMAL: _ClassVar[WireInput.ExternalContactState]
        CONTACT_SHORT_CIRCUIT: _ClassVar[WireInput.ExternalContactState]
        NOT_AVAILABLE: _ClassVar[WireInput.ExternalContactState]

    NO_EXTERNAL_CONTACT_STATE: WireInput.ExternalContactState
    BROKEN: WireInput.ExternalContactState
    NORMAL: WireInput.ExternalContactState
    CONTACT_SHORT_CIRCUIT: WireInput.ExternalContactState
    NOT_AVAILABLE: WireInput.ExternalContactState
    class ExternalContactAlarmMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTERNAL_CONTACT_ALARM_MODE_INFO: _ClassVar[
            WireInput.ExternalContactAlarmMode
        ]
        BISTABLE: _ClassVar[WireInput.ExternalContactAlarmMode]
        PULSE: _ClassVar[WireInput.ExternalContactAlarmMode]

    NO_EXTERNAL_CONTACT_ALARM_MODE_INFO: WireInput.ExternalContactAlarmMode
    BISTABLE: WireInput.ExternalContactAlarmMode
    PULSE: WireInput.ExternalContactAlarmMode
    class WireInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_WIRE_INPUT_TYPE_INFO: _ClassVar[WireInput.WireInputType]
        SENSOR: _ClassVar[WireInput.WireInputType]
        TAMPER: _ClassVar[WireInput.WireInputType]

    NO_WIRE_INPUT_TYPE_INFO: WireInput.WireInputType
    SENSOR: WireInput.WireInputType
    TAMPER: WireInput.WireInputType
    class BypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BYPASS_MODE_INFO: _ClassVar[WireInput.BypassMode]
        OFF: _ClassVar[WireInput.BypassMode]
        ON: _ClassVar[WireInput.BypassMode]

    NO_BYPASS_MODE_INFO: WireInput.BypassMode
    OFF: WireInput.BypassMode
    ON: WireInput.BypassMode
    class IsBypassMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_IN_BYPASS_MODE: _ClassVar[WireInput.IsBypassMode]
        ENABLED_BYPASS: _ClassVar[WireInput.IsBypassMode]
        NOT_USED: _ClassVar[WireInput.IsBypassMode]
        AUTO_BYPASS_BY_COUNT: _ClassVar[WireInput.IsBypassMode]
        AUTO_BYPASS_BY_ACTIVE: _ClassVar[WireInput.IsBypassMode]

    NO_IN_BYPASS_MODE: WireInput.IsBypassMode
    ENABLED_BYPASS: WireInput.IsBypassMode
    NOT_USED: WireInput.IsBypassMode
    AUTO_BYPASS_BY_COUNT: WireInput.IsBypassMode
    AUTO_BYPASS_BY_ACTIVE: WireInput.IsBypassMode
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHIME_TRIGGER_INFO: _ClassVar[WireInput.ChimeTrigger]
        CHIME_EXTRA_CONTACT: _ClassVar[WireInput.ChimeTrigger]

    NO_CHIME_TRIGGER_INFO: WireInput.ChimeTrigger
    CHIME_EXTRA_CONTACT: WireInput.ChimeTrigger
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    APPLY_DELAYS_TO_NIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ARM_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_MODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALARM_MODE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_STATE_FIELD_NUMBER: _ClassVar[int]
    TAMPERED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_BYPASS_MODE_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    VERIFIES_ALARM_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    siren_triggers: _containers.RepeatedScalarFieldContainer[WireInput.SirenTrigger]
    group_id: str
    arm_delay_seconds: int
    alarm_delay_seconds: int
    apply_delays_to_night_mode: bool
    night_mode_arm: bool
    external_contact_mode: WireInput.ExternalContactMode
    external_contact_alarm_mode: WireInput.ExternalContactAlarmMode
    external_contact_state: WireInput.ExternalContactState
    tampered: bool
    external_contact_always_active: bool
    service_problems: int
    bypass_mode: WireInput.BypassMode
    is_bypass_mode: _containers.RepeatedScalarFieldContainer[WireInput.IsBypassMode]
    wire_input_type: WireInput.WireInputType
    room_id: str
    cms_device_index: int
    verifies_alarm: bool
    perimeter_arm_delay_seconds: int
    perimeter_alarm_delay_seconds: int
    chime_triggers: _containers.RepeatedScalarFieldContainer[WireInput.ChimeTrigger]
    chime_signal: int
    def __init__(
        self,
        id: str | None = ...,
        name: _name_pb2.Name | _Mapping | None = ...,
        siren_triggers: _Iterable[WireInput.SirenTrigger | str] | None = ...,
        group_id: str | None = ...,
        arm_delay_seconds: int | None = ...,
        alarm_delay_seconds: int | None = ...,
        apply_delays_to_night_mode: bool = ...,
        night_mode_arm: bool = ...,
        external_contact_mode: WireInput.ExternalContactMode | str | None = ...,
        external_contact_alarm_mode: WireInput.ExternalContactAlarmMode
        | str
        | None = ...,
        external_contact_state: WireInput.ExternalContactState | str | None = ...,
        tampered: bool = ...,
        external_contact_always_active: bool = ...,
        service_problems: int | None = ...,
        bypass_mode: WireInput.BypassMode | str | None = ...,
        is_bypass_mode: _Iterable[WireInput.IsBypassMode | str] | None = ...,
        wire_input_type: WireInput.WireInputType | str | None = ...,
        room_id: str | None = ...,
        cms_device_index: int | None = ...,
        verifies_alarm: bool = ...,
        perimeter_arm_delay_seconds: int | None = ...,
        perimeter_alarm_delay_seconds: int | None = ...,
        chime_triggers: _Iterable[WireInput.ChimeTrigger | str] | None = ...,
        chime_signal: int | None = ...,
    ) -> None: ...
