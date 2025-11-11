from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.integration.credentials import (
    credentials_info_pb2 as _credentials_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllSpaceIntegrationCredentialsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("credentials",)
        CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        credentials: _containers.RepeatedCompositeFieldContainer[
            _credentials_info_pb2.CredentialsInfo
        ]
        def __init__(
            self,
            credentials: _Iterable[_credentials_info_pb2.CredentialsInfo | _Mapping]
            | None = ...,
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
    success: FindAllSpaceIntegrationCredentialsResponse.Success
    failure: FindAllSpaceIntegrationCredentialsResponse.Failure
    def __init__(
        self,
        success: FindAllSpaceIntegrationCredentialsResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAllSpaceIntegrationCredentialsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
