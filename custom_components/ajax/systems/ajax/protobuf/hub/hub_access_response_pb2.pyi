from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class HubAccessResponse(_message.Message):
    __slots__ = (
        "access_level",
        "access_time",
        "is_request_declined",
        "pro_name",
        "profi_mail",
        "user_id",
    )
    PROFI_MAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PRO_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_REQUEST_DECLINED_FIELD_NUMBER: _ClassVar[int]
    profi_mail: str
    user_id: str
    pro_name: str
    access_level: int
    access_time: int
    is_request_declined: bool
    def __init__(
        self,
        profi_mail: str | None = ...,
        user_id: str | None = ...,
        pro_name: str | None = ...,
        access_level: int | None = ...,
        access_time: int | None = ...,
        is_request_declined: bool = ...,
    ) -> None: ...
