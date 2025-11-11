from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandTurnEthernetRequest(_message.Message):
    __slots__ = ("device_id", "device_type", "hub_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DeviceCommandTurnEthernetRequest.State]
        STATE_OFF: _ClassVar[DeviceCommandTurnEthernetRequest.State]
        STATE_ON: _ClassVar[DeviceCommandTurnEthernetRequest.State]

    STATE_UNSPECIFIED: DeviceCommandTurnEthernetRequest.State
    STATE_OFF: DeviceCommandTurnEthernetRequest.State
    STATE_ON: DeviceCommandTurnEthernetRequest.State
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    state: DeviceCommandTurnEthernetRequest.State
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        state: DeviceCommandTurnEthernetRequest.State | str | None = ...,
    ) -> None: ...
