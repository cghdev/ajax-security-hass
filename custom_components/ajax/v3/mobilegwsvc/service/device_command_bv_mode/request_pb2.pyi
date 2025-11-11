from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandBvModeRequest(_message.Message):
    __slots__ = ("alarm_verification_mode", "hub_id")
    class AlarmVerificationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM_VERIFICATION_MODE_UNSPECIFIED: _ClassVar[
            DeviceCommandBvModeRequest.AlarmVerificationMode
        ]
        ALARM_VERIFICATION_MODE_DISABLE: _ClassVar[
            DeviceCommandBvModeRequest.AlarmVerificationMode
        ]
        ALARM_VERIFICATION_MODE_ENABLE: _ClassVar[
            DeviceCommandBvModeRequest.AlarmVerificationMode
        ]

    ALARM_VERIFICATION_MODE_UNSPECIFIED: (
        DeviceCommandBvModeRequest.AlarmVerificationMode
    )
    ALARM_VERIFICATION_MODE_DISABLE: DeviceCommandBvModeRequest.AlarmVerificationMode
    ALARM_VERIFICATION_MODE_ENABLE: DeviceCommandBvModeRequest.AlarmVerificationMode
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    alarm_verification_mode: DeviceCommandBvModeRequest.AlarmVerificationMode
    def __init__(
        self,
        hub_id: str | None = ...,
        alarm_verification_mode: DeviceCommandBvModeRequest.AlarmVerificationMode
        | str
        | None = ...,
    ) -> None: ...
