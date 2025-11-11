from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CommonSoundCompliancePatternPart(_message.Message):
    __slots__ = (
        "chosen_sound_compliance_pattern",
        "sound_compliance_patterns_capabilities",
    )
    class SoundCompliancePattern(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOUND_COMPLIANCE_PATTERN_UNSPECIFIED: _ClassVar[
            CommonSoundCompliancePatternPart.SoundCompliancePattern
        ]
        SOUND_COMPLIANCE_PATTERN_ORDINARY: _ClassVar[
            CommonSoundCompliancePatternPart.SoundCompliancePattern
        ]
        SOUND_COMPLIANCE_PATTERN_NFA2P: _ClassVar[
            CommonSoundCompliancePatternPart.SoundCompliancePattern
        ]

    SOUND_COMPLIANCE_PATTERN_UNSPECIFIED: (
        CommonSoundCompliancePatternPart.SoundCompliancePattern
    )
    SOUND_COMPLIANCE_PATTERN_ORDINARY: (
        CommonSoundCompliancePatternPart.SoundCompliancePattern
    )
    SOUND_COMPLIANCE_PATTERN_NFA2P: (
        CommonSoundCompliancePatternPart.SoundCompliancePattern
    )
    class CommonSoundCompliancePatternPartSettings(_message.Message):
        __slots__ = ("compliance_pattern",)
        COMPLIANCE_PATTERN_FIELD_NUMBER: _ClassVar[int]
        compliance_pattern: CommonSoundCompliancePatternPart.SoundCompliancePattern
        def __init__(
            self,
            compliance_pattern: CommonSoundCompliancePatternPart.SoundCompliancePattern
            | str
            | None = ...,
        ) -> None: ...

    CHOSEN_SOUND_COMPLIANCE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SOUND_COMPLIANCE_PATTERNS_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    chosen_sound_compliance_pattern: (
        CommonSoundCompliancePatternPart.SoundCompliancePattern
    )
    sound_compliance_patterns_capabilities: _containers.RepeatedScalarFieldContainer[
        CommonSoundCompliancePatternPart.SoundCompliancePattern
    ]
    def __init__(
        self,
        chosen_sound_compliance_pattern: CommonSoundCompliancePatternPart.SoundCompliancePattern
        | str
        | None = ...,
        sound_compliance_patterns_capabilities: _Iterable[
            CommonSoundCompliancePatternPart.SoundCompliancePattern | str
        ]
        | None = ...,
    ) -> None: ...
