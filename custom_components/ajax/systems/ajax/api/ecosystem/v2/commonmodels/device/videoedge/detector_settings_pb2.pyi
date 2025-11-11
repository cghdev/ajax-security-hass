from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DetectorSettings(_message.Message):
    __slots__ = (
        "enabled",
        "fake_settings",
        "motion_settings",
        "object_settings",
        "pir_settings",
    )
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FAKE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MOTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PIR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    fake_settings: FakeDetectorSettings
    motion_settings: MotionDetectorSettings
    object_settings: ObjectDetectorSettings
    pir_settings: PirDetectorSettings
    def __init__(
        self,
        enabled: bool = ...,
        fake_settings: FakeDetectorSettings | _Mapping | None = ...,
        motion_settings: MotionDetectorSettings | _Mapping | None = ...,
        object_settings: ObjectDetectorSettings | _Mapping | None = ...,
        pir_settings: PirDetectorSettings | _Mapping | None = ...,
    ) -> None: ...

class PirDetectorSettings(_message.Message):
    __slots__ = ("pir_details_sensitivity",)
    class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SENSITIVITY_UNSPECIFIED: _ClassVar[PirDetectorSettings.Sensitivity]
        SENSITIVITY_LOW: _ClassVar[PirDetectorSettings.Sensitivity]
        SENSITIVITY_MID: _ClassVar[PirDetectorSettings.Sensitivity]
        SENSITIVITY_HIGH: _ClassVar[PirDetectorSettings.Sensitivity]

    SENSITIVITY_UNSPECIFIED: PirDetectorSettings.Sensitivity
    SENSITIVITY_LOW: PirDetectorSettings.Sensitivity
    SENSITIVITY_MID: PirDetectorSettings.Sensitivity
    SENSITIVITY_HIGH: PirDetectorSettings.Sensitivity
    class PirDetailsSensitivity(_message.Message):
        __slots__ = ("sensitivity",)
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        sensitivity: PirDetectorSettings.Sensitivity
        def __init__(
            self, sensitivity: PirDetectorSettings.Sensitivity | str | None = ...
        ) -> None: ...

    PIR_DETAILS_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    pir_details_sensitivity: PirDetectorSettings.PirDetailsSensitivity
    def __init__(
        self,
        pir_details_sensitivity: PirDetectorSettings.PirDetailsSensitivity
        | _Mapping
        | None = ...,
    ) -> None: ...

class FakeDetectorSettings(_message.Message):
    __slots__ = ("loop_duration", "with_ts_text")
    LOOP_DURATION_FIELD_NUMBER: _ClassVar[int]
    WITH_TS_TEXT_FIELD_NUMBER: _ClassVar[int]
    loop_duration: _duration_pb2.Duration
    with_ts_text: bool
    def __init__(
        self,
        loop_duration: _duration_pb2.Duration | _Mapping | None = ...,
        with_ts_text: bool = ...,
    ) -> None: ...

class MotionDetectorSettings(_message.Message):
    __slots__ = ("mask",)
    class Mask(_message.Message):
        __slots__ = ("min_count", "sensitivity")
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        MIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        sensitivity: int
        min_count: int
        def __init__(
            self, sensitivity: int | None = ..., min_count: int | None = ...
        ) -> None: ...

    MASK_FIELD_NUMBER: _ClassVar[int]
    mask: MotionDetectorSettings.Mask
    def __init__(
        self, mask: MotionDetectorSettings.Mask | _Mapping | None = ...
    ) -> None: ...

class ObjectDetectorSettings(_message.Message):
    __slots__ = ("class_settings",)
    class ClassSettings(_message.Message):
        __slots__ = ("enabled", "object_class", "sensitivity")
        class ObjectClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OBJECT_CLASS_UNSPECIFIED: _ClassVar[
                ObjectDetectorSettings.ClassSettings.ObjectClass
            ]
            OBJECT_CLASS_PERSON: _ClassVar[
                ObjectDetectorSettings.ClassSettings.ObjectClass
            ]
            OBJECT_CLASS_PET: _ClassVar[
                ObjectDetectorSettings.ClassSettings.ObjectClass
            ]
            OBJECT_CLASS_VEHICLE: _ClassVar[
                ObjectDetectorSettings.ClassSettings.ObjectClass
            ]

        OBJECT_CLASS_UNSPECIFIED: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_PERSON: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_PET: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_VEHICLE: ObjectDetectorSettings.ClassSettings.ObjectClass
        OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        object_class: ObjectDetectorSettings.ClassSettings.ObjectClass
        enabled: bool
        sensitivity: int
        def __init__(
            self,
            object_class: ObjectDetectorSettings.ClassSettings.ObjectClass
            | str
            | None = ...,
            enabled: bool = ...,
            sensitivity: int | None = ...,
        ) -> None: ...

    CLASS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    class_settings: _containers.RepeatedCompositeFieldContainer[
        ObjectDetectorSettings.ClassSettings
    ]
    def __init__(
        self,
        class_settings: _Iterable[ObjectDetectorSettings.ClassSettings | _Mapping]
        | None = ...,
    ) -> None: ...
