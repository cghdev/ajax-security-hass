from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AccessKey(_message.Message):
    __slots__ = (
        "access_key_id",
        "associated_group_id",
        "associated_user_id",
        "cms_device_index",
        "id",
        "name",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    access_key_id: str
    associated_group_id: str
    associated_user_id: str
    cms_device_index: int
    def __init__(
        self,
        id: str | None = ...,
        name: _name_pb2.Name | _Mapping | None = ...,
        access_key_id: str | None = ...,
        associated_group_id: str | None = ...,
        associated_user_id: str | None = ...,
        cms_device_index: int | None = ...,
    ) -> None: ...
