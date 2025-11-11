from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.gw import error_pb2 as _error_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREATED: _ClassVar[EventType]
    DELETED: _ClassVar[EventType]

class Response(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESSFUL: _ClassVar[Response]

CREATED: EventType
DELETED: EventType
SUCCESSFUL: Response

class SessionInfo(_message.Message):
    __slots__ = ("event_type", "session", "user_id")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session: Session
    event_type: EventType
    user_id: str
    def __init__(
        self,
        session: Session | _Mapping | None = ...,
        event_type: EventType | str | None = ...,
        user_id: str | None = ...,
    ) -> None: ...

class Session(_message.Message):
    __slots__ = (
        "application_label",
        "client_device_id",
        "client_device_model",
        "client_os",
        "client_version_major",
        "is_active",
        "last_connection_ip",
        "legacy_session",
        "session_creation_timestamp",
        "session_expiry_time",
        "session_id",
        "session_refresh_timestamp",
    )
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTION_IP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_OS_FIELD_NUMBER: _ClassVar[int]
    SESSION_EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    LEGACY_SESSION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_LABEL_FIELD_NUMBER: _ClassVar[int]
    SESSION_REFRESH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    session_creation_timestamp: int
    last_connection_ip: str
    client_device_model: str
    client_os: str
    session_expiry_time: int
    client_version_major: str
    client_device_id: str
    legacy_session: bool
    application_label: str
    session_refresh_timestamp: int
    is_active: bool
    def __init__(
        self,
        session_id: int | None = ...,
        session_creation_timestamp: int | None = ...,
        last_connection_ip: str | None = ...,
        client_device_model: str | None = ...,
        client_os: str | None = ...,
        session_expiry_time: int | None = ...,
        client_version_major: str | None = ...,
        client_device_id: str | None = ...,
        legacy_session: bool = ...,
        application_label: str | None = ...,
        session_refresh_timestamp: int | None = ...,
        is_active: bool = ...,
    ) -> None: ...

class GetActiveSessionsResponse(_message.Message):
    __slots__ = ("error", "sessions")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    sessions: ActiveSessions
    error: _error_pb2.GwError
    def __init__(
        self,
        sessions: ActiveSessions | _Mapping | None = ...,
        error: _error_pb2.GwError | _Mapping | None = ...,
    ) -> None: ...

class ActiveSessions(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(
        self, sessions: _Iterable[Session | _Mapping] | None = ...
    ) -> None: ...

class DropUserSessionResponse(_message.Message):
    __slots__ = ("error", "response")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    response: Response
    error: _error_pb2.GwError
    def __init__(
        self,
        response: Response | str | None = ...,
        error: _error_pb2.GwError | _Mapping | None = ...,
    ) -> None: ...

class CreateNewSessionResponse(_message.Message):
    __slots__ = ("error", "session")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    session: Session
    error: _error_pb2.GwError
    def __init__(
        self,
        session: Session | _Mapping | None = ...,
        error: _error_pb2.GwError | _Mapping | None = ...,
    ) -> None: ...
