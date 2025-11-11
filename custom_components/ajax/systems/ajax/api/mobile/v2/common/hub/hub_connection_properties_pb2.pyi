from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.time import (
    duration_option_pb2 as _duration_option_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubConnectionProperties(_message.Message):
    __slots__ = (
        "hub_channel_offline_event_delay_duration",
        "hub_offline_event_delay_duration",
    )
    class HubOfflineEventDelayDuration(_message.Message):
        __slots__ = ("duration_options",)
        DURATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        duration_options: _containers.RepeatedCompositeFieldContainer[
            _duration_option_pb2.DurationOption
        ]
        def __init__(
            self,
            duration_options: _Iterable[_duration_option_pb2.DurationOption | _Mapping]
            | None = ...,
        ) -> None: ...

    class HubChannelOfflineEventDelayDuration(_message.Message):
        __slots__ = ("duration_options",)
        DURATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        duration_options: _containers.RepeatedCompositeFieldContainer[
            _duration_option_pb2.DurationOption
        ]
        def __init__(
            self,
            duration_options: _Iterable[_duration_option_pb2.DurationOption | _Mapping]
            | None = ...,
        ) -> None: ...

    HUB_OFFLINE_EVENT_DELAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    HUB_CHANNEL_OFFLINE_EVENT_DELAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    hub_offline_event_delay_duration: (
        HubConnectionProperties.HubOfflineEventDelayDuration
    )
    hub_channel_offline_event_delay_duration: (
        HubConnectionProperties.HubChannelOfflineEventDelayDuration
    )
    def __init__(
        self,
        hub_offline_event_delay_duration: HubConnectionProperties.HubOfflineEventDelayDuration
        | _Mapping
        | None = ...,
        hub_channel_offline_event_delay_duration: HubConnectionProperties.HubChannelOfflineEventDelayDuration
        | _Mapping
        | None = ...,
    ) -> None: ...
