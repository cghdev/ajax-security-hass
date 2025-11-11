from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import (
    action_timer_pb2 as _action_timer_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LightSwitchChannel(_message.Message):
    __slots__ = (
        "brightness",
        "id",
        "is_transitioning",
        "name",
        "shutoff_timer",
        "state",
    )
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LightSwitchChannel.State]
        STATE_OFF: _ClassVar[LightSwitchChannel.State]
        STATE_ON: _ClassVar[LightSwitchChannel.State]

    STATE_UNSPECIFIED: LightSwitchChannel.State
    STATE_OFF: LightSwitchChannel.State
    STATE_ON: LightSwitchChannel.State
    class ChannelId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_ID_UNSPECIFIED: _ClassVar[LightSwitchChannel.ChannelId]
        CHANNEL_ID_1: _ClassVar[LightSwitchChannel.ChannelId]
        CHANNEL_ID_2: _ClassVar[LightSwitchChannel.ChannelId]

    CHANNEL_ID_UNSPECIFIED: LightSwitchChannel.ChannelId
    CHANNEL_ID_1: LightSwitchChannel.ChannelId
    CHANNEL_ID_2: LightSwitchChannel.ChannelId
    class Brightness(_message.Message):
        __slots__ = ("level",)
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        level: int
        def __init__(self, level: int | None = ...) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SHUTOFF_TIMER_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSITIONING_FIELD_NUMBER: _ClassVar[int]
    id: LightSwitchChannel.ChannelId
    name: str
    state: LightSwitchChannel.State
    shutoff_timer: _action_timer_pb2.ActionTimer
    brightness: LightSwitchChannel.Brightness
    is_transitioning: bool
    def __init__(
        self,
        id: LightSwitchChannel.ChannelId | str | None = ...,
        name: str | None = ...,
        state: LightSwitchChannel.State | str | None = ...,
        shutoff_timer: _action_timer_pb2.ActionTimer | _Mapping | None = ...,
        brightness: LightSwitchChannel.Brightness | _Mapping | None = ...,
        is_transitioning: bool = ...,
    ) -> None: ...
