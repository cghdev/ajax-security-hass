from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    space_pb2 as _space_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineEventCount(_message.Message):
    __slots__ = ("event_count", "grouping_key", "hub_hex_id", "isAlarm", "space")
    ISALARM_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUPING_KEY_FIELD_NUMBER: _ClassVar[int]
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    isAlarm: bool
    event_count: int
    grouping_key: int
    hub_hex_id: str
    space: _space_pb2.NotificationSpace
    def __init__(
        self,
        isAlarm: bool = ...,
        event_count: int | None = ...,
        grouping_key: int | None = ...,
        hub_hex_id: str | None = ...,
        space: _space_pb2.NotificationSpace | _Mapping | None = ...,
    ) -> None: ...
