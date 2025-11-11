from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import (
    common_arming_part_pb2 as _common_arming_part_pb2,
)
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from v3.mobilegwsvc.commonmodels.hub.device import (
    motion_cam_video_base_pb2 as _motion_cam_video_base_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeIntrusionSettingsRequest(_message.Message):
    __slots__ = (
        "alarm_delay_seconds",
        "arm_delay_seconds",
        "arming_mode",
        "night_mode_alarm_delay_seconds",
        "night_mode_arm_delay_seconds",
        "siren_triggers",
        "space_locator",
        "video_edge_id",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    arm_delay_seconds: int
    alarm_delay_seconds: int
    night_mode_arm_delay_seconds: int
    night_mode_alarm_delay_seconds: int
    arming_mode: _common_arming_part_pb2.CommonArmingPart.ArmingMode
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        _motion_cam_video_base_pb2.MotionCamVideoBase.SirenTrigger
    ]
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_id: str | None = ...,
        arm_delay_seconds: int | None = ...,
        alarm_delay_seconds: int | None = ...,
        night_mode_arm_delay_seconds: int | None = ...,
        night_mode_alarm_delay_seconds: int | None = ...,
        arming_mode: _common_arming_part_pb2.CommonArmingPart.ArmingMode
        | str
        | None = ...,
        siren_triggers: _Iterable[
            _motion_cam_video_base_pb2.MotionCamVideoBase.SirenTrigger | str
        ]
        | None = ...,
    ) -> None: ...
