from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_in_space_pb2 as _smart_lock_in_space_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllSmartLocksBySpaceRequest(_message.Message):
    __slots__ = ("space_id",)
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: str | None = ...) -> None: ...

class FindAllSmartLocksBySpaceResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("smart_locks",)
        SMART_LOCKS_FIELD_NUMBER: _ClassVar[int]
        smart_locks: _containers.RepeatedCompositeFieldContainer[
            _smart_lock_in_space_pb2.SmartLockInSpace
        ]
        def __init__(
            self,
            smart_locks: _Iterable[_smart_lock_in_space_pb2.SmartLockInSpace | _Mapping]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        permission_denied: _response_pb2.DefaultError
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        def __init__(
            self,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllSmartLocksBySpaceResponse.Success
    failure: FindAllSmartLocksBySpaceResponse.Failure
    def __init__(
        self,
        success: FindAllSmartLocksBySpaceResponse.Success | _Mapping | None = ...,
        failure: FindAllSmartLocksBySpaceResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
