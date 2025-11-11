from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class TakePhotoPart(_message.Message):
    __slots__ = ("capabilities", "take_photo_triggers")
    class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TakePhotoPart.TriggerType]
        TRIGGER_TYPE_IF_MASKING_DETECTED: _ClassVar[TakePhotoPart.TriggerType]
        TRIGGER_TYPE_IF_LID_OPENED: _ClassVar[TakePhotoPart.TriggerType]
        TRIGGER_TYPE_IF_DEVICE_MOVED: _ClassVar[TakePhotoPart.TriggerType]

    TRIGGER_TYPE_UNSPECIFIED: TakePhotoPart.TriggerType
    TRIGGER_TYPE_IF_MASKING_DETECTED: TakePhotoPart.TriggerType
    TRIGGER_TYPE_IF_LID_OPENED: TakePhotoPart.TriggerType
    TRIGGER_TYPE_IF_DEVICE_MOVED: TakePhotoPart.TriggerType
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[TakePhotoPart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[TakePhotoPart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[TakePhotoPart.IsEnabled]

    IS_ENABLED_UNSPECIFIED: TakePhotoPart.IsEnabled
    IS_ENABLED_DISABLED: TakePhotoPart.IsEnabled
    IS_ENABLED_ENABLED: TakePhotoPart.IsEnabled
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[TakePhotoPart.Capability]
        CAPABILITY_TAKE_PHOTO_TRIGGERS: _ClassVar[TakePhotoPart.Capability]

    CAPABILITY_UNSPECIFIED: TakePhotoPart.Capability
    CAPABILITY_TAKE_PHOTO_TRIGGERS: TakePhotoPart.Capability
    class TakePhotoPartSettings(_message.Message):
        __slots__ = ("take_photo_triggers",)
        TAKE_PHOTO_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
        take_photo_triggers: _containers.RepeatedCompositeFieldContainer[
            TakePhotoPart.TakePhotoTrigger
        ]
        def __init__(
            self,
            take_photo_triggers: _Iterable[TakePhotoPart.TakePhotoTrigger | _Mapping]
            | None = ...,
        ) -> None: ...

    class TakePhotoTrigger(_message.Message):
        __slots__ = ("is_enabled", "trigger_type")
        TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        trigger_type: TakePhotoPart.TriggerType
        is_enabled: TakePhotoPart.IsEnabled
        def __init__(
            self,
            trigger_type: TakePhotoPart.TriggerType | str | None = ...,
            is_enabled: TakePhotoPart.IsEnabled | str | None = ...,
        ) -> None: ...

    TAKE_PHOTO_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    take_photo_triggers: _containers.RepeatedCompositeFieldContainer[
        TakePhotoPart.TakePhotoTrigger
    ]
    capabilities: _containers.RepeatedScalarFieldContainer[TakePhotoPart.Capability]
    def __init__(
        self,
        take_photo_triggers: _Iterable[TakePhotoPart.TakePhotoTrigger | _Mapping]
        | None = ...,
        capabilities: _Iterable[TakePhotoPart.Capability | str] | None = ...,
    ) -> None: ...
