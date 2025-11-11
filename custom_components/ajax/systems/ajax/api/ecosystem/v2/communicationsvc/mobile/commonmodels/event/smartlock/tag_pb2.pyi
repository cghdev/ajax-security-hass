from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Added(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Removed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedManually(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByExternalUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedBySpaceMember(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockingFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DoorbellPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedAutomatically(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByKeypad(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadTemporarilyDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockedByMatter(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockEventTag(_message.Message):
    __slots__ = (
        "added",
        "battery_low",
        "connection_loss",
        "doorbell_pressed",
        "keypad_temporarily_disabled",
        "locked_automatically",
        "locked_by_external_user",
        "locked_by_keypad",
        "locked_by_matter",
        "locked_by_scenario",
        "locked_by_space_member",
        "locked_manually",
        "locking_failed",
        "removed",
    )
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_MANUALLY_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_EXTERNAL_USER_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    LOCKING_FAILED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    DOORBELL_PRESSED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_KEYPAD_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_TEMPORARILY_DISABLED_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BY_MATTER_FIELD_NUMBER: _ClassVar[int]
    added: Added
    removed: Removed
    connection_loss: ConnectionLoss
    locked_manually: LockedManually
    locked_by_external_user: LockedByExternalUser
    locked_by_space_member: LockedBySpaceMember
    locked_by_scenario: LockedByScenario
    locking_failed: LockingFailed
    battery_low: BatteryLow
    doorbell_pressed: DoorbellPressed
    locked_automatically: LockedAutomatically
    locked_by_keypad: LockedByKeypad
    keypad_temporarily_disabled: KeypadTemporarilyDisabled
    locked_by_matter: LockedByMatter
    def __init__(
        self,
        added: Added | _Mapping | None = ...,
        removed: Removed | _Mapping | None = ...,
        connection_loss: ConnectionLoss | _Mapping | None = ...,
        locked_manually: LockedManually | _Mapping | None = ...,
        locked_by_external_user: LockedByExternalUser | _Mapping | None = ...,
        locked_by_space_member: LockedBySpaceMember | _Mapping | None = ...,
        locked_by_scenario: LockedByScenario | _Mapping | None = ...,
        locking_failed: LockingFailed | _Mapping | None = ...,
        battery_low: BatteryLow | _Mapping | None = ...,
        doorbell_pressed: DoorbellPressed | _Mapping | None = ...,
        locked_automatically: LockedAutomatically | _Mapping | None = ...,
        locked_by_keypad: LockedByKeypad | _Mapping | None = ...,
        keypad_temporarily_disabled: KeypadTemporarilyDisabled | _Mapping | None = ...,
        locked_by_matter: LockedByMatter | _Mapping | None = ...,
    ) -> None: ...
