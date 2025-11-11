from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateJoinByQrResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "hub_offline",
            "illegal_argument",
            "limit_reached",
            "member_already_exists",
        )
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        member_already_exists: _response_pb2.Error
        hub_offline: _response_pb2.Error
        limit_reached: _response_pb2.Error
        def __init__(
            self,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            member_already_exists: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            limit_reached: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: InitiateJoinByQrResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: InitiateJoinByQrResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
