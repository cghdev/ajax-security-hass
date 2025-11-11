from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CalculateGeofenceIntentionResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("space_id", "space_name")
        SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        space_name: str
        space_id: str
        def __init__(
            self, space_name: str | None = ..., space_id: str | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CalculateGeofenceIntentionResponse.Success
    failure: CalculateGeofenceIntentionResponse.Failure
    def __init__(
        self,
        success: CalculateGeofenceIntentionResponse.Success | _Mapping | None = ...,
        failure: CalculateGeofenceIntentionResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
