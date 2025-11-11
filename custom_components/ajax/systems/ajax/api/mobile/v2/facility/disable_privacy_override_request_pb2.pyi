from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DisablePrivacyOverrideRequest(_message.Message):
    __slots__ = ("facility_id",)
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    facility_id: str
    def __init__(self, facility_id: str | None = ...) -> None: ...

class DisablePrivacyOverrideResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "already_processed",
            "bad_request",
            "facility_not_found",
            "hub_is_armed",
            "hub_is_offline",
            "message",
            "permission_denied",
        )
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        FACILITY_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_ARMED_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        ALREADY_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        facility_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        hub_is_armed: _response_pb2.DefaultError
        hub_is_offline: _response_pb2.DefaultError
        already_processed: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            facility_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_is_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            already_processed: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DisablePrivacyOverrideResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: DisablePrivacyOverrideResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
