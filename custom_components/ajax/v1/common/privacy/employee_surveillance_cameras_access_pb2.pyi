from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.common.privacy import (
    surveillance_cameras_devices_pb2 as _surveillance_cameras_devices_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class EmployeeSurveillanceCamerasAccess(_message.Message):
    __slots__ = ("allowed", "not_allowed")
    class NotAllowed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Allowed(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _surveillance_cameras_devices_pb2.SurveillanceCamerasDevices
        def __init__(
            self,
            devices: _surveillance_cameras_devices_pb2.SurveillanceCamerasDevices
            | _Mapping
            | None = ...,
        ) -> None: ...

    NOT_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    not_allowed: EmployeeSurveillanceCamerasAccess.NotAllowed
    allowed: EmployeeSurveillanceCamerasAccess.Allowed
    def __init__(
        self,
        not_allowed: EmployeeSurveillanceCamerasAccess.NotAllowed
        | _Mapping
        | None = ...,
        allowed: EmployeeSurveillanceCamerasAccess.Allowed | _Mapping | None = ...,
    ) -> None: ...
