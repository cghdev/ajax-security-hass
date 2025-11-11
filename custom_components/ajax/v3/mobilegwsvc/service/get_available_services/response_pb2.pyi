from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    accounting_company_pb2 as _accounting_company_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import reseller_pb2 as _reseller_pb2
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.type import user_role_pb2 as _user_role_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetAvailableServicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "available_service_groups_list",
            "available_services",
            "ungrouped_available_services_list",
        )
        AVAILABLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        UNGROUPED_AVAILABLE_SERVICES_LIST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SERVICE_GROUPS_LIST_FIELD_NUMBER: _ClassVar[int]
        available_services: _containers.RepeatedCompositeFieldContainer[
            GetAvailableServicesResponse.AvailableService
        ]
        ungrouped_available_services_list: (
            GetAvailableServicesResponse.AvailableServicesList
        )
        available_service_groups_list: (
            GetAvailableServicesResponse.AvailableServiceGroupsList
        )
        def __init__(
            self,
            available_services: _Iterable[
                GetAvailableServicesResponse.AvailableService | _Mapping
            ]
            | None = ...,
            ungrouped_available_services_list: GetAvailableServicesResponse.AvailableServicesList
            | _Mapping
            | None = ...,
            available_service_groups_list: GetAvailableServicesResponse.AvailableServiceGroupsList
            | _Mapping
            | None = ...,
        ) -> None: ...

    class AvailableServicesList(_message.Message):
        __slots__ = ("ungrouped_available_services",)
        UNGROUPED_AVAILABLE_SERVICES_FIELD_NUMBER: _ClassVar[int]
        ungrouped_available_services: _containers.RepeatedCompositeFieldContainer[
            GetAvailableServicesResponse.AvailableService
        ]
        def __init__(
            self,
            ungrouped_available_services: _Iterable[
                GetAvailableServicesResponse.AvailableService | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class AvailableServiceGroupsList(_message.Message):
        __slots__ = ("available_service_groups",)
        AVAILABLE_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        available_service_groups: _containers.RepeatedCompositeFieldContainer[
            GetAvailableServicesResponse.AvailableServicesGroup
        ]
        def __init__(
            self,
            available_service_groups: _Iterable[
                GetAvailableServicesResponse.AvailableServicesGroup | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class AvailableService(_message.Message):
        __slots__ = ("reseller_infos", "resellers", "service")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        RESELLERS_FIELD_NUMBER: _ClassVar[int]
        RESELLER_INFOS_FIELD_NUMBER: _ClassVar[int]
        service: _service_pb2.Service
        resellers: _containers.RepeatedCompositeFieldContainer[
            _accounting_company_pb2.AccountingCompany
        ]
        reseller_infos: _containers.RepeatedCompositeFieldContainer[
            _reseller_pb2.Reseller
        ]
        def __init__(
            self,
            service: _service_pb2.Service | _Mapping | None = ...,
            resellers: _Iterable[_accounting_company_pb2.AccountingCompany | _Mapping]
            | None = ...,
            reseller_infos: _Iterable[_reseller_pb2.Reseller | _Mapping] | None = ...,
        ) -> None: ...

    class AvailableServicesGroup(_message.Message):
        __slots__ = ("id", "item", "lokalise_id", "name", "order")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOKALISE_ID_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        ORDER_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        lokalise_id: str
        item: _containers.RepeatedCompositeFieldContainer[
            GetAvailableServicesResponse.AvailableServicesGroupItem
        ]
        order: int
        def __init__(
            self,
            id: str | None = ...,
            name: str | None = ...,
            lokalise_id: str | None = ...,
            item: _Iterable[
                GetAvailableServicesResponse.AvailableServicesGroupItem | _Mapping
            ]
            | None = ...,
            order: int | None = ...,
        ) -> None: ...

    class AvailableServicesGroupItem(_message.Message):
        __slots__ = ("order", "service")
        ORDER_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        order: int
        service: GetAvailableServicesResponse.AvailableService
        def __init__(
            self,
            order: int | None = ...,
            service: GetAvailableServicesResponse.AvailableService
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "available_mandatory_service_not_found",
            "bad_request",
            "dealer_not_found",
            "not_available_for_user",
            "reseller_not_found",
        )
        class NotAvailableForUserError(_message.Message):
            __slots__ = ("user_role",)
            USER_ROLE_FIELD_NUMBER: _ClassVar[int]
            user_role: _user_role_pb2.UserRole
            def __init__(
                self, user_role: _user_role_pb2.UserRole | str | None = ...
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_MANDATORY_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NOT_AVAILABLE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        available_mandatory_service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        not_available_for_user: (
            GetAvailableServicesResponse.Failure.NotAvailableForUserError
        )
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            available_mandatory_service_not_found: _response_pb2.Error
            | _Mapping
            | None = ...,
            reseller_not_found: _response_pb2.Error | _Mapping | None = ...,
            dealer_not_found: _response_pb2.Error | _Mapping | None = ...,
            not_available_for_user: GetAvailableServicesResponse.Failure.NotAvailableForUserError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetAvailableServicesResponse.Success
    failure: GetAvailableServicesResponse.Failure
    def __init__(
        self,
        success: GetAvailableServicesResponse.Success | _Mapping | None = ...,
        failure: GetAvailableServicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
