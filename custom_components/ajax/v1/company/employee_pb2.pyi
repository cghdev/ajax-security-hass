from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import role_pb2 as _role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Employee(_message.Message):
    __slots__ = ()
    class ComplexRole(_message.Message):
        __slots__ = ("roles",)
        ROLES_FIELD_NUMBER: _ClassVar[int]
        roles: _containers.RepeatedScalarFieldContainer[_role_pb2.Role]
        def __init__(
            self, roles: _Iterable[_role_pb2.Role | str] | None = ...
        ) -> None: ...

    class EmployeeInfo(_message.Message):
        __slots__ = (
            "cluster_company_id",
            "employee_id",
            "first_name",
            "last_name",
            "photo_id",
            "role",
        )
        EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        employee_id: str
        first_name: str
        last_name: str
        role: Employee.ComplexRole
        photo_id: str
        cluster_company_id: str
        def __init__(
            self,
            employee_id: str | None = ...,
            first_name: str | None = ...,
            last_name: str | None = ...,
            role: Employee.ComplexRole | _Mapping | None = ...,
            photo_id: str | None = ...,
            cluster_company_id: str | None = ...,
        ) -> None: ...

    def __init__(self) -> None: ...
