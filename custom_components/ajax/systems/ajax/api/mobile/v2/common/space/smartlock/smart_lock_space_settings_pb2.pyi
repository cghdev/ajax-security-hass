from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_event_settings_pb2 as _smart_lock_event_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockSpaceSettings(_message.Message):
    __slots__ = ("event_settings", "group_id", "room_id")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    room_id: str
    event_settings: _smart_lock_event_settings_pb2.SmartLockEventSettings
    group_id: str
    def __init__(
        self,
        room_id: str | None = ...,
        event_settings: _smart_lock_event_settings_pb2.SmartLockEventSettings
        | _Mapping
        | None = ...,
        group_id: str | None = ...,
    ) -> None: ...
