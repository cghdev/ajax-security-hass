from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import company_pb2 as _company_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UserStreamCompaniesResponse(_message.Message):
    __slots__ = ("user_companies",)
    USER_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    user_companies: _containers.RepeatedCompositeFieldContainer[_company_pb2.Company]
    def __init__(
        self, user_companies: _Iterable[_company_pb2.Company | _Mapping] | None = ...
    ) -> None: ...
