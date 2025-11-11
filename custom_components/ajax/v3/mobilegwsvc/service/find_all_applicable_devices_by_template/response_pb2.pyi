from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_id_pb2 as _light_device_id_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllApplicableDevicesByTemplateResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("device_ids",)
        DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
        device_ids: _containers.RepeatedCompositeFieldContainer[
            _light_device_id_pb2.LightDeviceId
        ]
        def __init__(
            self,
            device_ids: _Iterable[_light_device_id_pb2.LightDeviceId | _Mapping]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "permission_denied", "space_not_found")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        def __init__(
            self,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: FindAllApplicableDevicesByTemplateResponse.Success
    failure: FindAllApplicableDevicesByTemplateResponse.Failure
    def __init__(
        self,
        success: FindAllApplicableDevicesByTemplateResponse.Success
        | _Mapping
        | None = ...,
        failure: FindAllApplicableDevicesByTemplateResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
