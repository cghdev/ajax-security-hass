from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDisablementRequest(_message.Message):
    __slots__ = ("device_id", "device_type", "en54_disablement_endpoints", "hub_id")
    class En54DisablementEndpoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EN54_DISABLEMENT_ENDPOINT_UNSPECIFIED: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_SMOKE: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_TEMPERATURE: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_SOUNDER: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_VAD: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_OUTPUT_1: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_OUTPUT_2: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_INPUT: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]
        EN54_DISABLEMENT_ENDPOINT_MCP: _ClassVar[
            DeviceCommandDisablementRequest.En54DisablementEndpoint
        ]

    EN54_DISABLEMENT_ENDPOINT_UNSPECIFIED: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_SMOKE: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_TEMPERATURE: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_SOUNDER: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_VAD: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_OUTPUT_1: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_OUTPUT_2: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_INPUT: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    EN54_DISABLEMENT_ENDPOINT_MCP: (
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    )
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EN54_DISABLEMENT_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    en54_disablement_endpoints: _containers.RepeatedScalarFieldContainer[
        DeviceCommandDisablementRequest.En54DisablementEndpoint
    ]
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        en54_disablement_endpoints: _Iterable[
            DeviceCommandDisablementRequest.En54DisablementEndpoint | str
        ]
        | None = ...,
    ) -> None: ...
