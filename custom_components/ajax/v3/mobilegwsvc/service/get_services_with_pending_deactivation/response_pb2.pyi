from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.accounting import (
    enriched_target_info_pb2 as _enriched_target_info_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import service_pb2 as _service_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetServicesWithPendingDeactivationResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("target_services",)
        class TargetPendingDeactivationServices(_message.Message):
            __slots__ = ("pending_deactivation_services", "target_info")
            class PendingDeactivationService(_message.Message):
                __slots__ = ("deactivation_date", "service")
                DEACTIVATION_DATE_FIELD_NUMBER: _ClassVar[int]
                SERVICE_FIELD_NUMBER: _ClassVar[int]
                deactivation_date: _timestamp_pb2.Timestamp
                service: _service_pb2.Service
                def __init__(
                    self,
                    deactivation_date: _timestamp_pb2.Timestamp | _Mapping | None = ...,
                    service: _service_pb2.Service | _Mapping | None = ...,
                ) -> None: ...

            TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
            PENDING_DEACTIVATION_SERVICES_FIELD_NUMBER: _ClassVar[int]
            target_info: _enriched_target_info_pb2.EnrichedTargetInfo
            pending_deactivation_services: _containers.RepeatedCompositeFieldContainer[
                GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices.PendingDeactivationService
            ]
            def __init__(
                self,
                target_info: _enriched_target_info_pb2.EnrichedTargetInfo
                | _Mapping
                | None = ...,
                pending_deactivation_services: _Iterable[
                    GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices.PendingDeactivationService
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        TARGET_SERVICES_FIELD_NUMBER: _ClassVar[int]
        target_services: _containers.RepeatedCompositeFieldContainer[
            GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices
        ]
        def __init__(
            self,
            target_services: _Iterable[
                GetServicesWithPendingDeactivationResponse.Success.TargetPendingDeactivationServices
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("not_found",)
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        not_found: _response_pb2.Error
        def __init__(
            self, not_found: _response_pb2.Error | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetServicesWithPendingDeactivationResponse.Success
    failure: GetServicesWithPendingDeactivationResponse.Failure
    def __init__(
        self,
        success: GetServicesWithPendingDeactivationResponse.Success
        | _Mapping
        | None = ...,
        failure: GetServicesWithPendingDeactivationResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
