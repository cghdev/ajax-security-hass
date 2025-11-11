from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllZombieChannelsOnVideoEdgeResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("channels",)
        class ZombieChannel(_message.Message):
            __slots__ = ("id", "name")
            ID_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            id: str
            name: str
            def __init__(
                self, id: str | None = ..., name: str | None = ...
            ) -> None: ...

        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        channels: _containers.RepeatedCompositeFieldContainer[
            FindAllZombieChannelsOnVideoEdgeResponse.Success.ZombieChannel
        ]
        def __init__(
            self,
            channels: _Iterable[
                FindAllZombieChannelsOnVideoEdgeResponse.Success.ZombieChannel
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "space_not_found",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllZombieChannelsOnVideoEdgeResponse.Success
    failure: FindAllZombieChannelsOnVideoEdgeResponse.Failure
    def __init__(
        self,
        success: FindAllZombieChannelsOnVideoEdgeResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAllZombieChannelsOnVideoEdgeResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
