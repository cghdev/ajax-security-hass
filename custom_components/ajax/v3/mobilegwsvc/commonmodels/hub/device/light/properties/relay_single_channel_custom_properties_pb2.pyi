from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.hub.device.light.properties import (
    relay_channel_pb2 as _relay_channel_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class RelaySingleChannelCustomProperties(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _relay_channel_pb2.RelayChannel
    def __init__(
        self, channel: _relay_channel_pb2.RelayChannel | _Mapping | None = ...
    ) -> None: ...
