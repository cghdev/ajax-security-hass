from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.type import dayofweek_pb2 as _dayofweek_pb2
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduledAccess(_message.Message):
    __slots__ = (
        "enabled",
        "id",
        "name",
        "notification_enabled",
        "schedules",
        "targets",
    )
    class Target(_message.Message):
        __slots__ = ("device_id", "device_type")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        device_type: _object_type_pb2.ObjectType
        def __init__(
            self,
            device_id: str | None = ...,
            device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        ) -> None: ...

    class Schedule(_message.Message):
        __slots__ = (
            "end_hour",
            "end_minute",
            "is_active",
            "start_hour",
            "start_minute",
            "week_days",
        )
        WEEK_DAYS_FIELD_NUMBER: _ClassVar[int]
        START_HOUR_FIELD_NUMBER: _ClassVar[int]
        START_MINUTE_FIELD_NUMBER: _ClassVar[int]
        END_HOUR_FIELD_NUMBER: _ClassVar[int]
        END_MINUTE_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        week_days: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
        start_hour: int
        start_minute: int
        end_hour: int
        end_minute: int
        is_active: bool
        def __init__(
            self,
            week_days: _Iterable[_dayofweek_pb2.DayOfWeek | str] | None = ...,
            start_hour: int | None = ...,
            start_minute: int | None = ...,
            end_hour: int | None = ...,
            end_minute: int | None = ...,
            is_active: bool = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    targets: _containers.RepeatedCompositeFieldContainer[ScheduledAccess.Target]
    schedules: _containers.RepeatedCompositeFieldContainer[ScheduledAccess.Schedule]
    enabled: bool
    notification_enabled: bool
    def __init__(
        self,
        id: int | None = ...,
        name: str | None = ...,
        targets: _Iterable[ScheduledAccess.Target | _Mapping] | None = ...,
        schedules: _Iterable[ScheduledAccess.Schedule | _Mapping] | None = ...,
        enabled: bool = ...,
        notification_enabled: bool = ...,
    ) -> None: ...
