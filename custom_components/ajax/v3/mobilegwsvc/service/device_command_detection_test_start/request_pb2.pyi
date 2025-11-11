from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)
from v3.mobilegwsvc.commonmodels.sensor import (
    detection_zone_test_sensor_pb2 as _detection_zone_test_sensor_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandDetectionTestStartRequest(_message.Message):
    __slots__ = (
        "additional_param",
        "device_id",
        "device_sensor",
        "hub_id",
        "object_type",
    )
    class Outdoor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTDOOR_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_UPPER_PIR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_LOWER_PIR: _ClassVar[DeviceCommandDetectionTestStartRequest.Outdoor]
        OUTDOOR_MASKING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.Outdoor
        ]

    OUTDOOR_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_UPPER_PIR: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_LOWER_PIR: DeviceCommandDetectionTestStartRequest.Outdoor
    OUTDOOR_MASKING_SENSOR: DeviceCommandDetectionTestStartRequest.Outdoor
    class Curtain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURTAIN_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.Curtain]
        CURTAIN_MOVING_SENSOR: _ClassVar[DeviceCommandDetectionTestStartRequest.Curtain]
        CURTAIN_MASKING_SENSORS: _ClassVar[
            DeviceCommandDetectionTestStartRequest.Curtain
        ]

    CURTAIN_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.Curtain
    CURTAIN_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.Curtain
    CURTAIN_MASKING_SENSORS: DeviceCommandDetectionTestStartRequest.Curtain
    class DualCurtain(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DUAL_CURTAIN_UNSPECIFIED: _ClassVar[
            DeviceCommandDetectionTestStartRequest.DualCurtain
        ]
        DUAL_CURTAIN_ALL_PIR_SENSORS: _ClassVar[
            DeviceCommandDetectionTestStartRequest.DualCurtain
        ]
        DUAL_CURTAIN_UPPER_PIR_SENSORS: _ClassVar[
            DeviceCommandDetectionTestStartRequest.DualCurtain
        ]
        DUAL_CURTAIN_LOWER_PIR_SENSORS: _ClassVar[
            DeviceCommandDetectionTestStartRequest.DualCurtain
        ]
        DUAL_CURTAIN_MASKING_SENSORS: _ClassVar[
            DeviceCommandDetectionTestStartRequest.DualCurtain
        ]

    DUAL_CURTAIN_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_ALL_PIR_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_UPPER_PIR_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_LOWER_PIR_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    DUAL_CURTAIN_MASKING_SENSORS: DeviceCommandDetectionTestStartRequest.DualCurtain
    class ButtonS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUTTON_S_UNSPECIFIED: _ClassVar[DeviceCommandDetectionTestStartRequest.ButtonS]
        BUTTON_S_BUTTON_TEST: _ClassVar[DeviceCommandDetectionTestStartRequest.ButtonS]

    BUTTON_S_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.ButtonS
    BUTTON_S_BUTTON_TEST: DeviceCommandDetectionTestStartRequest.ButtonS
    class CurtainOutdoor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURTAIN_OUTDOOR_UNSPECIFIED: _ClassVar[
            DeviceCommandDetectionTestStartRequest.CurtainOutdoor
        ]
        CURTAIN_OUTDOOR_MOVING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.CurtainOutdoor
        ]
        CURTAIN_OUTDOOR_MASKING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.CurtainOutdoor
        ]

    CURTAIN_OUTDOOR_UNSPECIFIED: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
    CURTAIN_OUTDOOR_MOVING_SENSOR: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
    CURTAIN_OUTDOOR_MASKING_SENSOR: (
        DeviceCommandDetectionTestStartRequest.CurtainOutdoor
    )
    class MotionProtectG3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOTION_PROTECT_G3_UNSPECIFIED: _ClassVar[
            DeviceCommandDetectionTestStartRequest.MotionProtectG3
        ]
        MOTION_PROTECT_G3_MOVING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.MotionProtectG3
        ]
        MOTION_PROTECT_G3_MASKING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.MotionProtectG3
        ]

    MOTION_PROTECT_G3_UNSPECIFIED: (
        DeviceCommandDetectionTestStartRequest.MotionProtectG3
    )
    MOTION_PROTECT_G3_MOVING_SENSOR: (
        DeviceCommandDetectionTestStartRequest.MotionProtectG3
    )
    MOTION_PROTECT_G3_MASKING_SENSOR: (
        DeviceCommandDetectionTestStartRequest.MotionProtectG3
    )
    class MotionCamSPhodAm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOTION_CAM_S_PHOD_AM_UNSPECIFIED: _ClassVar[
            DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
        ]
        MOTION_CAM_S_PHOD_AM_MOVING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
        ]
        MOTION_CAM_S_PHOD_AM_MASKING_SENSOR: _ClassVar[
            DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
        ]

    MOTION_CAM_S_PHOD_AM_UNSPECIFIED: (
        DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
    )
    MOTION_CAM_S_PHOD_AM_MOVING_SENSOR: (
        DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
    )
    MOTION_CAM_S_PHOD_AM_MASKING_SENSOR: (
        DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
    )
    class AdditionalParam(_message.Message):
        __slots__ = (
            "button_s",
            "curtain",
            "curtain_outdoor",
            "dual_curtain",
            "motion_cam_s_phod_am",
            "motion_protect_g3",
            "outdoor",
        )
        OUTDOOR_FIELD_NUMBER: _ClassVar[int]
        CURTAIN_FIELD_NUMBER: _ClassVar[int]
        DUAL_CURTAIN_FIELD_NUMBER: _ClassVar[int]
        BUTTON_S_FIELD_NUMBER: _ClassVar[int]
        CURTAIN_OUTDOOR_FIELD_NUMBER: _ClassVar[int]
        MOTION_PROTECT_G3_FIELD_NUMBER: _ClassVar[int]
        MOTION_CAM_S_PHOD_AM_FIELD_NUMBER: _ClassVar[int]
        outdoor: DeviceCommandDetectionTestStartRequest.Outdoor
        curtain: DeviceCommandDetectionTestStartRequest.Curtain
        dual_curtain: DeviceCommandDetectionTestStartRequest.DualCurtain
        button_s: DeviceCommandDetectionTestStartRequest.ButtonS
        curtain_outdoor: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
        motion_protect_g3: DeviceCommandDetectionTestStartRequest.MotionProtectG3
        motion_cam_s_phod_am: DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
        def __init__(
            self,
            outdoor: DeviceCommandDetectionTestStartRequest.Outdoor | str | None = ...,
            curtain: DeviceCommandDetectionTestStartRequest.Curtain | str | None = ...,
            dual_curtain: DeviceCommandDetectionTestStartRequest.DualCurtain
            | str
            | None = ...,
            button_s: DeviceCommandDetectionTestStartRequest.ButtonS | str | None = ...,
            curtain_outdoor: DeviceCommandDetectionTestStartRequest.CurtainOutdoor
            | str
            | None = ...,
            motion_protect_g3: DeviceCommandDetectionTestStartRequest.MotionProtectG3
            | str
            | None = ...,
            motion_cam_s_phod_am: DeviceCommandDetectionTestStartRequest.MotionCamSPhodAm
            | str
            | None = ...,
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    additional_param: DeviceCommandDetectionTestStartRequest.AdditionalParam
    device_sensor: _detection_zone_test_sensor_pb2.DeviceSensor
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        additional_param: DeviceCommandDetectionTestStartRequest.AdditionalParam
        | _Mapping
        | None = ...,
        device_sensor: _detection_zone_test_sensor_pb2.DeviceSensor
        | _Mapping
        | None = ...,
    ) -> None: ...
