from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space import (
    space_profile_pb2 as _space_profile_pb2,
)
from v3.mobilegwsvc.commonmodels.space.integration import (
    space_integration_type_pb2 as _space_integration_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialsInfo(_message.Message):
    __slots__ = ("created_at", "external_user", "id", "relations", "type")
    class Relation(_message.Message):
        __slots__ = ("space_relation", "standalone_device_relation")
        STANDALONE_DEVICE_RELATION_FIELD_NUMBER: _ClassVar[int]
        SPACE_RELATION_FIELD_NUMBER: _ClassVar[int]
        standalone_device_relation: CredentialsInfo.StandaloneDeviceRelation
        space_relation: CredentialsInfo.SpaceRelation
        def __init__(
            self,
            standalone_device_relation: CredentialsInfo.StandaloneDeviceRelation
            | _Mapping
            | None = ...,
            space_relation: CredentialsInfo.SpaceRelation | _Mapping | None = ...,
        ) -> None: ...

    class StandaloneDeviceRelation(_message.Message):
        __slots__ = (
            "device_name",
            "room_id",
            "room_name",
            "smart_lock_id",
            "space_id",
            "space_name",
        )
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        smart_lock_id: str
        device_name: str
        space_name: str
        room_id: str
        room_name: str
        def __init__(
            self,
            space_id: str | None = ...,
            smart_lock_id: str | None = ...,
            device_name: str | None = ...,
            space_name: str | None = ...,
            room_id: str | None = ...,
            room_name: str | None = ...,
        ) -> None: ...

    class SpaceRelation(_message.Message):
        __slots__ = ("profile", "space_id", "space_name")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        space_name: str
        profile: _space_profile_pb2.SpaceProfile
        def __init__(
            self,
            space_id: str | None = ...,
            space_name: str | None = ...,
            profile: _space_profile_pb2.SpaceProfile | _Mapping | None = ...,
        ) -> None: ...

    class ExternalUser(_message.Message):
        __slots__ = ("email", "id", "image_url")
        ID_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        id: str
        email: str
        image_url: str
        def __init__(
            self,
            id: str | None = ...,
            email: str | None = ...,
            image_url: str | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_USER_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: _space_integration_type_pb2.SpaceIntegrationType
    created_at: _timestamp_pb2.Timestamp
    relations: _containers.RepeatedCompositeFieldContainer[CredentialsInfo.Relation]
    external_user: CredentialsInfo.ExternalUser
    def __init__(
        self,
        id: str | None = ...,
        type: _space_integration_type_pb2.SpaceIntegrationType | str | None = ...,
        created_at: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        relations: _Iterable[CredentialsInfo.Relation | _Mapping] | None = ...,
        external_user: CredentialsInfo.ExternalUser | _Mapping | None = ...,
    ) -> None: ...
