from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class PassiveHub(_message.Message):
    __slots__ = (
        "add_hub_by_qr_transition",
        "id",
        "room_id",
        "transfer_hub_settings_transition",
    )
    class AddHubByQrTransition(_message.Message):
        __slots__ = ("stage",)
        class Stage(_message.Message):
            __slots__ = ("transition_failed", "transition_in_progress")
            class TransitionInProgress(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            class TransitionFailed(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            TRANSITION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FAILED_FIELD_NUMBER: _ClassVar[int]
            transition_in_progress: (
                PassiveHub.AddHubByQrTransition.Stage.TransitionInProgress
            )
            transition_failed: PassiveHub.AddHubByQrTransition.Stage.TransitionFailed
            def __init__(
                self,
                transition_in_progress: PassiveHub.AddHubByQrTransition.Stage.TransitionInProgress
                | _Mapping
                | None = ...,
                transition_failed: PassiveHub.AddHubByQrTransition.Stage.TransitionFailed
                | _Mapping
                | None = ...,
            ) -> None: ...

        STAGE_FIELD_NUMBER: _ClassVar[int]
        stage: PassiveHub.AddHubByQrTransition.Stage
        def __init__(
            self, stage: PassiveHub.AddHubByQrTransition.Stage | _Mapping | None = ...
        ) -> None: ...

    class TransferHubSettingsTransition(_message.Message):
        __slots__ = ("stage",)
        class Stage(_message.Message):
            __slots__ = (
                "transition_completed",
                "transition_failed",
                "transition_in_progress",
            )
            class TransitionInProgress(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            class TransitionFailed(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            class TransitionCompleted(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            TRANSITION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FAILED_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_COMPLETED_FIELD_NUMBER: _ClassVar[int]
            transition_in_progress: (
                PassiveHub.TransferHubSettingsTransition.Stage.TransitionInProgress
            )
            transition_failed: (
                PassiveHub.TransferHubSettingsTransition.Stage.TransitionFailed
            )
            transition_completed: (
                PassiveHub.TransferHubSettingsTransition.Stage.TransitionCompleted
            )
            def __init__(
                self,
                transition_in_progress: PassiveHub.TransferHubSettingsTransition.Stage.TransitionInProgress
                | _Mapping
                | None = ...,
                transition_failed: PassiveHub.TransferHubSettingsTransition.Stage.TransitionFailed
                | _Mapping
                | None = ...,
                transition_completed: PassiveHub.TransferHubSettingsTransition.Stage.TransitionCompleted
                | _Mapping
                | None = ...,
            ) -> None: ...

        STAGE_FIELD_NUMBER: _ClassVar[int]
        stage: PassiveHub.TransferHubSettingsTransition.Stage
        def __init__(
            self,
            stage: PassiveHub.TransferHubSettingsTransition.Stage
            | _Mapping
            | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_HUB_BY_QR_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_HUB_SETTINGS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    room_id: str
    add_hub_by_qr_transition: PassiveHub.AddHubByQrTransition
    transfer_hub_settings_transition: PassiveHub.TransferHubSettingsTransition
    def __init__(
        self,
        id: str | None = ...,
        room_id: str | None = ...,
        add_hub_by_qr_transition: PassiveHub.AddHubByQrTransition
        | _Mapping
        | None = ...,
        transfer_hub_settings_transition: PassiveHub.TransferHubSettingsTransition
        | _Mapping
        | None = ...,
    ) -> None: ...
