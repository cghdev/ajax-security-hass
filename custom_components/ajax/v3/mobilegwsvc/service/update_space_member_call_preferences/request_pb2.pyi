from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space.member import (
    display_member_notification_preferences_pb2 as _display_member_notification_preferences_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateSpaceMemberCallPreferencesRequest(_message.Message):
    __slots__ = ("call_preferences_patches", "hub_id", "member_id")
    class CallPreferencesPatch(_message.Message):
        __slots__ = ("call_preference", "enabled")
        CALL_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        call_preference: (
            _display_member_notification_preferences_pb2.DisplayMemberCallPreference
        )
        enabled: bool
        def __init__(
            self,
            call_preference: _display_member_notification_preferences_pb2.DisplayMemberCallPreference
            | str
            | None = ...,
            enabled: bool = ...,
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_PREFERENCES_PATCHES_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    member_id: str
    call_preferences_patches: _containers.RepeatedCompositeFieldContainer[
        UpdateSpaceMemberCallPreferencesRequest.CallPreferencesPatch
    ]
    def __init__(
        self,
        hub_id: str | None = ...,
        member_id: str | None = ...,
        call_preferences_patches: _Iterable[
            UpdateSpaceMemberCallPreferencesRequest.CallPreferencesPatch | _Mapping
        ]
        | None = ...,
    ) -> None: ...
