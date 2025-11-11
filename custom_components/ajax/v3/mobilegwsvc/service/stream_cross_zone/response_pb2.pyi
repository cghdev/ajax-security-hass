from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import cross_zone_pb2 as _cross_zone_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCrossZoneResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("created", "deleted", "snapshot", "updated")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamCrossZoneResponse.CrossZones
        created: StreamCrossZoneResponse.CrossZones
        updated: StreamCrossZoneResponse.CrossZones
        deleted: StreamCrossZoneResponse.CrossZones
        def __init__(
            self,
            snapshot: StreamCrossZoneResponse.CrossZones | _Mapping | None = ...,
            created: StreamCrossZoneResponse.CrossZones | _Mapping | None = ...,
            updated: StreamCrossZoneResponse.CrossZones | _Mapping | None = ...,
            deleted: StreamCrossZoneResponse.CrossZones | _Mapping | None = ...,
        ) -> None: ...

    class CrossZones(_message.Message):
        __slots__ = ("cross_zones",)
        CROSS_ZONES_FIELD_NUMBER: _ClassVar[int]
        cross_zones: _containers.RepeatedCompositeFieldContainer[
            _cross_zone_pb2.CrossZone
        ]
        def __init__(
            self,
            cross_zones: _Iterable[_cross_zone_pb2.CrossZone | _Mapping] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_not_found",
            "illegal_argument",
            "request_timeout",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        illegal_argument: _response_pb2.Error
        request_timeout: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            request_timeout: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamCrossZoneResponse.Success
    failure: StreamCrossZoneResponse.Failure
    def __init__(
        self,
        success: StreamCrossZoneResponse.Success | _Mapping | None = ...,
        failure: StreamCrossZoneResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
