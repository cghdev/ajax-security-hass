from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class FireDeviceActionButton(_message.Message):
    __slots__ = (
        "critical_co_button",
        "critical_smoke_button",
        "mute_button",
        "postpone_button",
    )
    class MuteCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_COMMAND_UNSPECIFIED: _ClassVar[FireDeviceActionButton.MuteCommand]
        MUTE_COMMAND_OWN: _ClassVar[FireDeviceActionButton.MuteCommand]
        MUTE_COMMAND_OWN_PLUS_EXTERNAL: _ClassVar[FireDeviceActionButton.MuteCommand]

    MUTE_COMMAND_UNSPECIFIED: FireDeviceActionButton.MuteCommand
    MUTE_COMMAND_OWN: FireDeviceActionButton.MuteCommand
    MUTE_COMMAND_OWN_PLUS_EXTERNAL: FireDeviceActionButton.MuteCommand
    class RequiredPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUIRED_PERMISSION_UNSPECIFIED: _ClassVar[
            FireDeviceActionButton.RequiredPermission
        ]
        REQUIRED_PERMISSION_GROUPS: _ClassVar[FireDeviceActionButton.RequiredPermission]
        REQUIRED_PERMISSION_MUTE: _ClassVar[FireDeviceActionButton.RequiredPermission]
        REQUIRED_PERMISSION_HOME_AUTOMATION: _ClassVar[
            FireDeviceActionButton.RequiredPermission
        ]

    REQUIRED_PERMISSION_UNSPECIFIED: FireDeviceActionButton.RequiredPermission
    REQUIRED_PERMISSION_GROUPS: FireDeviceActionButton.RequiredPermission
    REQUIRED_PERMISSION_MUTE: FireDeviceActionButton.RequiredPermission
    REQUIRED_PERMISSION_HOME_AUTOMATION: FireDeviceActionButton.RequiredPermission
    class MuteButton(_message.Message):
        __slots__ = ("mute_command", "required_permissions")
        MUTE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        mute_command: FireDeviceActionButton.MuteCommand
        required_permissions: _containers.RepeatedScalarFieldContainer[
            FireDeviceActionButton.RequiredPermission
        ]
        def __init__(
            self,
            mute_command: FireDeviceActionButton.MuteCommand | str | None = ...,
            required_permissions: _Iterable[
                FireDeviceActionButton.RequiredPermission | str
            ]
            | None = ...,
        ) -> None: ...

    class CriticalSmokeButton(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class CriticalCOButton(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class PostponeButton(_message.Message):
        __slots__ = ("required_permission",)
        REQUIRED_PERMISSION_FIELD_NUMBER: _ClassVar[int]
        required_permission: _containers.RepeatedScalarFieldContainer[
            FireDeviceActionButton.RequiredPermission
        ]
        def __init__(
            self,
            required_permission: _Iterable[
                FireDeviceActionButton.RequiredPermission | str
            ]
            | None = ...,
        ) -> None: ...

    MUTE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_SMOKE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_CO_BUTTON_FIELD_NUMBER: _ClassVar[int]
    POSTPONE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    mute_button: FireDeviceActionButton.MuteButton
    critical_smoke_button: FireDeviceActionButton.CriticalSmokeButton
    critical_co_button: FireDeviceActionButton.CriticalCOButton
    postpone_button: FireDeviceActionButton.PostponeButton
    def __init__(
        self,
        mute_button: FireDeviceActionButton.MuteButton | _Mapping | None = ...,
        critical_smoke_button: FireDeviceActionButton.CriticalSmokeButton
        | _Mapping
        | None = ...,
        critical_co_button: FireDeviceActionButton.CriticalCOButton
        | _Mapping
        | None = ...,
        postpone_button: FireDeviceActionButton.PostponeButton | _Mapping | None = ...,
    ) -> None: ...
