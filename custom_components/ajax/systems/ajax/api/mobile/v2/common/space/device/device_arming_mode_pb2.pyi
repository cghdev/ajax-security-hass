from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceArmingMode(_message.Message):
    __slots__ = ("disabled", "entry_exit", "follower", "instant")
    class Instant(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class EntryExit(_message.Message):
        __slots__ = (
            "alarm_delay",
            "arm_delay",
            "night_mode_alarm_delay",
            "night_mode_arm_delay",
        )
        ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        NIGHT_MODE_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        NIGHT_MODE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        arm_delay: _duration_pb2.Duration
        alarm_delay: _duration_pb2.Duration
        night_mode_arm_delay: _duration_pb2.Duration
        night_mode_alarm_delay: _duration_pb2.Duration
        def __init__(
            self,
            arm_delay: _duration_pb2.Duration | _Mapping | None = ...,
            alarm_delay: _duration_pb2.Duration | _Mapping | None = ...,
            night_mode_arm_delay: _duration_pb2.Duration | _Mapping | None = ...,
            night_mode_alarm_delay: _duration_pb2.Duration | _Mapping | None = ...,
        ) -> None: ...

    class Follower(_message.Message):
        __slots__ = ("night_mode_alarm_delay",)
        NIGHT_MODE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
        night_mode_alarm_delay: _duration_pb2.Duration
        def __init__(
            self, night_mode_alarm_delay: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    class Disabled(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    INSTANT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_EXIT_FIELD_NUMBER: _ClassVar[int]
    FOLLOWER_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    instant: DeviceArmingMode.Instant
    entry_exit: DeviceArmingMode.EntryExit
    follower: DeviceArmingMode.Follower
    disabled: DeviceArmingMode.Disabled
    def __init__(
        self,
        instant: DeviceArmingMode.Instant | _Mapping | None = ...,
        entry_exit: DeviceArmingMode.EntryExit | _Mapping | None = ...,
        follower: DeviceArmingMode.Follower | _Mapping | None = ...,
        disabled: DeviceArmingMode.Disabled | _Mapping | None = ...,
    ) -> None: ...
