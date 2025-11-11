from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_pb2 as _smart_lock_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetUrlRequest(_message.Message):
    __slots__ = ("smart_lock_type",)
    SMART_LOCK_TYPE_FIELD_NUMBER: _ClassVar[int]
    smart_lock_type: _smart_lock_pb2.SmartLockType
    def __init__(
        self, smart_lock_type: _smart_lock_pb2.SmartLockType | str | None = ...
    ) -> None: ...

class GetUrlResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: str | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetUrlResponse.Success
    failure: GetUrlResponse.Failure
    def __init__(
        self,
        success: GetUrlResponse.Success | _Mapping | None = ...,
        failure: GetUrlResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
