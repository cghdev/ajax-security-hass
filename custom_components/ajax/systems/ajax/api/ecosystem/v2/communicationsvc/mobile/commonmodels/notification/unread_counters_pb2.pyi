from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    folder_pb2 as _folder_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UnreadNotificationCounters(_message.Message):
    __slots__ = ("counters",)
    class UnreadCounterEntry(_message.Message):
        __slots__ = ("folder", "unread_events_count")
        FOLDER_FIELD_NUMBER: _ClassVar[int]
        UNREAD_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        folder: _folder_pb2.NotificationFolder
        unread_events_count: int
        def __init__(
            self,
            folder: _folder_pb2.NotificationFolder | str | None = ...,
            unread_events_count: int | None = ...,
        ) -> None: ...

    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    counters: _containers.RepeatedCompositeFieldContainer[
        UnreadNotificationCounters.UnreadCounterEntry
    ]
    def __init__(
        self,
        counters: _Iterable[UnreadNotificationCounters.UnreadCounterEntry | _Mapping]
        | None = ...,
    ) -> None: ...
