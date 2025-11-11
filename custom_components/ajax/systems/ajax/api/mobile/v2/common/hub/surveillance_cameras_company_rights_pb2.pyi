from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SurveillanceCamerasCompanyRights(_message.Message):
    __slots__ = ("availability_type", "shared_cameras")
    class AvailabilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_AVAILABILITY_TYPE_INFO: _ClassVar[
            SurveillanceCamerasCompanyRights.AvailabilityType
        ]
        NEVER: _ClassVar[SurveillanceCamerasCompanyRights.AvailabilityType]
        ALWAYS: _ClassVar[SurveillanceCamerasCompanyRights.AvailabilityType]

    NO_AVAILABILITY_TYPE_INFO: SurveillanceCamerasCompanyRights.AvailabilityType
    NEVER: SurveillanceCamerasCompanyRights.AvailabilityType
    ALWAYS: SurveillanceCamerasCompanyRights.AvailabilityType
    class SurveillanceCamerasDevices(_message.Message):
        __slots__ = ("device_id",)
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        device_id: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, device_id: _Iterable[str] | None = ...) -> None: ...

    SHARED_CAMERAS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    shared_cameras: SurveillanceCamerasCompanyRights.SurveillanceCamerasDevices
    availability_type: SurveillanceCamerasCompanyRights.AvailabilityType
    def __init__(
        self,
        shared_cameras: SurveillanceCamerasCompanyRights.SurveillanceCamerasDevices
        | _Mapping
        | None = ...,
        availability_type: SurveillanceCamerasCompanyRights.AvailabilityType
        | str
        | None = ...,
    ) -> None: ...
