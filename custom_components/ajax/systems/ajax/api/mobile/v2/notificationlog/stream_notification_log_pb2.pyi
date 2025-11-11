from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    folder_pb2 as _folder_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_pb2 as _notification_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    origin_id_pb2 as _origin_id_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    unread_counters_pb2 as _unread_counters_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamNotificationLogRequest(_message.Message):
    __slots__ = ("origin",)
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    origin: _origin_id_pb2.NotificationOriginId
    def __init__(
        self, origin: _origin_id_pb2.NotificationOriginId | _Mapping | None = ...
    ) -> None: ...

class StreamNotificationLogResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("events",)
        class Event(_message.Message):
            __slots__ = (
                "available_folders_updated",
                "counters_updated",
                "last_available_notifications",
                "notification_created",
                "notification_updated",
            )
            NOTIFICATION_CREATED_FIELD_NUMBER: _ClassVar[int]
            NOTIFICATION_UPDATED_FIELD_NUMBER: _ClassVar[int]
            COUNTERS_UPDATED_FIELD_NUMBER: _ClassVar[int]
            AVAILABLE_FOLDERS_UPDATED_FIELD_NUMBER: _ClassVar[int]
            LAST_AVAILABLE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
            notification_created: _notification_pb2.Notification
            notification_updated: _notification_pb2.Notification
            counters_updated: _unread_counters_pb2.UnreadNotificationCounters
            available_folders_updated: (
                StreamNotificationLogResponse.Success.AvailableFolders
            )
            last_available_notifications: (
                StreamNotificationLogResponse.Success.LastAvailableNotifications
            )
            def __init__(
                self,
                notification_created: _notification_pb2.Notification
                | _Mapping
                | None = ...,
                notification_updated: _notification_pb2.Notification
                | _Mapping
                | None = ...,
                counters_updated: _unread_counters_pb2.UnreadNotificationCounters
                | _Mapping
                | None = ...,
                available_folders_updated: StreamNotificationLogResponse.Success.AvailableFolders
                | _Mapping
                | None = ...,
                last_available_notifications: StreamNotificationLogResponse.Success.LastAvailableNotifications
                | _Mapping
                | None = ...,
            ) -> None: ...

        class AvailableFolders(_message.Message):
            __slots__ = ("available_folders",)
            AVAILABLE_FOLDERS_FIELD_NUMBER: _ClassVar[int]
            available_folders: _containers.RepeatedScalarFieldContainer[
                _folder_pb2.NotificationFolder
            ]
            def __init__(
                self,
                available_folders: _Iterable[_folder_pb2.NotificationFolder | str]
                | None = ...,
            ) -> None: ...

        class LastAvailableNotifications(_message.Message):
            __slots__ = ("infos", "last_notification_token")
            class LastAvailableNotification(_message.Message):
                __slots__ = ("folder", "last_notification_token")
                FOLDER_FIELD_NUMBER: _ClassVar[int]
                LAST_NOTIFICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
                folder: _folder_pb2.NotificationFolder
                last_notification_token: str
                def __init__(
                    self,
                    folder: _folder_pb2.NotificationFolder | str | None = ...,
                    last_notification_token: str | None = ...,
                ) -> None: ...

            INFOS_FIELD_NUMBER: _ClassVar[int]
            LAST_NOTIFICATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            infos: _containers.RepeatedCompositeFieldContainer[
                StreamNotificationLogResponse.Success.LastAvailableNotifications.LastAvailableNotification
            ]
            last_notification_token: str
            def __init__(
                self,
                infos: _Iterable[
                    StreamNotificationLogResponse.Success.LastAvailableNotifications.LastAvailableNotification
                    | _Mapping
                ]
                | None = ...,
                last_notification_token: str | None = ...,
            ) -> None: ...

        EVENTS_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[
            StreamNotificationLogResponse.Success.Event
        ]
        def __init__(
            self,
            events: _Iterable[StreamNotificationLogResponse.Success.Event | _Mapping]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "internal_error", "not_found")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.DefaultError
        not_found: _response_pb2.DefaultError
        internal_error: _response_pb2.DefaultError
        def __init__(
            self,
            illegal_argument: _response_pb2.DefaultError | _Mapping | None = ...,
            not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            internal_error: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamNotificationLogResponse.Success
    failure: StreamNotificationLogResponse.Failure
    def __init__(
        self,
        success: StreamNotificationLogResponse.Success | _Mapping | None = ...,
        failure: StreamNotificationLogResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
