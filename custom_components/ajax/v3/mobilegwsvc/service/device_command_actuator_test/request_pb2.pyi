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

class DeviceCommandActuatorTestRequest(_message.Message):
    __slots__ = ("actuator_test_option", "device_id", "device_type", "hub_id")
    class ActuatorTestFormatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTUATOR_TEST_FORMAT_TYPE_UNSPECIFIED: _ClassVar[
            DeviceCommandActuatorTestRequest.ActuatorTestFormatType
        ]
        ACTUATOR_TEST_FORMAT_TYPE_ACTUATOR_ENDPOINTS: _ClassVar[
            DeviceCommandActuatorTestRequest.ActuatorTestFormatType
        ]

    ACTUATOR_TEST_FORMAT_TYPE_UNSPECIFIED: (
        DeviceCommandActuatorTestRequest.ActuatorTestFormatType
    )
    ACTUATOR_TEST_FORMAT_TYPE_ACTUATOR_ENDPOINTS: (
        DeviceCommandActuatorTestRequest.ActuatorTestFormatType
    )
    class ActuatorTestEndpoints(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTUATOR_TEST_ENDPOINTS_UNSPECIFIED: _ClassVar[
            DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
        ]
        ACTUATOR_TEST_ENDPOINTS_SOUNDER: _ClassVar[
            DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
        ]
        ACTUATOR_TEST_ENDPOINTS_VAD: _ClassVar[
            DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
        ]

    ACTUATOR_TEST_ENDPOINTS_UNSPECIFIED: (
        DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
    )
    ACTUATOR_TEST_ENDPOINTS_SOUNDER: (
        DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
    )
    ACTUATOR_TEST_ENDPOINTS_VAD: DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
    class ActuatorTestOption(_message.Message):
        __slots__ = (
            "actuator_test_action",
            "actuator_test_endpoints",
            "actuator_test_format_type",
        )
        ACTUATOR_TEST_FORMAT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ACTUATOR_TEST_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        ACTUATOR_TEST_ACTION_FIELD_NUMBER: _ClassVar[int]
        actuator_test_format_type: (
            DeviceCommandActuatorTestRequest.ActuatorTestFormatType
        )
        actuator_test_endpoints: _containers.RepeatedScalarFieldContainer[
            DeviceCommandActuatorTestRequest.ActuatorTestEndpoints
        ]
        actuator_test_action: DeviceCommandActuatorTestRequest.ActuatorTestAction
        def __init__(
            self,
            actuator_test_format_type: DeviceCommandActuatorTestRequest.ActuatorTestFormatType
            | str
            | None = ...,
            actuator_test_endpoints: _Iterable[
                DeviceCommandActuatorTestRequest.ActuatorTestEndpoints | str
            ]
            | None = ...,
            actuator_test_action: DeviceCommandActuatorTestRequest.ActuatorTestAction
            | _Mapping
            | None = ...,
        ) -> None: ...

    class ActuatorTestAction(_message.Message):
        __slots__ = ("actuator_test_start", "actuator_test_stop")
        ACTUATOR_TEST_START_FIELD_NUMBER: _ClassVar[int]
        ACTUATOR_TEST_STOP_FIELD_NUMBER: _ClassVar[int]
        actuator_test_start: DeviceCommandActuatorTestRequest.ActuatorTestStart
        actuator_test_stop: DeviceCommandActuatorTestRequest.ActuatorTestStop
        def __init__(
            self,
            actuator_test_start: DeviceCommandActuatorTestRequest.ActuatorTestStart
            | _Mapping
            | None = ...,
            actuator_test_stop: DeviceCommandActuatorTestRequest.ActuatorTestStop
            | _Mapping
            | None = ...,
        ) -> None: ...

    class ActuatorTestStart(_message.Message):
        __slots__ = ("seconds_for_test",)
        SECONDS_FOR_TEST_FIELD_NUMBER: _ClassVar[int]
        seconds_for_test: int
        def __init__(self, seconds_for_test: int | None = ...) -> None: ...

    class ActuatorTestStop(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTUATOR_TEST_OPTION_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    device_type: _object_type_pb2.ObjectType
    actuator_test_option: DeviceCommandActuatorTestRequest.ActuatorTestOption
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        actuator_test_option: DeviceCommandActuatorTestRequest.ActuatorTestOption
        | _Mapping
        | None = ...,
    ) -> None: ...
