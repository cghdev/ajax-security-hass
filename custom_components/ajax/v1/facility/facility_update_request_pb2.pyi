from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.facility import facility_pb2 as _facility_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityUpdateRequest(_message.Message):
    __slots__ = ("facility", "notes")
    class FacilityUpdateModel(_message.Message):
        __slots__ = ("facility_id", "general_info", "mask", "version")
        FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
        GENERAL_INFO_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        facility_id: str
        general_info: _facility_pb2.Facility.GeneralInfo
        version: int
        mask: _field_mask_pb2.FieldMask
        def __init__(
            self,
            facility_id: str | None = ...,
            general_info: _facility_pb2.Facility.GeneralInfo | _Mapping | None = ...,
            version: int | None = ...,
            mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        ) -> None: ...

    FACILITY_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    facility: FacilityUpdateRequest.FacilityUpdateModel
    notes: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility.Note]
    def __init__(
        self,
        facility: FacilityUpdateRequest.FacilityUpdateModel | _Mapping | None = ...,
        notes: _Iterable[_facility_pb2.Facility.Note | _Mapping] | None = ...,
    ) -> None: ...
