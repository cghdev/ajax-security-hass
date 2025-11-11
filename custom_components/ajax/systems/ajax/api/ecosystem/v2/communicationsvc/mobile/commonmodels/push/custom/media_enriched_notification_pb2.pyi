from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    media_pb2 as _media_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_pb2 as _notification_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class MediaEnrichedNotification(_message.Message):
    __slots__ = ("media", "notification")
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    media: _media_pb2.NotificationMedia
    def __init__(
        self,
        notification: _notification_pb2.Notification | _Mapping | None = ...,
        media: _media_pb2.NotificationMedia | _Mapping | None = ...,
    ) -> None: ...
