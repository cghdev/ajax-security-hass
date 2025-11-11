from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.video.privacy import (
    channel_permission_pb2 as _channel_permission_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelPermissionUpdate(_message.Message):
    __slots__ = ("permission", "state")
    class ChannelPermissionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_PERMISSION_STATE_UNSPECIFIED: _ClassVar[
            ChannelPermissionUpdate.ChannelPermissionState
        ]
        CHANNEL_PERMISSION_STATE_ENABLED: _ClassVar[
            ChannelPermissionUpdate.ChannelPermissionState
        ]
        CHANNEL_PERMISSION_STATE_DISABLED: _ClassVar[
            ChannelPermissionUpdate.ChannelPermissionState
        ]

    CHANNEL_PERMISSION_STATE_UNSPECIFIED: ChannelPermissionUpdate.ChannelPermissionState
    CHANNEL_PERMISSION_STATE_ENABLED: ChannelPermissionUpdate.ChannelPermissionState
    CHANNEL_PERMISSION_STATE_DISABLED: ChannelPermissionUpdate.ChannelPermissionState
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    permission: _channel_permission_pb2.ChannelPermission
    state: ChannelPermissionUpdate.ChannelPermissionState
    def __init__(
        self,
        permission: _channel_permission_pb2.ChannelPermission | str | None = ...,
        state: ChannelPermissionUpdate.ChannelPermissionState | str | None = ...,
    ) -> None: ...
