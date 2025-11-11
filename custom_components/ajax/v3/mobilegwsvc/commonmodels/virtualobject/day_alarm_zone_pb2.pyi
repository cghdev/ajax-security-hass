from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DayAlarmZone(_message.Message):
    __slots__ = (
        "devices_count",
        "id",
        "name",
        "notify_about_deactivation",
        "open_door_alarm",
        "timer",
        "triggers_count",
    )
    class OpenDoorAlarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPEN_DOOR_ALARM_UNSPECIFIED: _ClassVar[DayAlarmZone.OpenDoorAlarm]
        OPEN_DOOR_ALARM_OFF: _ClassVar[DayAlarmZone.OpenDoorAlarm]
        OPEN_DOOR_ALARM_ON: _ClassVar[DayAlarmZone.OpenDoorAlarm]

    OPEN_DOOR_ALARM_UNSPECIFIED: DayAlarmZone.OpenDoorAlarm
    OPEN_DOOR_ALARM_OFF: DayAlarmZone.OpenDoorAlarm
    OPEN_DOOR_ALARM_ON: DayAlarmZone.OpenDoorAlarm
    class NotifyAboutDeactivation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFY_ABOUT_DEACTIVATION_UNSPECIFIED: _ClassVar[
            DayAlarmZone.NotifyAboutDeactivation
        ]
        NOTIFY_ABOUT_DEACTIVATION_FALSE: _ClassVar[DayAlarmZone.NotifyAboutDeactivation]
        NOTIFY_ABOUT_DEACTIVATION_TRUE: _ClassVar[DayAlarmZone.NotifyAboutDeactivation]

    NOTIFY_ABOUT_DEACTIVATION_UNSPECIFIED: DayAlarmZone.NotifyAboutDeactivation
    NOTIFY_ABOUT_DEACTIVATION_FALSE: DayAlarmZone.NotifyAboutDeactivation
    NOTIFY_ABOUT_DEACTIVATION_TRUE: DayAlarmZone.NotifyAboutDeactivation
    class Timer(_message.Message):
        __slots__ = ("bypass_duration",)
        BYPASS_DURATION_FIELD_NUMBER: _ClassVar[int]
        bypass_duration: _duration_pb2.Duration
        def __init__(
            self, bypass_duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    class TriggersCount(_message.Message):
        __slots__ = ("bypass_trigger_count",)
        BYPASS_TRIGGER_COUNT_FIELD_NUMBER: _ClassVar[int]
        bypass_trigger_count: int
        def __init__(self, bypass_trigger_count: int | None = ...) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPEN_DOOR_ALARM_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ABOUT_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    open_door_alarm: DayAlarmZone.OpenDoorAlarm
    notify_about_deactivation: DayAlarmZone.NotifyAboutDeactivation
    devices_count: int
    triggers_count: DayAlarmZone.TriggersCount
    timer: DayAlarmZone.Timer
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        open_door_alarm: DayAlarmZone.OpenDoorAlarm | str | None = ...,
        notify_about_deactivation: DayAlarmZone.NotifyAboutDeactivation
        | str
        | None = ...,
        devices_count: int | None = ...,
        triggers_count: DayAlarmZone.TriggersCount | _Mapping | None = ...,
        timer: DayAlarmZone.Timer | _Mapping | None = ...,
    ) -> None: ...
