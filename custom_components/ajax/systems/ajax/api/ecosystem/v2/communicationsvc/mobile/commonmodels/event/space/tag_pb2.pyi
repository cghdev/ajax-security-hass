from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class UnknownEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceDuressDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceNightModeOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceNightModeOnWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceNightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceDuressNightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupDuressDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpacePanicButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentPermissionsRequestReceived(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryPermissionsRequestReceived(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedPermanentPermissionsApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedTemporaryPermissionsApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedFullPermissionsRejected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TimezoneChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Added(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Removed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Created(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Deleted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NotifiedAboutRemoving(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupAutoArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupAutoArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceGroupAutoDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceAutoArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceAutoArmedWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceAutoDisarmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinSpaceRequestReceived(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinSpaceRequestDeclined(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExitDelayComplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SpaceEventTag(_message.Message):
    __slots__ = (
        "added",
        "created",
        "deleted",
        "exit_delay_complete",
        "join_space_request_declined",
        "join_space_request_received",
        "notified_about_removing",
        "permanent_permissions_request_received",
        "removed",
        "requested_full_permissions_rejected",
        "requested_permanent_permissions_approved",
        "requested_temporary_permissions_approved",
        "space_armed",
        "space_armed_with_malfunctions",
        "space_auto_armed",
        "space_auto_armed_with_malfunctions",
        "space_auto_disarmed",
        "space_disarmed",
        "space_duress_disarmed",
        "space_duress_night_mode_off",
        "space_group_armed",
        "space_group_armed_with_malfunctions",
        "space_group_auto_armed",
        "space_group_auto_armed_with_malfunctions",
        "space_group_auto_disarmed",
        "space_group_disarmed",
        "space_group_duress_disarmed",
        "space_night_mode_off",
        "space_night_mode_on",
        "space_night_mode_on_with_malfunctions",
        "space_panic_button_pressed",
        "temporary_permissions_request_received",
        "timezone_changed",
        "unknown_event",
    )
    SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_NIGHT_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    SPACE_NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_DISARMED_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_PERMISSIONS_REQUEST_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PERMISSIONS_REQUEST_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PERMANENT_PERMISSIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TEMPORARY_PERMISSIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FULL_PERMISSIONS_REJECTED_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_NIGHT_MODE_ON_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_DURESS_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_DURESS_NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_DURESS_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_PANIC_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    NOTIFIED_ABOUT_REMOVING_FIELD_NUMBER: _ClassVar[int]
    EXIT_DELAY_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_AUTO_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_AUTO_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_GROUP_AUTO_DISARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_AUTO_ARMED_FIELD_NUMBER: _ClassVar[int]
    SPACE_AUTO_ARMED_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPACE_AUTO_DISARMED_FIELD_NUMBER: _ClassVar[int]
    JOIN_SPACE_REQUEST_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    JOIN_SPACE_REQUEST_DECLINED_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EVENT_FIELD_NUMBER: _ClassVar[int]
    space_armed: SpaceArmed
    space_disarmed: SpaceDisarmed
    space_night_mode_on: SpaceNightModeOn
    space_night_mode_off: SpaceNightModeOff
    space_group_armed: SpaceGroupArmed
    space_group_disarmed: SpaceGroupDisarmed
    permanent_permissions_request_received: PermanentPermissionsRequestReceived
    temporary_permissions_request_received: TemporaryPermissionsRequestReceived
    requested_permanent_permissions_approved: RequestedPermanentPermissionsApproved
    requested_temporary_permissions_approved: RequestedTemporaryPermissionsApproved
    requested_full_permissions_rejected: RequestedFullPermissionsRejected
    space_group_armed_with_malfunctions: SpaceGroupArmedWithMalfunctions
    space_armed_with_malfunctions: SpaceArmedWithMalfunctions
    space_night_mode_on_with_malfunctions: SpaceNightModeOnWithMalfunctions
    space_duress_disarmed: SpaceDuressDisarmed
    space_duress_night_mode_off: SpaceDuressNightModeOff
    space_group_duress_disarmed: SpaceGroupDuressDisarmed
    space_panic_button_pressed: SpacePanicButtonPressed
    timezone_changed: TimezoneChanged
    added: Added
    removed: Removed
    created: Created
    deleted: Deleted
    notified_about_removing: NotifiedAboutRemoving
    exit_delay_complete: ExitDelayComplete
    space_group_auto_armed: SpaceGroupAutoArmed
    space_group_auto_armed_with_malfunctions: SpaceGroupAutoArmedWithMalfunctions
    space_group_auto_disarmed: SpaceGroupAutoDisarmed
    space_auto_armed: SpaceAutoArmed
    space_auto_armed_with_malfunctions: SpaceAutoArmedWithMalfunctions
    space_auto_disarmed: SpaceAutoDisarmed
    join_space_request_received: JoinSpaceRequestReceived
    join_space_request_declined: JoinSpaceRequestDeclined
    unknown_event: UnknownEvent
    def __init__(
        self,
        space_armed: SpaceArmed | _Mapping | None = ...,
        space_disarmed: SpaceDisarmed | _Mapping | None = ...,
        space_night_mode_on: SpaceNightModeOn | _Mapping | None = ...,
        space_night_mode_off: SpaceNightModeOff | _Mapping | None = ...,
        space_group_armed: SpaceGroupArmed | _Mapping | None = ...,
        space_group_disarmed: SpaceGroupDisarmed | _Mapping | None = ...,
        permanent_permissions_request_received: PermanentPermissionsRequestReceived
        | _Mapping
        | None = ...,
        temporary_permissions_request_received: TemporaryPermissionsRequestReceived
        | _Mapping
        | None = ...,
        requested_permanent_permissions_approved: RequestedPermanentPermissionsApproved
        | _Mapping
        | None = ...,
        requested_temporary_permissions_approved: RequestedTemporaryPermissionsApproved
        | _Mapping
        | None = ...,
        requested_full_permissions_rejected: RequestedFullPermissionsRejected
        | _Mapping
        | None = ...,
        space_group_armed_with_malfunctions: SpaceGroupArmedWithMalfunctions
        | _Mapping
        | None = ...,
        space_armed_with_malfunctions: SpaceArmedWithMalfunctions
        | _Mapping
        | None = ...,
        space_night_mode_on_with_malfunctions: SpaceNightModeOnWithMalfunctions
        | _Mapping
        | None = ...,
        space_duress_disarmed: SpaceDuressDisarmed | _Mapping | None = ...,
        space_duress_night_mode_off: SpaceDuressNightModeOff | _Mapping | None = ...,
        space_group_duress_disarmed: SpaceGroupDuressDisarmed | _Mapping | None = ...,
        space_panic_button_pressed: SpacePanicButtonPressed | _Mapping | None = ...,
        timezone_changed: TimezoneChanged | _Mapping | None = ...,
        added: Added | _Mapping | None = ...,
        removed: Removed | _Mapping | None = ...,
        created: Created | _Mapping | None = ...,
        deleted: Deleted | _Mapping | None = ...,
        notified_about_removing: NotifiedAboutRemoving | _Mapping | None = ...,
        exit_delay_complete: ExitDelayComplete | _Mapping | None = ...,
        space_group_auto_armed: SpaceGroupAutoArmed | _Mapping | None = ...,
        space_group_auto_armed_with_malfunctions: SpaceGroupAutoArmedWithMalfunctions
        | _Mapping
        | None = ...,
        space_group_auto_disarmed: SpaceGroupAutoDisarmed | _Mapping | None = ...,
        space_auto_armed: SpaceAutoArmed | _Mapping | None = ...,
        space_auto_armed_with_malfunctions: SpaceAutoArmedWithMalfunctions
        | _Mapping
        | None = ...,
        space_auto_disarmed: SpaceAutoDisarmed | _Mapping | None = ...,
        join_space_request_received: JoinSpaceRequestReceived | _Mapping | None = ...,
        join_space_request_declined: JoinSpaceRequestDeclined | _Mapping | None = ...,
        unknown_event: UnknownEvent | _Mapping | None = ...,
    ) -> None: ...
