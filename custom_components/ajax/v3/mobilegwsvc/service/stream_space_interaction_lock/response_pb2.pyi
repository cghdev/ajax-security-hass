from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.lock import (
    space_interaction_lock_pb2 as _space_interaction_lock_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceInteractionLockResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("delete", "snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamSpaceInteractionLockResponse.Snapshot
        update: StreamSpaceInteractionLockResponse.Update
        delete: StreamSpaceInteractionLockResponse.Delete
        def __init__(
            self,
            snapshot: StreamSpaceInteractionLockResponse.Snapshot
            | _Mapping
            | None = ...,
            update: StreamSpaceInteractionLockResponse.Update | _Mapping | None = ...,
            delete: StreamSpaceInteractionLockResponse.Delete | _Mapping | None = ...,
        ) -> None: ...

    class Snapshot(_message.Message):
        __slots__ = ("space_interaction_locks",)
        SPACE_INTERACTION_LOCKS_FIELD_NUMBER: _ClassVar[int]
        space_interaction_locks: _containers.RepeatedCompositeFieldContainer[
            _space_interaction_lock_pb2.SpaceInteractionLock
        ]
        def __init__(
            self,
            space_interaction_locks: _Iterable[
                _space_interaction_lock_pb2.SpaceInteractionLock | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Update(_message.Message):
        __slots__ = ("space_interaction_lock",)
        SPACE_INTERACTION_LOCK_FIELD_NUMBER: _ClassVar[int]
        space_interaction_lock: _space_interaction_lock_pb2.SpaceInteractionLock
        def __init__(
            self,
            space_interaction_lock: _space_interaction_lock_pb2.SpaceInteractionLock
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Delete(_message.Message):
        __slots__ = ("space_interaction_lock",)
        SPACE_INTERACTION_LOCK_FIELD_NUMBER: _ClassVar[int]
        space_interaction_lock: _space_interaction_lock_pb2.SpaceInteractionLock
        def __init__(
            self,
            space_interaction_lock: _space_interaction_lock_pb2.SpaceInteractionLock
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "message")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.Error
        def __init__(
            self,
            message: str | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSpaceInteractionLockResponse.Success
    failure: StreamSpaceInteractionLockResponse.Failure
    def __init__(
        self,
        success: StreamSpaceInteractionLockResponse.Success | _Mapping | None = ...,
        failure: StreamSpaceInteractionLockResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
