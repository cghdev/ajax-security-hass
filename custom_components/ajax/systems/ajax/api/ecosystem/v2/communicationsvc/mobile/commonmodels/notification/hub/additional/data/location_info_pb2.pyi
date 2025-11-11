from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LocationInfo(_message.Message):
    __slots__ = ("acc", "latitude", "longitude", "speed", "time")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ACC_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    latitude: str
    longitude: str
    acc: float
    speed: float
    time: _timestamp_pb2.Timestamp
    def __init__(
        self,
        latitude: str | None = ...,
        longitude: str | None = ...,
        acc: float | None = ...,
        speed: float | None = ...,
        time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
    ) -> None: ...
