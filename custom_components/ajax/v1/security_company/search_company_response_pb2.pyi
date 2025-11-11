from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.security_company import security_company_pb2 as _security_company_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SearchCompanyResponse(_message.Message):
    __slots__ = ("companies",)
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    companies: _containers.RepeatedCompositeFieldContainer[
        _security_company_pb2.SecurityCompanyPreview
    ]
    def __init__(
        self,
        companies: _Iterable[_security_company_pb2.SecurityCompanyPreview | _Mapping]
        | None = ...,
    ) -> None: ...
