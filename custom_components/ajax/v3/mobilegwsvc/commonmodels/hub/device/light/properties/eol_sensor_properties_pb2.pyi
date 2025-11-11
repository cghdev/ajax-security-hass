from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    custom_alarm_type_pb2 as _custom_alarm_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class EolSensorProperties(_message.Message):
    __slots__ = ("eol_sensors",)
    class EolSensor(_message.Message):
        __slots__ = ("custom_alarm_type", "is_main_sensor")
        CUSTOM_ALARM_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_MAIN_SENSOR_FIELD_NUMBER: _ClassVar[int]
        custom_alarm_type: _custom_alarm_type_pb2.CustomAlarmType
        is_main_sensor: bool
        def __init__(
            self,
            custom_alarm_type: _custom_alarm_type_pb2.CustomAlarmType
            | str
            | None = ...,
            is_main_sensor: bool = ...,
        ) -> None: ...

    EOL_SENSORS_FIELD_NUMBER: _ClassVar[int]
    eol_sensors: _containers.RepeatedCompositeFieldContainer[
        EolSensorProperties.EolSensor
    ]
    def __init__(
        self,
        eol_sensors: _Iterable[EolSensorProperties.EolSensor | _Mapping] | None = ...,
    ) -> None: ...
