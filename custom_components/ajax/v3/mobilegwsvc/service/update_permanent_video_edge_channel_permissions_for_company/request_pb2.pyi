from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.privacy import (
    channel_permission_policy_pb2 as _channel_permission_policy_pb2,
)
from v3.mobilegwsvc.commonmodels.video.privacy import (
    channel_permission_update_pb2 as _channel_permission_update_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePermanentVideoEdgeChannelPermissionsForCompanyRequest(_message.Message):
    __slots__ = (
        "channel_id",
        "company_hex_id",
        "policy",
        "space_locator",
        "updates",
        "video_edge_id",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    company_hex_id: str
    video_edge_id: str
    channel_id: str
    updates: _containers.RepeatedCompositeFieldContainer[
        _channel_permission_update_pb2.ChannelPermissionUpdate
    ]
    policy: _channel_permission_policy_pb2.ChannelPermissionPolicy
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        company_hex_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        updates: _Iterable[
            _channel_permission_update_pb2.ChannelPermissionUpdate | _Mapping
        ]
        | None = ...,
        policy: _channel_permission_policy_pb2.ChannelPermissionPolicy
        | _Mapping
        | None = ...,
    ) -> None: ...
