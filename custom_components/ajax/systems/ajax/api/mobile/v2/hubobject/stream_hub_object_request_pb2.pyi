from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.hubobject.model import hub_object_pb2 as _hub_object_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubObjectRequest(_message.Message):
    __slots__ = ("hex_id",)
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    def __init__(self, hex_id: str | None = ...) -> None: ...

class StreamHubObject(_message.Message):
    __slots__ = ("create", "delete", "snapshot", "update")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    snapshot: _hub_object_pb2.HubObject
    create: _hub_object_pb2.HubObject
    update: _hub_object_pb2.HubObject
    delete: _hub_object_pb2.HubObject
    def __init__(
        self,
        snapshot: _hub_object_pb2.HubObject | _Mapping | None = ...,
        create: _hub_object_pb2.HubObject | _Mapping | None = ...,
        update: _hub_object_pb2.HubObject | _Mapping | None = ...,
        delete: _hub_object_pb2.HubObject | _Mapping | None = ...,
    ) -> None: ...
