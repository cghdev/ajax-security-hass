from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class PrivacyMotionCamAccess(_message.Message):
    __slots__ = ("access_type", "device_id", "device_type", "user_id")
    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISABLED: _ClassVar[PrivacyMotionCamAccess.AccessType]
        ALWAYS: _ClassVar[PrivacyMotionCamAccess.AccessType]
        ARMED: _ClassVar[PrivacyMotionCamAccess.AccessType]

    DISABLED: PrivacyMotionCamAccess.AccessType
    ALWAYS: PrivacyMotionCamAccess.AccessType
    ARMED: PrivacyMotionCamAccess.AccessType
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOTION_CAM: _ClassVar[PrivacyMotionCamAccess.DeviceType]
        MOTION_CAM_OUTDOOR: _ClassVar[PrivacyMotionCamAccess.DeviceType]
        MOTION_CAM_FIBRA_BASE: _ClassVar[PrivacyMotionCamAccess.DeviceType]

    MOTION_CAM: PrivacyMotionCamAccess.DeviceType
    MOTION_CAM_OUTDOOR: PrivacyMotionCamAccess.DeviceType
    MOTION_CAM_FIBRA_BASE: PrivacyMotionCamAccess.DeviceType
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    device_id: str
    device_type: PrivacyMotionCamAccess.DeviceType
    access_type: PrivacyMotionCamAccess.AccessType
    def __init__(
        self,
        user_id: str | None = ...,
        device_id: str | None = ...,
        device_type: PrivacyMotionCamAccess.DeviceType | str | None = ...,
        access_type: PrivacyMotionCamAccess.AccessType | str | None = ...,
    ) -> None: ...
