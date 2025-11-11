from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class GwError(_message.Message):
    __slots__ = (
        "authentication_error",
        "hub_already_in_use_by_another_company_error",
        "hub_already_in_use_error",
        "hub_not_found_by_master_key_error",
        "internal_error",
        "master_key_error",
        "not_found_error",
        "permission_denied_error",
        "request_was_already_sent_error",
        "timeout_error",
    )
    class NotFoundError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class InternalError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class AuthenticationError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class TimeoutError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class MasterKeyError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class HubAlreadyInUseError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class HubAlreadyInUseByAnotherCompanyError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class RequestWasAlreadySentError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class HubNotFoundByMasterKeyError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    class PermissionDeniedError(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_ERROR_FIELD_NUMBER: _ClassVar[int]
    MASTER_KEY_ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_ALREADY_IN_USE_ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_ALREADY_IN_USE_BY_ANOTHER_COMPANY_ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_WAS_ALREADY_SENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_NOT_FOUND_BY_MASTER_KEY_ERROR_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_ERROR_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    not_found_error: GwError.NotFoundError
    authentication_error: GwError.AuthenticationError
    timeout_error: GwError.TimeoutError
    master_key_error: GwError.MasterKeyError
    hub_already_in_use_error: GwError.HubAlreadyInUseError
    hub_already_in_use_by_another_company_error: (
        GwError.HubAlreadyInUseByAnotherCompanyError
    )
    request_was_already_sent_error: GwError.RequestWasAlreadySentError
    hub_not_found_by_master_key_error: GwError.HubNotFoundByMasterKeyError
    permission_denied_error: GwError.PermissionDeniedError
    internal_error: GwError.InternalError
    def __init__(
        self,
        not_found_error: GwError.NotFoundError | _Mapping | None = ...,
        authentication_error: GwError.AuthenticationError | _Mapping | None = ...,
        timeout_error: GwError.TimeoutError | _Mapping | None = ...,
        master_key_error: GwError.MasterKeyError | _Mapping | None = ...,
        hub_already_in_use_error: GwError.HubAlreadyInUseError | _Mapping | None = ...,
        hub_already_in_use_by_another_company_error: GwError.HubAlreadyInUseByAnotherCompanyError
        | _Mapping
        | None = ...,
        request_was_already_sent_error: GwError.RequestWasAlreadySentError
        | _Mapping
        | None = ...,
        hub_not_found_by_master_key_error: GwError.HubNotFoundByMasterKeyError
        | _Mapping
        | None = ...,
        permission_denied_error: GwError.PermissionDeniedError | _Mapping | None = ...,
        internal_error: GwError.InternalError | _Mapping | None = ...,
    ) -> None: ...
