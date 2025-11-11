from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryVideoAccessApprovedToProData(_message.Message):
    __slots__ = (
        "duration",
        "request_id",
        "requester_email",
        "requester_member_id",
        "requester_name",
    )
    REQUESTER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    requester_member_id: str
    requester_name: str
    requester_email: str
    request_id: str
    duration: _duration_pb2.Duration
    def __init__(
        self,
        requester_member_id: str | None = ...,
        requester_name: str | None = ...,
        requester_email: str | None = ...,
        request_id: str | None = ...,
        duration: _duration_pb2.Duration | _Mapping | None = ...,
    ) -> None: ...
