from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyCompanyTemplateRequest(_message.Message):
    __slots__ = ("hub_id", "objects", "template_id")
    class HubObject(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: _object_type_pb2.ObjectType
        def __init__(
            self,
            id: str | None = ...,
            type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        ) -> None: ...

    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    hub_id: str
    objects: _containers.RepeatedCompositeFieldContainer[
        ApplyCompanyTemplateRequest.HubObject
    ]
    def __init__(
        self,
        template_id: str | None = ...,
        hub_id: str | None = ...,
        objects: _Iterable[ApplyCompanyTemplateRequest.HubObject | _Mapping]
        | None = ...,
    ) -> None: ...
