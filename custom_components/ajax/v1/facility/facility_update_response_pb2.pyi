from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.facility import facility_pb2 as _facility_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityUpdateResponse(_message.Message):
    __slots__ = ("facility", "notes")
    FACILITY_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    facility: _facility_pb2.Facility
    notes: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility.Note]
    def __init__(
        self,
        facility: _facility_pb2.Facility | _Mapping | None = ...,
        notes: _Iterable[_facility_pb2.Facility.Note | _Mapping] | None = ...,
    ) -> None: ...
