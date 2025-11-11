from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common import resource_id_pb2 as _resource_id_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetFirmwareMetadataRequest(_message.Message):
    __slots__ = ("language_code", "resource_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    resource_id: _resource_id_pb2.ResourceId
    language_code: str
    def __init__(
        self,
        resource_id: _resource_id_pb2.ResourceId | _Mapping | None = ...,
        language_code: str | None = ...,
    ) -> None: ...

class GetFirmwareMetadataResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("before_proceed_notes", "release_notes")
        RELEASE_NOTES_FIELD_NUMBER: _ClassVar[int]
        BEFORE_PROCEED_NOTES_FIELD_NUMBER: _ClassVar[int]
        release_notes: _containers.RepeatedScalarFieldContainer[str]
        before_proceed_notes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            release_notes: _Iterable[str] | None = ...,
            before_proceed_notes: _Iterable[str] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "message", "not_found")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        message: str
        illegal_argument: _response_pb2.DefaultError
        not_found: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            illegal_argument: _response_pb2.DefaultError | _Mapping | None = ...,
            not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetFirmwareMetadataResponse.Success
    failure: GetFirmwareMetadataResponse.Failure
    def __init__(
        self,
        success: GetFirmwareMetadataResponse.Success | _Mapping | None = ...,
        failure: GetFirmwareMetadataResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
