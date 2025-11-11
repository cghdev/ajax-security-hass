from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionsClaimType(_message.Message):
    __slots__ = ("permanent", "rejected", "temporary")
    class Permanent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Rejected(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Temporary(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        def __init__(
            self, duration: _duration_pb2.Duration | _Mapping | None = ...
        ) -> None: ...

    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    permanent: PermissionsClaimType.Permanent
    temporary: PermissionsClaimType.Temporary
    rejected: PermissionsClaimType.Rejected
    def __init__(
        self,
        permanent: PermissionsClaimType.Permanent | _Mapping | None = ...,
        temporary: PermissionsClaimType.Temporary | _Mapping | None = ...,
        rejected: PermissionsClaimType.Rejected | _Mapping | None = ...,
    ) -> None: ...
