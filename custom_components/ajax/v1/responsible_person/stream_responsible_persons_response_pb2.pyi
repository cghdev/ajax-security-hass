from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.responsible_person import responsible_person_pb2 as _responsible_person_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamResponsiblePersonsResponse(_message.Message):
    __slots__ = ("responsible_persons",)
    RESPONSIBLE_PERSONS_FIELD_NUMBER: _ClassVar[int]
    responsible_persons: _containers.RepeatedCompositeFieldContainer[
        _responsible_person_pb2.ResponsiblePerson
    ]
    def __init__(
        self,
        responsible_persons: _Iterable[
            _responsible_person_pb2.ResponsiblePerson | _Mapping
        ]
        | None = ...,
    ) -> None: ...
