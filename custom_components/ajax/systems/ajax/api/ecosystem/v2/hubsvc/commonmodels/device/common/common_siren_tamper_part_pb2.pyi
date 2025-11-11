from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CommonSirenTamperPart(_message.Message):
    __slots__ = ("alert_if_lid_is_open",)
    class AlertIfLidIsOpen(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALERT_IF_LID_IS_OPEN_UNSPECIFIED: _ClassVar[
            CommonSirenTamperPart.AlertIfLidIsOpen
        ]
        ALERT_IF_LID_IS_OPEN_DISABLED: _ClassVar[CommonSirenTamperPart.AlertIfLidIsOpen]
        ALERT_IF_LID_IS_OPEN_ENABLED: _ClassVar[CommonSirenTamperPart.AlertIfLidIsOpen]

    ALERT_IF_LID_IS_OPEN_UNSPECIFIED: CommonSirenTamperPart.AlertIfLidIsOpen
    ALERT_IF_LID_IS_OPEN_DISABLED: CommonSirenTamperPart.AlertIfLidIsOpen
    ALERT_IF_LID_IS_OPEN_ENABLED: CommonSirenTamperPart.AlertIfLidIsOpen
    class CommonSirenTamperPartSettings(_message.Message):
        __slots__ = ("alert_if_lid_is_open",)
        ALERT_IF_LID_IS_OPEN_FIELD_NUMBER: _ClassVar[int]
        alert_if_lid_is_open: CommonSirenTamperPart.AlertIfLidIsOpen
        def __init__(
            self,
            alert_if_lid_is_open: CommonSirenTamperPart.AlertIfLidIsOpen
            | str
            | None = ...,
        ) -> None: ...

    ALERT_IF_LID_IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    alert_if_lid_is_open: CommonSirenTamperPart.AlertIfLidIsOpen
    def __init__(
        self,
        alert_if_lid_is_open: CommonSirenTamperPart.AlertIfLidIsOpen | str | None = ...,
    ) -> None: ...
