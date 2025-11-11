from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import (
    onvif_user_pb2 as _onvif_user_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class OnvifSettings(_message.Message):
    __slots__ = ("http_port", "max_users_number", "user_auth_enabled", "users")
    USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    MAX_USERS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    user_auth_enabled: bool
    users: _containers.RepeatedCompositeFieldContainer[_onvif_user_pb2.OnvifUser]
    http_port: int
    max_users_number: int
    def __init__(
        self,
        user_auth_enabled: bool = ...,
        users: _Iterable[_onvif_user_pb2.OnvifUser | _Mapping] | None = ...,
        http_port: int | None = ...,
        max_users_number: int | None = ...,
    ) -> None: ...
