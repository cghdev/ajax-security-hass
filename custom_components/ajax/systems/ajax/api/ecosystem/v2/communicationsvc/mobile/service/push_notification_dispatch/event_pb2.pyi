from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_pb2 as _notification_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import (
    media_enriched_notification_pb2 as _media_enriched_notification_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import (
    new_user_session_pb2 as _new_user_session_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import (
    offline_event_count_pb2 as _offline_event_count_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.push.custom import (
    session_invalidation_notification_pb2 as _session_invalidation_notification_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class PushNotificationDispatchEvent(_message.Message):
    __slots__ = (
        "media_enriched_notification",
        "new_user_session",
        "notification",
        "offline_event_count",
        "session_invalidation",
    )
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEW_USER_SESSION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ENRICHED_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_INVALIDATION_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    offline_event_count: _offline_event_count_pb2.OfflineEventCount
    new_user_session: _new_user_session_pb2.NewUserSession
    media_enriched_notification: (
        _media_enriched_notification_pb2.MediaEnrichedNotification
    )
    session_invalidation: _session_invalidation_notification_pb2.SessionInvalidation
    def __init__(
        self,
        notification: _notification_pb2.Notification | _Mapping | None = ...,
        offline_event_count: _offline_event_count_pb2.OfflineEventCount
        | _Mapping
        | None = ...,
        new_user_session: _new_user_session_pb2.NewUserSession | _Mapping | None = ...,
        media_enriched_notification: _media_enriched_notification_pb2.MediaEnrichedNotification
        | _Mapping
        | None = ...,
        session_invalidation: _session_invalidation_notification_pb2.SessionInvalidation
        | _Mapping
        | None = ...,
    ) -> None: ...
