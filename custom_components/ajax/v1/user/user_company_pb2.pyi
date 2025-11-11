from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import company_pb2 as _company_pb2
from v1.company import employee_pb2 as _employee_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UserCompany(_message.Message):
    __slots__ = (
        "cluster_company_id",
        "company_id",
        "company_logo",
        "company_name",
        "company_status",
        "enabled_features",
        "privacy_override_management_authorization_status",
        "role",
        "service_type",
    )
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_STATUS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_LOGO_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDE_MANAGEMENT_AUTHORIZATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    company_name: str
    company_status: _company_pb2.Company.Status
    role: _employee_pb2.Employee.ComplexRole
    company_logo: _company_pb2.Company.Logo
    cluster_company_id: str
    privacy_override_management_authorization_status: (
        _company_pb2.Company.PrivacyOverrideManagementAuthorizationStatus
    )
    service_type: _company_pb2.Company.ServiceType
    enabled_features: _containers.RepeatedScalarFieldContainer[
        _company_pb2.Company.Feature
    ]
    def __init__(
        self,
        company_id: str | None = ...,
        company_name: str | None = ...,
        company_status: _company_pb2.Company.Status | str | None = ...,
        role: _employee_pb2.Employee.ComplexRole | _Mapping | None = ...,
        company_logo: _company_pb2.Company.Logo | _Mapping | None = ...,
        cluster_company_id: str | None = ...,
        privacy_override_management_authorization_status: _company_pb2.Company.PrivacyOverrideManagementAuthorizationStatus
        | str
        | None = ...,
        service_type: _company_pb2.Company.ServiceType | str | None = ...,
        enabled_features: _Iterable[_company_pb2.Company.Feature | str] | None = ...,
    ) -> None: ...
