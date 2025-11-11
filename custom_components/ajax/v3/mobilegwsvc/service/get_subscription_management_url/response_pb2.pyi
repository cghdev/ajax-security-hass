from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetSubscriptionManagementUrlResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("request_id", "subscription_management_url")
        SUBSCRIPTION_MANAGEMENT_URL_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        subscription_management_url: str
        request_id: str
        def __init__(
            self,
            subscription_management_url: str | None = ...,
            request_id: str | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("available_service_not_found", "illegal_argument")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_SERVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        available_service_not_found: _response_pb2.Error
        def __init__(
            self,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            available_service_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetSubscriptionManagementUrlResponse.Success
    failure: GetSubscriptionManagementUrlResponse.Failure
    def __init__(
        self,
        success: GetSubscriptionManagementUrlResponse.Success | _Mapping | None = ...,
        failure: GetSubscriptionManagementUrlResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
