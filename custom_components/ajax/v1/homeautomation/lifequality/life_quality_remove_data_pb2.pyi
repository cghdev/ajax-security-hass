from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class LifeQualityRemoveDataRequest(_message.Message):
    __slots__ = ("device_hex_id", "hub_hex_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    device_hex_id: str
    def __init__(
        self, hub_hex_id: str | None = ..., device_hex_id: str | None = ...
    ) -> None: ...

class LifeQualityRemoveDataResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "authentication_error",
            "internal_error",
            "message",
            "not_found_error",
            "timeout_error",
        )
        class NotFoundError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class InternalError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class AuthenticationError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class TimeoutError(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_ERROR_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        message: str
        not_found_error: LifeQualityRemoveDataResponse.Failure.NotFoundError
        authentication_error: LifeQualityRemoveDataResponse.Failure.AuthenticationError
        timeout_error: LifeQualityRemoveDataResponse.Failure.TimeoutError
        internal_error: LifeQualityRemoveDataResponse.Failure.InternalError
        def __init__(
            self,
            message: str | None = ...,
            not_found_error: LifeQualityRemoveDataResponse.Failure.NotFoundError
            | _Mapping
            | None = ...,
            authentication_error: LifeQualityRemoveDataResponse.Failure.AuthenticationError
            | _Mapping
            | None = ...,
            timeout_error: LifeQualityRemoveDataResponse.Failure.TimeoutError
            | _Mapping
            | None = ...,
            internal_error: LifeQualityRemoveDataResponse.Failure.InternalError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: LifeQualityRemoveDataResponse.Success
    failure: LifeQualityRemoveDataResponse.Failure
    def __init__(
        self,
        success: LifeQualityRemoveDataResponse.Success | _Mapping | None = ...,
        failure: LifeQualityRemoveDataResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
