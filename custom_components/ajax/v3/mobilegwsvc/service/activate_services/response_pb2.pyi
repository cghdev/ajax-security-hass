from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.accounting import (
    enriched_target_info_pb2 as _enriched_target_info_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateServicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("subscription_id",)
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        subscription_id: str
        def __init__(self, subscription_id: str | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "already_active_on_targets",
            "bad_request",
            "dealer_not_found",
            "illegal_state",
            "linkage_not_active",
            "linkage_suspended",
            "no_price_in_currency",
            "reseller_not_found",
            "service_not_found",
            "target_suspended",
        )
        class AlreadyActiveOnTargetsError(_message.Message):
            __slots__ = ("feature_target_infos",)
            FEATURE_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
            feature_target_infos: _containers.RepeatedCompositeFieldContainer[
                _enriched_target_info_pb2.EnrichedTargetInfo
            ]
            def __init__(
                self,
                feature_target_infos: _Iterable[
                    _enriched_target_info_pb2.EnrichedTargetInfo | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        RESELLER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEALER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        LINKAGE_NOT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        LINKAGE_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        TARGET_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
        NO_PRICE_IN_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_STATE_FIELD_NUMBER: _ClassVar[int]
        ALREADY_ACTIVE_ON_TARGETS_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        service_not_found: _response_pb2.Error
        reseller_not_found: _response_pb2.Error
        dealer_not_found: _response_pb2.Error
        linkage_not_active: _response_pb2.Error
        linkage_suspended: _response_pb2.Error
        target_suspended: _response_pb2.Error
        no_price_in_currency: _response_pb2.Error
        illegal_state: _response_pb2.Error
        already_active_on_targets: (
            ActivateServicesResponse.Failure.AlreadyActiveOnTargetsError
        )
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            service_not_found: _response_pb2.Error | _Mapping | None = ...,
            reseller_not_found: _response_pb2.Error | _Mapping | None = ...,
            dealer_not_found: _response_pb2.Error | _Mapping | None = ...,
            linkage_not_active: _response_pb2.Error | _Mapping | None = ...,
            linkage_suspended: _response_pb2.Error | _Mapping | None = ...,
            target_suspended: _response_pb2.Error | _Mapping | None = ...,
            no_price_in_currency: _response_pb2.Error | _Mapping | None = ...,
            illegal_state: _response_pb2.Error | _Mapping | None = ...,
            already_active_on_targets: ActivateServicesResponse.Failure.AlreadyActiveOnTargetsError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ActivateServicesResponse.Success
    failure: ActivateServicesResponse.Failure
    def __init__(
        self,
        success: ActivateServicesResponse.Success | _Mapping | None = ...,
        failure: ActivateServicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
