from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2_1
from systems.ajax.api.mobile.v2.common.space import space_lite_pb2 as _space_lite_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("lite_space",)
        LITE_SPACE_FIELD_NUMBER: _ClassVar[int]
        lite_space: _space_lite_pb2.LiteSpace
        def __init__(
            self, lite_space: _space_lite_pb2.LiteSpace | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("add_device_failed", "bad_request", "empty_spaces_limit_exceeded")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        ADD_DEVICE_FAILED_FIELD_NUMBER: _ClassVar[int]
        EMPTY_SPACES_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        add_device_failed: _response_pb2_1.AddDeviceError
        empty_spaces_limit_exceeded: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            add_device_failed: _response_pb2_1.AddDeviceError | _Mapping | None = ...,
            empty_spaces_limit_exceeded: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateSpaceResponse.Success
    failure: CreateSpaceResponse.Failure
    def __init__(
        self,
        success: CreateSpaceResponse.Success | _Mapping | None = ...,
        failure: CreateSpaceResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
