from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class JoinSpaceRequestInfo(_message.Message):
    __slots__ = (
        "initiator_email",
        "initiator_first_name",
        "initiator_last_name",
        "initiator_phone",
        "request_id",
    )
    INITIATOR_FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_PHONE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    initiator_first_name: str
    initiator_last_name: str
    initiator_email: str
    initiator_phone: str
    request_id: str
    def __init__(
        self,
        initiator_first_name: str | None = ...,
        initiator_last_name: str | None = ...,
        initiator_email: str | None = ...,
        initiator_phone: str | None = ...,
        request_id: str | None = ...,
    ) -> None: ...
