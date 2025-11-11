from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AskVideoEdgeDirectConnectAccessResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("encrypted_key", "encrypted_key_signature", "raw_key")
        RAW_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_KEY_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        raw_key: bytes
        encrypted_key: bytes
        encrypted_key_signature: bytes
        def __init__(
            self,
            raw_key: bytes | None = ...,
            encrypted_key: bytes | None = ...,
            encrypted_key_signature: bytes | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "certificate_not_found",
            "permission_denied",
            "space_armed",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        certificate_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            certificate_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AskVideoEdgeDirectConnectAccessResponse.Success
    failure: AskVideoEdgeDirectConnectAccessResponse.Failure
    def __init__(
        self,
        success: AskVideoEdgeDirectConnectAccessResponse.Success
        | _Mapping
        | None = ...,
        failure: AskVideoEdgeDirectConnectAccessResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
