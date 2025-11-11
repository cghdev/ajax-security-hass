from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.accounting import (
    find_available_services_context_pb2 as _find_available_services_context_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    postpayment_service_group_pb2 as _postpayment_service_group_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    prepayment_service_group_pb2 as _prepayment_service_group_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting.failure import (
    not_available_for_user_error_pb2 as _not_available_for_user_error_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindAvailableExtraServicesDataForSpaceResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("post_payment_flow_data", "prepayment_flow_data")
        class PrepaymentData(_message.Message):
            __slots__ = ("available_prepayment_service_groups",)
            AVAILABLE_PREPAYMENT_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
            available_prepayment_service_groups: (
                _containers.RepeatedCompositeFieldContainer[
                    _prepayment_service_group_pb2.AvailablePrePaymentServiceGroup
                ]
            )
            def __init__(
                self,
                available_prepayment_service_groups: _Iterable[
                    _prepayment_service_group_pb2.AvailablePrePaymentServiceGroup
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class PostPaymentData(_message.Message):
            __slots__ = ("available_post_payment_service_groups", "current_context")
            AVAILABLE_POST_PAYMENT_SERVICE_GROUPS_FIELD_NUMBER: _ClassVar[int]
            CURRENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
            available_post_payment_service_groups: (
                _containers.RepeatedCompositeFieldContainer[
                    _postpayment_service_group_pb2.AvailablePostPaymentServiceGroup
                ]
            )
            current_context: (
                _find_available_services_context_pb2.FindAvailableServicesContext
            )
            def __init__(
                self,
                available_post_payment_service_groups: _Iterable[
                    _postpayment_service_group_pb2.AvailablePostPaymentServiceGroup
                    | _Mapping
                ]
                | None = ...,
                current_context: _find_available_services_context_pb2.FindAvailableServicesContext
                | _Mapping
                | None = ...,
            ) -> None: ...

        PREPAYMENT_FLOW_DATA_FIELD_NUMBER: _ClassVar[int]
        POST_PAYMENT_FLOW_DATA_FIELD_NUMBER: _ClassVar[int]
        prepayment_flow_data: (
            FindAvailableExtraServicesDataForSpaceResponse.Success.PrepaymentData
        )
        post_payment_flow_data: (
            FindAvailableExtraServicesDataForSpaceResponse.Success.PostPaymentData
        )
        def __init__(
            self,
            prepayment_flow_data: FindAvailableExtraServicesDataForSpaceResponse.Success.PrepaymentData
            | _Mapping
            | None = ...,
            post_payment_flow_data: FindAvailableExtraServicesDataForSpaceResponse.Success.PostPaymentData
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "available_mandatory_service_not_found",
            "bad_request",
            "dealer_not_found",
            "internal_error",
            "not_available_for_user",
            "reseller_not_found",
        )
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_MANDATORY_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NOT_AVAILABLE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
        internal_error: _response_pb2.Error
        bad_request: _response_pb2.Error
        available_mandatory_service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        not_available_for_user: (
            _not_available_for_user_error_pb2.NotAvailableForUserError
        )
        def __init__(
            self,
            internal_error: _response_pb2.Error | _Mapping | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            available_mandatory_service_not_found: _response_pb2.Error
            | _Mapping
            | None = ...,
            reseller_not_found: _response_pb2.Error | _Mapping | None = ...,
            dealer_not_found: _response_pb2.Error | _Mapping | None = ...,
            not_available_for_user: _not_available_for_user_error_pb2.NotAvailableForUserError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAvailableExtraServicesDataForSpaceResponse.Success
    failure: FindAvailableExtraServicesDataForSpaceResponse.Failure
    def __init__(
        self,
        success: FindAvailableExtraServicesDataForSpaceResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAvailableExtraServicesDataForSpaceResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
