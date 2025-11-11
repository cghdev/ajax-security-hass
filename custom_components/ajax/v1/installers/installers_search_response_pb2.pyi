from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import company_pb2 as _company_pb2
from v1.common import hub_user_pb2 as _hub_user_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class InstallersSearchResponse(_message.Message):
    __slots__ = ("companies", "hub_users")
    HUB_USERS_FIELD_NUMBER: _ClassVar[int]
    COMPANIES_FIELD_NUMBER: _ClassVar[int]
    hub_users: _containers.RepeatedCompositeFieldContainer[_hub_user_pb2.HubUser]
    companies: _containers.RepeatedCompositeFieldContainer[_company_pb2.Company]
    def __init__(
        self,
        hub_users: _Iterable[_hub_user_pb2.HubUser | _Mapping] | None = ...,
        companies: _Iterable[_company_pb2.Company | _Mapping] | None = ...,
    ) -> None: ...
