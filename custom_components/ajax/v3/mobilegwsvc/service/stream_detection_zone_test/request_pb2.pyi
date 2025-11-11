from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDetectionZoneTestRequest(_message.Message):
    __slots__ = ("device_detection_zone_test", "hub_detection_zone_test")
    class HubDetectionZoneTest(_message.Message):
        __slots__ = ("hub_id",)
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        def __init__(self, hub_id: str | None = ...) -> None: ...

    class DeviceDetectionZoneTest(_message.Message):
        __slots__ = ("device_id", "hub_id")
        HUB_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        hub_id: str
        device_id: str
        def __init__(
            self, hub_id: str | None = ..., device_id: str | None = ...
        ) -> None: ...

    HUB_DETECTION_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETECTION_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    hub_detection_zone_test: StreamDetectionZoneTestRequest.HubDetectionZoneTest
    device_detection_zone_test: StreamDetectionZoneTestRequest.DeviceDetectionZoneTest
    def __init__(
        self,
        hub_detection_zone_test: StreamDetectionZoneTestRequest.HubDetectionZoneTest
        | _Mapping
        | None = ...,
        device_detection_zone_test: StreamDetectionZoneTestRequest.DeviceDetectionZoneTest
        | _Mapping
        | None = ...,
    ) -> None: ...
