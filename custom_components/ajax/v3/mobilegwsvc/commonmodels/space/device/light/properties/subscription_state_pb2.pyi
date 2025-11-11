from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    service_state_pb2 as _service_state_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionState(_message.Message):
    __slots__ = ("service_state",)
    SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    service_state: _service_state_pb2.ServiceState
    def __init__(
        self, service_state: _service_state_pb2.ServiceState | str | None = ...
    ) -> None: ...
