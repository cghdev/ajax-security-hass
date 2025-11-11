from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UploadSpaceImageResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("images",)
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        images: _image_pb2.Images
        def __init__(
            self, images: _image_pb2.Images | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "too_large_file", "unsupported_format")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        TOO_LARGE_FILE_FIELD_NUMBER: _ClassVar[int]
        UNSUPPORTED_FORMAT_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        too_large_file: _response_pb2.DefaultError
        unsupported_format: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            too_large_file: _response_pb2.DefaultError | _Mapping | None = ...,
            unsupported_format: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UploadSpaceImageResponse.Success
    failure: UploadSpaceImageResponse.Failure
    def __init__(
        self,
        success: UploadSpaceImageResponse.Success | _Mapping | None = ...,
        failure: UploadSpaceImageResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
