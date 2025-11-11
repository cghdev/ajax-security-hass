from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceRequest(_message.Message):
    __slots__ = ("device_qr_code", "image_id", "name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    image_id: str
    device_qr_code: str
    def __init__(
        self,
        name: str | None = ...,
        image_id: str | None = ...,
        device_qr_code: str | None = ...,
    ) -> None: ...
