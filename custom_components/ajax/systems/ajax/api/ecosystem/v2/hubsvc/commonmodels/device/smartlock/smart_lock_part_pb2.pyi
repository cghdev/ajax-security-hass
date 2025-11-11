from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    patch_type_pb2 as _patch_type_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_chimes_pb2 as _device_chimes_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockPart(_message.Message):
    __slots__ = (
        "arming_actions",
        "autolock",
        "door_open_device_chimes",
        "door_open_too_long_alarm_delay",
        "door_status",
        "hardware_error",
        "lock_status",
    )
    class DoorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOOR_STATUS_UNSPECIFIED: _ClassVar[SmartLockPart.DoorStatus]
        DOOR_STATUS_CLOSED: _ClassVar[SmartLockPart.DoorStatus]
        DOOR_STATUS_OPEN: _ClassVar[SmartLockPart.DoorStatus]

    DOOR_STATUS_UNSPECIFIED: SmartLockPart.DoorStatus
    DOOR_STATUS_CLOSED: SmartLockPart.DoorStatus
    DOOR_STATUS_OPEN: SmartLockPart.DoorStatus
    class LockStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCK_STATUS_UNSPECIFIED: _ClassVar[SmartLockPart.LockStatus]
        LOCK_STATUS_LOCKED: _ClassVar[SmartLockPart.LockStatus]
        LOCK_STATUS_UNLOCKED: _ClassVar[SmartLockPart.LockStatus]

    LOCK_STATUS_UNSPECIFIED: SmartLockPart.LockStatus
    LOCK_STATUS_LOCKED: SmartLockPart.LockStatus
    LOCK_STATUS_UNLOCKED: SmartLockPart.LockStatus
    class HardwareError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARDWARE_ERROR_UNSPECIFIED: _ClassVar[SmartLockPart.HardwareError]
        HARDWARE_ERROR_NOT_DETECTED: _ClassVar[SmartLockPart.HardwareError]
        HARDWARE_ERROR_DETECTED: _ClassVar[SmartLockPart.HardwareError]

    HARDWARE_ERROR_UNSPECIFIED: SmartLockPart.HardwareError
    HARDWARE_ERROR_NOT_DETECTED: SmartLockPart.HardwareError
    HARDWARE_ERROR_DETECTED: SmartLockPart.HardwareError
    class ArmingAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARMING_ACTION_UNSPECIFIED: _ClassVar[SmartLockPart.ArmingAction]
        ARMING_ACTION_LOCK_ON_ARM: _ClassVar[SmartLockPart.ArmingAction]
        ARMING_ACTION_UNLOCK_ON_ARM: _ClassVar[SmartLockPart.ArmingAction]
        ARMING_ACTION_LOCK_ON_DISARM: _ClassVar[SmartLockPart.ArmingAction]
        ARMING_ACTION_UNLOCK_ON_DISARM: _ClassVar[SmartLockPart.ArmingAction]
        ARMING_ACTION_REACT_ON_PERIMETRAL_ARM: _ClassVar[SmartLockPart.ArmingAction]
        ARMING_ACTION_AFTER_EXIT_DELAY: _ClassVar[SmartLockPart.ArmingAction]

    ARMING_ACTION_UNSPECIFIED: SmartLockPart.ArmingAction
    ARMING_ACTION_LOCK_ON_ARM: SmartLockPart.ArmingAction
    ARMING_ACTION_UNLOCK_ON_ARM: SmartLockPart.ArmingAction
    ARMING_ACTION_LOCK_ON_DISARM: SmartLockPart.ArmingAction
    ARMING_ACTION_UNLOCK_ON_DISARM: SmartLockPart.ArmingAction
    ARMING_ACTION_REACT_ON_PERIMETRAL_ARM: SmartLockPart.ArmingAction
    ARMING_ACTION_AFTER_EXIT_DELAY: SmartLockPart.ArmingAction
    class Autolock(_message.Message):
        __slots__ = ("autolock_timeout", "autolock_timeout_deprecated", "autolock_type")
        class AutolockType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUTOLOCK_TYPE_UNSPECIFIED: _ClassVar[SmartLockPart.Autolock.AutolockType]
            AUTOLOCK_TYPE_AFTER_TIME_ELAPSED: _ClassVar[
                SmartLockPart.Autolock.AutolockType
            ]
            AUTOLOCK_TYPE_INSTANT_OR_TIME_ELAPSED: _ClassVar[
                SmartLockPart.Autolock.AutolockType
            ]
            AUTOLOCK_TYPE_DISABLED: _ClassVar[SmartLockPart.Autolock.AutolockType]

        AUTOLOCK_TYPE_UNSPECIFIED: SmartLockPart.Autolock.AutolockType
        AUTOLOCK_TYPE_AFTER_TIME_ELAPSED: SmartLockPart.Autolock.AutolockType
        AUTOLOCK_TYPE_INSTANT_OR_TIME_ELAPSED: SmartLockPart.Autolock.AutolockType
        AUTOLOCK_TYPE_DISABLED: SmartLockPart.Autolock.AutolockType
        class AutolockTimeout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUTOLOCK_TIMEOUT_UNSPECIFIED: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_10_SECONDS: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_20_SECONDS: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_30_SECONDS: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_1_MINUTE: _ClassVar[SmartLockPart.Autolock.AutolockTimeout]
            AUTOLOCK_TIMEOUT_1_MINUTE_30_SECONDS: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_2_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_2_MINUTES_30_SECONDS: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_3_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_4_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_5_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_10_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_20_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]
            AUTOLOCK_TIMEOUT_30_MINUTES: _ClassVar[
                SmartLockPart.Autolock.AutolockTimeout
            ]

        AUTOLOCK_TIMEOUT_UNSPECIFIED: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_10_SECONDS: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_20_SECONDS: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_30_SECONDS: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_1_MINUTE: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_1_MINUTE_30_SECONDS: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_2_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_2_MINUTES_30_SECONDS: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_3_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_4_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_5_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_10_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_20_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TIMEOUT_30_MINUTES: SmartLockPart.Autolock.AutolockTimeout
        AUTOLOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
        AUTOLOCK_TIMEOUT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        AUTOLOCK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        autolock_type: SmartLockPart.Autolock.AutolockType
        autolock_timeout_deprecated: _duration_pb2.Duration
        autolock_timeout: SmartLockPart.Autolock.AutolockTimeout
        def __init__(
            self,
            autolock_type: SmartLockPart.Autolock.AutolockType | str | None = ...,
            autolock_timeout_deprecated: _duration_pb2.Duration | _Mapping | None = ...,
            autolock_timeout: SmartLockPart.Autolock.AutolockTimeout | str | None = ...,
        ) -> None: ...

    class DoorOpenDeviceChimes(_message.Message):
        __slots__ = ("chimes_sound", "chimes_triggers")
        class DoorOpenChimesTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DOOR_OPEN_CHIMES_TRIGGER_UNSPECIFIED: _ClassVar[
                SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
            ]
            DOOR_OPEN_CHIMES_TRIGGER_REED: _ClassVar[
                SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
            ]

        DOOR_OPEN_CHIMES_TRIGGER_UNSPECIFIED: (
            SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
        )
        DOOR_OPEN_CHIMES_TRIGGER_REED: (
            SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
        )
        CHIMES_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        CHIMES_SOUND_FIELD_NUMBER: _ClassVar[int]
        chimes_triggers: _containers.RepeatedScalarFieldContainer[
            SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
        ]
        chimes_sound: _device_chimes_pb2.DeviceChimes.Sound
        def __init__(
            self,
            chimes_triggers: _Iterable[
                SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger | str
            ]
            | None = ...,
            chimes_sound: _device_chimes_pb2.DeviceChimes.Sound | str | None = ...,
        ) -> None: ...

    class SmartLockPartSettings(_message.Message):
        __slots__ = (
            "arming_actions",
            "autolock",
            "door_open_device_chimes",
            "door_open_too_long_alarm_delay",
        )
        class AutolockSettings(_message.Message):
            __slots__ = (
                "autolock_timeout",
                "autolock_timeout_deprecated",
                "autolock_type",
            )
            AUTOLOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
            AUTOLOCK_TIMEOUT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
            AUTOLOCK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
            autolock_type: SmartLockPart.Autolock.AutolockType
            autolock_timeout_deprecated: _duration_pb2.Duration
            autolock_timeout: SmartLockPart.Autolock.AutolockTimeout
            def __init__(
                self,
                autolock_type: SmartLockPart.Autolock.AutolockType | str | None = ...,
                autolock_timeout_deprecated: _duration_pb2.Duration
                | _Mapping
                | None = ...,
                autolock_timeout: SmartLockPart.Autolock.AutolockTimeout
                | str
                | None = ...,
            ) -> None: ...

        class DoorOpenDeviceChimesSettings(_message.Message):
            __slots__ = ("chimes_sound", "chimes_triggers")
            class ChimesTriggerPatch(_message.Message):
                __slots__ = ("chimes_trigger", "patch_type")
                PATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
                CHIMES_TRIGGER_FIELD_NUMBER: _ClassVar[int]
                patch_type: _patch_type_pb2.PatchType
                chimes_trigger: SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
                def __init__(
                    self,
                    patch_type: _patch_type_pb2.PatchType | str | None = ...,
                    chimes_trigger: SmartLockPart.DoorOpenDeviceChimes.DoorOpenChimesTrigger
                    | str
                    | None = ...,
                ) -> None: ...

            CHIMES_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
            CHIMES_SOUND_FIELD_NUMBER: _ClassVar[int]
            chimes_triggers: _containers.RepeatedCompositeFieldContainer[
                SmartLockPart.SmartLockPartSettings.DoorOpenDeviceChimesSettings.ChimesTriggerPatch
            ]
            chimes_sound: _device_chimes_pb2.DeviceChimes.Sound
            def __init__(
                self,
                chimes_triggers: _Iterable[
                    SmartLockPart.SmartLockPartSettings.DoorOpenDeviceChimesSettings.ChimesTriggerPatch
                    | _Mapping
                ]
                | None = ...,
                chimes_sound: _device_chimes_pb2.DeviceChimes.Sound | str | None = ...,
            ) -> None: ...

        class ArmingActionPatch(_message.Message):
            __slots__ = ("arming_action", "patch_type")
            PATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
            ARMING_ACTION_FIELD_NUMBER: _ClassVar[int]
            patch_type: _patch_type_pb2.PatchType
            arming_action: SmartLockPart.ArmingAction
            def __init__(
                self,
                patch_type: _patch_type_pb2.PatchType | str | None = ...,
                arming_action: SmartLockPart.ArmingAction | str | None = ...,
            ) -> None: ...

        DOOR_OPEN_TOO_LONG_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        AUTOLOCK_FIELD_NUMBER: _ClassVar[int]
        DOOR_OPEN_DEVICE_CHIMES_FIELD_NUMBER: _ClassVar[int]
        ARMING_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        door_open_too_long_alarm_delay: _duration_pb2.Duration
        autolock: SmartLockPart.SmartLockPartSettings.AutolockSettings
        door_open_device_chimes: (
            SmartLockPart.SmartLockPartSettings.DoorOpenDeviceChimesSettings
        )
        arming_actions: _containers.RepeatedCompositeFieldContainer[
            SmartLockPart.SmartLockPartSettings.ArmingActionPatch
        ]
        def __init__(
            self,
            door_open_too_long_alarm_delay: _duration_pb2.Duration
            | _Mapping
            | None = ...,
            autolock: SmartLockPart.SmartLockPartSettings.AutolockSettings
            | _Mapping
            | None = ...,
            door_open_device_chimes: SmartLockPart.SmartLockPartSettings.DoorOpenDeviceChimesSettings
            | _Mapping
            | None = ...,
            arming_actions: _Iterable[
                SmartLockPart.SmartLockPartSettings.ArmingActionPatch | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    DOOR_STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_ERROR_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_TOO_LONG_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    AUTOLOCK_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_DEVICE_CHIMES_FIELD_NUMBER: _ClassVar[int]
    ARMING_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    door_status: SmartLockPart.DoorStatus
    lock_status: SmartLockPart.LockStatus
    hardware_error: SmartLockPart.HardwareError
    door_open_too_long_alarm_delay: _duration_pb2.Duration
    autolock: SmartLockPart.Autolock
    door_open_device_chimes: SmartLockPart.DoorOpenDeviceChimes
    arming_actions: _containers.RepeatedScalarFieldContainer[SmartLockPart.ArmingAction]
    def __init__(
        self,
        door_status: SmartLockPart.DoorStatus | str | None = ...,
        lock_status: SmartLockPart.LockStatus | str | None = ...,
        hardware_error: SmartLockPart.HardwareError | str | None = ...,
        door_open_too_long_alarm_delay: _duration_pb2.Duration | _Mapping | None = ...,
        autolock: SmartLockPart.Autolock | _Mapping | None = ...,
        door_open_device_chimes: SmartLockPart.DoorOpenDeviceChimes
        | _Mapping
        | None = ...,
        arming_actions: _Iterable[SmartLockPart.ArmingAction | str] | None = ...,
    ) -> None: ...
