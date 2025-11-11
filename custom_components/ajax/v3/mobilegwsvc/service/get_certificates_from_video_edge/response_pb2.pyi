from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.crypto import (
    x509_certificate_pb2 as _x509_certificate_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetCertificatesFromVideoEdgeResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "pkcs10_supported",
            "pkcs12_supported",
            "server_certificates",
            "supported_rsa_key_lengths",
            "supported_signature_algorithms",
            "supported_x509_versions",
        )
        SUPPORTED_X509_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_RSA_KEY_LENGTHS_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_SIGNATURE_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
        SERVER_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
        PKCS12_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        PKCS10_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        supported_x509_versions: _containers.RepeatedScalarFieldContainer[
            _x509_certificate_pb2.X509Version
        ]
        supported_rsa_key_lengths: _containers.RepeatedScalarFieldContainer[int]
        supported_signature_algorithms: _containers.RepeatedScalarFieldContainer[
            _types_pb2.CryptoHashAlgorithm
        ]
        server_certificates: _containers.RepeatedCompositeFieldContainer[
            _x509_certificate_pb2.X509Certificate
        ]
        pkcs12_supported: bool
        pkcs10_supported: bool
        def __init__(
            self,
            supported_x509_versions: _Iterable[_x509_certificate_pb2.X509Version | str]
            | None = ...,
            supported_rsa_key_lengths: _Iterable[int] | None = ...,
            supported_signature_algorithms: _Iterable[
                _types_pb2.CryptoHashAlgorithm | str
            ]
            | None = ...,
            server_certificates: _Iterable[
                _x509_certificate_pb2.X509Certificate | _Mapping
            ]
            | None = ...,
            pkcs12_supported: bool = ...,
            pkcs10_supported: bool = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
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
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
            unimplemented_video_edge_command: _response_pb2.Error
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetCertificatesFromVideoEdgeResponse.Success
    failure: GetCertificatesFromVideoEdgeResponse.Failure
    def __init__(
        self,
        success: GetCertificatesFromVideoEdgeResponse.Success | _Mapping | None = ...,
        failure: GetCertificatesFromVideoEdgeResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
