from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from v3.mobilegwsvc.commonmodels.hub.device import (
    motion_cam_video_base_pb2 as _motion_cam_video_base_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeChimeSettingsRequest(_message.Message):
    __slots__ = ("chime", "space_locator", "video_edge_id")
    class Chime(_message.Message):
        __slots__ = ("digital", "mechanical", "off", "siren")
        class OffMode(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class MechanicalMode(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: _duration_pb2.Duration
            def __init__(
                self, duration: _duration_pb2.Duration | _Mapping | None = ...
            ) -> None: ...

        class DigitalMode(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: _duration_pb2.Duration
            def __init__(
                self, duration: _duration_pb2.Duration | _Mapping | None = ...
            ) -> None: ...

        class SirenMode(_message.Message):
            __slots__ = ("chime_signal", "chime_triggers")
            CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
            CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
            chime_triggers: _containers.RepeatedScalarFieldContainer[
                _motion_cam_video_base_pb2.MotionCamVideoBase.ChimeTrigger
            ]
            chime_signal: int
            def __init__(
                self,
                chime_triggers: _Iterable[
                    _motion_cam_video_base_pb2.MotionCamVideoBase.ChimeTrigger | str
                ]
                | None = ...,
                chime_signal: int | None = ...,
            ) -> None: ...

        OFF_FIELD_NUMBER: _ClassVar[int]
        MECHANICAL_FIELD_NUMBER: _ClassVar[int]
        DIGITAL_FIELD_NUMBER: _ClassVar[int]
        SIREN_FIELD_NUMBER: _ClassVar[int]
        off: SetVideoEdgeChimeSettingsRequest.Chime.OffMode
        mechanical: SetVideoEdgeChimeSettingsRequest.Chime.MechanicalMode
        digital: SetVideoEdgeChimeSettingsRequest.Chime.DigitalMode
        siren: SetVideoEdgeChimeSettingsRequest.Chime.SirenMode
        def __init__(
            self,
            off: SetVideoEdgeChimeSettingsRequest.Chime.OffMode | _Mapping | None = ...,
            mechanical: SetVideoEdgeChimeSettingsRequest.Chime.MechanicalMode
            | _Mapping
            | None = ...,
            digital: SetVideoEdgeChimeSettingsRequest.Chime.DigitalMode
            | _Mapping
            | None = ...,
            siren: SetVideoEdgeChimeSettingsRequest.Chime.SirenMode
            | _Mapping
            | None = ...,
        ) -> None: ...

    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHIME_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    chime: SetVideoEdgeChimeSettingsRequest.Chime
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_id: str | None = ...,
        chime: SetVideoEdgeChimeSettingsRequest.Chime | _Mapping | None = ...,
    ) -> None: ...
