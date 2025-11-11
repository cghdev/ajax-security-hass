from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveSpaceMemberRequest(_message.Message):
    __slots__ = ("space_locator", "space_member_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    space_member_id: str
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        space_member_id: str | None = ...,
    ) -> None: ...

class RemoveSpaceMemberResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "active_subscription_exist_error",
            "bad_request",
            "permission_denied",
            "space_armed",
            "space_locked",
            "unable_to_delete_last_member",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        UNABLE_TO_DELETE_LAST_MEMBER_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_SUBSCRIPTION_EXIST_ERROR_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        unable_to_delete_last_member: _response_pb2.DefaultError
        active_subscription_exist_error: _response_pb2.ActiveSubscriptionExistError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            unable_to_delete_last_member: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            active_subscription_exist_error: _response_pb2.ActiveSubscriptionExistError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RemoveSpaceMemberResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: RemoveSpaceMemberResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
