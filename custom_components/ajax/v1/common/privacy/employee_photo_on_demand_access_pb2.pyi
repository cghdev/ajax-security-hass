from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v1.common.privacy import (
    photo_on_demand_devices_pb2 as _photo_on_demand_devices_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class EmployeePhotoOnDemandAccess(_message.Message):
    __slots__ = (
        "after_alarm",
        "allowed_always",
        "employee_event_photos_access",
        "not_allowed",
        "when_armed",
    )
    class NotAllowed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class AllowedAlways(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
        def __init__(
            self,
            devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
            | _Mapping
            | None = ...,
        ) -> None: ...

    class WhenArmed(_message.Message):
        __slots__ = ("allowed", "forbidden")
        class Allowed(_message.Message):
            __slots__ = ("devices",)
            DEVICES_FIELD_NUMBER: _ClassVar[int]
            devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
            def __init__(
                self,
                devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
                | _Mapping
                | None = ...,
            ) -> None: ...

        class ForbiddenUntilArmed(_message.Message):
            __slots__ = ("devices",)
            DEVICES_FIELD_NUMBER: _ClassVar[int]
            devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
            def __init__(
                self,
                devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
                | _Mapping
                | None = ...,
            ) -> None: ...

        ALLOWED_FIELD_NUMBER: _ClassVar[int]
        FORBIDDEN_FIELD_NUMBER: _ClassVar[int]
        allowed: EmployeePhotoOnDemandAccess.WhenArmed.Allowed
        forbidden: EmployeePhotoOnDemandAccess.WhenArmed.ForbiddenUntilArmed
        def __init__(
            self,
            allowed: EmployeePhotoOnDemandAccess.WhenArmed.Allowed
            | _Mapping
            | None = ...,
            forbidden: EmployeePhotoOnDemandAccess.WhenArmed.ForbiddenUntilArmed
            | _Mapping
            | None = ...,
        ) -> None: ...

    class AfterAlarm(_message.Message):
        __slots__ = (
            "capture_photo_available_until",
            "configured_time_to_capture_photo_minutes",
            "devices",
        )
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_PHOTO_AVAILABLE_UNTIL_FIELD_NUMBER: _ClassVar[int]
        CONFIGURED_TIME_TO_CAPTURE_PHOTO_MINUTES_FIELD_NUMBER: _ClassVar[int]
        devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
        capture_photo_available_until: _timestamp_pb2.Timestamp
        configured_time_to_capture_photo_minutes: _wrappers_pb2.UInt32Value
        def __init__(
            self,
            devices: _photo_on_demand_devices_pb2.PhotoOnDemandDevices
            | _Mapping
            | None = ...,
            capture_photo_available_until: _timestamp_pb2.Timestamp
            | _Mapping
            | None = ...,
            configured_time_to_capture_photo_minutes: _wrappers_pb2.UInt32Value
            | _Mapping
            | None = ...,
        ) -> None: ...

    class EmployeeEventPhotosAccess(_message.Message):
        __slots__ = ("event_photos_accesses",)
        class EventPhotosAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EVENT_PHOTOS_ACCESS_UNSPECIFIED: _ClassVar[
                EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
            ]
            EVENT_PHOTOS_ACCESS_PHOTO_ON_DEMAND: _ClassVar[
                EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
            ]
            EVENT_PHOTOS_ACCESS_PHOTO_BY_ALARM_SCENARIO: _ClassVar[
                EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
            ]

        EVENT_PHOTOS_ACCESS_UNSPECIFIED: (
            EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
        )
        EVENT_PHOTOS_ACCESS_PHOTO_ON_DEMAND: (
            EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
        )
        EVENT_PHOTOS_ACCESS_PHOTO_BY_ALARM_SCENARIO: (
            EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
        )
        EVENT_PHOTOS_ACCESSES_FIELD_NUMBER: _ClassVar[int]
        event_photos_accesses: _containers.RepeatedScalarFieldContainer[
            EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
        ]
        def __init__(
            self,
            event_photos_accesses: _Iterable[
                EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess.EventPhotosAccess
                | str
            ]
            | None = ...,
        ) -> None: ...

    EMPLOYEE_EVENT_PHOTOS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    NOT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ALWAYS_FIELD_NUMBER: _ClassVar[int]
    WHEN_ARMED_FIELD_NUMBER: _ClassVar[int]
    AFTER_ALARM_FIELD_NUMBER: _ClassVar[int]
    employee_event_photos_access: EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess
    not_allowed: EmployeePhotoOnDemandAccess.NotAllowed
    allowed_always: EmployeePhotoOnDemandAccess.AllowedAlways
    when_armed: EmployeePhotoOnDemandAccess.WhenArmed
    after_alarm: EmployeePhotoOnDemandAccess.AfterAlarm
    def __init__(
        self,
        employee_event_photos_access: EmployeePhotoOnDemandAccess.EmployeeEventPhotosAccess
        | _Mapping
        | None = ...,
        not_allowed: EmployeePhotoOnDemandAccess.NotAllowed | _Mapping | None = ...,
        allowed_always: EmployeePhotoOnDemandAccess.AllowedAlways
        | _Mapping
        | None = ...,
        when_armed: EmployeePhotoOnDemandAccess.WhenArmed | _Mapping | None = ...,
        after_alarm: EmployeePhotoOnDemandAccess.AfterAlarm | _Mapping | None = ...,
    ) -> None: ...
