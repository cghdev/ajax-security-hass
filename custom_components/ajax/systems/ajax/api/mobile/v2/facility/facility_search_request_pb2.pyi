from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from v1.facility import facility_pb2 as _facility_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FacilitySearchRequest(_message.Message):
    __slots__ = ("limit", "offset", "search_phrase")
    SEARCH_PHRASE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search_phrase: str
    limit: int
    offset: int
    def __init__(
        self,
        search_phrase: str | None = ...,
        limit: int | None = ...,
        offset: int | None = ...,
    ) -> None: ...

class FacilitySearchResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("counter", "facilities", "offset")
        FACILITIES_FIELD_NUMBER: _ClassVar[int]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        COUNTER_FIELD_NUMBER: _ClassVar[int]
        facilities: _containers.RepeatedCompositeFieldContainer[_facility_pb2.Facility]
        offset: int
        counter: int
        def __init__(
            self,
            facilities: _Iterable[_facility_pb2.Facility | _Mapping] | None = ...,
            offset: int | None = ...,
            counter: int | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "message")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FacilitySearchResponse.Success
    failure: FacilitySearchResponse.Failure
    def __init__(
        self,
        success: FacilitySearchResponse.Success | _Mapping | None = ...,
        failure: FacilitySearchResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
