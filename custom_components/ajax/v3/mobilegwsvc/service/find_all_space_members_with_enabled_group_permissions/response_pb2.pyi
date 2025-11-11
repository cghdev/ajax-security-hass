from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllSpaceMembersWithEnabledGroupPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("space_member_ids",)
        SPACE_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
        space_member_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, space_member_ids: _Iterable[str] | None = ...) -> None: ...

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
    success: FindAllSpaceMembersWithEnabledGroupPermissionsResponse.Success
    failure: FindAllSpaceMembersWithEnabledGroupPermissionsResponse.Failure
    def __init__(
        self,
        success: FindAllSpaceMembersWithEnabledGroupPermissionsResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAllSpaceMembersWithEnabledGroupPermissionsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
