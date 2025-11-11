from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateUserDayAlarmZonePermissionRequest(_message.Message):
    __slots__ = ("day_alarm_permission", "hub_id", "user_id")
    class DayAlarmPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DAY_ALARM_PERMISSION_UNSPECIFIED: _ClassVar[
            UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
        ]
        DAY_ALARM_PERMISSION_NONE: _ClassVar[
            UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
        ]
        DAY_ALARM_PERMISSION_TEMPORARY_BYPASS: _ClassVar[
            UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
        ]
        DAY_ALARM_PERMISSION_PERMANENT_BYPASS: _ClassVar[
            UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
        ]

    DAY_ALARM_PERMISSION_UNSPECIFIED: (
        UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
    )
    DAY_ALARM_PERMISSION_NONE: (
        UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
    )
    DAY_ALARM_PERMISSION_TEMPORARY_BYPASS: (
        UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
    )
    DAY_ALARM_PERMISSION_PERMANENT_BYPASS: (
        UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
    )
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    user_id: str
    day_alarm_permission: UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
    def __init__(
        self,
        hub_id: str | None = ...,
        user_id: str | None = ...,
        day_alarm_permission: UpdateUserDayAlarmZonePermissionRequest.DayAlarmPermission
        | str
        | None = ...,
    ) -> None: ...
