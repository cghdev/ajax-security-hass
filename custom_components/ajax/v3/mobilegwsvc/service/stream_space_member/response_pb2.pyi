from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.space.member import (
    space_member_pb2 as _space_member_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceMemberResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        class Snapshot(_message.Message):
            __slots__ = ("space_member",)
            SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
            space_member: _space_member_pb2.SpaceMember
            def __init__(
                self,
                space_member: _space_member_pb2.SpaceMember | _Mapping | None = ...,
            ) -> None: ...

        class Update(_message.Message):
            __slots__ = ("space_member", "update_type")
            class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UPDATE_TYPE_UNSPECIFIED: _ClassVar[
                    StreamSpaceMemberResponse.Success.Update.UpdateType
                ]
                UPDATE_TYPE_ADD: _ClassVar[
                    StreamSpaceMemberResponse.Success.Update.UpdateType
                ]
                UPDATE_TYPE_UPDATE: _ClassVar[
                    StreamSpaceMemberResponse.Success.Update.UpdateType
                ]
                UPDATE_TYPE_REMOVE: _ClassVar[
                    StreamSpaceMemberResponse.Success.Update.UpdateType
                ]

            UPDATE_TYPE_UNSPECIFIED: StreamSpaceMemberResponse.Success.Update.UpdateType
            UPDATE_TYPE_ADD: StreamSpaceMemberResponse.Success.Update.UpdateType
            UPDATE_TYPE_UPDATE: StreamSpaceMemberResponse.Success.Update.UpdateType
            UPDATE_TYPE_REMOVE: StreamSpaceMemberResponse.Success.Update.UpdateType
            SPACE_MEMBER_FIELD_NUMBER: _ClassVar[int]
            UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            space_member: _space_member_pb2.SpaceMember
            update_type: StreamSpaceMemberResponse.Success.Update.UpdateType
            def __init__(
                self,
                space_member: _space_member_pb2.SpaceMember | _Mapping | None = ...,
                update_type: StreamSpaceMemberResponse.Success.Update.UpdateType
                | str
                | None = ...,
            ) -> None: ...

        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamSpaceMemberResponse.Success.Snapshot
        update: StreamSpaceMemberResponse.Success.Update
        def __init__(
            self,
            snapshot: StreamSpaceMemberResponse.Success.Snapshot
            | _Mapping
            | None = ...,
            update: StreamSpaceMemberResponse.Success.Update | _Mapping | None = ...,
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
    success: StreamSpaceMemberResponse.Success
    failure: StreamSpaceMemberResponse.Failure
    def __init__(
        self,
        success: StreamSpaceMemberResponse.Success | _Mapping | None = ...,
        failure: StreamSpaceMemberResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
