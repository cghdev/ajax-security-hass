from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class AlarmVerification(_message.Message):
    __slots__ = ("verification",)
    class Verification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERIFICATION_UNSPECIFIED: _ClassVar[AlarmVerification.Verification]
        VERIFICATION_DISABLED: _ClassVar[AlarmVerification.Verification]
        VERIFICATION_ENABLED: _ClassVar[AlarmVerification.Verification]

    VERIFICATION_UNSPECIFIED: AlarmVerification.Verification
    VERIFICATION_DISABLED: AlarmVerification.Verification
    VERIFICATION_ENABLED: AlarmVerification.Verification
    class AlarmVerificationSettings(_message.Message):
        __slots__ = ("verification",)
        VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        verification: AlarmVerification.Verification
        def __init__(
            self, verification: AlarmVerification.Verification | str | None = ...
        ) -> None: ...

    VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    verification: AlarmVerification.Verification
    def __init__(
        self, verification: AlarmVerification.Verification | str | None = ...
    ) -> None: ...
