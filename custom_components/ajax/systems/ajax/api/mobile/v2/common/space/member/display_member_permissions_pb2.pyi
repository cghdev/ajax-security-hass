from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DisplaySpaceMemberSpacePermission(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_UNSPECIFIED: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_PRIVACY_SETTINGS_MANAGEMENT: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_SECURITY_MODE_CHANGE: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_PANIC: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_NIGHT_MODE: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_VIEW_DEVICES_AND_ROOMS: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_VIEW_NOTIFICATIONS: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]
    DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_SYSTEM_SETTINGS: _ClassVar[
        DisplaySpaceMemberSpacePermission
    ]

class DisplaySpaceMemberDayAlarmPermission(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_UNSPECIFIED: _ClassVar[
        DisplaySpaceMemberDayAlarmPermission
    ]
    DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_NONE: _ClassVar[
        DisplaySpaceMemberDayAlarmPermission
    ]
    DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_TEMPORARY_BYPASS: _ClassVar[
        DisplaySpaceMemberDayAlarmPermission
    ]
    DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_PERMANENT_BYPASS: _ClassVar[
        DisplaySpaceMemberDayAlarmPermission
    ]

class DisplaySpaceMemberHubPermission(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_UNSPECIFIED: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_HOME_AUTOMATION_CONTROLS: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_CHIME_ACTIVATION: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_SECURITY_MANAGEMENT_VIA_BLUETOOTH: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_FIRE_ALARM_MUTING: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_CAMERA_WATCH: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_START_BUKHOOR: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_FW_UPDATE: _ClassVar[
        DisplaySpaceMemberHubPermission
    ]

class DisplaySpaceMemberHubPermissionExtended(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_EXTENDED_UNSPECIFIED: _ClassVar[
        DisplaySpaceMemberHubPermissionExtended
    ]
    DISPLAY_SPACE_MEMBER_HUB_PERMISSION_EXTENDED_ACCESS_LEVEL_2: _ClassVar[
        DisplaySpaceMemberHubPermissionExtended
    ]

DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_UNSPECIFIED: DisplaySpaceMemberSpacePermission
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_PRIVACY_SETTINGS_MANAGEMENT: (
    DisplaySpaceMemberSpacePermission
)
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_SECURITY_MODE_CHANGE: (
    DisplaySpaceMemberSpacePermission
)
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_PANIC: DisplaySpaceMemberSpacePermission
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_NIGHT_MODE: DisplaySpaceMemberSpacePermission
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_VIEW_DEVICES_AND_ROOMS: (
    DisplaySpaceMemberSpacePermission
)
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_VIEW_NOTIFICATIONS: (
    DisplaySpaceMemberSpacePermission
)
DISPLAY_SPACE_MEMBER_SPACE_PERMISSION_SYSTEM_SETTINGS: DisplaySpaceMemberSpacePermission
DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_UNSPECIFIED: (
    DisplaySpaceMemberDayAlarmPermission
)
DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_NONE: DisplaySpaceMemberDayAlarmPermission
DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_TEMPORARY_BYPASS: (
    DisplaySpaceMemberDayAlarmPermission
)
DISPLAY_SPACE_MEMBER_DAY_ALARM_PERMISSION_PERMANENT_BYPASS: (
    DisplaySpaceMemberDayAlarmPermission
)
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_UNSPECIFIED: DisplaySpaceMemberHubPermission
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_HOME_AUTOMATION_CONTROLS: (
    DisplaySpaceMemberHubPermission
)
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_CHIME_ACTIVATION: DisplaySpaceMemberHubPermission
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_SECURITY_MANAGEMENT_VIA_BLUETOOTH: (
    DisplaySpaceMemberHubPermission
)
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_FIRE_ALARM_MUTING: DisplaySpaceMemberHubPermission
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_CAMERA_WATCH: DisplaySpaceMemberHubPermission
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_START_BUKHOOR: DisplaySpaceMemberHubPermission
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_FW_UPDATE: DisplaySpaceMemberHubPermission
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_EXTENDED_UNSPECIFIED: (
    DisplaySpaceMemberHubPermissionExtended
)
DISPLAY_SPACE_MEMBER_HUB_PERMISSION_EXTENDED_ACCESS_LEVEL_2: (
    DisplaySpaceMemberHubPermissionExtended
)

class DisplayMemberPermissions(_message.Message):
    __slots__ = (
        "day_alarm_permission",
        "hub_permissions",
        "hub_permissions_extended",
        "space_permissions",
    )
    SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_PERMISSIONS_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    space_permissions: _containers.RepeatedScalarFieldContainer[
        DisplaySpaceMemberSpacePermission
    ]
    hub_permissions: _containers.RepeatedScalarFieldContainer[
        DisplaySpaceMemberHubPermission
    ]
    hub_permissions_extended: _containers.RepeatedScalarFieldContainer[
        DisplaySpaceMemberHubPermissionExtended
    ]
    day_alarm_permission: DisplaySpaceMemberDayAlarmPermission
    def __init__(
        self,
        space_permissions: _Iterable[DisplaySpaceMemberSpacePermission | str]
        | None = ...,
        hub_permissions: _Iterable[DisplaySpaceMemberHubPermission | str] | None = ...,
        hub_permissions_extended: _Iterable[
            DisplaySpaceMemberHubPermissionExtended | str
        ]
        | None = ...,
        day_alarm_permission: DisplaySpaceMemberDayAlarmPermission | str | None = ...,
    ) -> None: ...
