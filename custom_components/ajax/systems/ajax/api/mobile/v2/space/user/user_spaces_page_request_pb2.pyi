from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common import pagination_pb2 as _pagination_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import space_lite_pb2 as _space_lite_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindUserSpacesWithPaginationRequest(_message.Message):
    __slots__ = ("limit", "pagination", "search_phrase")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PHRASE_FIELD_NUMBER: _ClassVar[int]
    limit: int
    pagination: _pagination_pb2.Pagination
    search_phrase: str
    def __init__(
        self,
        limit: int | None = ...,
        pagination: _pagination_pb2.Pagination | _Mapping | None = ...,
        search_phrase: str | None = ...,
    ) -> None: ...

class FindUserSpacesWithPaginationResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("pagination", "spaces")
        SPACES_FIELD_NUMBER: _ClassVar[int]
        PAGINATION_FIELD_NUMBER: _ClassVar[int]
        spaces: _containers.RepeatedCompositeFieldContainer[_space_lite_pb2.LiteSpace]
        pagination: _pagination_pb2.Pagination
        def __init__(
            self,
            spaces: _Iterable[_space_lite_pb2.LiteSpace | _Mapping] | None = ...,
            pagination: _pagination_pb2.Pagination | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        def __init__(
            self, bad_request: _response_pb2.DefaultError | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindUserSpacesWithPaginationResponse.Success
    failure: FindUserSpacesWithPaginationResponse.Failure
    def __init__(
        self,
        success: FindUserSpacesWithPaginationResponse.Success | _Mapping | None = ...,
        failure: FindUserSpacesWithPaginationResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
