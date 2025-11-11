from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LL_NONE: _ClassVar[LogLevel]
    LL_OFF: _ClassVar[LogLevel]
    LL_FATAL: _ClassVar[LogLevel]
    LL_ERROR: _ClassVar[LogLevel]
    LL_WARN: _ClassVar[LogLevel]
    LL_INFO: _ClassVar[LogLevel]
    LL_DEBUG: _ClassVar[LogLevel]
    LL_TRACE: _ClassVar[LogLevel]
    LL_ALL: _ClassVar[LogLevel]

LL_NONE: LogLevel
LL_OFF: LogLevel
LL_FATAL: LogLevel
LL_ERROR: LogLevel
LL_WARN: LogLevel
LL_INFO: LogLevel
LL_DEBUG: LogLevel
LL_TRACE: LogLevel
LL_ALL: LogLevel

class LoggingSettings(_message.Message):
    __slots__ = ("log_max_bytes", "module_levels", "root_level")
    class ModuleLogLevel(_message.Message):
        __slots__ = ("level", "module")
        MODULE_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        module: str
        level: LogLevel
        def __init__(
            self, module: str | None = ..., level: LogLevel | str | None = ...
        ) -> None: ...

    LOG_MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    ROOT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MODULE_LEVELS_FIELD_NUMBER: _ClassVar[int]
    log_max_bytes: int
    root_level: LogLevel
    module_levels: _containers.RepeatedCompositeFieldContainer[
        LoggingSettings.ModuleLogLevel
    ]
    def __init__(
        self,
        log_max_bytes: int | None = ...,
        root_level: LogLevel | str | None = ...,
        module_levels: _Iterable[LoggingSettings.ModuleLogLevel | _Mapping]
        | None = ...,
    ) -> None: ...

class DiagnosticsSettings(_message.Message):
    __slots__ = ("logging_settings",)
    LOGGING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    logging_settings: LoggingSettings
    def __init__(
        self, logging_settings: LoggingSettings | _Mapping | None = ...
    ) -> None: ...
