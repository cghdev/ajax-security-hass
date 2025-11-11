from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CancelTemporaryVideoEdgeChannelPermissionsRequest(_message.Message):
    __slots__ = ("assignee_id", "space_locator")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_ID_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    assignee_id: str
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        assignee_id: str | None = ...,
    ) -> None: ...
