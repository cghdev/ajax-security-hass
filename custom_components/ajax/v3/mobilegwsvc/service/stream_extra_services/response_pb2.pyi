from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.accounting import (
    extra_service_pb2 as _extra_service_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    extra_service_state_pb2 as _extra_service_state_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    service_activation_availability_status_pb2 as _service_activation_availability_status_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamExtraServicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "stream_update", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        STREAM_UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamExtraServicesResponse.ExtraServices
        update: StreamExtraServicesResponse.Update
        stream_update: StreamExtraServicesResponse.StreamUpdate
        def __init__(
            self,
            snapshot: StreamExtraServicesResponse.ExtraServices | _Mapping | None = ...,
            update: StreamExtraServicesResponse.Update | _Mapping | None = ...,
            stream_update: StreamExtraServicesResponse.StreamUpdate
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Update(_message.Message):
        __slots__ = (
            "extra_service_added",
            "extra_service_id",
            "extra_service_reactivated",
            "extra_service_removed",
            "extra_service_replaced",
            "extra_service_state_updated",
            "subscription_id",
        )
        EXTRA_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_STATE_UPDATED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_REMOVED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_REACTIVATED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_REPLACED_FIELD_NUMBER: _ClassVar[int]
        extra_service_id: str
        subscription_id: str
        extra_service_added: StreamExtraServicesResponse.ExtraServiceAdded
        extra_service_state_updated: (
            StreamExtraServicesResponse.ExtraServiceStateUpdated
        )
        extra_service_removed: StreamExtraServicesResponse.ExtraServiceRemoved
        extra_service_reactivated: StreamExtraServicesResponse.ExtraServiceReactivated
        extra_service_replaced: StreamExtraServicesResponse.ExtraServiceReplaced
        def __init__(
            self,
            extra_service_id: str | None = ...,
            subscription_id: str | None = ...,
            extra_service_added: StreamExtraServicesResponse.ExtraServiceAdded
            | _Mapping
            | None = ...,
            extra_service_state_updated: StreamExtraServicesResponse.ExtraServiceStateUpdated
            | _Mapping
            | None = ...,
            extra_service_removed: StreamExtraServicesResponse.ExtraServiceRemoved
            | _Mapping
            | None = ...,
            extra_service_reactivated: StreamExtraServicesResponse.ExtraServiceReactivated
            | _Mapping
            | None = ...,
            extra_service_replaced: StreamExtraServicesResponse.ExtraServiceReplaced
            | _Mapping
            | None = ...,
        ) -> None: ...

    class ExtraServiceAdded(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(
            self,
            new_extra_service: _extra_service_pb2.ExtraService | _Mapping | None = ...,
        ) -> None: ...

    class ExtraServiceStateUpdated(_message.Message):
        __slots__ = ("extra_service", "new_state")
        NEW_STATE_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_state: _extra_service_state_pb2.ExtraServiceState
        extra_service: _extra_service_pb2.ExtraService
        def __init__(
            self,
            new_state: _extra_service_state_pb2.ExtraServiceState
            | _Mapping
            | None = ...,
            extra_service: _extra_service_pb2.ExtraService | _Mapping | None = ...,
        ) -> None: ...

    class ExtraServiceRemoved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ExtraServiceReactivated(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(
            self,
            new_extra_service: _extra_service_pb2.ExtraService | _Mapping | None = ...,
        ) -> None: ...

    class ExtraServiceReplaced(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(
            self,
            new_extra_service: _extra_service_pb2.ExtraService | _Mapping | None = ...,
        ) -> None: ...

    class ExtraServices(_message.Message):
        __slots__ = ("extra_services", "service_activation_availability_status")
        EXTRA_SERVICES_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACTIVATION_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        extra_services: _containers.RepeatedCompositeFieldContainer[
            _extra_service_pb2.ExtraService
        ]
        service_activation_availability_status: _service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus
        def __init__(
            self,
            extra_services: _Iterable[_extra_service_pb2.ExtraService | _Mapping]
            | None = ...,
            service_activation_availability_status: _service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus
            | str
            | None = ...,
        ) -> None: ...

    class StreamUpdate(_message.Message):
        __slots__ = ("service_activation_availability_status_changed",)
        SERVICE_ACTIVATION_AVAILABILITY_STATUS_CHANGED_FIELD_NUMBER: _ClassVar[int]
        service_activation_availability_status_changed: (
            StreamExtraServicesResponse.ServiceActivationAvailabilityStatusChanged
        )
        def __init__(
            self,
            service_activation_availability_status_changed: StreamExtraServicesResponse.ServiceActivationAvailabilityStatusChanged
            | _Mapping
            | None = ...,
        ) -> None: ...

    class ServiceActivationAvailabilityStatusChanged(_message.Message):
        __slots__ = ("service_activation_availability_status",)
        SERVICE_ACTIVATION_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
        service_activation_availability_status: _service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus
        def __init__(
            self,
            service_activation_availability_status: _service_activation_availability_status_pb2.ServiceActivationAvailabilityStatus
            | str
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "extra_services_not_available",
            "illegal_argument",
            "message",
            "request_timeout",
        )
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICES_NOT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        message: str
        request_timeout: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        extra_services_not_available: _response_pb2.Error
        def __init__(
            self,
            message: str | None = ...,
            request_timeout: _response_pb2.Error | _Mapping | None = ...,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            extra_services_not_available: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamExtraServicesResponse.Success
    failure: StreamExtraServicesResponse.Failure
    def __init__(
        self,
        success: StreamExtraServicesResponse.Success | _Mapping | None = ...,
        failure: StreamExtraServicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
