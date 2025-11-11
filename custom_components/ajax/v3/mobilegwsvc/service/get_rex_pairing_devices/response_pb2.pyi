from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.virtualobject import (
    selected_device_pb2 as _selected_device_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetRexPairingDevicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[
            _selected_device_pb2.SelectedDevice
        ]
        def __init__(
            self,
            devices: _Iterable[_selected_device_pb2.SelectedDevice | _Mapping]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetRexPairingDevicesResponse.Success
    failure: GetRexPairingDevicesResponse.Failure
    def __init__(
        self,
        success: GetRexPairingDevicesResponse.Success | _Mapping | None = ...,
        failure: GetRexPairingDevicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
