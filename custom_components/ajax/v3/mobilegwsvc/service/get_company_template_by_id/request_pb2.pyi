from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompanyTemplateByIdRequest(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: str | None = ...) -> None: ...
