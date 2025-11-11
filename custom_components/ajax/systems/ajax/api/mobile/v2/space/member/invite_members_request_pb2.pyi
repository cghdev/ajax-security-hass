from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class InviteSpaceMembersRequest(_message.Message):
    __slots__ = ("emails", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    emails: _containers.RepeatedCompositeFieldContainer[SpaceMemberEmail]
    def __init__(
        self,
        space_id: str | None = ...,
        emails: _Iterable[SpaceMemberEmail | _Mapping] | None = ...,
    ) -> None: ...

class InviteSpaceMembersResponse(_message.Message):
    __slots__ = ("result",)
    class InviteResult(_message.Message):
        __slots__ = ("email", "failure", "success")
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        email: SpaceMemberEmail
        success: _response_pb2.Success
        failure: InviteSpaceMembersResponse.Failure
        def __init__(
            self,
            email: SpaceMemberEmail | _Mapping | None = ...,
            success: _response_pb2.Success | _Mapping | None = ...,
            failure: InviteSpaceMembersResponse.Failure | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "already_exist",
            "bad_request",
            "permission_denied",
            "pro_not_found",
            "space_armed",
            "space_locked",
            "too_many_users",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        TOO_MANY_USERS_FIELD_NUMBER: _ClassVar[int]
        ALREADY_EXIST_FIELD_NUMBER: _ClassVar[int]
        PRO_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        too_many_users: _response_pb2.DefaultError
        already_exist: _response_pb2.DefaultError
        pro_not_found: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            too_many_users: _response_pb2.DefaultError | _Mapping | None = ...,
            already_exist: _response_pb2.DefaultError | _Mapping | None = ...,
            pro_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[
        InviteSpaceMembersResponse.InviteResult
    ]
    def __init__(
        self,
        result: _Iterable[InviteSpaceMembersResponse.InviteResult | _Mapping]
        | None = ...,
    ) -> None: ...

class SpaceMemberEmail(_message.Message):
    __slots__ = ("pro_email", "user_email")
    PRO_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    pro_email: str
    user_email: str
    def __init__(
        self, pro_email: str | None = ..., user_email: str | None = ...
    ) -> None: ...
