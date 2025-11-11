from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class OfflineNotifications(_message.Message):
    __slots__ = ("notification",)
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(
        self, notification: _Iterable[_any_pb2.Any | _Mapping] | None = ...
    ) -> None: ...
