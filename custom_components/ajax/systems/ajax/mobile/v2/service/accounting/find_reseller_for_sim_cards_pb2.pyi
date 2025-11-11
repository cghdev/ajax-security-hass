from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    accounting_company_pb2 as _accounting_company_pb2,
)
from systems.ajax.api.mobile.v2.common.accounting import feature_pb2 as _feature_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindResellerForSimCardsRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: str | None = ...) -> None: ...

class FindResellerForSimCardsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("company", "features")
        COMPANY_FIELD_NUMBER: _ClassVar[int]
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        company: _accounting_company_pb2.AccountingCompany
        features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
        def __init__(
            self,
            company: _accounting_company_pb2.AccountingCompany | _Mapping | None = ...,
            features: _Iterable[_feature_pb2.Feature | _Mapping] | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("message", "not_found")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        message: str
        not_found: _response_pb2.DefaultError
        def __init__(
            self,
            message: str | None = ...,
            not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindResellerForSimCardsResponse.Success
    failure: FindResellerForSimCardsResponse.Failure
    def __init__(
        self,
        success: FindResellerForSimCardsResponse.Success | _Mapping | None = ...,
        failure: FindResellerForSimCardsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
