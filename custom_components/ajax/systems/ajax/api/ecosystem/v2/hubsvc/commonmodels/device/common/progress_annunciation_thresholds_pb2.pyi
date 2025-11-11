from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ProgressAnnunciationThreshold(_message.Message):
    __slots__ = ("entry_delay", "exit_delay")
    class Delay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELAY_UNSPECIFIED: _ClassVar[ProgressAnnunciationThreshold.Delay]
        DELAY_DISABLED: _ClassVar[ProgressAnnunciationThreshold.Delay]
        DELAY_5_SEC: _ClassVar[ProgressAnnunciationThreshold.Delay]
        DELAY_10_SEC: _ClassVar[ProgressAnnunciationThreshold.Delay]
        DELAY_15_SEC: _ClassVar[ProgressAnnunciationThreshold.Delay]

    DELAY_UNSPECIFIED: ProgressAnnunciationThreshold.Delay
    DELAY_DISABLED: ProgressAnnunciationThreshold.Delay
    DELAY_5_SEC: ProgressAnnunciationThreshold.Delay
    DELAY_10_SEC: ProgressAnnunciationThreshold.Delay
    DELAY_15_SEC: ProgressAnnunciationThreshold.Delay
    class ProgressAnnunciationThresholdSettings(_message.Message):
        __slots__ = ("entry_delay", "exit_delay")
        ENTRY_DELAY_FIELD_NUMBER: _ClassVar[int]
        EXIT_DELAY_FIELD_NUMBER: _ClassVar[int]
        entry_delay: ProgressAnnunciationThreshold.Delay
        exit_delay: ProgressAnnunciationThreshold.Delay
        def __init__(
            self,
            entry_delay: ProgressAnnunciationThreshold.Delay | str | None = ...,
            exit_delay: ProgressAnnunciationThreshold.Delay | str | None = ...,
        ) -> None: ...

    ENTRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    EXIT_DELAY_FIELD_NUMBER: _ClassVar[int]
    entry_delay: ProgressAnnunciationThreshold.Delay
    exit_delay: ProgressAnnunciationThreshold.Delay
    def __init__(
        self,
        entry_delay: ProgressAnnunciationThreshold.Delay | str | None = ...,
        exit_delay: ProgressAnnunciationThreshold.Delay | str | None = ...,
    ) -> None: ...
