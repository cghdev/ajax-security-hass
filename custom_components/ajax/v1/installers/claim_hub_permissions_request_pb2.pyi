from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ClaimHubPermissionsRequest(_message.Message):
    __slots__ = ("hub_hex_id", "permanent", "temporary")
    class Permanent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Temporary(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(
            self, duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    permanent: ClaimHubPermissionsRequest.Permanent
    temporary: ClaimHubPermissionsRequest.Temporary
    def __init__(
        self,
        hub_hex_id: str | None = ...,
        permanent: ClaimHubPermissionsRequest.Permanent | _Mapping | None = ...,
        temporary: ClaimHubPermissionsRequest.Temporary | _Mapping | None = ...,
    ) -> None: ...
