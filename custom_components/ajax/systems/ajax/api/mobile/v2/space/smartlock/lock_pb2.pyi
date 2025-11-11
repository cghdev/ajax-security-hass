from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LockSmartLockRequest(_message.Message):
    __slots__ = ("smart_lock_id", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_id: str
    def __init__(
        self, space_id: str | None = ..., smart_lock_id: str | None = ...
    ) -> None: ...

class LockSmartLockResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "external_service_access_denied",
            "message",
            "permission_denied",
            "smart_lock_not_found",
            "smart_lock_offline",
            "space_not_found",
        )
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_SERVICE_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        smart_lock_not_found: _response_pb2.DefaultError
        external_service_access_denied: _response_pb2.DefaultError
        smart_lock_offline: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            smart_lock_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            external_service_access_denied: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            smart_lock_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: LockSmartLockResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: LockSmartLockResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
