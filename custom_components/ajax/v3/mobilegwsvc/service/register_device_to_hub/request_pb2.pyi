from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterDeviceToHubRequest(_message.Message):
    __slots__ = (
        "device_location",
        "device_name",
        "device_qr_code",
        "fire_zone_id",
        "group_id",
        "hub_id",
        "lock_master_code",
        "room_id",
    )
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCK_MASTER_CODE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    room_id: str
    group_id: str
    device_name: str
    device_qr_code: str
    fire_zone_id: str
    device_location: str
    lock_master_code: str
    def __init__(
        self,
        hub_id: str | None = ...,
        room_id: str | None = ...,
        group_id: str | None = ...,
        device_name: str | None = ...,
        device_qr_code: str | None = ...,
        fire_zone_id: str | None = ...,
        device_location: str | None = ...,
        lock_master_code: str | None = ...,
    ) -> None: ...
