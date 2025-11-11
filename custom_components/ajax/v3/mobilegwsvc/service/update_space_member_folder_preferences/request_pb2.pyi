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

class UpdateSpaceMemberFolderPreferencesRequest(_message.Message):
    __slots__ = ("preference_patch",)
    class FolderPreferencesPatch(_message.Message):
        __slots__ = ("folder_preferences_patch", "member_id", "space_id")
        class FolderPreferencePatch(_message.Message):
            __slots__ = ("enabled", "preference")
            PREFERENCE_FIELD_NUMBER: _ClassVar[int]
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            preference: _display_member_notification_preferences_pb2.DisplayMemberFolderPreference
            enabled: bool
            def __init__(
                self,
                preference: _display_member_notification_preferences_pb2.DisplayMemberFolderPreference
                | str
                | None = ...,
                enabled: bool = ...,
            ) -> None: ...

        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        FOLDER_PREFERENCES_PATCH_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        member_id: str
        folder_preferences_patch: _containers.RepeatedCompositeFieldContainer[
            UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch.FolderPreferencePatch
        ]
        def __init__(
            self,
            space_id: str | None = ...,
            member_id: str | None = ...,
            folder_preferences_patch: _Iterable[
                UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch.FolderPreferencePatch
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    PREFERENCE_PATCH_FIELD_NUMBER: _ClassVar[int]
    preference_patch: UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch
    def __init__(
        self,
        preference_patch: UpdateSpaceMemberFolderPreferencesRequest.FolderPreferencesPatch
        | _Mapping
        | None = ...,
    ) -> None: ...
