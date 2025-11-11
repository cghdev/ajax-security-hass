from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.resource.audio import (
    audio_format_pb2 as _audio_format_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindAudioFilesForAudioScenariosResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("audio_files",)
        AUDIO_FILES_FIELD_NUMBER: _ClassVar[int]
        audio_files: _containers.RepeatedCompositeFieldContainer[
            FindAudioFilesForAudioScenariosResponse.AudioFile
        ]
        def __init__(
            self,
            audio_files: _Iterable[
                FindAudioFilesForAudioScenariosResponse.AudioFile | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("file_not_found",)
        FILE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        file_not_found: _response_pb2.Error
        def __init__(
            self, file_not_found: _response_pb2.Error | _Mapping | None = ...
        ) -> None: ...

    class AudioFile(_message.Message):
        __slots__ = (
            "audio_file_variant",
            "expiration_time",
            "file_id",
            "file_name",
            "sample_id",
            "slot_id",
        )
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        SLOT_ID_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FILE_VARIANT_FIELD_NUMBER: _ClassVar[int]
        EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
        file_id: str
        slot_id: int
        sample_id: int
        file_name: str
        audio_file_variant: FindAudioFilesForAudioScenariosResponse.AudioFileVariant
        expiration_time: _timestamp_pb2.Timestamp
        def __init__(
            self,
            file_id: str | None = ...,
            slot_id: int | None = ...,
            sample_id: int | None = ...,
            file_name: str | None = ...,
            audio_file_variant: FindAudioFilesForAudioScenariosResponse.AudioFileVariant
            | _Mapping
            | None = ...,
            expiration_time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        ) -> None: ...

    class AudioFileVariant(_message.Message):
        __slots__ = ("audio_format", "duration", "url")
        AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        audio_format: _audio_format_pb2.AudioFormat
        url: str
        duration: _duration_pb2.Duration
        def __init__(
            self,
            audio_format: _audio_format_pb2.AudioFormat | str | None = ...,
            url: str | None = ...,
            duration: _duration_pb2.Duration | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAudioFilesForAudioScenariosResponse.Success
    failure: FindAudioFilesForAudioScenariosResponse.Failure
    def __init__(
        self,
        success: FindAudioFilesForAudioScenariosResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAudioFilesForAudioScenariosResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
