from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.security_company import security_company_pb2 as _security_company_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompaniesResponse(_message.Message):
    __slots__ = ("all", "on_monitoring")
    ON_MONITORING_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    on_monitoring: _containers.RepeatedCompositeFieldContainer[
        _security_company_pb2.SecurityCompanyPreview
    ]
    all: _containers.RepeatedCompositeFieldContainer[
        _security_company_pb2.SecurityCompanyPreview
    ]
    def __init__(
        self,
        on_monitoring: _Iterable[
            _security_company_pb2.SecurityCompanyPreview | _Mapping
        ]
        | None = ...,
        all: _Iterable[_security_company_pb2.SecurityCompanyPreview | _Mapping]
        | None = ...,
    ) -> None: ...

class GetCompaniesResponseV2(_message.Message):
    __slots__ = ("all",)
    ALL_FIELD_NUMBER: _ClassVar[int]
    all: _containers.RepeatedCompositeFieldContainer[
        _security_company_pb2.SecurityCompanyPreview
    ]
    def __init__(
        self,
        all: _Iterable[_security_company_pb2.SecurityCompanyPreview | _Mapping]
        | None = ...,
    ) -> None: ...
