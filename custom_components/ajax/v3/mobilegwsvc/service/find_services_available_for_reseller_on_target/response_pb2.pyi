from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindServicesAvailableForResellerOnTargetResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("services",)
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
        def __init__(
            self, services: _Iterable[_service_pb2.Service | _Mapping] | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(
            self, bad_request: _response_pb2.Error | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindServicesAvailableForResellerOnTargetResponse.Success
    failure: FindServicesAvailableForResellerOnTargetResponse.Failure
    def __init__(
        self,
        success: FindServicesAvailableForResellerOnTargetResponse.Success
        | _Mapping
        | None = ...,
        failure: FindServicesAvailableForResellerOnTargetResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
