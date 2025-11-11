from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.sensor import (
    detection_zone_test_sensor_pb2 as _detection_zone_test_sensor_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDetectionZoneTestResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "trigger_event", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_EVENT_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDetectionZoneTestResponse.Snapshot
        update: StreamDetectionZoneTestResponse.Update
        trigger_event: StreamDetectionZoneTestResponse.TriggerEvent
        def __init__(
            self,
            snapshot: StreamDetectionZoneTestResponse.Snapshot | _Mapping | None = ...,
            update: StreamDetectionZoneTestResponse.Update | _Mapping | None = ...,
            trigger_event: StreamDetectionZoneTestResponse.TriggerEvent
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Snapshot(_message.Message):
        __slots__ = ("statuses",)
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        statuses: _containers.RepeatedCompositeFieldContainer[
            StreamDetectionZoneTestResponse.DeviceStatus
        ]
        def __init__(
            self,
            statuses: _Iterable[StreamDetectionZoneTestResponse.DeviceStatus | _Mapping]
            | None = ...,
        ) -> None: ...

    class Update(_message.Message):
        __slots__ = ("statuses",)
        STATUSES_FIELD_NUMBER: _ClassVar[int]
        statuses: _containers.RepeatedCompositeFieldContainer[
            StreamDetectionZoneTestResponse.DeviceStatus
        ]
        def __init__(
            self,
            statuses: _Iterable[StreamDetectionZoneTestResponse.DeviceStatus | _Mapping]
            | None = ...,
        ) -> None: ...

    class TriggerEvent(_message.Message):
        __slots__ = ("device_id", "message_info")
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_INFO_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        message_info: StreamDetectionZoneTestResponse.MessageInfo
        def __init__(
            self,
            device_id: str | None = ...,
            message_info: StreamDetectionZoneTestResponse.MessageInfo
            | _Mapping
            | None = ...,
        ) -> None: ...

    class DeviceStatus(_message.Message):
        __slots__ = ("device_id", "device_sensors", "device_test_status")
        class DeviceTestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEVICE_TEST_STATUS_UNSPECIFIED: _ClassVar[
                StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
            ]
            DEVICE_TEST_STATUS_INACTIVE: _ClassVar[
                StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
            ]
            DEVICE_TEST_STATUS_AWAITING_START: _ClassVar[
                StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
            ]
            DEVICE_TEST_STATUS_IN_PROGRESS: _ClassVar[
                StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
            ]
            DEVICE_TEST_STATUS_AWAITING_FINISH: _ClassVar[
                StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
            ]

        DEVICE_TEST_STATUS_UNSPECIFIED: (
            StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        )
        DEVICE_TEST_STATUS_INACTIVE: (
            StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        )
        DEVICE_TEST_STATUS_AWAITING_START: (
            StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        )
        DEVICE_TEST_STATUS_IN_PROGRESS: (
            StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        )
        DEVICE_TEST_STATUS_AWAITING_FINISH: (
            StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        )
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SENSORS_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        device_test_status: (
            StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
        )
        device_sensors: _containers.RepeatedCompositeFieldContainer[
            _detection_zone_test_sensor_pb2.DeviceSensor
        ]
        def __init__(
            self,
            device_id: str | None = ...,
            device_test_status: StreamDetectionZoneTestResponse.DeviceStatus.DeviceTestStatus
            | str
            | None = ...,
            device_sensors: _Iterable[
                _detection_zone_test_sensor_pb2.DeviceSensor | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class MessageInfo(_message.Message):
        __slots__ = ("device_name", "room_name", "trigger_type")
        class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TRIGGER_TYPE_UNSPECIFIED: _ClassVar[
                StreamDetectionZoneTestResponse.MessageInfo.TriggerType
            ]
            TRIGGER_TYPE_DEVICE: _ClassVar[
                StreamDetectionZoneTestResponse.MessageInfo.TriggerType
            ]
            TRIGGER_TYPE_LEFT_SIDE: _ClassVar[
                StreamDetectionZoneTestResponse.MessageInfo.TriggerType
            ]
            TRIGGER_TYPE_RIGHT_SIDE: _ClassVar[
                StreamDetectionZoneTestResponse.MessageInfo.TriggerType
            ]

        TRIGGER_TYPE_UNSPECIFIED: (
            StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        )
        TRIGGER_TYPE_DEVICE: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        TRIGGER_TYPE_LEFT_SIDE: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        TRIGGER_TYPE_RIGHT_SIDE: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
        device_name: str
        room_name: str
        trigger_type: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
        def __init__(
            self,
            device_name: str | None = ...,
            room_name: str | None = ...,
            trigger_type: StreamDetectionZoneTestResponse.MessageInfo.TriggerType
            | str
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDetectionZoneTestResponse.Success
    failure: StreamDetectionZoneTestResponse.Failure
    def __init__(
        self,
        success: StreamDetectionZoneTestResponse.Success | _Mapping | None = ...,
        failure: StreamDetectionZoneTestResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
