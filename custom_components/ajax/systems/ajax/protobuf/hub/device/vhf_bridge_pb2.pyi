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

class VhfBridge(_message.Message):
    __slots__ = (
        "battery_broken",
        "battery_charge_tracking",
        "channels_status",
        "channels_trip",
        "charging",
        "common_part",
        "count_protect",
        "event_ch1",
        "event_ch2",
        "event_ch3",
        "event_ch4",
        "event_ch5",
        "event_ch6",
        "event_ch7",
        "event_ch8",
        "events_state",
        "externally_powered",
        "pause_length",
        "pulse_length",
        "subtype",
    )
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATE_INFO: _ClassVar[VhfBridge.State]
        INACTIVE: _ClassVar[VhfBridge.State]
        ACTIVE: _ClassVar[VhfBridge.State]

    NO_STATE_INFO: VhfBridge.State
    INACTIVE: VhfBridge.State
    ACTIVE: VhfBridge.State
    class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_CONNECTION_TYPE_INFO: _ClassVar[VhfBridge.ConnectionType]
        NEGATIVE: _ClassVar[VhfBridge.ConnectionType]
        POSITIVE: _ClassVar[VhfBridge.ConnectionType]

    NO_CONNECTION_TYPE_INFO: VhfBridge.ConnectionType
    NEGATIVE: VhfBridge.ConnectionType
    POSITIVE: VhfBridge.ConnectionType
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_ASSIGNED_OUTPUT: _ClassVar[VhfBridge.Event]
        INTRUSION_ALARM: _ClassVar[VhfBridge.Event]
        FIRE_ALARM: _ClassVar[VhfBridge.Event]
        MEDICAL_ALARM: _ClassVar[VhfBridge.Event]
        PANIC_ALARM: _ClassVar[VhfBridge.Event]
        ALARM: _ClassVar[VhfBridge.Event]
        MALFUNCTION: _ClassVar[VhfBridge.Event]
        BRIDGE_LOST_EXT_POWER: _ClassVar[VhfBridge.Event]
        BRIDGE_BATTERY_LOW: _ClassVar[VhfBridge.Event]
        HUB_LOST_EXT_POWER: _ClassVar[VhfBridge.Event]
        HUB_BATTERY_LOW: _ClassVar[VhfBridge.Event]
        TAMPER_ALARM: _ClassVar[VhfBridge.Event]
        SECURITY_STATE: _ClassVar[VhfBridge.Event]
        CONFIRMED_ALARM: _ClassVar[VhfBridge.Event]
        CONFIRMED_HU_ALARM: _ClassVar[VhfBridge.Event]
        BRIDGE_JWL_CONN_LOST: _ClassVar[VhfBridge.Event]

    NOT_ASSIGNED_OUTPUT: VhfBridge.Event
    INTRUSION_ALARM: VhfBridge.Event
    FIRE_ALARM: VhfBridge.Event
    MEDICAL_ALARM: VhfBridge.Event
    PANIC_ALARM: VhfBridge.Event
    ALARM: VhfBridge.Event
    MALFUNCTION: VhfBridge.Event
    BRIDGE_LOST_EXT_POWER: VhfBridge.Event
    BRIDGE_BATTERY_LOW: VhfBridge.Event
    HUB_LOST_EXT_POWER: VhfBridge.Event
    HUB_BATTERY_LOW: VhfBridge.Event
    TAMPER_ALARM: VhfBridge.Event
    SECURITY_STATE: VhfBridge.Event
    CONFIRMED_ALARM: VhfBridge.Event
    CONFIRMED_HU_ALARM: VhfBridge.Event
    BRIDGE_JWL_CONN_LOST: VhfBridge.Event
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_STATUS_INFO: _ClassVar[VhfBridge.Status]
        OFF: _ClassVar[VhfBridge.Status]
        ON: _ClassVar[VhfBridge.Status]

    NO_STATUS_INFO: VhfBridge.Status
    OFF: VhfBridge.Status
    ON: VhfBridge.Status
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[VhfBridge.Subtype]

    NO_SUBTYPE: VhfBridge.Subtype
    class ChannelTrip(_message.Message):
        __slots__ = ("channel_id", "connection_type")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        connection_type: VhfBridge.ConnectionType
        def __init__(
            self,
            channel_id: int | None = ...,
            connection_type: VhfBridge.ConnectionType | str | None = ...,
        ) -> None: ...

    class EventState(_message.Message):
        __slots__ = ("event", "state")
        EVENT_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        event: VhfBridge.Event
        state: VhfBridge.State
        def __init__(
            self,
            event: VhfBridge.Event | str | None = ...,
            state: VhfBridge.State | str | None = ...,
        ) -> None: ...

    class ChannelStatus(_message.Message):
        __slots__ = ("channel_id", "status")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        channel_id: int
        status: VhfBridge.Status
        def __init__(
            self,
            channel_id: int | None = ...,
            status: VhfBridge.Status | str | None = ...,
        ) -> None: ...

    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_POWERED_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH1_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH2_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH3_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH4_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH5_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH6_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH7_FIELD_NUMBER: _ClassVar[int]
    EVENT_CH8_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_TRIP_FIELD_NUMBER: _ClassVar[int]
    PULSE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PAUSE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    COUNT_PROTECT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_STATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHARGING_FIELD_NUMBER: _ClassVar[int]
    BATTERY_BROKEN_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGE_TRACKING_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    externally_powered: _wrappers_pb2.BoolValue
    event_ch1: VhfBridge.Event
    event_ch2: VhfBridge.Event
    event_ch3: VhfBridge.Event
    event_ch4: VhfBridge.Event
    event_ch5: VhfBridge.Event
    event_ch6: VhfBridge.Event
    event_ch7: VhfBridge.Event
    event_ch8: VhfBridge.Event
    channels_trip: _containers.RepeatedCompositeFieldContainer[VhfBridge.ChannelTrip]
    pulse_length: int
    pause_length: int
    count_protect: int
    events_state: _containers.RepeatedCompositeFieldContainer[VhfBridge.EventState]
    channels_status: _containers.RepeatedCompositeFieldContainer[
        VhfBridge.ChannelStatus
    ]
    charging: _wrappers_pb2.BoolValue
    battery_broken: _wrappers_pb2.BoolValue
    battery_charge_tracking: bool
    subtype: VhfBridge.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        externally_powered: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        event_ch1: VhfBridge.Event | str | None = ...,
        event_ch2: VhfBridge.Event | str | None = ...,
        event_ch3: VhfBridge.Event | str | None = ...,
        event_ch4: VhfBridge.Event | str | None = ...,
        event_ch5: VhfBridge.Event | str | None = ...,
        event_ch6: VhfBridge.Event | str | None = ...,
        event_ch7: VhfBridge.Event | str | None = ...,
        event_ch8: VhfBridge.Event | str | None = ...,
        channels_trip: _Iterable[VhfBridge.ChannelTrip | _Mapping] | None = ...,
        pulse_length: int | None = ...,
        pause_length: int | None = ...,
        count_protect: int | None = ...,
        events_state: _Iterable[VhfBridge.EventState | _Mapping] | None = ...,
        channels_status: _Iterable[VhfBridge.ChannelStatus | _Mapping] | None = ...,
        charging: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        battery_broken: _wrappers_pb2.BoolValue | _Mapping | None = ...,
        battery_charge_tracking: bool = ...,
        subtype: VhfBridge.Subtype | str | None = ...,
    ) -> None: ...
