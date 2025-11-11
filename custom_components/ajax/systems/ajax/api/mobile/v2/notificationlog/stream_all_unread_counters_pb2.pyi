from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamAllUnreadCountersRequest(_message.Message):
    __slots__ = ("counters_origin_type",)
    class CountersOriginType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPACE: _ClassVar[StreamAllUnreadCountersRequest.CountersOriginType]
        HUB: _ClassVar[StreamAllUnreadCountersRequest.CountersOriginType]

    SPACE: StreamAllUnreadCountersRequest.CountersOriginType
    HUB: StreamAllUnreadCountersRequest.CountersOriginType
    COUNTERS_ORIGIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    counters_origin_type: StreamAllUnreadCountersRequest.CountersOriginType
    def __init__(
        self,
        counters_origin_type: StreamAllUnreadCountersRequest.CountersOriginType
        | str
        | None = ...,
    ) -> None: ...

class StreamAllUnreadCountersResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("origin_counters",)
        class OriginTotalCounter(_message.Message):
            __slots__ = ("originId", "total_counter")
            ORIGINID_FIELD_NUMBER: _ClassVar[int]
            TOTAL_COUNTER_FIELD_NUMBER: _ClassVar[int]
            originId: str
            total_counter: int
            def __init__(
                self, originId: str | None = ..., total_counter: int | None = ...
            ) -> None: ...

        ORIGIN_COUNTERS_FIELD_NUMBER: _ClassVar[int]
        origin_counters: _containers.RepeatedCompositeFieldContainer[
            StreamAllUnreadCountersResponse.Success.OriginTotalCounter
        ]
        def __init__(
            self,
            origin_counters: _Iterable[
                StreamAllUnreadCountersResponse.Success.OriginTotalCounter | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "internal_error")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.DefaultError
        internal_error: _response_pb2.DefaultError
        def __init__(
            self,
            illegal_argument: _response_pb2.DefaultError | _Mapping | None = ...,
            internal_error: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamAllUnreadCountersResponse.Success
    failure: StreamAllUnreadCountersResponse.Failure
    def __init__(
        self,
        success: StreamAllUnreadCountersResponse.Success | _Mapping | None = ...,
        failure: StreamAllUnreadCountersResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
