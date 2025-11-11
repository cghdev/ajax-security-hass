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
from v3.mobilegwsvc.commonmodels.accounting import (
    subscription_action_pb2 as _subscription_action_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    subscription_owner_pb2 as _subscription_owner_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ExtraService(_message.Message):
    __slots__ = (
        "accounting_company",
        "available_subscription_actions",
        "enriched_target_info",
        "extra_service_state",
        "id",
        "service",
        "service_switch_availability_status",
        "sorting_key",
        "subscription_id",
        "subscription_owner",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    ENRICHED_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTING_COMPANY_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_SWITCH_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_OWNER_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SUBSCRIPTION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    service: _service_pb2.Service
    extra_service_state: _extra_service_state_pb2.ExtraServiceState
    enriched_target_info: _containers.RepeatedCompositeFieldContainer[
        _enriched_target_info_pb2.EnrichedTargetInfo
    ]
    accounting_company: _accounting_company_pb2.AccountingCompany
    sorting_key: str
    subscription_id: str
    service_switch_availability_status: (
        _service_switch_availability_status_pb2.ServiceSwitchAvailabilityStatus
    )
    subscription_owner: _subscription_owner_pb2.SubscriptionOwner
    available_subscription_actions: _containers.RepeatedScalarFieldContainer[
        _subscription_action_pb2.SubscriptionAction
    ]
    def __init__(
        self,
        id: str | None = ...,
        service: _service_pb2.Service | _Mapping | None = ...,
        extra_service_state: _extra_service_state_pb2.ExtraServiceState
        | _Mapping
        | None = ...,
        enriched_target_info: _Iterable[
            _enriched_target_info_pb2.EnrichedTargetInfo | _Mapping
        ]
        | None = ...,
        accounting_company: _accounting_company_pb2.AccountingCompany
        | _Mapping
        | None = ...,
        sorting_key: str | None = ...,
        subscription_id: str | None = ...,
        service_switch_availability_status: _service_switch_availability_status_pb2.ServiceSwitchAvailabilityStatus
        | str
        | None = ...,
        subscription_owner: _subscription_owner_pb2.SubscriptionOwner
        | _Mapping
        | None = ...,
        available_subscription_actions: _Iterable[
            _subscription_action_pb2.SubscriptionAction | str
        ]
        | None = ...,
    ) -> None: ...
