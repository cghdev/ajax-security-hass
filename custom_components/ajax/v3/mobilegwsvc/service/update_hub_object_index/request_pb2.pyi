from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.hub.object import (
    hub_object_type_with_index_pb2 as _hub_object_type_with_index_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateHubObjectIndexRequest(_message.Message):
    __slots__ = ("hub_id", "hub_object_type_with_index", "index", "object_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_OBJECT_TYPE_WITH_INDEX_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    hub_object_type_with_index: _hub_object_type_with_index_pb2.HubObjectTypeWithIndex
    object_id: str
    index: int
    def __init__(
        self,
        hub_id: str | None = ...,
        hub_object_type_with_index: _hub_object_type_with_index_pb2.HubObjectTypeWithIndex
        | str
        | None = ...,
        object_id: str | None = ...,
        index: int | None = ...,
    ) -> None: ...
