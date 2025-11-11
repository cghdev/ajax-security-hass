from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import hub_index_pb2 as _hub_index_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetHubIndexesResponse(_message.Message):
    __slots__ = ("hub_indexes",)
    HUB_INDEXES_FIELD_NUMBER: _ClassVar[int]
    hub_indexes: _containers.RepeatedCompositeFieldContainer[_hub_index_pb2.HubIndex]
    def __init__(
        self, hub_indexes: _Iterable[_hub_index_pb2.HubIndex | _Mapping] | None = ...
    ) -> None: ...
