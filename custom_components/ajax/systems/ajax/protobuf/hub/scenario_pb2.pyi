from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2
from systems.ajax.protobuf.hub import object_type_pb2 as _object_type_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Scenario(_message.Message):
    __slots__ = (
        "alarm_sources",
        "enabled",
        "id",
        "name",
        "schedules",
        "source_condition",
        "source_type",
        "target_action",
        "target_condition",
        "targets",
        "time_before_action",
    )
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SOURCE_TYPE: _ClassVar[Scenario.SourceType]
        INSTRUCTION_FIRE_LEAK: _ClassVar[Scenario.SourceType]
        SCHEDULE: _ClassVar[Scenario.SourceType]
        BUTTON: _ClassVar[Scenario.SourceType]

    NO_SOURCE_TYPE: Scenario.SourceType
    INSTRUCTION_FIRE_LEAK: Scenario.SourceType
    SCHEDULE: Scenario.SourceType
    BUTTON: Scenario.SourceType
    class SourceCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SOURCE_CONDITION: _ClassVar[Scenario.SourceCondition]
        OR: _ClassVar[Scenario.SourceCondition]
        AND: _ClassVar[Scenario.SourceCondition]

    NO_SOURCE_CONDITION: Scenario.SourceCondition
    OR: Scenario.SourceCondition
    AND: Scenario.SourceCondition
    class TargetAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TARGET_ACTION: _ClassVar[Scenario.TargetAction]
        OFF: _ClassVar[Scenario.TargetAction]
        ON: _ClassVar[Scenario.TargetAction]
        CHANGE_STAGE: _ClassVar[Scenario.TargetAction]
        DISARM: _ClassVar[Scenario.TargetAction]
        ARM: _ClassVar[Scenario.TargetAction]
        DISARM_NIGHT_MODE: _ClassVar[Scenario.TargetAction]
        ARM_NIGHT_MODE: _ClassVar[Scenario.TargetAction]
        MAKE_PHOTO: _ClassVar[Scenario.TargetAction]

    NO_TARGET_ACTION: Scenario.TargetAction
    OFF: Scenario.TargetAction
    ON: Scenario.TargetAction
    CHANGE_STAGE: Scenario.TargetAction
    DISARM: Scenario.TargetAction
    ARM: Scenario.TargetAction
    DISARM_NIGHT_MODE: Scenario.TargetAction
    ARM_NIGHT_MODE: Scenario.TargetAction
    MAKE_PHOTO: Scenario.TargetAction
    class TargetCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_TARGET_CONDITION_INFO: _ClassVar[Scenario.TargetCondition]
        ON_DEVICE_ARM: _ClassVar[Scenario.TargetCondition]
        ON_DEVICE_DISARM: _ClassVar[Scenario.TargetCondition]

    NO_TARGET_CONDITION_INFO: Scenario.TargetCondition
    ON_DEVICE_ARM: Scenario.TargetCondition
    ON_DEVICE_DISARM: Scenario.TargetCondition
    class AlarmSource(_message.Message):
        __slots__ = ("source_event_number", "source_id", "source_object_type")
        SOURCE_EVENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SOURCE_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        source_event_number: int
        source_object_type: _object_type_pb2.ObjectType
        source_id: str
        def __init__(
            self,
            source_event_number: int | None = ...,
            source_object_type: _object_type_pb2.ObjectType | str | None = ...,
            source_id: str | None = ...,
        ) -> None: ...

    class Target(_message.Message):
        __slots__ = ("target_id", "target_object_type")
        TARGET_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        target_object_type: _object_type_pb2.ObjectType
        target_id: str
        def __init__(
            self,
            target_object_type: _object_type_pb2.ObjectType | str | None = ...,
            target_id: str | None = ...,
        ) -> None: ...

    class Schedule(_message.Message):
        __slots__ = (
            "enabled",
            "hours",
            "id",
            "last_run_utc",
            "minutes",
            "scenario_bits",
            "week_days",
        )
        class WeekDays(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_WEEK_DAYS_INFO: _ClassVar[Scenario.Schedule.WeekDays]
            SUNDAY: _ClassVar[Scenario.Schedule.WeekDays]
            MONDAY: _ClassVar[Scenario.Schedule.WeekDays]
            TUESDAY: _ClassVar[Scenario.Schedule.WeekDays]
            WEDNESDAY: _ClassVar[Scenario.Schedule.WeekDays]
            THURSDAY: _ClassVar[Scenario.Schedule.WeekDays]
            FRIDAY: _ClassVar[Scenario.Schedule.WeekDays]
            SATURDAY: _ClassVar[Scenario.Schedule.WeekDays]

        NO_WEEK_DAYS_INFO: Scenario.Schedule.WeekDays
        SUNDAY: Scenario.Schedule.WeekDays
        MONDAY: Scenario.Schedule.WeekDays
        TUESDAY: Scenario.Schedule.WeekDays
        WEDNESDAY: Scenario.Schedule.WeekDays
        THURSDAY: Scenario.Schedule.WeekDays
        FRIDAY: Scenario.Schedule.WeekDays
        SATURDAY: Scenario.Schedule.WeekDays
        ID_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        WEEK_DAYS_FIELD_NUMBER: _ClassVar[int]
        HOURS_FIELD_NUMBER: _ClassVar[int]
        MINUTES_FIELD_NUMBER: _ClassVar[int]
        LAST_RUN_UTC_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_BITS_FIELD_NUMBER: _ClassVar[int]
        id: str
        enabled: bool
        week_days: _containers.RepeatedScalarFieldContainer[Scenario.Schedule.WeekDays]
        hours: int
        minutes: int
        last_run_utc: int
        scenario_bits: int
        def __init__(
            self,
            id: str | None = ...,
            enabled: bool = ...,
            week_days: _Iterable[Scenario.Schedule.WeekDays | str] | None = ...,
            hours: int | None = ...,
            minutes: int | None = ...,
            last_run_utc: int | None = ...,
            scenario_bits: int | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ACTION_FIELD_NUMBER: _ClassVar[int]
    TIME_BEFORE_ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ALARM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    enabled: bool
    source_type: Scenario.SourceType
    source_condition: Scenario.SourceCondition
    target_action: Scenario.TargetAction
    time_before_action: int
    target_condition: _containers.RepeatedScalarFieldContainer[Scenario.TargetCondition]
    alarm_sources: _containers.RepeatedCompositeFieldContainer[Scenario.AlarmSource]
    targets: _containers.RepeatedCompositeFieldContainer[Scenario.Target]
    schedules: _containers.RepeatedCompositeFieldContainer[Scenario.Schedule]
    def __init__(
        self,
        id: str | None = ...,
        name: _name_pb2.Name | _Mapping | None = ...,
        enabled: bool = ...,
        source_type: Scenario.SourceType | str | None = ...,
        source_condition: Scenario.SourceCondition | str | None = ...,
        target_action: Scenario.TargetAction | str | None = ...,
        time_before_action: int | None = ...,
        target_condition: _Iterable[Scenario.TargetCondition | str] | None = ...,
        alarm_sources: _Iterable[Scenario.AlarmSource | _Mapping] | None = ...,
        targets: _Iterable[Scenario.Target | _Mapping] | None = ...,
        schedules: _Iterable[Scenario.Schedule | _Mapping] | None = ...,
    ) -> None: ...
