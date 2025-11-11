from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteResponsiblePersonRequest(_message.Message):
    __slots__ = ("facility_id", "facility_responsible_person_id")
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    FACILITY_RESPONSIBLE_PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    facility_id: str
    facility_responsible_person_id: str
    def __init__(
        self,
        facility_id: str | None = ...,
        facility_responsible_person_id: str | None = ...,
    ) -> None: ...
