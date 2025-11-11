from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.scenario.alarm import (
    alarm_pb2 as _alarm_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmSource(_message.Message):
    __slots__ = ("alarms", "hts_alarm", "source_id")
    class HtsAlarm(_message.Message):
        __slots__ = ("hts_device_type", "hts_event_codes")
        HTS_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        HTS_EVENT_CODES_FIELD_NUMBER: _ClassVar[int]
        hts_device_type: str
        hts_event_codes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            hts_device_type: str | None = ...,
            hts_event_codes: _Iterable[str] | None = ...,
        ) -> None: ...

    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ALARMS_FIELD_NUMBER: _ClassVar[int]
    HTS_ALARM_FIELD_NUMBER: _ClassVar[int]
    source_id: str
    alarms: _containers.RepeatedCompositeFieldContainer[_alarm_pb2.Alarm]
    hts_alarm: AlarmSource.HtsAlarm
    def __init__(
        self,
        source_id: str | None = ...,
        alarms: _Iterable[_alarm_pb2.Alarm | _Mapping] | None = ...,
        hts_alarm: AlarmSource.HtsAlarm | _Mapping | None = ...,
    ) -> None: ...
