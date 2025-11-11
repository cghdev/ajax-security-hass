from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_pb2 as _notification_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineNotificationsData(_message.Message):
    __slots__ = ("notifications", "parent_notification_id")
    PARENT_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    parent_notification_id: str
    notifications: _containers.RepeatedCompositeFieldContainer[
        _notification_pb2.Notification
    ]
    def __init__(
        self,
        parent_notification_id: str | None = ...,
        notifications: _Iterable[_notification_pb2.Notification | _Mapping]
        | None = ...,
    ) -> None: ...
