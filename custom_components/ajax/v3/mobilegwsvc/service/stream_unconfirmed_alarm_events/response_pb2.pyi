from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    notification_pb2 as _notification_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamUnconfirmedAlarmEventsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("created", "snapshot", "updated")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamUnconfirmedAlarmEventsResponse.Notifications
        created: StreamUnconfirmedAlarmEventsResponse.Notifications
        updated: StreamUnconfirmedAlarmEventsResponse.Notifications
        def __init__(
            self,
            snapshot: StreamUnconfirmedAlarmEventsResponse.Notifications
            | _Mapping
            | None = ...,
            created: StreamUnconfirmedAlarmEventsResponse.Notifications
            | _Mapping
            | None = ...,
            updated: StreamUnconfirmedAlarmEventsResponse.Notifications
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Notifications(_message.Message):
        __slots__ = ("notifications",)
        NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
        notifications: _containers.RepeatedCompositeFieldContainer[
            _notification_pb2.Notification
        ]
        def __init__(
            self,
            notifications: _Iterable[_notification_pb2.Notification | _Mapping]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "not_found", "request_timeout")
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        not_found: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        request_timeout: _response_pb2.Error
        def __init__(
            self,
            not_found: _response_pb2.Error | _Mapping | None = ...,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            request_timeout: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamUnconfirmedAlarmEventsResponse.Success
    failure: StreamUnconfirmedAlarmEventsResponse.Failure
    def __init__(
        self,
        success: StreamUnconfirmedAlarmEventsResponse.Success | _Mapping | None = ...,
        failure: StreamUnconfirmedAlarmEventsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
