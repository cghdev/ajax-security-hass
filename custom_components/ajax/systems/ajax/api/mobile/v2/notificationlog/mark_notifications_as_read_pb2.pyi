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
    origin_id_pb2 as _origin_id_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class MarkNotificationsAsReadRequest(_message.Message):
    __slots__ = ("mark_as_read", "origin")
    class Action(_message.Message):
        __slots__ = ("all", "all_in_folder", "some_in_folder")
        class AllNotifications(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class AllNotificationsInFolder(_message.Message):
            __slots__ = ("folder",)
            FOLDER_FIELD_NUMBER: _ClassVar[int]
            folder: _folder_pb2.NotificationFolder
            def __init__(
                self, folder: _folder_pb2.NotificationFolder | str | None = ...
            ) -> None: ...

        class SomeNotificationsInFolder(_message.Message):
            __slots__ = ("folder", "read_notifications_tokens")
            FOLDER_FIELD_NUMBER: _ClassVar[int]
            READ_NOTIFICATIONS_TOKENS_FIELD_NUMBER: _ClassVar[int]
            folder: _folder_pb2.NotificationFolder
            read_notifications_tokens: _containers.RepeatedScalarFieldContainer[str]
            def __init__(
                self,
                folder: _folder_pb2.NotificationFolder | str | None = ...,
                read_notifications_tokens: _Iterable[str] | None = ...,
            ) -> None: ...

        ALL_FIELD_NUMBER: _ClassVar[int]
        ALL_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
        SOME_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
        all: MarkNotificationsAsReadRequest.Action.AllNotifications
        all_in_folder: MarkNotificationsAsReadRequest.Action.AllNotificationsInFolder
        some_in_folder: MarkNotificationsAsReadRequest.Action.SomeNotificationsInFolder
        def __init__(
            self,
            all: MarkNotificationsAsReadRequest.Action.AllNotifications
            | _Mapping
            | None = ...,
            all_in_folder: MarkNotificationsAsReadRequest.Action.AllNotificationsInFolder
            | _Mapping
            | None = ...,
            some_in_folder: MarkNotificationsAsReadRequest.Action.SomeNotificationsInFolder
            | _Mapping
            | None = ...,
        ) -> None: ...

    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    MARK_AS_READ_FIELD_NUMBER: _ClassVar[int]
    origin: _origin_id_pb2.NotificationOriginId
    mark_as_read: _containers.RepeatedCompositeFieldContainer[
        MarkNotificationsAsReadRequest.Action
    ]
    def __init__(
        self,
        origin: _origin_id_pb2.NotificationOriginId | _Mapping | None = ...,
        mark_as_read: _Iterable[MarkNotificationsAsReadRequest.Action | _Mapping]
        | None = ...,
    ) -> None: ...

class MarkNotificationsAsReadResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

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
    success: MarkNotificationsAsReadResponse.Success
    failure: MarkNotificationsAsReadResponse.Failure
    def __init__(
        self,
        success: MarkNotificationsAsReadResponse.Success | _Mapping | None = ...,
        failure: MarkNotificationsAsReadResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
