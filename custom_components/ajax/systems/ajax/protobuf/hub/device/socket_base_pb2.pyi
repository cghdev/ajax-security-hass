from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SocketBase(_message.Message):
    __slots__ = (
        "arming_disarming_actions",
        "channel_mode",
        "channel_normal_state",
        "channel_status",
        "common_part",
        "count_protect",
        "current_protection_threshold",
        "impulse_duration",
        "subtype",
        "type_g",
        "voltage_protection_off",
    )
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[SocketBase.Subtype]
        TYPE_G: _ClassVar[SocketBase.Subtype]

    NO_SUBTYPE: SocketBase.Subtype
    TYPE_G: SocketBase.Subtype
    class ChannelState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLTAGE_TOO_LOW: _ClassVar[SocketBase.ChannelState]
        VOLTAGE_TOO_HIGH: _ClassVar[SocketBase.ChannelState]
        CURRENT_PROTECTION_ACTUATION: _ClassVar[SocketBase.ChannelState]
        CONTACTS_STUCK: _ClassVar[SocketBase.ChannelState]
        TEMPERATURE_PROTECTION_ACTUATION: _ClassVar[SocketBase.ChannelState]
        BUTTON_PRESSED: _ClassVar[SocketBase.ChannelState]
        SWITCHED_ON: _ClassVar[SocketBase.ChannelState]

    VOLTAGE_TOO_LOW: SocketBase.ChannelState
    VOLTAGE_TOO_HIGH: SocketBase.ChannelState
    CURRENT_PROTECTION_ACTUATION: SocketBase.ChannelState
    CONTACTS_STUCK: SocketBase.ChannelState
    TEMPERATURE_PROTECTION_ACTUATION: SocketBase.ChannelState
    BUTTON_PRESSED: SocketBase.ChannelState
    SWITCHED_ON: SocketBase.ChannelState
    class ChannelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHANNEL_MODE: _ClassVar[SocketBase.ChannelMode]
        BISTABLE: _ClassVar[SocketBase.ChannelMode]
        IMPULSE: _ClassVar[SocketBase.ChannelMode]

    NO_CHANNEL_MODE: SocketBase.ChannelMode
    BISTABLE: SocketBase.ChannelMode
    IMPULSE: SocketBase.ChannelMode
    class ChannelNormalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CHANNEL_NORMAL_STATE: _ClassVar[SocketBase.ChannelNormalState]
        NORMALLY_OPEN: _ClassVar[SocketBase.ChannelNormalState]
        NORMALLY_CLOSED: _ClassVar[SocketBase.ChannelNormalState]

    NO_CHANNEL_NORMAL_STATE: SocketBase.ChannelNormalState
    NORMALLY_OPEN: SocketBase.ChannelNormalState
    NORMALLY_CLOSED: SocketBase.ChannelNormalState
    class ArmingDisarmingActions(_message.Message):
        __slots__ = ("action_on_arming", "action_on_disarming")
        class ActionOnArming(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_ACTION_ON_ARMING: _ClassVar[
                SocketBase.ArmingDisarmingActions.ActionOnArming
            ]
            TURN_ON_ON_ARMING: _ClassVar[
                SocketBase.ArmingDisarmingActions.ActionOnArming
            ]
            TURN_OFF_ON_ARMING: _ClassVar[
                SocketBase.ArmingDisarmingActions.ActionOnArming
            ]

        NO_ACTION_ON_ARMING: SocketBase.ArmingDisarmingActions.ActionOnArming
        TURN_ON_ON_ARMING: SocketBase.ArmingDisarmingActions.ActionOnArming
        TURN_OFF_ON_ARMING: SocketBase.ArmingDisarmingActions.ActionOnArming
        class ActionOnDisarming(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_ACTION_ON_DISARMING: _ClassVar[
                SocketBase.ArmingDisarmingActions.ActionOnDisarming
            ]
            TURN_ON_ON_DISARMING: _ClassVar[
                SocketBase.ArmingDisarmingActions.ActionOnDisarming
            ]
            TURN_OFF_ON_DISARMING: _ClassVar[
                SocketBase.ArmingDisarmingActions.ActionOnDisarming
            ]

        NO_ACTION_ON_DISARMING: SocketBase.ArmingDisarmingActions.ActionOnDisarming
        TURN_ON_ON_DISARMING: SocketBase.ArmingDisarmingActions.ActionOnDisarming
        TURN_OFF_ON_DISARMING: SocketBase.ArmingDisarmingActions.ActionOnDisarming
        ACTION_ON_ARMING_FIELD_NUMBER: _ClassVar[int]
        ACTION_ON_DISARMING_FIELD_NUMBER: _ClassVar[int]
        action_on_arming: SocketBase.ArmingDisarmingActions.ActionOnArming
        action_on_disarming: SocketBase.ArmingDisarmingActions.ActionOnDisarming
        def __init__(
            self,
            action_on_arming: SocketBase.ArmingDisarmingActions.ActionOnArming
            | str
            | None = ...,
            action_on_disarming: SocketBase.ArmingDisarmingActions.ActionOnDisarming
            | str
            | None = ...,
        ) -> None: ...

    class TypeG(_message.Message):
        __slots__ = (
            "current",
            "energy_counter_averaging",
            "indication_brightness",
            "indication_mode",
            "last_energy_counter_reset",
            "power",
            "power_counter",
            "voltage",
        )
        class IndicationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_INDICATION_MODE_INFO: _ClassVar[SocketBase.TypeG.IndicationMode]
            DISABLE: _ClassVar[SocketBase.TypeG.IndicationMode]
            ENABLE: _ClassVar[SocketBase.TypeG.IndicationMode]
            ENABLE_WHEN_ACTIVE: _ClassVar[SocketBase.TypeG.IndicationMode]

        NO_INDICATION_MODE_INFO: SocketBase.TypeG.IndicationMode
        DISABLE: SocketBase.TypeG.IndicationMode
        ENABLE: SocketBase.TypeG.IndicationMode
        ENABLE_WHEN_ACTIVE: SocketBase.TypeG.IndicationMode
        class EnergyCounterAveraging(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_ENERGY_COUNTER_AVERAGING_INFO: _ClassVar[
                SocketBase.TypeG.EnergyCounterAveraging
            ]
            ON: _ClassVar[SocketBase.TypeG.EnergyCounterAveraging]
            OFF: _ClassVar[SocketBase.TypeG.EnergyCounterAveraging]

        NO_ENERGY_COUNTER_AVERAGING_INFO: SocketBase.TypeG.EnergyCounterAveraging
        ON: SocketBase.TypeG.EnergyCounterAveraging
        OFF: SocketBase.TypeG.EnergyCounterAveraging
        POWER_FIELD_NUMBER: _ClassVar[int]
        POWER_COUNTER_FIELD_NUMBER: _ClassVar[int]
        CURRENT_FIELD_NUMBER: _ClassVar[int]
        VOLTAGE_FIELD_NUMBER: _ClassVar[int]
        INDICATION_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
        INDICATION_MODE_FIELD_NUMBER: _ClassVar[int]
        ENERGY_COUNTER_AVERAGING_FIELD_NUMBER: _ClassVar[int]
        LAST_ENERGY_COUNTER_RESET_FIELD_NUMBER: _ClassVar[int]
        power: _wrappers_pb2.Int32Value
        power_counter: _wrappers_pb2.Int32Value
        current: _wrappers_pb2.Int32Value
        voltage: _wrappers_pb2.Int32Value
        indication_brightness: int
        indication_mode: SocketBase.TypeG.IndicationMode
        energy_counter_averaging: SocketBase.TypeG.EnergyCounterAveraging
        last_energy_counter_reset: _timestamp_pb2.Timestamp
        def __init__(
            self,
            power: _wrappers_pb2.Int32Value | _Mapping | None = ...,
            power_counter: _wrappers_pb2.Int32Value | _Mapping | None = ...,
            current: _wrappers_pb2.Int32Value | _Mapping | None = ...,
            voltage: _wrappers_pb2.Int32Value | _Mapping | None = ...,
            indication_brightness: int | None = ...,
            indication_mode: SocketBase.TypeG.IndicationMode | str | None = ...,
            energy_counter_averaging: SocketBase.TypeG.EnergyCounterAveraging
            | str
            | None = ...,
            last_energy_counter_reset: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        ) -> None: ...

    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MODE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NORMAL_STATE_FIELD_NUMBER: _ClassVar[int]
    IMPULSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    VOLTAGE_PROTECTION_OFF_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROTECTION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ARMING_DISARMING_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    COUNT_PROTECT_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_G_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    channel_status: _containers.RepeatedScalarFieldContainer[SocketBase.ChannelState]
    channel_mode: SocketBase.ChannelMode
    channel_normal_state: SocketBase.ChannelNormalState
    impulse_duration: int
    voltage_protection_off: bool
    current_protection_threshold: int
    arming_disarming_actions: SocketBase.ArmingDisarmingActions
    count_protect: int
    subtype: SocketBase.Subtype
    type_g: SocketBase.TypeG
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        channel_status: _Iterable[SocketBase.ChannelState | str] | None = ...,
        channel_mode: SocketBase.ChannelMode | str | None = ...,
        channel_normal_state: SocketBase.ChannelNormalState | str | None = ...,
        impulse_duration: int | None = ...,
        voltage_protection_off: bool = ...,
        current_protection_threshold: int | None = ...,
        arming_disarming_actions: SocketBase.ArmingDisarmingActions
        | _Mapping
        | None = ...,
        count_protect: int | None = ...,
        subtype: SocketBase.Subtype | str | None = ...,
        type_g: SocketBase.TypeG | _Mapping | None = ...,
    ) -> None: ...
