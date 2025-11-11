from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    update_pb2 as _update_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateHubDeviceRequest(_message.Message):
    __slots__ = ("device_id", "hub_id", "object_type", "update")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    update: _containers.RepeatedCompositeFieldContainer[_update_pb2.Update]
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        update: _Iterable[_update_pb2.Update | _Mapping] | None = ...,
    ) -> None: ...
