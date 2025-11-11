from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_profile_pb2 as _light_device_profile_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LightCommonHubDevice(_message.Message):
    __slots__ = ("hub_id", "object_type", "profile")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    profile: _light_device_profile_pb2.LightDeviceProfile
    hub_id: str
    object_type: _object_type_pb2.ObjectType
    def __init__(
        self,
        profile: _light_device_profile_pb2.LightDeviceProfile | _Mapping | None = ...,
        hub_id: str | None = ...,
        object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
    ) -> None: ...
