from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import (
    qualifier_pb2 as _qualifier_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Alarm(_message.Message):
    __slots__ = ("hub_alarm",)
    HUB_ALARM_FIELD_NUMBER: _ClassVar[int]
    hub_alarm: _qualifier_pb2.HubEventQualifier
    def __init__(
        self, hub_alarm: _qualifier_pb2.HubEventQualifier | _Mapping | None = ...
    ) -> None: ...
