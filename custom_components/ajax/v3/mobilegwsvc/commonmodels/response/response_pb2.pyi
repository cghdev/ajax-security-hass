from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_TYPE_UNSPECIFIED: _ClassVar[UpdateType]
    UPDATE_TYPE_ADD: _ClassVar[UpdateType]
    UPDATE_TYPE_UPDATE: _ClassVar[UpdateType]
    UPDATE_TYPE_REMOVE: _ClassVar[UpdateType]

UPDATE_TYPE_UNSPECIFIED: UpdateType
UPDATE_TYPE_ADD: UpdateType
UPDATE_TYPE_UPDATE: UpdateType
UPDATE_TYPE_REMOVE: UpdateType

class Error(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Success(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HubBusyError(_message.Message):
    __slots__ = ("error_cause",)
    ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
    error_cause: ErrorCause
    def __init__(self, error_cause: ErrorCause | _Mapping | None = ...) -> None: ...

class HubWrongStateError(_message.Message):
    __slots__ = ("error_cause",)
    ERROR_CAUSE_FIELD_NUMBER: _ClassVar[int]
    error_cause: ErrorCause
    def __init__(self, error_cause: ErrorCause | _Mapping | None = ...) -> None: ...

class ErrorCause(_message.Message):
    __slots__ = (
        "active_call",
        "armed",
        "battery_low",
        "buses_problem",
        "card_process",
        "dev_always_active",
        "dev_busy",
        "dev_bypassed",
        "dev_offline",
        "dev_power_overload",
        "dev_zone_test",
        "dfu_in_progress",
        "exit_timer",
        "ext_power",
        "extra_comm_chan_required",
        "fp_bukhoor_forbidden_time",
        "fp_fire_alarm",
        "hub_pwr_test",
        "hub_scan",
        "in_lines_short_circuit",
        "iwh_objects_limit_error",
        "iwh_test_in_progress",
        "jamming_detected",
        "not_supported",
        "out_lines_short_circuit",
        "radiotest",
        "ring_disconnected",
        "ring_problem",
        "ring_unregistered",
        "route",
        "source",
        "walk_test_in_progress",
        "wifi_func_not_work",
        "wrong_power_supply_settings",
    )
    class Source(_message.Message):
        __slots__ = ("device_hex_id", "object_type")
        DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_hex_id: str
        object_type: _object_type_pb2.ObjectType
        def __init__(
            self,
            device_hex_id: str | None = ...,
            object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        ) -> None: ...

    HUB_SCAN_FIELD_NUMBER: _ClassVar[int]
    HUB_PWR_TEST_FIELD_NUMBER: _ClassVar[int]
    DEV_BUSY_FIELD_NUMBER: _ClassVar[int]
    DFU_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RADIOTEST_FIELD_NUMBER: _ClassVar[int]
    DEV_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    CARD_PROCESS_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    EXIT_TIMER_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    DEV_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    EXT_POWER_FIELD_NUMBER: _ClassVar[int]
    DEV_ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BUSES_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    IWH_OBJECTS_LIMIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    IWH_TEST_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RING_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    RING_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    RING_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CALL_FIELD_NUMBER: _ClassVar[int]
    FP_BUKHOOR_FORBIDDEN_TIME_FIELD_NUMBER: _ClassVar[int]
    FP_FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    DEV_BYPASSED_FIELD_NUMBER: _ClassVar[int]
    WRONG_POWER_SUPPLY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IN_LINES_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    OUT_LINES_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    WIFI_FUNC_NOT_WORK_FIELD_NUMBER: _ClassVar[int]
    DEV_POWER_OVERLOAD_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COMM_CHAN_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    JAMMING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    WALK_TEST_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    hub_scan: Error
    hub_pwr_test: Error
    dev_busy: Error
    dfu_in_progress: Error
    radiotest: Error
    dev_zone_test: Error
    card_process: Error
    armed: Error
    exit_timer: Error
    route: Error
    dev_offline: Error
    ext_power: Error
    dev_always_active: Error
    not_supported: Error
    buses_problem: Error
    iwh_objects_limit_error: Error
    iwh_test_in_progress: Error
    ring_problem: Error
    ring_unregistered: Error
    ring_disconnected: Error
    active_call: Error
    fp_bukhoor_forbidden_time: Error
    fp_fire_alarm: Error
    dev_bypassed: Error
    wrong_power_supply_settings: Error
    in_lines_short_circuit: Error
    out_lines_short_circuit: Error
    wifi_func_not_work: Error
    dev_power_overload: Error
    battery_low: Error
    extra_comm_chan_required: Error
    jamming_detected: Error
    walk_test_in_progress: Error
    source: ErrorCause.Source
    def __init__(
        self,
        hub_scan: Error | _Mapping | None = ...,
        hub_pwr_test: Error | _Mapping | None = ...,
        dev_busy: Error | _Mapping | None = ...,
        dfu_in_progress: Error | _Mapping | None = ...,
        radiotest: Error | _Mapping | None = ...,
        dev_zone_test: Error | _Mapping | None = ...,
        card_process: Error | _Mapping | None = ...,
        armed: Error | _Mapping | None = ...,
        exit_timer: Error | _Mapping | None = ...,
        route: Error | _Mapping | None = ...,
        dev_offline: Error | _Mapping | None = ...,
        ext_power: Error | _Mapping | None = ...,
        dev_always_active: Error | _Mapping | None = ...,
        not_supported: Error | _Mapping | None = ...,
        buses_problem: Error | _Mapping | None = ...,
        iwh_objects_limit_error: Error | _Mapping | None = ...,
        iwh_test_in_progress: Error | _Mapping | None = ...,
        ring_problem: Error | _Mapping | None = ...,
        ring_unregistered: Error | _Mapping | None = ...,
        ring_disconnected: Error | _Mapping | None = ...,
        active_call: Error | _Mapping | None = ...,
        fp_bukhoor_forbidden_time: Error | _Mapping | None = ...,
        fp_fire_alarm: Error | _Mapping | None = ...,
        dev_bypassed: Error | _Mapping | None = ...,
        wrong_power_supply_settings: Error | _Mapping | None = ...,
        in_lines_short_circuit: Error | _Mapping | None = ...,
        out_lines_short_circuit: Error | _Mapping | None = ...,
        wifi_func_not_work: Error | _Mapping | None = ...,
        dev_power_overload: Error | _Mapping | None = ...,
        battery_low: Error | _Mapping | None = ...,
        extra_comm_chan_required: Error | _Mapping | None = ...,
        jamming_detected: Error | _Mapping | None = ...,
        walk_test_in_progress: Error | _Mapping | None = ...,
        source: ErrorCause.Source | _Mapping | None = ...,
    ) -> None: ...
