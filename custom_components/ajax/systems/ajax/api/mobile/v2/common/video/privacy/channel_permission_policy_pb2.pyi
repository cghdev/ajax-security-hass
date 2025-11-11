from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelPermissionPolicy(_message.Message):
    __slots__ = ("after_alarm", "always", "when_armed")
    class AlwaysChannelPermissionPolicy(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class WhenArmedChannelPermissionPolicy(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class AfterAlarmChannelPermissionPolicy(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(
            self, duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    ALWAYS_FIELD_NUMBER: _ClassVar[int]
    WHEN_ARMED_FIELD_NUMBER: _ClassVar[int]
    AFTER_ALARM_FIELD_NUMBER: _ClassVar[int]
    always: ChannelPermissionPolicy.AlwaysChannelPermissionPolicy
    when_armed: ChannelPermissionPolicy.WhenArmedChannelPermissionPolicy
    after_alarm: ChannelPermissionPolicy.AfterAlarmChannelPermissionPolicy
    def __init__(
        self,
        always: ChannelPermissionPolicy.AlwaysChannelPermissionPolicy
        | _Mapping
        | None = ...,
        when_armed: ChannelPermissionPolicy.WhenArmedChannelPermissionPolicy
        | _Mapping
        | None = ...,
        after_alarm: ChannelPermissionPolicy.AfterAlarmChannelPermissionPolicy
        | _Mapping
        | None = ...,
    ) -> None: ...
