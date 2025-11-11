from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event import (
    transition_pb2 as _transition_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import (
    notification_type_case_pb2 as _notification_type_case_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.event.hub import (
    tag_pb2 as _tag_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubEventQualifier(_message.Message):
    __slots__ = ("case", "tag", "transition")
    TAG_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    tag: _tag_pb2.HubEventTag
    transition: _transition_pb2.EventTransition
    case: _notification_type_case_pb2.Case
    def __init__(
        self,
        tag: _tag_pb2.HubEventTag | _Mapping | None = ...,
        transition: _transition_pb2.EventTransition | _Mapping | None = ...,
        case: _notification_type_case_pb2.Case | str | None = ...,
    ) -> None: ...
