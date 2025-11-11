from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSpaceRequest(_message.Message):
    __slots__ = ("space_locator",)
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self, space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...
    ) -> None: ...

class DeleteSpaceResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "space_armed",
            "space_has_subscriptions",
            "space_has_subscriptions_by_member",
            "space_locked",
            "space_not_found",
            "space_on_monitoring",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ON_MONITORING_FIELD_NUMBER: _ClassVar[int]
        SPACE_HAS_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        SPACE_HAS_SUBSCRIPTIONS_BY_MEMBER_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        space_on_monitoring: _response_pb2.DefaultError
        space_has_subscriptions: _response_pb2.DefaultError
        space_has_subscriptions_by_member: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            space_on_monitoring: _response_pb2.DefaultError | _Mapping | None = ...,
            space_has_subscriptions: _response_pb2.DefaultError | _Mapping | None = ...,
            space_has_subscriptions_by_member: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeleteSpaceResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: DeleteSpaceResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
