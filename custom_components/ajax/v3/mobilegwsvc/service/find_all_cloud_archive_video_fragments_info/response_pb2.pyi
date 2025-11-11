from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
import datetime
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video import time_zone_pb2 as _time_zone_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllCloudArchiveVideoFragmentsInfoResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("fragments_info", "time_zone_map")
        class VideoFragmentInfo(_message.Message):
            __slots__ = ("duration", "fragment_id", "timestamp")
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            fragment_id: int
            timestamp: _timestamp_pb2.Timestamp
            duration: _duration_pb2.Duration
            def __init__(
                self,
                fragment_id: int | None = ...,
                timestamp: datetime.datetime
                | _timestamp_pb2.Timestamp
                | _Mapping
                | None = ...,
                duration: datetime.timedelta
                | _duration_pb2.Duration
                | _Mapping
                | None = ...,
            ) -> None: ...

        FRAGMENTS_INFO_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_MAP_FIELD_NUMBER: _ClassVar[int]
        fragments_info: _containers.RepeatedCompositeFieldContainer[
            FindAllCloudArchiveVideoFragmentsInfoResponse.Success.VideoFragmentInfo
        ]
        time_zone_map: _containers.RepeatedCompositeFieldContainer[
            _time_zone_pb2.TimeZone
        ]
        def __init__(
            self,
            fragments_info: _Iterable[
                FindAllCloudArchiveVideoFragmentsInfoResponse.Success.VideoFragmentInfo
                | _Mapping
            ]
            | None = ...,
            time_zone_map: _Iterable[_time_zone_pb2.TimeZone | _Mapping] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllCloudArchiveVideoFragmentsInfoResponse.Success
    failure: FindAllCloudArchiveVideoFragmentsInfoResponse.Failure
    def __init__(
        self,
        success: FindAllCloudArchiveVideoFragmentsInfoResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAllCloudArchiveVideoFragmentsInfoResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
