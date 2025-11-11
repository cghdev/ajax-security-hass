from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.videoedge.network import (
    network_interface_pb2 as _network_interface_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ScanVideoEdgeWifiResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "network_interfaces_removed",
            "network_interfaces_replaced",
            "network_interfaces_snapshot",
        )
        class NetworkInterfacesSnapshot(_message.Message):
            __slots__ = ("network_interfaces",)
            NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            network_interfaces: _containers.RepeatedCompositeFieldContainer[
                _network_interface_pb2.NetworkInterface
            ]
            def __init__(
                self,
                network_interfaces: _Iterable[
                    _network_interface_pb2.NetworkInterface | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class NetworkInterfacesReplaced(_message.Message):
            __slots__ = ("network_interfaces",)
            NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
            network_interfaces: _containers.RepeatedCompositeFieldContainer[
                _network_interface_pb2.NetworkInterface
            ]
            def __init__(
                self,
                network_interfaces: _Iterable[
                    _network_interface_pb2.NetworkInterface | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class NetworkInterfacesRemoved(_message.Message):
            __slots__ = ("network_interface_ids",)
            NETWORK_INTERFACE_IDS_FIELD_NUMBER: _ClassVar[int]
            network_interface_ids: _containers.RepeatedScalarFieldContainer[str]
            def __init__(
                self, network_interface_ids: _Iterable[str] | None = ...
            ) -> None: ...

        NETWORK_INTERFACES_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACES_REPLACED_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACES_REMOVED_FIELD_NUMBER: _ClassVar[int]
        network_interfaces_snapshot: (
            ScanVideoEdgeWifiResponse.Success.NetworkInterfacesSnapshot
        )
        network_interfaces_replaced: (
            ScanVideoEdgeWifiResponse.Success.NetworkInterfacesReplaced
        )
        network_interfaces_removed: (
            ScanVideoEdgeWifiResponse.Success.NetworkInterfacesRemoved
        )
        def __init__(
            self,
            network_interfaces_snapshot: ScanVideoEdgeWifiResponse.Success.NetworkInterfacesSnapshot
            | _Mapping
            | None = ...,
            network_interfaces_replaced: ScanVideoEdgeWifiResponse.Success.NetworkInterfacesReplaced
            | _Mapping
            | None = ...,
            network_interfaces_removed: ScanVideoEdgeWifiResponse.Success.NetworkInterfacesRemoved
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_is_busy",
            "permission_denied",
            "space_armed",
            "space_not_found",
            "unimplemented_video_edge_command",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNIMPLEMENTED_VIDEO_EDGE_COMMAND_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        unimplemented_video_edge_command: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
            unimplemented_video_edge_command: _response_pb2.Error
            | _Mapping
            | None = ...,
            hub_is_busy: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ScanVideoEdgeWifiResponse.Success
    failure: ScanVideoEdgeWifiResponse.Failure
    def __init__(
        self,
        success: ScanVideoEdgeWifiResponse.Success | _Mapping | None = ...,
        failure: ScanVideoEdgeWifiResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
