from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceWarnings(_message.Message):
    __slots__ = ("warnings",)
    class WarningData(_message.Message):
        __slots__ = ("antimasking_not_calibrated", "installation_issue")
        INSTALLATION_ISSUE_FIELD_NUMBER: _ClassVar[int]
        ANTIMASKING_NOT_CALIBRATED_FIELD_NUMBER: _ClassVar[int]
        installation_issue: DeviceWarnings.InstallationIssue
        antimasking_not_calibrated: DeviceWarnings.AntimaskingNotCalibrated
        def __init__(
            self,
            installation_issue: DeviceWarnings.InstallationIssue
            | _Mapping
            | None = ...,
            antimasking_not_calibrated: DeviceWarnings.AntimaskingNotCalibrated
            | _Mapping
            | None = ...,
        ) -> None: ...

    class InstallationIssue(_message.Message):
        __slots__ = ("detection_pir_sensor",)
        class DetectionPirSensor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DETECTION_PIR_SENSOR_UNSPECIFIED: _ClassVar[
                DeviceWarnings.InstallationIssue.DetectionPirSensor
            ]
            DETECTION_PIR_SENSOR_SINGLE: _ClassVar[
                DeviceWarnings.InstallationIssue.DetectionPirSensor
            ]
            DETECTION_PIR_SENSOR_MANY: _ClassVar[
                DeviceWarnings.InstallationIssue.DetectionPirSensor
            ]

        DETECTION_PIR_SENSOR_UNSPECIFIED: (
            DeviceWarnings.InstallationIssue.DetectionPirSensor
        )
        DETECTION_PIR_SENSOR_SINGLE: DeviceWarnings.InstallationIssue.DetectionPirSensor
        DETECTION_PIR_SENSOR_MANY: DeviceWarnings.InstallationIssue.DetectionPirSensor
        DETECTION_PIR_SENSOR_FIELD_NUMBER: _ClassVar[int]
        detection_pir_sensor: DeviceWarnings.InstallationIssue.DetectionPirSensor
        def __init__(
            self,
            detection_pir_sensor: DeviceWarnings.InstallationIssue.DetectionPirSensor
            | str
            | None = ...,
        ) -> None: ...

    class AntimaskingNotCalibrated(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    warnings: _containers.RepeatedCompositeFieldContainer[DeviceWarnings.WarningData]
    def __init__(
        self, warnings: _Iterable[DeviceWarnings.WarningData | _Mapping] | None = ...
    ) -> None: ...
