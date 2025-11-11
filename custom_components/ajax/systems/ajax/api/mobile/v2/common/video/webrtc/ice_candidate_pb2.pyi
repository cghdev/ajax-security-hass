from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class IceCandidate(_message.Message):
    __slots__ = ("sdp", "sdp_mid", "sdp_mline_index")
    SDP_MID_FIELD_NUMBER: _ClassVar[int]
    SDP_MLINE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    sdp_mid: str
    sdp_mline_index: int
    sdp: str
    def __init__(
        self,
        sdp_mid: str | None = ...,
        sdp_mline_index: int | None = ...,
        sdp: str | None = ...,
    ) -> None: ...
