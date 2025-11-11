from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteAudioFileForAudioScenariosRequest(_message.Message):
    __slots__ = ("audio_sample_identifier", "hub_id")
    class AudioSampleIdentifier(_message.Message):
        __slots__ = ("file_id", "slot_id")
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        slot_id: int
        file_id: str
        def __init__(
            self, slot_id: int | None = ..., file_id: str | None = ...
        ) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SAMPLE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    audio_sample_identifier: (
        DeleteAudioFileForAudioScenariosRequest.AudioSampleIdentifier
    )
    def __init__(
        self,
        hub_id: str | None = ...,
        audio_sample_identifier: DeleteAudioFileForAudioScenariosRequest.AudioSampleIdentifier
        | _Mapping
        | None = ...,
    ) -> None: ...
