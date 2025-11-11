from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.scheduled_acesss import (
    scheduled_access_pb2 as _scheduled_access_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScheduledAccessRequest(_message.Message):
    __slots__ = ("hub_id", "scheduled_access")
    SCHEDULED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_access: _scheduled_access_pb2.ScheduledAccess
    hub_id: str
    def __init__(
        self,
        scheduled_access: _scheduled_access_pb2.ScheduledAccess | _Mapping | None = ...,
        hub_id: str | None = ...,
    ) -> None: ...
