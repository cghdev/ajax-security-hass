from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.space.company import (
    company_billing_info_pb2 as _company_billing_info_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    standalone_device_permissions_pb2 as _standalone_device_permissions_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company import (
    company_info_pb2 as _company_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceMonitoringCompany(_message.Message):
    __slots__ = (
        "account_number_required_status",
        "company_billing_info",
        "company_info",
        "devices_permissions",
        "hub_user_index",
        "space_member_id",
        "status",
    )
    class AccountNumberRequiredStatus(
        int, metaclass=_enum_type_wrapper.EnumTypeWrapper
    ):
        __slots__ = ()
        ACCOUNT_NUMBER_REQUIRED_STATUS_UNSPECIFIED: _ClassVar[
            SpaceMonitoringCompany.AccountNumberRequiredStatus
        ]
        ACCOUNT_NUMBER_REQUIRED_STATUS_REQUIRED: _ClassVar[
            SpaceMonitoringCompany.AccountNumberRequiredStatus
        ]
        ACCOUNT_NUMBER_REQUIRED_STATUS_NOT_REQUIRED: _ClassVar[
            SpaceMonitoringCompany.AccountNumberRequiredStatus
        ]

    ACCOUNT_NUMBER_REQUIRED_STATUS_UNSPECIFIED: (
        SpaceMonitoringCompany.AccountNumberRequiredStatus
    )
    ACCOUNT_NUMBER_REQUIRED_STATUS_REQUIRED: (
        SpaceMonitoringCompany.AccountNumberRequiredStatus
    )
    ACCOUNT_NUMBER_REQUIRED_STATUS_NOT_REQUIRED: (
        SpaceMonitoringCompany.AccountNumberRequiredStatus
    )
    class MonitoringCompanyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MONITORING_COMPANY_STATUS_UNSPECIFIED: _ClassVar[
            SpaceMonitoringCompany.MonitoringCompanyStatus
        ]
        PENDING_APPROVAL: _ClassVar[SpaceMonitoringCompany.MonitoringCompanyStatus]
        APPROVED: _ClassVar[SpaceMonitoringCompany.MonitoringCompanyStatus]
        PENDING_DELETION: _ClassVar[SpaceMonitoringCompany.MonitoringCompanyStatus]

    MONITORING_COMPANY_STATUS_UNSPECIFIED: (
        SpaceMonitoringCompany.MonitoringCompanyStatus
    )
    PENDING_APPROVAL: SpaceMonitoringCompany.MonitoringCompanyStatus
    APPROVED: SpaceMonitoringCompany.MonitoringCompanyStatus
    PENDING_DELETION: SpaceMonitoringCompany.MonitoringCompanyStatus
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_REQUIRED_STATUS_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    company_info: _company_info_pb2.CompanyInfo
    status: SpaceMonitoringCompany.MonitoringCompanyStatus
    hub_user_index: int
    devices_permissions: _containers.RepeatedCompositeFieldContainer[
        _standalone_device_permissions_pb2.StandaloneDevicePermissions
    ]
    account_number_required_status: SpaceMonitoringCompany.AccountNumberRequiredStatus
    space_member_id: str
    company_billing_info: _company_billing_info_pb2.CompanyBillingInfo
    def __init__(
        self,
        company_info: _company_info_pb2.CompanyInfo | _Mapping | None = ...,
        status: SpaceMonitoringCompany.MonitoringCompanyStatus | str | None = ...,
        hub_user_index: int | None = ...,
        devices_permissions: _Iterable[
            _standalone_device_permissions_pb2.StandaloneDevicePermissions | _Mapping
        ]
        | None = ...,
        account_number_required_status: SpaceMonitoringCompany.AccountNumberRequiredStatus
        | str
        | None = ...,
        space_member_id: str | None = ...,
        company_billing_info: _company_billing_info_pb2.CompanyBillingInfo
        | _Mapping
        | None = ...,
    ) -> None: ...
