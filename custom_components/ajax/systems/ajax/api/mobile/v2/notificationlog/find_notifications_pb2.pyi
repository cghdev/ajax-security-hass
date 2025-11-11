from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    filter_pb2 as _filter_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_pb2 as _notification_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    offline_notifications_data_pb2 as _offline_notifications_data_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindNotificationsRequest(_message.Message):
    __slots__ = ("filter", "limit", "pagination")
    class Pagination(_message.Message):
        __slots__ = ("backward_pagination_token", "forward_pagination_token")
        FORWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        BACKWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        forward_pagination_token: str
        backward_pagination_token: str
        def __init__(
            self,
            forward_pagination_token: str | None = ...,
            backward_pagination_token: str | None = ...,
        ) -> None: ...

    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    filter: _filter_pb2.NotificationsFilter
    limit: int
    pagination: FindNotificationsRequest.Pagination
    def __init__(
        self,
        filter: _filter_pb2.NotificationsFilter | _Mapping | None = ...,
        limit: int | None = ...,
        pagination: FindNotificationsRequest.Pagination | _Mapping | None = ...,
    ) -> None: ...

class FindNotificationsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "next_backward_pagination_token",
            "next_forward_pagination_token",
            "notifications",
            "offline_notifications_data",
        )
        NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
        NEXT_FORWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        NEXT_BACKWARD_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        OFFLINE_NOTIFICATIONS_DATA_FIELD_NUMBER: _ClassVar[int]
        notifications: _containers.RepeatedCompositeFieldContainer[
            _notification_pb2.Notification
        ]
        next_forward_pagination_token: str
        next_backward_pagination_token: str
        offline_notifications_data: _containers.RepeatedCompositeFieldContainer[
            _offline_notifications_data_pb2.OfflineNotificationsData
        ]
        def __init__(
            self,
            notifications: _Iterable[_notification_pb2.Notification | _Mapping]
            | None = ...,
            next_forward_pagination_token: str | None = ...,
            next_backward_pagination_token: str | None = ...,
            offline_notifications_data: _Iterable[
                _offline_notifications_data_pb2.OfflineNotificationsData | _Mapping
            ]
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
    success: FindNotificationsResponse.Success
    failure: FindNotificationsResponse.Failure
    def __init__(
        self,
        success: FindNotificationsResponse.Success | _Mapping | None = ...,
        failure: FindNotificationsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
