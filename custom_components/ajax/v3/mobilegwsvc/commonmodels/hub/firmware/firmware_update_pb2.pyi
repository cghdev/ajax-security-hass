from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdate(_message.Message):
    __slots__ = ("status", "target_id")
    class Status(_message.Message):
        __slots__ = ("downloading", "failure", "installing", "not_started", "success")
        NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
        DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        INSTALLING_FIELD_NUMBER: _ClassVar[int]
        not_started: _empty_pb2.Empty
        downloading: int
        success: _empty_pb2.Empty
        failure: _empty_pb2.Empty
        installing: _empty_pb2.Empty
        def __init__(
            self,
            not_started: _empty_pb2.Empty | _Mapping | None = ...,
            downloading: int | None = ...,
            success: _empty_pb2.Empty | _Mapping | None = ...,
            failure: _empty_pb2.Empty | _Mapping | None = ...,
            installing: _empty_pb2.Empty | _Mapping | None = ...,
        ) -> None: ...

    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    status: FirmwareUpdate.Status
    def __init__(
        self,
        target_id: str | None = ...,
        status: FirmwareUpdate.Status | _Mapping | None = ...,
    ) -> None: ...
