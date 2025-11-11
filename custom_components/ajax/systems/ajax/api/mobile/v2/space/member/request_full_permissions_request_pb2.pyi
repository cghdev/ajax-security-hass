from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class RequestFullPermissionsRequest(_message.Message):
    __slots__ = ("permanent_permissions", "space_locator", "temporary_permissions")
    class PermanentPermissions(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class TemporaryPermissions(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(
            self, duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    permanent_permissions: RequestFullPermissionsRequest.PermanentPermissions
    temporary_permissions: RequestFullPermissionsRequest.TemporaryPermissions
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        permanent_permissions: RequestFullPermissionsRequest.PermanentPermissions
        | _Mapping
        | None = ...,
        temporary_permissions: RequestFullPermissionsRequest.TemporaryPermissions
        | _Mapping
        | None = ...,
    ) -> None: ...

class RequestFullPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: RequestFullPermissionsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: RequestFullPermissionsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
