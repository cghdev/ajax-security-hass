from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandSamplePlayRequest(_message.Message):
    __slots__ = ("device_id", "hub_id", "object_type", "sample_play")
    class SamplePlay(_message.Message):
        __slots__ = ("audio_sample_index", "repeat_count")
        AUDIO_SAMPLE_INDEX_FIELD_NUMBER: _ClassVar[int]
        REPEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
        audio_sample_index: int
        repeat_count: int
        def __init__(
            self, audio_sample_index: int | None = ..., repeat_count: int | None = ...
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_PLAY_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    device_id: str
    object_type: _object_type_pb2.ObjectType
    sample_play: DeviceCommandSamplePlayRequest.SamplePlay
    def __init__(
        self,
        hub_id: str | None = ...,
        device_id: str | None = ...,
        object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        sample_play: DeviceCommandSamplePlayRequest.SamplePlay | _Mapping | None = ...,
    ) -> None: ...
