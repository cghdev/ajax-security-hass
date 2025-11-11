from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.videoedge.channel import (
    channel_pb2 as _channel_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_id_pb2 as _light_device_id_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_pb2 as _light_device_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_state_pb2 as _light_device_state_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_status_pb2 as _light_device_status_pb2,
)
from v3.mobilegwsvc.commonmodels.space.smartlock.light import (
    light_smart_lock_pb2 as _light_smart_lock_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.light import (
    light_video_edge_pb2 as _light_video_edge_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamLightDevicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "updates")
        class Snapshot(_message.Message):
            __slots__ = ("light_devices",)
            LIGHT_DEVICES_FIELD_NUMBER: _ClassVar[int]
            light_devices: _containers.RepeatedCompositeFieldContainer[
                _light_device_pb2.LightDevice
            ]
            def __init__(
                self,
                light_devices: _Iterable[_light_device_pb2.LightDevice | _Mapping]
                | None = ...,
            ) -> None: ...

        class Updates(_message.Message):
            __slots__ = ("updates",)
            UPDATES_FIELD_NUMBER: _ClassVar[int]
            updates: _containers.RepeatedCompositeFieldContainer[
                StreamLightDevicesResponse.Success.Update
            ]
            def __init__(
                self,
                updates: _Iterable[StreamLightDevicesResponse.Success.Update | _Mapping]
                | None = ...,
            ) -> None: ...

        class Update(_message.Message):
            __slots__ = (
                "device_id",
                "light_smart_lock_update",
                "light_video_edge_channel_update",
                "light_video_edge_update",
                "malfunctions_update",
                "snapshot_update",
                "state_update",
                "status_update",
            )
            class SnapshotUpdate(_message.Message):
                __slots__ = ("light_device", "update_type")
                LIGHT_DEVICE_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                light_device: _light_device_pb2.LightDevice
                update_type: _response_pb2.UpdateType
                def __init__(
                    self,
                    light_device: _light_device_pb2.LightDevice | _Mapping | None = ...,
                    update_type: _response_pb2.UpdateType | str | None = ...,
                ) -> None: ...

            class LightSmartLockUpdate(_message.Message):
                __slots__ = ("spread_properties_update",)
                class SmartLockSpreadPropertiesUpdate(_message.Message):
                    __slots__ = ("spread_property", "update_type")
                    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                    SPREAD_PROPERTY_FIELD_NUMBER: _ClassVar[int]
                    update_type: _response_pb2.UpdateType
                    spread_property: (
                        _light_smart_lock_pb2.LightSmartLock.SmartLockSpreadProperty
                    )
                    def __init__(
                        self,
                        update_type: _response_pb2.UpdateType | str | None = ...,
                        spread_property: _light_smart_lock_pb2.LightSmartLock.SmartLockSpreadProperty
                        | _Mapping
                        | None = ...,
                    ) -> None: ...

                SPREAD_PROPERTIES_UPDATE_FIELD_NUMBER: _ClassVar[int]
                spread_properties_update: StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate.SmartLockSpreadPropertiesUpdate
                def __init__(
                    self,
                    spread_properties_update: StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate.SmartLockSpreadPropertiesUpdate
                    | _Mapping
                    | None = ...,
                ) -> None: ...

            class LightVideoEdgeUpdate(_message.Message):
                __slots__ = ("name", "room_id", "spread_properties_update")
                class SpreadPropertiesUpdate(_message.Message):
                    __slots__ = ("spread_properties", "update_type")
                    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                    update_type: _response_pb2.UpdateType
                    spread_properties: (
                        _light_video_edge_pb2.LightVideoEdge.SpreadProperties
                    )
                    def __init__(
                        self,
                        update_type: _response_pb2.UpdateType | str | None = ...,
                        spread_properties: _light_video_edge_pb2.LightVideoEdge.SpreadProperties
                        | _Mapping
                        | None = ...,
                    ) -> None: ...

                SPREAD_PROPERTIES_UPDATE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                spread_properties_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate.SpreadPropertiesUpdate
                name: str
                room_id: str
                def __init__(
                    self,
                    spread_properties_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate.SpreadPropertiesUpdate
                    | _Mapping
                    | None = ...,
                    name: str | None = ...,
                    room_id: str | None = ...,
                ) -> None: ...

            class LightVideoEdgeChannelUpdate(_message.Message):
                __slots__ = (
                    "backup_channel_properties",
                    "group_id",
                    "name",
                    "room_id",
                    "source_aliases",
                    "spread_properties_update",
                )
                class SpreadPropertiesUpdate(_message.Message):
                    __slots__ = ("spread_properties", "update_type")
                    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                    SPREAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                    update_type: _response_pb2.UpdateType
                    spread_properties: (
                        _light_video_edge_pb2.LightVideoEdgeChannel.SpreadProperties
                    )
                    def __init__(
                        self,
                        update_type: _response_pb2.UpdateType | str | None = ...,
                        spread_properties: _light_video_edge_pb2.LightVideoEdgeChannel.SpreadProperties
                        | _Mapping
                        | None = ...,
                    ) -> None: ...

                SOURCE_ALIASES_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                GROUP_ID_FIELD_NUMBER: _ClassVar[int]
                BACKUP_CHANNEL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
                SPREAD_PROPERTIES_UPDATE_FIELD_NUMBER: _ClassVar[int]
                source_aliases: _channel_pb2.SourceAliases
                name: str
                room_id: str
                group_id: str
                backup_channel_properties: (
                    _light_video_edge_pb2.LightVideoEdgeChannel.BackupChannelProperties
                )
                spread_properties_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate.SpreadPropertiesUpdate
                def __init__(
                    self,
                    source_aliases: _channel_pb2.SourceAliases | _Mapping | None = ...,
                    name: str | None = ...,
                    room_id: str | None = ...,
                    group_id: str | None = ...,
                    backup_channel_properties: _light_video_edge_pb2.LightVideoEdgeChannel.BackupChannelProperties
                    | _Mapping
                    | None = ...,
                    spread_properties_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate.SpreadPropertiesUpdate
                    | _Mapping
                    | None = ...,
                ) -> None: ...

            class StatusUpdate(_message.Message):
                __slots__ = ("status", "update_type")
                STATUS_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                status: _light_device_status_pb2.LightDeviceStatus
                update_type: _response_pb2.UpdateType
                def __init__(
                    self,
                    status: _light_device_status_pb2.LightDeviceStatus
                    | _Mapping
                    | None = ...,
                    update_type: _response_pb2.UpdateType | str | None = ...,
                ) -> None: ...

            class StateUpdate(_message.Message):
                __slots__ = ("state", "update_type")
                STATE_FIELD_NUMBER: _ClassVar[int]
                UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
                state: _light_device_state_pb2.LightDeviceState
                update_type: _response_pb2.UpdateType
                def __init__(
                    self,
                    state: _light_device_state_pb2.LightDeviceState | str | None = ...,
                    update_type: _response_pb2.UpdateType | str | None = ...,
                ) -> None: ...

            DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            SNAPSHOT_UPDATE_FIELD_NUMBER: _ClassVar[int]
            STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
            MALFUNCTIONS_UPDATE_FIELD_NUMBER: _ClassVar[int]
            STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
            LIGHT_VIDEO_EDGE_UPDATE_FIELD_NUMBER: _ClassVar[int]
            LIGHT_VIDEO_EDGE_CHANNEL_UPDATE_FIELD_NUMBER: _ClassVar[int]
            LIGHT_SMART_LOCK_UPDATE_FIELD_NUMBER: _ClassVar[int]
            device_id: _light_device_id_pb2.LightDeviceId
            snapshot_update: StreamLightDevicesResponse.Success.Update.SnapshotUpdate
            status_update: StreamLightDevicesResponse.Success.Update.StatusUpdate
            malfunctions_update: int
            state_update: StreamLightDevicesResponse.Success.Update.StateUpdate
            light_video_edge_update: (
                StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate
            )
            light_video_edge_channel_update: (
                StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate
            )
            light_smart_lock_update: (
                StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate
            )
            def __init__(
                self,
                device_id: _light_device_id_pb2.LightDeviceId | _Mapping | None = ...,
                snapshot_update: StreamLightDevicesResponse.Success.Update.SnapshotUpdate
                | _Mapping
                | None = ...,
                status_update: StreamLightDevicesResponse.Success.Update.StatusUpdate
                | _Mapping
                | None = ...,
                malfunctions_update: int | None = ...,
                state_update: StreamLightDevicesResponse.Success.Update.StateUpdate
                | _Mapping
                | None = ...,
                light_video_edge_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeUpdate
                | _Mapping
                | None = ...,
                light_video_edge_channel_update: StreamLightDevicesResponse.Success.Update.LightVideoEdgeChannelUpdate
                | _Mapping
                | None = ...,
                light_smart_lock_update: StreamLightDevicesResponse.Success.Update.LightSmartLockUpdate
                | _Mapping
                | None = ...,
            ) -> None: ...

        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamLightDevicesResponse.Success.Snapshot
        updates: StreamLightDevicesResponse.Success.Updates
        def __init__(
            self,
            snapshot: StreamLightDevicesResponse.Success.Snapshot
            | _Mapping
            | None = ...,
            updates: StreamLightDevicesResponse.Success.Updates | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        def __init__(
            self, bad_request: _response_pb2.Error | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamLightDevicesResponse.Success
    failure: StreamLightDevicesResponse.Failure
    def __init__(
        self,
        success: StreamLightDevicesResponse.Success | _Mapping | None = ...,
        failure: StreamLightDevicesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
