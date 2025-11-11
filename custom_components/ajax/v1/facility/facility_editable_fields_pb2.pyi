from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class FacilityEditableFields(_message.Message):
    __slots__ = ("editable_sections", "general_info_editable_fields")
    class EditableSection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIA: _ClassVar[FacilityEditableFields.EditableSection]
        NOTES: _ClassVar[FacilityEditableFields.EditableSection]
        RESPONSIBLE_PERSONS: _ClassVar[FacilityEditableFields.EditableSection]
        PRIVACY_OVERRIDE: _ClassVar[FacilityEditableFields.EditableSection]

    MEDIA: FacilityEditableFields.EditableSection
    NOTES: FacilityEditableFields.EditableSection
    RESPONSIBLE_PERSONS: FacilityEditableFields.EditableSection
    PRIVACY_OVERRIDE: FacilityEditableFields.EditableSection
    GENERAL_INFO_EDITABLE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    general_info_editable_fields: _field_mask_pb2.FieldMask
    editable_sections: _containers.RepeatedScalarFieldContainer[
        FacilityEditableFields.EditableSection
    ]
    def __init__(
        self,
        general_info_editable_fields: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        editable_sections: _Iterable[FacilityEditableFields.EditableSection | str]
        | None = ...,
    ) -> None: ...
