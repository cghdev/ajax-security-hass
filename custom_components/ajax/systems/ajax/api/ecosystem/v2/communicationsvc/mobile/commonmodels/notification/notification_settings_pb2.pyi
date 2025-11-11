from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_channel_pb2 as _notification_channel_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationSettings(_message.Message):
    __slots__ = ("alarms", "armings", "events", "malfunctions")
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ARMINGS_FIELD_NUMBER: _ClassVar[int]
    alarms: _notification_channel_pb2.NotificationChannels
    events: _notification_channel_pb2.NotificationChannels
    malfunctions: _notification_channel_pb2.NotificationChannels
    armings: _notification_channel_pb2.NotificationChannels
    def __init__(
        self,
        alarms: _notification_channel_pb2.NotificationChannels | _Mapping | None = ...,
        events: _notification_channel_pb2.NotificationChannels | _Mapping | None = ...,
        malfunctions: _notification_channel_pb2.NotificationChannels
        | _Mapping
        | None = ...,
        armings: _notification_channel_pb2.NotificationChannels | _Mapping | None = ...,
    ) -> None: ...
