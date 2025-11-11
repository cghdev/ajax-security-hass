from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveJoinByQrResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "already_exist",
            "permission_denied",
            "request_expired",
            "space_armed",
            "too_many_users",
        )
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        TOO_MANY_USERS_FIELD_NUMBER: _ClassVar[int]
        ALREADY_EXIST_FIELD_NUMBER: _ClassVar[int]
        REQUEST_EXPIRED_FIELD_NUMBER: _ClassVar[int]
        permission_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        too_many_users: _response_pb2.Error
        already_exist: _response_pb2.Error
        request_expired: _response_pb2.Error
        def __init__(
            self,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            too_many_users: _response_pb2.Error | _Mapping | None = ...,
            already_exist: _response_pb2.Error | _Mapping | None = ...,
            request_expired: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: ApproveJoinByQrResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: ApproveJoinByQrResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
