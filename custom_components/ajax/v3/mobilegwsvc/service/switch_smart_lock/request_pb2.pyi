from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchSmartLockRequest(_message.Message):
    __slots__ = ("action", "smart_lock_id", "space_id")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[SwitchSmartLockRequest.Action]
        ACTION_UNLOCK: _ClassVar[SwitchSmartLockRequest.Action]
        ACTION_LOCK: _ClassVar[SwitchSmartLockRequest.Action]
        ACTION_UNLATCH: _ClassVar[SwitchSmartLockRequest.Action]

    ACTION_UNSPECIFIED: SwitchSmartLockRequest.Action
    ACTION_UNLOCK: SwitchSmartLockRequest.Action
    ACTION_LOCK: SwitchSmartLockRequest.Action
    ACTION_UNLATCH: SwitchSmartLockRequest.Action
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_id: str
    action: SwitchSmartLockRequest.Action
    def __init__(
        self,
        space_id: str | None = ...,
        smart_lock_id: str | None = ...,
        action: SwitchSmartLockRequest.Action | str | None = ...,
    ) -> None: ...
