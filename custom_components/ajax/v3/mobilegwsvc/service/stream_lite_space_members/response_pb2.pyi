from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.space.member import (
    lite_space_member_pb2 as _lite_space_member_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamLiteSpaceMembersResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamLiteSpaceMembersResponse.Snapshot
        update: StreamLiteSpaceMembersResponse.Update
        def __init__(
            self,
            snapshot: StreamLiteSpaceMembersResponse.Snapshot | _Mapping | None = ...,
            update: StreamLiteSpaceMembersResponse.Update | _Mapping | None = ...,
        ) -> None: ...

    class Snapshot(_message.Message):
        __slots__ = ("lite_space_members",)
        LITE_SPACE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        lite_space_members: StreamLiteSpaceMembersResponse.LiteSpaceMembers
        def __init__(
            self,
            lite_space_members: StreamLiteSpaceMembersResponse.LiteSpaceMembers
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Update(_message.Message):
        __slots__ = ("lite_space_member", "update_type")
        class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UPDATE_TYPE_UNSPECIFIED: _ClassVar[
                StreamLiteSpaceMembersResponse.Update.UpdateType
            ]
            UPDATE_TYPE_ADD: _ClassVar[StreamLiteSpaceMembersResponse.Update.UpdateType]
            UPDATE_TYPE_UPDATE: _ClassVar[
                StreamLiteSpaceMembersResponse.Update.UpdateType
            ]
            UPDATE_TYPE_REMOVE: _ClassVar[
                StreamLiteSpaceMembersResponse.Update.UpdateType
            ]

        UPDATE_TYPE_UNSPECIFIED: StreamLiteSpaceMembersResponse.Update.UpdateType
        UPDATE_TYPE_ADD: StreamLiteSpaceMembersResponse.Update.UpdateType
        UPDATE_TYPE_UPDATE: StreamLiteSpaceMembersResponse.Update.UpdateType
        UPDATE_TYPE_REMOVE: StreamLiteSpaceMembersResponse.Update.UpdateType
        LITE_SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        lite_space_member: _lite_space_member_pb2.LiteSpaceMember
        update_type: StreamLiteSpaceMembersResponse.Update.UpdateType
        def __init__(
            self,
            lite_space_member: _lite_space_member_pb2.LiteSpaceMember
            | _Mapping
            | None = ...,
            update_type: StreamLiteSpaceMembersResponse.Update.UpdateType
            | str
            | None = ...,
        ) -> None: ...

    class LiteSpaceMembers(_message.Message):
        __slots__ = ("lite_space_members",)
        LITE_SPACE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        lite_space_members: _containers.RepeatedCompositeFieldContainer[
            _lite_space_member_pb2.LiteSpaceMember
        ]
        def __init__(
            self,
            lite_space_members: _Iterable[
                _lite_space_member_pb2.LiteSpaceMember | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamLiteSpaceMembersResponse.Success
    failure: StreamLiteSpaceMembersResponse.Failure
    def __init__(
        self,
        success: StreamLiteSpaceMembersResponse.Success | _Mapping | None = ...,
        failure: StreamLiteSpaceMembersResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
