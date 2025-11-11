from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ArmingRestrictionsPart(_message.Message):
    __slots__ = ("integrity_checks",)
    class IntegrityCheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTEGRITY_CHECK_TYPE_UNSPECIFIED: _ClassVar[
            ArmingRestrictionsPart.IntegrityCheckType
        ]
        INTEGRITY_CHECK_TYPE_TAMPER: _ClassVar[
            ArmingRestrictionsPart.IntegrityCheckType
        ]

    INTEGRITY_CHECK_TYPE_UNSPECIFIED: ArmingRestrictionsPart.IntegrityCheckType
    INTEGRITY_CHECK_TYPE_TAMPER: ArmingRestrictionsPart.IntegrityCheckType
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[ArmingRestrictionsPart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[ArmingRestrictionsPart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[ArmingRestrictionsPart.IsEnabled]

    IS_ENABLED_UNSPECIFIED: ArmingRestrictionsPart.IsEnabled
    IS_ENABLED_DISABLED: ArmingRestrictionsPart.IsEnabled
    IS_ENABLED_ENABLED: ArmingRestrictionsPart.IsEnabled
    class ArmingRestrictionsPartSettings(_message.Message):
        __slots__ = ("integrity_checks",)
        INTEGRITY_CHECKS_FIELD_NUMBER: _ClassVar[int]
        integrity_checks: _containers.RepeatedCompositeFieldContainer[
            ArmingRestrictionsPart.IntegrityCheck
        ]
        def __init__(
            self,
            integrity_checks: _Iterable[
                ArmingRestrictionsPart.IntegrityCheck | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class IntegrityCheck(_message.Message):
        __slots__ = ("integrity_check_type", "is_enabled")
        INTEGRITY_CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        integrity_check_type: ArmingRestrictionsPart.IntegrityCheckType
        is_enabled: ArmingRestrictionsPart.IsEnabled
        def __init__(
            self,
            integrity_check_type: ArmingRestrictionsPart.IntegrityCheckType
            | str
            | None = ...,
            is_enabled: ArmingRestrictionsPart.IsEnabled | str | None = ...,
        ) -> None: ...

    INTEGRITY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    integrity_checks: _containers.RepeatedCompositeFieldContainer[
        ArmingRestrictionsPart.IntegrityCheck
    ]
    def __init__(
        self,
        integrity_checks: _Iterable[ArmingRestrictionsPart.IntegrityCheck | _Mapping]
        | None = ...,
    ) -> None: ...
