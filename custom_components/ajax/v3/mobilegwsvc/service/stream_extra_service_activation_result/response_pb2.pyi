from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.accounting import (
    extra_service_pb2 as _extra_service_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamExtraServiceActivationResultResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "extra_service_activated",
            "extra_service_activation_in_progress",
            "extra_service_failed_to_activate",
        )
        EXTRA_SERVICE_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_FAILED_TO_ACTIVATE_FIELD_NUMBER: _ClassVar[int]
        EXTRA_SERVICE_ACTIVATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        extra_service_activated: (
            StreamExtraServiceActivationResultResponse.ExtraServiceActivated
        )
        extra_service_failed_to_activate: (
            StreamExtraServiceActivationResultResponse.ExtraServiceFailedToActivate
        )
        extra_service_activation_in_progress: (
            StreamExtraServiceActivationResultResponse.ExtraServiceActivationInProgress
        )
        def __init__(
            self,
            extra_service_activated: StreamExtraServiceActivationResultResponse.ExtraServiceActivated
            | _Mapping
            | None = ...,
            extra_service_failed_to_activate: StreamExtraServiceActivationResultResponse.ExtraServiceFailedToActivate
            | _Mapping
            | None = ...,
            extra_service_activation_in_progress: StreamExtraServiceActivationResultResponse.ExtraServiceActivationInProgress
            | _Mapping
            | None = ...,
        ) -> None: ...

    class ExtraServiceActivated(_message.Message):
        __slots__ = ("new_extra_service",)
        NEW_EXTRA_SERVICE_FIELD_NUMBER: _ClassVar[int]
        new_extra_service: _extra_service_pb2.ExtraService
        def __init__(
            self,
            new_extra_service: _extra_service_pb2.ExtraService | _Mapping | None = ...,
        ) -> None: ...

    class ExtraServiceFailedToActivate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ExtraServiceActivationInProgress(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "message", "request_timeout")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        message: str
        request_timeout: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        def __init__(
            self,
            message: str | None = ...,
            request_timeout: _response_pb2.Error | _Mapping | None = ...,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamExtraServiceActivationResultResponse.Success
    failure: StreamExtraServiceActivationResultResponse.Failure
    def __init__(
        self,
        success: StreamExtraServiceActivationResultResponse.Success
        | _Mapping
        | None = ...,
        failure: StreamExtraServiceActivationResultResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
