from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceSecurityTransitionFailure(_message.Message):
    __slots__ = (
        "cancelled",
        "hub_alarm_reset_required",
        "hub_blocked_by_service_provider",
        "hub_busy",
        "hub_detected_malfunctions",
        "hub_offline",
        "timed_out",
    )
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
    HUB_BLOCKED_BY_SERVICE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    HUB_ALARM_RESET_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    HUB_DETECTED_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    timed_out: _response_pb2.DefaultError
    cancelled: _response_pb2.DefaultError
    hub_offline: _response_pb2.DefaultError
    hub_busy: _response_pb2.DefaultError
    hub_blocked_by_service_provider: _response_pb2.DefaultError
    hub_alarm_reset_required: _response_pb2.DefaultError
    hub_detected_malfunctions: _response_pb2.HubDetectedMalfunctionsError
    def __init__(
        self,
        timed_out: _response_pb2.DefaultError | _Mapping | None = ...,
        cancelled: _response_pb2.DefaultError | _Mapping | None = ...,
        hub_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        hub_busy: _response_pb2.DefaultError | _Mapping | None = ...,
        hub_blocked_by_service_provider: _response_pb2.DefaultError
        | _Mapping
        | None = ...,
        hub_alarm_reset_required: _response_pb2.DefaultError | _Mapping | None = ...,
        hub_detected_malfunctions: _response_pb2.HubDetectedMalfunctionsError
        | _Mapping
        | None = ...,
    ) -> None: ...
