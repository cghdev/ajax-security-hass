from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import category_pb2 as _category_pb2
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_target_pb2 as _feature_target_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceGroup(_message.Message):
    __slots__ = (
        "category",
        "description",
        "feature_target",
        "id",
        "lokalise_id",
        "max_target_count_to_assign",
        "name",
        "order",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOKALISE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    MAX_TARGET_COUNT_TO_ASSIGN_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    lokalise_id: str
    description: str
    order: int
    max_target_count_to_assign: int
    category: _category_pb2.Category
    feature_target: _feature_target_pb2.FeatureTarget
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        lokalise_id: str | None = ...,
        description: str | None = ...,
        order: int | None = ...,
        max_target_count_to_assign: int | None = ...,
        category: _category_pb2.Category | str | None = ...,
        feature_target: _feature_target_pb2.FeatureTarget | str | None = ...,
    ) -> None: ...
