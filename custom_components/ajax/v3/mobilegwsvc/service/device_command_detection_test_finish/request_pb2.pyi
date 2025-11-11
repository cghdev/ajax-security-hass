from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDetectionTestFinishRequest(_message.Message):
    __slots__ = (
        "device_detection_zone_test_finish",
        "device_id",
        "hub_detection_zone_test_finish",
        "hub_id",
        "object_type",
    )
    class HubDetectionZoneTestFinish(_message.Message):
        __slots__ = ("hub_id",)
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        def __init__(self, hub_id: str | None = ...) -> None: ...

    class DeviceDetectionZoneTestFinish(_message.Message):
        __slots__ = ("device_id", "hub_id", "object_type")
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        device_id: str
        object_type: _object_type_pb2.ObjectType
        def __init__(
            self,
            hub_id: str | None = ...,
            device_id: str | None = ...,
            object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HUB_DETECTION_ZONE_TEST_FINISH_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETECTION_ZONE_TEST_FINISH_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    hub_detection_zone_test_finish: (
        DeviceCommandDetectionTestFinishRequest.HubDetectionZoneTestFinish
    )
    device_detection_zone_test_finish: (
        DeviceCommandDetectionTestFinishRequest.DeviceDetectionZoneTestFinish
    )
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        hub_detection_zone_test_finish: DeviceCommandDetectionTestFinishRequest.HubDetectionZoneTestFinish
        | _Mapping
        | None = ...,
        device_detection_zone_test_finish: DeviceCommandDetectionTestFinishRequest.DeviceDetectionZoneTestFinish
        | _Mapping
        | None = ...,
    ) -> None: ...
