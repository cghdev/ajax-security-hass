from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteAudioFileForAudioScenariosResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = ("conflict", "illegal_argument")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        CONFLICT_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        conflict: _response_pb2.Error
        def __init__(
            self,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            conflict: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeleteAudioFileForAudioScenariosResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: DeleteAudioFileForAudioScenariosResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
