from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.facility import facility_pb2 as _facility_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FacilitySearchResponse(_message.Message):
    __slots__ = ("counter", "facilities", "offset")
    FACILITIES_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    facilities: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility]
    offset: int
    counter: int
    def __init__(
        self,
        facilities: _Iterable[_facility_pb2.Facility | _Mapping] | None = ...,
        offset: int | None = ...,
        counter: int | None = ...,
    ) -> None: ...
