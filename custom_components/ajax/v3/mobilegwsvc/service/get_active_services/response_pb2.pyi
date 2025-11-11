from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    accounting_company_pb2 as _accounting_company_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    enriched_target_info_pb2 as _enriched_target_info_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    extra_service_state_pb2 as _extra_service_state_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.accounting import (
    service_switch_availability_status_pb2 as _service_switch_availability_status_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetActiveServicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("active_services",)
        ACTIVE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        active_services: _containers.RepeatedCompositeFieldContainer[
            GetActiveServicesResponse.ActiveService
        ]
        def __init__(
            self,
            active_services: _Iterable[
                GetActiveServicesResponse.ActiveService | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class ActiveService(_message.Message):
        __slots__ = (
            "accounting_company",
            "enriched_target_info",
            "service",
            "service_state",
            "service_switch_availability_status",
            "subscription_id",
        )
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTING_COMPANY_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_SWITCH_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        ENRICHED_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
        SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        service: _service_pb2.Service
        accounting_company: _accounting_company_pb2.AccountingCompany
        subscription_id: str
        service_switch_availability_status: (
            _service_switch_availability_status_pb2.ServiceSwitchAvailabilityStatus
        )
        enriched_target_info: _containers.RepeatedCompositeFieldContainer[
            _enriched_target_info_pb2.EnrichedTargetInfo
        ]
        service_state: _extra_service_state_pb2.ExtraServiceState.Active
        def __init__(
            self,
            service: _service_pb2.Service | _Mapping | None = ...,
            accounting_company: _accounting_company_pb2.AccountingCompany
            | _Mapping
            | None = ...,
            subscription_id: str | None = ...,
            service_switch_availability_status: _service_switch_availability_status_pb2.ServiceSwitchAvailabilityStatus
            | str
            | None = ...,
            enriched_target_info: _Iterable[
                _enriched_target_info_pb2.EnrichedTargetInfo | _Mapping
            ]
            | None = ...,
            service_state: _extra_service_state_pb2.ExtraServiceState.Active
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "not_found_active_mandatory_service")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_ACTIVE_MANDATORY_SERVICE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        not_found_active_mandatory_service: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            not_found_active_mandatory_service: _response_pb2.Error
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetActiveServicesResponse.Success
    failure: GetActiveServicesResponse.Failure
    def __init__(
        self,
        success: GetActiveServicesResponse.Success | _Mapping | None = ...,
        failure: GetActiveServicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
