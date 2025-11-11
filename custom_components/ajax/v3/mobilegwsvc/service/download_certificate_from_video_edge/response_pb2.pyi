from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadCertificateFromVideoEdgeResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("certificates_pem",)
        CERTIFICATES_PEM_FIELD_NUMBER: _ClassVar[int]
        certificates_pem: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, certificates_pem: _Iterable[str] | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "certificate_not_found",
            "permission_denied",
            "space_not_found",
            "unimplemented_video_edge_command",
            "video_edge_is_offline",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        certificate_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
            unimplemented_video_edge_command: _response_pb2.Error
            | _Mapping
            | None = ...,
            certificate_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: DownloadCertificateFromVideoEdgeResponse.Success
    failure: DownloadCertificateFromVideoEdgeResponse.Failure
    def __init__(
        self,
        success: DownloadCertificateFromVideoEdgeResponse.Success
        | _Mapping
        | None = ...,
        failure: DownloadCertificateFromVideoEdgeResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
