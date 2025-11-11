from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import (
    day_alarm_zone_pb2 as _day_alarm_zone_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDayAlarmZonesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("created", "deleted", "snapshot", "updated")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDayAlarmZonesResponse.Snapshot
        created: StreamDayAlarmZonesResponse.Created
        updated: StreamDayAlarmZonesResponse.Updated
        deleted: StreamDayAlarmZonesResponse.Deleted
        def __init__(
            self,
            snapshot: StreamDayAlarmZonesResponse.Snapshot | _Mapping | None = ...,
            created: StreamDayAlarmZonesResponse.Created | _Mapping | None = ...,
            updated: StreamDayAlarmZonesResponse.Updated | _Mapping | None = ...,
            deleted: StreamDayAlarmZonesResponse.Deleted | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    class Snapshot(_message.Message):
        __slots__ = ("day_alarm_zones", "is_add_available", "is_cms_on")
        IS_ADD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        IS_CMS_ON_FIELD_NUMBER: _ClassVar[int]
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        is_add_available: bool
        is_cms_on: bool
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[
            _day_alarm_zone_pb2.DayAlarmZone
        ]
        def __init__(
            self,
            is_add_available: bool = ...,
            is_cms_on: bool = ...,
            day_alarm_zones: _Iterable[_day_alarm_zone_pb2.DayAlarmZone | _Mapping]
            | None = ...,
        ) -> None: ...

    class Created(_message.Message):
        __slots__ = ("day_alarm_zones", "is_add_available")
        IS_ADD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        is_add_available: bool
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[
            _day_alarm_zone_pb2.DayAlarmZone
        ]
        def __init__(
            self,
            is_add_available: bool = ...,
            day_alarm_zones: _Iterable[_day_alarm_zone_pb2.DayAlarmZone | _Mapping]
            | None = ...,
        ) -> None: ...

    class Updated(_message.Message):
        __slots__ = ("day_alarm_zones",)
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[
            _day_alarm_zone_pb2.DayAlarmZone
        ]
        def __init__(
            self,
            day_alarm_zones: _Iterable[_day_alarm_zone_pb2.DayAlarmZone | _Mapping]
            | None = ...,
        ) -> None: ...

    class Deleted(_message.Message):
        __slots__ = ("day_alarm_zones", "is_add_available")
        IS_ADD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DAY_ALARM_ZONES_FIELD_NUMBER: _ClassVar[int]
        is_add_available: bool
        day_alarm_zones: _containers.RepeatedCompositeFieldContainer[
            _day_alarm_zone_pb2.DayAlarmZone
        ]
        def __init__(
            self,
            is_add_available: bool = ...,
            day_alarm_zones: _Iterable[_day_alarm_zone_pb2.DayAlarmZone | _Mapping]
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDayAlarmZonesResponse.Success
    failure: StreamDayAlarmZonesResponse.Failure
    def __init__(
        self,
        success: StreamDayAlarmZonesResponse.Success | _Mapping | None = ...,
        failure: StreamDayAlarmZonesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
