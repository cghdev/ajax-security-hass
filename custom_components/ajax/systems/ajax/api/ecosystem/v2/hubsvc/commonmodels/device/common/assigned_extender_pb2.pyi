from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    connection_status_pb2 as _connection_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AssignedExtender(_message.Message):
    __slots__ = ("capabilities", "extender_info")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[AssignedExtender.Capability]
        CAPABILITY_REX: _ClassVar[AssignedExtender.Capability]
        CAPABILITY_REX2: _ClassVar[AssignedExtender.Capability]

    CAPABILITY_UNSPECIFIED: AssignedExtender.Capability
    CAPABILITY_REX: AssignedExtender.Capability
    CAPABILITY_REX2: AssignedExtender.Capability
    class ExtenderInfo(_message.Message):
        __slots__ = ("connection_status", "device_index", "id", "name", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[AssignedExtender.ExtenderInfo.Type]
            TYPE_REX: _ClassVar[AssignedExtender.ExtenderInfo.Type]
            TYPE_REX2: _ClassVar[AssignedExtender.ExtenderInfo.Type]
            TYPE_REX2_S: _ClassVar[AssignedExtender.ExtenderInfo.Type]

        TYPE_UNSPECIFIED: AssignedExtender.ExtenderInfo.Type
        TYPE_REX: AssignedExtender.ExtenderInfo.Type
        TYPE_REX2: AssignedExtender.ExtenderInfo.Type
        TYPE_REX2_S: AssignedExtender.ExtenderInfo.Type
        ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        device_index: int
        name: str
        connection_status: _connection_status_pb2.ConnectionStatus
        type: AssignedExtender.ExtenderInfo.Type
        def __init__(
            self,
            id: str | None = ...,
            device_index: int | None = ...,
            name: str | None = ...,
            connection_status: _connection_status_pb2.ConnectionStatus
            | str
            | None = ...,
            type: AssignedExtender.ExtenderInfo.Type | str | None = ...,
        ) -> None: ...

    EXTENDER_INFO_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    extender_info: AssignedExtender.ExtenderInfo
    capabilities: _containers.RepeatedScalarFieldContainer[AssignedExtender.Capability]
    def __init__(
        self,
        extender_info: AssignedExtender.ExtenderInfo | _Mapping | None = ...,
        capabilities: _Iterable[AssignedExtender.Capability | str] | None = ...,
    ) -> None: ...
