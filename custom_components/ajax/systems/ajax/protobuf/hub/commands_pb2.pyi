from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import camera_pb2 as _camera_pb2
from systems.ajax.protobuf.hub import object_type_pb2 as _object_type_pb2
from systems.ajax.protobuf.hub import scenario_pb2 as _scenario_pb2
from systems.ajax.protobuf.hub import update_pb2 as _update_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.hub.device import device_pb2 as _device_pb2
from systems.ajax.protobuf.hub.device import hub_device_pb2 as _hub_device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommand(_message.Message):
    __slots__ = (
        "add_access_card",
        "apply_update",
        "apply_updates",
        "arming",
        "cancel_access_key_search",
        "cancel_delete_security_company_binding",
        "cancel_search",
        "change_user_permissions",
        "change_user_role",
        "create_new_group",
        "create_new_room",
        "create_scenario",
        "create_security_company_binding",
        "delay_interconnect",
        "delete_access_card",
        "delete_access_key",
        "delete_group",
        "delete_room",
        "delete_scenario",
        "delete_security_company_binding",
        "detach_user",
        "device_command",
        "drop_cache",
        "drop_logs",
        "edit_stream_data",
        "engineer_attendance_required",
        "erase_access_card",
        "exit_card_mode",
        "forget_wifi_network",
        "get_gsm_sim_card_balance",
        "get_scanned_fibra_devices",
        "group_arming",
        "hub_id",
        "invite_users",
        "join_wifi_network",
        "join_wifi_network_advanced",
        "link_camera",
        "link_device",
        "mute_fire_detectors",
        "panic",
        "profi_hub_access_request",
        "register_access_key",
        "request_arming_reset",
        "reset_alarm_condition",
        "reset_sim_traffic_counter",
        "revoke_user_invite",
        "scan_fibra_devices",
        "scan_wifi_networks",
        "start_firmware_update",
        "start_migration",
        "stop_migration",
        "unlink_camera",
        "unlink_device",
        "update_card_state",
        "update_ethernet_settings",
        "update_groups_mode",
        "update_gsm_sim_card_balance_number",
        "update_gsm_sim_card_settings",
        "update_network_channel_state",
        "update_scenario",
        "update_wifi_settings",
    )
    class Answer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[HubCommand.Answer]
        DELIVERED: _ClassVar[HubCommand.Answer]
        DELIVERED_COMMAND_PERFORMED: _ClassVar[HubCommand.Answer]
        DELIVERED_COMMAND_NOT_PERFORMED: _ClassVar[HubCommand.Answer]
        MODE_FINISHED: _ClassVar[HubCommand.Answer]
        FAILED_INSUFFICIENT_ACCESS: _ClassVar[HubCommand.Answer]
        FAILED_UNKNOWN_COMMAND: _ClassVar[HubCommand.Answer]
        UNDELIVERED_RECEIVER_OFFLINE: _ClassVar[HubCommand.Answer]
        UNDELIVERED_WRONG_RECEIVER: _ClassVar[HubCommand.Answer]
        DELIVERED_WAS_ALREADY_PERFORMED: _ClassVar[HubCommand.Answer]
        FAILED_WRONG_PARAMETERS: _ClassVar[HubCommand.Answer]
        FAILED_WRONG_MESSAGE_TYPE: _ClassVar[HubCommand.Answer]
        TRANSPORT_EXCEPTION: _ClassVar[HubCommand.Answer]
        SERVER_ERROR: _ClassVar[HubCommand.Answer]
        REQUEST_DELIVERED: _ClassVar[HubCommand.Answer]
        BUSY: _ClassVar[HubCommand.Answer]
        HUB_ERROR: _ClassVar[HubCommand.Answer]
        WRONG_STATE: _ClassVar[HubCommand.Answer]
        OBJECTS_LIMIT: _ClassVar[HubCommand.Answer]
        PARAMS_APPLICATION_FAILURE: _ClassVar[HubCommand.Answer]
        PARTITION_NOT_EMPTY: _ClassVar[HubCommand.Answer]
        OBJECT_NOT_FOUND: _ClassVar[HubCommand.Answer]
        HUB_BLOCKED_BY_SERVICE_PROVIDER: _ClassVar[HubCommand.Answer]
        NO_DATA: _ClassVar[HubCommand.Answer]
        ALARM_RESET_NEEDED: _ClassVar[HubCommand.Answer]

    SUCCESS: HubCommand.Answer
    DELIVERED: HubCommand.Answer
    DELIVERED_COMMAND_PERFORMED: HubCommand.Answer
    DELIVERED_COMMAND_NOT_PERFORMED: HubCommand.Answer
    MODE_FINISHED: HubCommand.Answer
    FAILED_INSUFFICIENT_ACCESS: HubCommand.Answer
    FAILED_UNKNOWN_COMMAND: HubCommand.Answer
    UNDELIVERED_RECEIVER_OFFLINE: HubCommand.Answer
    UNDELIVERED_WRONG_RECEIVER: HubCommand.Answer
    DELIVERED_WAS_ALREADY_PERFORMED: HubCommand.Answer
    FAILED_WRONG_PARAMETERS: HubCommand.Answer
    FAILED_WRONG_MESSAGE_TYPE: HubCommand.Answer
    TRANSPORT_EXCEPTION: HubCommand.Answer
    SERVER_ERROR: HubCommand.Answer
    REQUEST_DELIVERED: HubCommand.Answer
    BUSY: HubCommand.Answer
    HUB_ERROR: HubCommand.Answer
    WRONG_STATE: HubCommand.Answer
    OBJECTS_LIMIT: HubCommand.Answer
    PARAMS_APPLICATION_FAILURE: HubCommand.Answer
    PARTITION_NOT_EMPTY: HubCommand.Answer
    OBJECT_NOT_FOUND: HubCommand.Answer
    HUB_BLOCKED_BY_SERVICE_PROVIDER: HubCommand.Answer
    NO_DATA: HubCommand.Answer
    ALARM_RESET_NEEDED: HubCommand.Answer
    class NetworkSettingsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_NETWORK_SETTINGS_STATUS_INFO: _ClassVar[HubCommand.NetworkSettingsStatus]
        NETWORK_SET_OK: _ClassVar[HubCommand.NetworkSettingsStatus]
        NETWORK_SET_ERROR: _ClassVar[HubCommand.NetworkSettingsStatus]

    NO_NETWORK_SETTINGS_STATUS_INFO: HubCommand.NetworkSettingsStatus
    NETWORK_SET_OK: HubCommand.NetworkSettingsStatus
    NETWORK_SET_ERROR: HubCommand.NetworkSettingsStatus
    class WifiNetworkJoinStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_WIFI_NETWORK_JOIN_STATUS_INO: _ClassVar[HubCommand.WifiNetworkJoinStatus]
        JOIN_SUCCESS: _ClassVar[HubCommand.WifiNetworkJoinStatus]
        JOIN_ERROR: _ClassVar[HubCommand.WifiNetworkJoinStatus]

    NO_WIFI_NETWORK_JOIN_STATUS_INO: HubCommand.WifiNetworkJoinStatus
    JOIN_SUCCESS: HubCommand.WifiNetworkJoinStatus
    JOIN_ERROR: HubCommand.WifiNetworkJoinStatus
    class Arming(_message.Message):
        __slots__ = ("ignore_problems", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ARM: _ClassVar[HubCommand.Arming.Type]
            DISARM: _ClassVar[HubCommand.Arming.Type]
            NIGHT_MODE_ON: _ClassVar[HubCommand.Arming.Type]
            NIGHT_MODE_OFF: _ClassVar[HubCommand.Arming.Type]

        ARM: HubCommand.Arming.Type
        DISARM: HubCommand.Arming.Type
        NIGHT_MODE_ON: HubCommand.Arming.Type
        NIGHT_MODE_OFF: HubCommand.Arming.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IGNORE_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
        type: HubCommand.Arming.Type
        ignore_problems: bool
        def __init__(
            self,
            type: HubCommand.Arming.Type | str | None = ...,
            ignore_problems: bool = ...,
        ) -> None: ...

    class Panic(_message.Message):
        __slots__ = ("panic_location",)
        class PanicLocation(_message.Message):
            __slots__ = ("accuracy", "latitude", "longitude", "speed", "timestamp")
            LATITUDE_FIELD_NUMBER: _ClassVar[int]
            LONGITUDE_FIELD_NUMBER: _ClassVar[int]
            ACCURACY_FIELD_NUMBER: _ClassVar[int]
            SPEED_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            latitude: float
            longitude: float
            accuracy: float
            speed: float
            timestamp: int
            def __init__(
                self,
                latitude: float | None = ...,
                longitude: float | None = ...,
                accuracy: float | None = ...,
                speed: float | None = ...,
                timestamp: int | None = ...,
            ) -> None: ...

        PANIC_LOCATION_FIELD_NUMBER: _ClassVar[int]
        panic_location: HubCommand.Panic.PanicLocation
        def __init__(
            self, panic_location: HubCommand.Panic.PanicLocation | _Mapping | None = ...
        ) -> None: ...

    class DropCache(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class CancelSearch(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class StartFirmwareUpdate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class UpdateGroupsMode(_message.Message):
        __slots__ = ("groups_mode",)
        class GroupsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OFF: _ClassVar[HubCommand.UpdateGroupsMode.GroupsMode]
            ON: _ClassVar[HubCommand.UpdateGroupsMode.GroupsMode]

        OFF: HubCommand.UpdateGroupsMode.GroupsMode
        ON: HubCommand.UpdateGroupsMode.GroupsMode
        GROUPS_MODE_FIELD_NUMBER: _ClassVar[int]
        groups_mode: HubCommand.UpdateGroupsMode.GroupsMode
        def __init__(
            self, groups_mode: HubCommand.UpdateGroupsMode.GroupsMode | str | None = ...
        ) -> None: ...

    class ResetSimTrafficCounter(_message.Message):
        __slots__ = ("sim_card_index",)
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        sim_card_index: int
        def __init__(self, sim_card_index: int | None = ...) -> None: ...

    class MuteFireDetectors(_message.Message):
        __slots__ = ("mute_type",)
        class MuteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ALL_FIRE_DETECTORS: _ClassVar[HubCommand.MuteFireDetectors.MuteType]
            ALL_FIRE_DETECTORS_EXCEPT_TRIGGERED: _ClassVar[
                HubCommand.MuteFireDetectors.MuteType
            ]

        ALL_FIRE_DETECTORS: HubCommand.MuteFireDetectors.MuteType
        ALL_FIRE_DETECTORS_EXCEPT_TRIGGERED: HubCommand.MuteFireDetectors.MuteType
        MUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        mute_type: HubCommand.MuteFireDetectors.MuteType
        def __init__(
            self, mute_type: HubCommand.MuteFireDetectors.MuteType | str | None = ...
        ) -> None: ...

    class ResetAlarmCondition(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class DelayInterconnect(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class UpdateCardState(_message.Message):
        __slots__ = ("card_id", "card_state")
        class CardState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OFF: _ClassVar[HubCommand.UpdateCardState.CardState]
            ON: _ClassVar[HubCommand.UpdateCardState.CardState]

        OFF: HubCommand.UpdateCardState.CardState
        ON: HubCommand.UpdateCardState.CardState
        CARD_STATE_FIELD_NUMBER: _ClassVar[int]
        CARD_ID_FIELD_NUMBER: _ClassVar[int]
        card_state: HubCommand.UpdateCardState.CardState
        card_id: str
        def __init__(
            self,
            card_state: HubCommand.UpdateCardState.CardState | str | None = ...,
            card_id: str | None = ...,
        ) -> None: ...

    class GroupArming(_message.Message):
        __slots__ = ("group_id", "ignore_problems", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ARM: _ClassVar[HubCommand.GroupArming.Type]
            DISARM: _ClassVar[HubCommand.GroupArming.Type]

        ARM: HubCommand.GroupArming.Type
        DISARM: HubCommand.GroupArming.Type
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IGNORE_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        type: HubCommand.GroupArming.Type
        ignore_problems: bool
        def __init__(
            self,
            group_id: str | None = ...,
            type: HubCommand.GroupArming.Type | str | None = ...,
            ignore_problems: bool = ...,
        ) -> None: ...

    class DropLogs(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class InviteUsers(_message.Message):
        __slots__ = ("emails", "role")
        class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            USER: _ClassVar[HubCommand.InviteUsers.Role]
            PRO: _ClassVar[HubCommand.InviteUsers.Role]

        USER: HubCommand.InviteUsers.Role
        PRO: HubCommand.InviteUsers.Role
        EMAILS_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        emails: _containers.RepeatedScalarFieldContainer[str]
        role: HubCommand.InviteUsers.Role
        def __init__(
            self,
            emails: _Iterable[str] | None = ...,
            role: HubCommand.InviteUsers.Role | str | None = ...,
        ) -> None: ...

    class RevokeUserInvite(_message.Message):
        __slots__ = ("email",)
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        email: str
        def __init__(self, email: str | None = ...) -> None: ...

    class ProfiHubAccessRequest(_message.Message):
        __slots__ = (
            "permissions",
            "time_of_access_in_hours",
            "user_email",
            "user_id",
            "user_name",
        )
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        TIME_OF_ACCESS_IN_HOURS_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        user_email: str
        user_name: str
        permissions: _containers.RepeatedScalarFieldContainer[_user_pb2.User.Permission]
        time_of_access_in_hours: int
        def __init__(
            self,
            user_id: str | None = ...,
            user_email: str | None = ...,
            user_name: str | None = ...,
            permissions: _Iterable[_user_pb2.User.Permission | str] | None = ...,
            time_of_access_in_hours: int | None = ...,
        ) -> None: ...

    class DetachUser(_message.Message):
        __slots__ = ("user_id",)
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        def __init__(self, user_id: str | None = ...) -> None: ...

    class CreateNewRoom(_message.Message):
        __slots__ = ("room_name",)
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        room_name: str
        def __init__(self, room_name: str | None = ...) -> None: ...

    class DeleteRoom(_message.Message):
        __slots__ = ("room_id",)
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        def __init__(self, room_id: str | None = ...) -> None: ...

    class CreateNewGroup(_message.Message):
        __slots__ = ("group_name",)
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        group_name: str
        def __init__(self, group_name: str | None = ...) -> None: ...

    class DeleteGroup(_message.Message):
        __slots__ = ("group_id",)
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        def __init__(self, group_id: str | None = ...) -> None: ...

    class LinkCamera(_message.Message):
        __slots__ = (
            "camera_name",
            "dvr",
            "parent_camera_id",
            "room_id",
            "service_type",
            "stream_data_url",
        )
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        CAMERA_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
        DVR_FIELD_NUMBER: _ClassVar[int]
        PARENT_CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        camera_name: str
        service_type: _camera_pb2.Camera.ServiceType
        stream_data_url: str
        dvr: bool
        parent_camera_id: str
        def __init__(
            self,
            room_id: str | None = ...,
            camera_name: str | None = ...,
            service_type: _camera_pb2.Camera.ServiceType | str | None = ...,
            stream_data_url: str | None = ...,
            dvr: bool = ...,
            parent_camera_id: str | None = ...,
        ) -> None: ...

    class UnlinkCamera(_message.Message):
        __slots__ = ("camera_id", "service_id")
        CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        camera_id: str
        service_id: str
        def __init__(
            self, camera_id: str | None = ..., service_id: str | None = ...
        ) -> None: ...

    class EditStreamData(_message.Message):
        __slots__ = (
            "camera_id",
            "dahua_or_uniview_settings",
            "hikvision_or_safire_settings",
            "service_id",
            "service_type",
            "stream_data_url",
        )
        SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
        CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
        HIKVISION_OR_SAFIRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        DAHUA_OR_UNIVIEW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        service_id: str
        camera_id: str
        service_type: _camera_pb2.Camera.ServiceType
        stream_data_url: str
        hikvision_or_safire_settings: _camera_pb2.Camera.HikvisionOrSafireSettings
        dahua_or_uniview_settings: _camera_pb2.Camera.DahuaOrUniviewSettings
        def __init__(
            self,
            service_id: str | None = ...,
            camera_id: str | None = ...,
            service_type: _camera_pb2.Camera.ServiceType | str | None = ...,
            stream_data_url: str | None = ...,
            hikvision_or_safire_settings: _camera_pb2.Camera.HikvisionOrSafireSettings
            | _Mapping
            | None = ...,
            dahua_or_uniview_settings: _camera_pb2.Camera.DahuaOrUniviewSettings
            | _Mapping
            | None = ...,
        ) -> None: ...

    class LinkDevice(_message.Message):
        __slots__ = (
            "device_name",
            "device_qr_code",
            "group_id",
            "room_id",
            "wire_input_multi_transmitter_id",
        )
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
        WIRE_INPUT_MULTI_TRANSMITTER_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        room_id: str
        group_id: str
        device_qr_code: str
        wire_input_multi_transmitter_id: HubCommand.WireInputMultiTransmitterId
        device_name: str
        def __init__(
            self,
            room_id: str | None = ...,
            group_id: str | None = ...,
            device_qr_code: str | None = ...,
            wire_input_multi_transmitter_id: HubCommand.WireInputMultiTransmitterId
            | _Mapping
            | None = ...,
            device_name: str | None = ...,
        ) -> None: ...

    class WireInputMultiTransmitterId(_message.Message):
        __slots__ = ("multi_transmitter_id", "wire_input_index")
        MULTI_TRANSMITTER_ID_FIELD_NUMBER: _ClassVar[int]
        WIRE_INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
        multi_transmitter_id: str
        wire_input_index: int
        def __init__(
            self,
            multi_transmitter_id: str | None = ...,
            wire_input_index: int | None = ...,
        ) -> None: ...

    class UnlinkDevice(_message.Message):
        __slots__ = ("device_id",)
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        device_id: str
        def __init__(self, device_id: str | None = ...) -> None: ...

    class ScanFibraDevices(_message.Message):
        __slots__ = ("action",)
        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_ACTION_INFO: _ClassVar[HubCommand.ScanFibraDevices.Action]
            START: _ClassVar[HubCommand.ScanFibraDevices.Action]
            STOP: _ClassVar[HubCommand.ScanFibraDevices.Action]

        NO_ACTION_INFO: HubCommand.ScanFibraDevices.Action
        START: HubCommand.ScanFibraDevices.Action
        STOP: HubCommand.ScanFibraDevices.Action
        ACTION_FIELD_NUMBER: _ClassVar[int]
        action: HubCommand.ScanFibraDevices.Action
        def __init__(
            self, action: HubCommand.ScanFibraDevices.Action | str | None = ...
        ) -> None: ...

    class GetScannedFibraDevices(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class CreateSecurityCompanyBinding(_message.Message):
        __slots__ = ("company_id",)
        COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        company_id: str
        def __init__(self, company_id: str | None = ...) -> None: ...

    class DeleteSecurityCompanyBinding(_message.Message):
        __slots__ = ("company_id",)
        COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        company_id: str
        def __init__(self, company_id: str | None = ...) -> None: ...

    class CancelDeleteSecurityCompanyBinding(_message.Message):
        __slots__ = ("company_id",)
        COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
        company_id: str
        def __init__(self, company_id: str | None = ...) -> None: ...

    class UpdateNetworkChannelState(_message.Message):
        __slots__ = ("channel", "state")
        class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_CHANNEL_INFO: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
            ETHERNET: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
            GSM: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]
            WIFI: _ClassVar[HubCommand.UpdateNetworkChannelState.Channel]

        NO_CHANNEL_INFO: HubCommand.UpdateNetworkChannelState.Channel
        ETHERNET: HubCommand.UpdateNetworkChannelState.Channel
        GSM: HubCommand.UpdateNetworkChannelState.Channel
        WIFI: HubCommand.UpdateNetworkChannelState.Channel
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_STATE_INFO: _ClassVar[HubCommand.UpdateNetworkChannelState.State]
            ON: _ClassVar[HubCommand.UpdateNetworkChannelState.State]
            OFF: _ClassVar[HubCommand.UpdateNetworkChannelState.State]

        NO_STATE_INFO: HubCommand.UpdateNetworkChannelState.State
        ON: HubCommand.UpdateNetworkChannelState.State
        OFF: HubCommand.UpdateNetworkChannelState.State
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        channel: HubCommand.UpdateNetworkChannelState.Channel
        state: HubCommand.UpdateNetworkChannelState.State
        def __init__(
            self,
            channel: HubCommand.UpdateNetworkChannelState.Channel | str | None = ...,
            state: HubCommand.UpdateNetworkChannelState.State | str | None = ...,
        ) -> None: ...

    class UpdateEthernetSettings(_message.Message):
        __slots__ = ("dhcp", "dns", "gate", "ip", "mask")
        DHCP_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        dhcp: bool
        ip: str
        mask: str
        gate: str
        dns: str
        def __init__(
            self,
            dhcp: bool = ...,
            ip: str | None = ...,
            mask: str | None = ...,
            gate: str | None = ...,
            dns: str | None = ...,
        ) -> None: ...

    class UpdateWifiSettings(_message.Message):
        __slots__ = ("dhcp", "dns", "gate", "ip", "mask")
        DHCP_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        dhcp: bool
        ip: str
        mask: str
        gate: str
        dns: str
        def __init__(
            self,
            dhcp: bool = ...,
            ip: str | None = ...,
            mask: str | None = ...,
            gate: str | None = ...,
            dns: str | None = ...,
        ) -> None: ...

    class UpdateGsmSimCardSettings(_message.Message):
        __slots__ = ("apn", "password", "sim_card_index", "username")
        APN_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        apn: str
        username: str
        password: str
        sim_card_index: int
        def __init__(
            self,
            apn: str | None = ...,
            username: str | None = ...,
            password: str | None = ...,
            sim_card_index: int | None = ...,
        ) -> None: ...

    class UpdateGsmSimCardBalanceNumber(_message.Message):
        __slots__ = ("balance_number", "sim_card_index")
        BALANCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        balance_number: str
        sim_card_index: int
        def __init__(
            self, balance_number: str | None = ..., sim_card_index: int | None = ...
        ) -> None: ...

    class GetGsmSimCardBalance(_message.Message):
        __slots__ = ("sim_card_index",)
        SIM_CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        sim_card_index: int
        def __init__(self, sim_card_index: int | None = ...) -> None: ...

    class ScanWifiNetworks(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class JoinWifiNetwork(_message.Message):
        __slots__ = ("password", "security_protocol", "ssid")
        SSID_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ssid: str
        security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
        password: str
        def __init__(
            self,
            ssid: str | None = ...,
            security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
            | str
            | None = ...,
            password: str | None = ...,
        ) -> None: ...

    class JoinWifiNetworkAdvanced(_message.Message):
        __slots__ = (
            "channel",
            "dhcp",
            "dns",
            "gate",
            "ip",
            "mask",
            "password",
            "security_protocol",
            "ssid",
        )
        SSID_FIELD_NUMBER: _ClassVar[int]
        SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        DHCP_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        GATE_FIELD_NUMBER: _ClassVar[int]
        DNS_FIELD_NUMBER: _ClassVar[int]
        MASK_FIELD_NUMBER: _ClassVar[int]
        ssid: str
        security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
        password: str
        dhcp: bool
        channel: int
        ip: str
        gate: str
        dns: str
        mask: str
        def __init__(
            self,
            ssid: str | None = ...,
            security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
            | str
            | None = ...,
            password: str | None = ...,
            dhcp: bool = ...,
            channel: int | None = ...,
            ip: str | None = ...,
            gate: str | None = ...,
            dns: str | None = ...,
            mask: str | None = ...,
        ) -> None: ...

    class ForgetWifiNetwork(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ApplyUpdate(_message.Message):
        __slots__ = ("update",)
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        update: _update_pb2.Update
        def __init__(
            self, update: _update_pb2.Update | _Mapping | None = ...
        ) -> None: ...

    class ApplyUpdates(_message.Message):
        __slots__ = ("updates",)
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        updates: _containers.RepeatedCompositeFieldContainer[_update_pb2.Update]
        def __init__(
            self, updates: _Iterable[_update_pb2.Update | _Mapping] | None = ...
        ) -> None: ...

    class Result(_message.Message):
        __slots__ = (
            "answer",
            "arming_error_details",
            "create_unit_response_details",
            "engineer_attendance_required_error_details",
            "gsm_sim_card_balance_response_details",
            "invite_users_response_details",
            "link_device_response_details",
            "migration_error_details",
            "network_settings_status",
            "register_access_key_error_details",
            "scan_wifi_networks_response_details",
            "scanned_fibra_devices_details",
            "wifi_network_join_status",
        )
        class ArmingErrorDetails(_message.Message):
            __slots__ = ("arm_prevent_objects",)
            class ArmPreventObject(_message.Message):
                __slots__ = (
                    "code",
                    "hub_name",
                    "source_id",
                    "source_name",
                    "source_room",
                    "source_room_id",
                    "source_type",
                    "text",
                )
                CODE_FIELD_NUMBER: _ClassVar[int]
                SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
                SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
                SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
                SOURCE_ROOM_FIELD_NUMBER: _ClassVar[int]
                SOURCE_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                TEXT_FIELD_NUMBER: _ClassVar[int]
                HUB_NAME_FIELD_NUMBER: _ClassVar[int]
                code: str
                source_id: str
                source_type: _object_type_pb2.ObjectType
                source_name: str
                source_room: str
                source_room_id: str
                text: str
                hub_name: str
                def __init__(
                    self,
                    code: str | None = ...,
                    source_id: str | None = ...,
                    source_type: _object_type_pb2.ObjectType | str | None = ...,
                    source_name: str | None = ...,
                    source_room: str | None = ...,
                    source_room_id: str | None = ...,
                    text: str | None = ...,
                    hub_name: str | None = ...,
                ) -> None: ...

            ARM_PREVENT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
            arm_prevent_objects: _containers.RepeatedCompositeFieldContainer[
                HubCommand.Result.ArmingErrorDetails.ArmPreventObject
            ]
            def __init__(
                self,
                arm_prevent_objects: _Iterable[
                    HubCommand.Result.ArmingErrorDetails.ArmPreventObject | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class MigrationErrorDetails(_message.Message):
            __slots__ = ("errors",)
            class MigrationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN_ERROR: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                NO_RIGHTS_ON_TARGET: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                NO_RIGHTS_ON_DONOR: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                TARGET_ARMED: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                TARGET_OFFLINE: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                DONOR_ONLINE: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                TARGET_FW_LOWER_MINIMAL: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                DONOR_FW_LOWER_MINIMAL: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                TARGET_FW_LOWER_DONOR: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                TARGET_STATE_FETCH_FAILED: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                DONOR_STATE_FETCH_FAILED: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                DONOR_TARGET_INCOMPATIBLE_TYPES: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                TARGET_IS_ALREADY_IN_MIGRATION: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]
                DONOR_IS_ALREADY_IN_MIGRATION: _ClassVar[
                    HubCommand.Result.MigrationErrorDetails.MigrationError
                ]

            UNKNOWN_ERROR: HubCommand.Result.MigrationErrorDetails.MigrationError
            NO_RIGHTS_ON_TARGET: HubCommand.Result.MigrationErrorDetails.MigrationError
            NO_RIGHTS_ON_DONOR: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_ARMED: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_OFFLINE: HubCommand.Result.MigrationErrorDetails.MigrationError
            DONOR_ONLINE: HubCommand.Result.MigrationErrorDetails.MigrationError
            TARGET_FW_LOWER_MINIMAL: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            DONOR_FW_LOWER_MINIMAL: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            TARGET_FW_LOWER_DONOR: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            TARGET_STATE_FETCH_FAILED: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            DONOR_STATE_FETCH_FAILED: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            DONOR_TARGET_INCOMPATIBLE_TYPES: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            TARGET_IS_ALREADY_IN_MIGRATION: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            DONOR_IS_ALREADY_IN_MIGRATION: (
                HubCommand.Result.MigrationErrorDetails.MigrationError
            )
            ERRORS_FIELD_NUMBER: _ClassVar[int]
            errors: _containers.RepeatedScalarFieldContainer[
                HubCommand.Result.MigrationErrorDetails.MigrationError
            ]
            def __init__(
                self,
                errors: _Iterable[
                    HubCommand.Result.MigrationErrorDetails.MigrationError | str
                ]
                | None = ...,
            ) -> None: ...

        class InviteUsersResponseDetails(_message.Message):
            __slots__ = ("invite_statuses",)
            class InviteStatus(_message.Message):
                __slots__ = ("email", "status")
                class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    NO_INVITE_STATUS_INFO: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]
                    USER_BOUND: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]
                    USER_INVITED: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]
                    INVALID_OR_NON_EXISTING_USER_EMAIL: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]
                    OBJECTS_LIMIT_EXCEEDED: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]
                    INVALID_OR_NON_EXISTING_PRO_EMAIL: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]
                    ALREADY_BOUND: _ClassVar[
                        HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    ]

                NO_INVITE_STATUS_INFO: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                USER_BOUND: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                USER_INVITED: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                INVALID_OR_NON_EXISTING_USER_EMAIL: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                OBJECTS_LIMIT_EXCEEDED: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                INVALID_OR_NON_EXISTING_PRO_EMAIL: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                ALREADY_BOUND: (
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                )
                EMAIL_FIELD_NUMBER: _ClassVar[int]
                STATUS_FIELD_NUMBER: _ClassVar[int]
                email: str
                status: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                def __init__(
                    self,
                    email: str | None = ...,
                    status: HubCommand.Result.InviteUsersResponseDetails.InviteStatus.Status
                    | str
                    | None = ...,
                ) -> None: ...

            INVITE_STATUSES_FIELD_NUMBER: _ClassVar[int]
            invite_statuses: _containers.RepeatedCompositeFieldContainer[
                HubCommand.Result.InviteUsersResponseDetails.InviteStatus
            ]
            def __init__(
                self,
                invite_statuses: _Iterable[
                    HubCommand.Result.InviteUsersResponseDetails.InviteStatus | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class LinkDeviceResponseDetails(_message.Message):
            __slots__ = ("fail_device_type", "fail_reason", "status")
            class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_STATUS_INFO: _ClassVar[
                    HubCommand.Result.LinkDeviceResponseDetails.Status
                ]
                SUCCESS: _ClassVar[HubCommand.Result.LinkDeviceResponseDetails.Status]
                SEARCH_TIMEOUT: _ClassVar[
                    HubCommand.Result.LinkDeviceResponseDetails.Status
                ]
                REGISTRATION_FAILED: _ClassVar[
                    HubCommand.Result.LinkDeviceResponseDetails.Status
                ]
                REGISTRATION_STEP: _ClassVar[
                    HubCommand.Result.LinkDeviceResponseDetails.Status
                ]

            NO_STATUS_INFO: HubCommand.Result.LinkDeviceResponseDetails.Status
            SUCCESS: HubCommand.Result.LinkDeviceResponseDetails.Status
            SEARCH_TIMEOUT: HubCommand.Result.LinkDeviceResponseDetails.Status
            REGISTRATION_FAILED: HubCommand.Result.LinkDeviceResponseDetails.Status
            REGISTRATION_STEP: HubCommand.Result.LinkDeviceResponseDetails.Status
            STATUS_FIELD_NUMBER: _ClassVar[int]
            FAIL_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
            FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
            status: HubCommand.Result.LinkDeviceResponseDetails.Status
            fail_device_type: str
            fail_reason: int
            def __init__(
                self,
                status: HubCommand.Result.LinkDeviceResponseDetails.Status
                | str
                | None = ...,
                fail_device_type: str | None = ...,
                fail_reason: int | None = ...,
            ) -> None: ...

        class GsmSimCardBalanceResponseDetails(_message.Message):
            __slots__ = ("balance",)
            BALANCE_FIELD_NUMBER: _ClassVar[int]
            balance: str
            def __init__(self, balance: str | None = ...) -> None: ...

        class ScanWifiNetworksResponseDetails(_message.Message):
            __slots__ = ("available_networks",)
            class WifiNetwork(_message.Message):
                __slots__ = ("security_protocol", "signal_level", "ssid")
                SSID_FIELD_NUMBER: _ClassVar[int]
                SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
                SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
                ssid: str
                security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
                signal_level: _hub_device_pb2.HubDevice.Wifi.SignalLevel
                def __init__(
                    self,
                    ssid: str | None = ...,
                    security_protocol: _hub_device_pb2.HubDevice.Wifi.SecurityProtocol
                    | str
                    | None = ...,
                    signal_level: _hub_device_pb2.HubDevice.Wifi.SignalLevel
                    | str
                    | None = ...,
                ) -> None: ...

            AVAILABLE_NETWORKS_FIELD_NUMBER: _ClassVar[int]
            available_networks: _containers.RepeatedCompositeFieldContainer[
                HubCommand.Result.ScanWifiNetworksResponseDetails.WifiNetwork
            ]
            def __init__(
                self,
                available_networks: _Iterable[
                    HubCommand.Result.ScanWifiNetworksResponseDetails.WifiNetwork
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class CreateUnitResponseDetails(_message.Message):
            __slots__ = ("group_id", "room_id")
            ROOM_ID_FIELD_NUMBER: _ClassVar[int]
            GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            room_id: str
            group_id: str
            def __init__(
                self, room_id: str | None = ..., group_id: str | None = ...
            ) -> None: ...

        class RegisterAccessKeyErrorDetails(_message.Message):
            __slots__ = ("fail_reason",)
            class FailReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_FAIL_REASON_INFO: _ClassVar[
                    HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
                ]
                KEY_ALREADY_IN_USE: _ClassVar[
                    HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
                ]
                NO_AVAILABLE_READERS: _ClassVar[
                    HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
                ]
                USER_NOT_FOUND: _ClassVar[
                    HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
                ]

            NO_FAIL_REASON_INFO: (
                HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            )
            KEY_ALREADY_IN_USE: (
                HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            )
            NO_AVAILABLE_READERS: (
                HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            )
            USER_NOT_FOUND: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
            fail_reason: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
            def __init__(
                self,
                fail_reason: HubCommand.Result.RegisterAccessKeyErrorDetails.FailReason
                | str
                | None = ...,
            ) -> None: ...

        class EngineerAttendanceRequiredErrorDetails(_message.Message):
            __slots__ = ("fail_reason",)
            class FailReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_FAIL_REASON_INFO: _ClassVar[
                    HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
                ]
                WRONG_OR_INACTIVE_REQUEST_ID: _ClassVar[
                    HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
                ]

            NO_FAIL_REASON_INFO: (
                HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
            )
            WRONG_OR_INACTIVE_REQUEST_ID: (
                HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
            )
            FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
            fail_reason: (
                HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
            )
            def __init__(
                self,
                fail_reason: HubCommand.Result.EngineerAttendanceRequiredErrorDetails.FailReason
                | str
                | None = ...,
            ) -> None: ...

        class ScannedFibraDevicesDetails(_message.Message):
            __slots__ = ("devices",)
            DEVICES_FIELD_NUMBER: _ClassVar[int]
            devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]
            def __init__(
                self, devices: _Iterable[_device_pb2.Device | _Mapping] | None = ...
            ) -> None: ...

        ANSWER_FIELD_NUMBER: _ClassVar[int]
        NETWORK_SETTINGS_STATUS_FIELD_NUMBER: _ClassVar[int]
        WIFI_NETWORK_JOIN_STATUS_FIELD_NUMBER: _ClassVar[int]
        ARMING_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        INVITE_USERS_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        LINK_DEVICE_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        GSM_SIM_CARD_BALANCE_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        SCAN_WIFI_NETWORKS_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        CREATE_UNIT_RESPONSE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        REGISTER_ACCESS_KEY_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        ENGINEER_ATTENDANCE_REQUIRED_ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
        SCANNED_FIBRA_DEVICES_DETAILS_FIELD_NUMBER: _ClassVar[int]
        answer: HubCommand.Answer
        network_settings_status: HubCommand.NetworkSettingsStatus
        wifi_network_join_status: HubCommand.WifiNetworkJoinStatus
        arming_error_details: HubCommand.Result.ArmingErrorDetails
        invite_users_response_details: HubCommand.Result.InviteUsersResponseDetails
        link_device_response_details: HubCommand.Result.LinkDeviceResponseDetails
        gsm_sim_card_balance_response_details: (
            HubCommand.Result.GsmSimCardBalanceResponseDetails
        )
        scan_wifi_networks_response_details: (
            HubCommand.Result.ScanWifiNetworksResponseDetails
        )
        migration_error_details: HubCommand.Result.MigrationErrorDetails
        create_unit_response_details: HubCommand.Result.CreateUnitResponseDetails
        register_access_key_error_details: (
            HubCommand.Result.RegisterAccessKeyErrorDetails
        )
        engineer_attendance_required_error_details: (
            HubCommand.Result.EngineerAttendanceRequiredErrorDetails
        )
        scanned_fibra_devices_details: HubCommand.Result.ScannedFibraDevicesDetails
        def __init__(
            self,
            answer: HubCommand.Answer | str | None = ...,
            network_settings_status: HubCommand.NetworkSettingsStatus
            | str
            | None = ...,
            wifi_network_join_status: HubCommand.WifiNetworkJoinStatus
            | str
            | None = ...,
            arming_error_details: HubCommand.Result.ArmingErrorDetails
            | _Mapping
            | None = ...,
            invite_users_response_details: HubCommand.Result.InviteUsersResponseDetails
            | _Mapping
            | None = ...,
            link_device_response_details: HubCommand.Result.LinkDeviceResponseDetails
            | _Mapping
            | None = ...,
            gsm_sim_card_balance_response_details: HubCommand.Result.GsmSimCardBalanceResponseDetails
            | _Mapping
            | None = ...,
            scan_wifi_networks_response_details: HubCommand.Result.ScanWifiNetworksResponseDetails
            | _Mapping
            | None = ...,
            migration_error_details: HubCommand.Result.MigrationErrorDetails
            | _Mapping
            | None = ...,
            create_unit_response_details: HubCommand.Result.CreateUnitResponseDetails
            | _Mapping
            | None = ...,
            register_access_key_error_details: HubCommand.Result.RegisterAccessKeyErrorDetails
            | _Mapping
            | None = ...,
            engineer_attendance_required_error_details: HubCommand.Result.EngineerAttendanceRequiredErrorDetails
            | _Mapping
            | None = ...,
            scanned_fibra_devices_details: HubCommand.Result.ScannedFibraDevicesDetails
            | _Mapping
            | None = ...,
        ) -> None: ...

    class CreateScenario(_message.Message):
        __slots__ = ("field_mask", "scenario")
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        scenario: _scenario_pb2.Scenario
        field_mask: _field_mask_pb2.FieldMask
        def __init__(
            self,
            scenario: _scenario_pb2.Scenario | _Mapping | None = ...,
            field_mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        ) -> None: ...

    class UpdateScenario(_message.Message):
        __slots__ = ("field_mask", "scenario")
        SCENARIO_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        scenario: _scenario_pb2.Scenario
        field_mask: _field_mask_pb2.FieldMask
        def __init__(
            self,
            scenario: _scenario_pb2.Scenario | _Mapping | None = ...,
            field_mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        ) -> None: ...

    class DeleteScenario(_message.Message):
        __slots__ = ("field_mask", "id")
        ID_FIELD_NUMBER: _ClassVar[int]
        FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
        id: str
        field_mask: _field_mask_pb2.FieldMask
        def __init__(
            self,
            id: str | None = ...,
            field_mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        ) -> None: ...

    class StartMigration(_message.Message):
        __slots__ = ("donor_id",)
        DONOR_ID_FIELD_NUMBER: _ClassVar[int]
        donor_id: str
        def __init__(self, donor_id: str | None = ...) -> None: ...

    class StopMigration(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class RequestArmingReset(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class EngineerAttendanceRequired(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class AddAccessCard(_message.Message):
        __slots__ = ("color", "name", "type", "user_id")
        class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WHITE: _ClassVar[HubCommand.AddAccessCard.Color]
            BLACK: _ClassVar[HubCommand.AddAccessCard.Color]

        WHITE: HubCommand.AddAccessCard.Color
        BLACK: HubCommand.AddAccessCard.Color
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CARD: _ClassVar[HubCommand.AddAccessCard.Type]
            TAG: _ClassVar[HubCommand.AddAccessCard.Type]

        CARD: HubCommand.AddAccessCard.Type
        TAG: HubCommand.AddAccessCard.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        color: HubCommand.AddAccessCard.Color
        type: HubCommand.AddAccessCard.Type
        user_id: str
        def __init__(
            self,
            name: str | None = ...,
            color: HubCommand.AddAccessCard.Color | str | None = ...,
            type: HubCommand.AddAccessCard.Type | str | None = ...,
            user_id: str | None = ...,
        ) -> None: ...

    class DeleteAccessCard(_message.Message):
        __slots__ = ("delete_mode", "id")
        class DeleteMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WITHOUT_CARD: _ClassVar[HubCommand.DeleteAccessCard.DeleteMode]
            WITH_CARD: _ClassVar[HubCommand.DeleteAccessCard.DeleteMode]

        WITHOUT_CARD: HubCommand.DeleteAccessCard.DeleteMode
        WITH_CARD: HubCommand.DeleteAccessCard.DeleteMode
        ID_FIELD_NUMBER: _ClassVar[int]
        DELETE_MODE_FIELD_NUMBER: _ClassVar[int]
        id: str
        delete_mode: HubCommand.DeleteAccessCard.DeleteMode
        def __init__(
            self,
            id: str | None = ...,
            delete_mode: HubCommand.DeleteAccessCard.DeleteMode | str | None = ...,
        ) -> None: ...

    class EraseAccessCard(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ExitCardMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class CancelAccessKeySearch(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class RegisterAccessKey(_message.Message):
        __slots__ = ("key_name",)
        KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        key_name: str
        def __init__(self, key_name: str | None = ...) -> None: ...

    class DeleteAccessKey(_message.Message):
        __slots__ = ("key_id",)
        KEY_ID_FIELD_NUMBER: _ClassVar[int]
        key_id: str
        def __init__(self, key_id: str | None = ...) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    ARMING_FIELD_NUMBER: _ClassVar[int]
    PANIC_FIELD_NUMBER: _ClassVar[int]
    DROP_CACHE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_SEARCH_FIELD_NUMBER: _ClassVar[int]
    START_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GROUPS_MODE_FIELD_NUMBER: _ClassVar[int]
    RESET_SIM_TRAFFIC_COUNTER_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIRE_DETECTORS_FIELD_NUMBER: _ClassVar[int]
    RESET_ALARM_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DELAY_INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CARD_STATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARMING_FIELD_NUMBER: _ClassVar[int]
    DROP_LOGS_FIELD_NUMBER: _ClassVar[int]
    INVITE_USERS_FIELD_NUMBER: _ClassVar[int]
    REVOKE_USER_INVITE_FIELD_NUMBER: _ClassVar[int]
    PROFI_HUB_ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DETACH_USER_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ARMING_RESET_FIELD_NUMBER: _ClassVar[int]
    ENGINEER_ATTENDANCE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_ROOM_FIELD_NUMBER: _ClassVar[int]
    DELETE_ROOM_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_GROUP_FIELD_NUMBER: _ClassVar[int]
    DELETE_GROUP_FIELD_NUMBER: _ClassVar[int]
    LINK_CAMERA_FIELD_NUMBER: _ClassVar[int]
    UNLINK_CAMERA_FIELD_NUMBER: _ClassVar[int]
    EDIT_STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    LINK_DEVICE_FIELD_NUMBER: _ClassVar[int]
    UNLINK_DEVICE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMAND_FIELD_NUMBER: _ClassVar[int]
    SCAN_FIBRA_DEVICES_FIELD_NUMBER: _ClassVar[int]
    GET_SCANNED_FIBRA_DEVICES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SECURITY_COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    DELETE_SECURITY_COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    CANCEL_DELETE_SECURITY_COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_NETWORK_CHANNEL_STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ETHERNET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_WIFI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GSM_SIM_CARD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GSM_SIM_CARD_BALANCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    GET_GSM_SIM_CARD_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SCAN_WIFI_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    JOIN_WIFI_NETWORK_FIELD_NUMBER: _ClassVar[int]
    JOIN_WIFI_NETWORK_ADVANCED_FIELD_NUMBER: _ClassVar[int]
    FORGET_WIFI_NETWORK_FIELD_NUMBER: _ClassVar[int]
    APPLY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    DELETE_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    APPLY_UPDATES_FIELD_NUMBER: _ClassVar[int]
    START_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    STOP_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    ADD_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    DELETE_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    ERASE_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    EXIT_CARD_MODE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_ACCESS_KEY_SEARCH_FIELD_NUMBER: _ClassVar[int]
    REGISTER_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    DELETE_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    arming: HubCommand.Arming
    panic: HubCommand.Panic
    drop_cache: HubCommand.DropCache
    cancel_search: HubCommand.CancelSearch
    start_firmware_update: HubCommand.StartFirmwareUpdate
    update_groups_mode: HubCommand.UpdateGroupsMode
    reset_sim_traffic_counter: HubCommand.ResetSimTrafficCounter
    mute_fire_detectors: HubCommand.MuteFireDetectors
    reset_alarm_condition: HubCommand.ResetAlarmCondition
    delay_interconnect: HubCommand.DelayInterconnect
    update_card_state: HubCommand.UpdateCardState
    group_arming: HubCommand.GroupArming
    drop_logs: HubCommand.DropLogs
    invite_users: HubCommand.InviteUsers
    revoke_user_invite: HubCommand.RevokeUserInvite
    profi_hub_access_request: HubCommand.ProfiHubAccessRequest
    detach_user: HubCommand.DetachUser
    change_user_role: ChangeUserRole
    change_user_permissions: ChangeUserPermissions
    request_arming_reset: HubCommand.RequestArmingReset
    engineer_attendance_required: HubCommand.EngineerAttendanceRequired
    create_new_room: HubCommand.CreateNewRoom
    delete_room: HubCommand.DeleteRoom
    create_new_group: HubCommand.CreateNewGroup
    delete_group: HubCommand.DeleteGroup
    link_camera: HubCommand.LinkCamera
    unlink_camera: HubCommand.UnlinkCamera
    edit_stream_data: HubCommand.EditStreamData
    link_device: HubCommand.LinkDevice
    unlink_device: HubCommand.UnlinkDevice
    device_command: DeviceCommand
    scan_fibra_devices: HubCommand.ScanFibraDevices
    get_scanned_fibra_devices: HubCommand.GetScannedFibraDevices
    create_security_company_binding: HubCommand.CreateSecurityCompanyBinding
    delete_security_company_binding: HubCommand.DeleteSecurityCompanyBinding
    cancel_delete_security_company_binding: (
        HubCommand.CancelDeleteSecurityCompanyBinding
    )
    update_network_channel_state: HubCommand.UpdateNetworkChannelState
    update_ethernet_settings: HubCommand.UpdateEthernetSettings
    update_wifi_settings: HubCommand.UpdateWifiSettings
    update_gsm_sim_card_settings: HubCommand.UpdateGsmSimCardSettings
    update_gsm_sim_card_balance_number: HubCommand.UpdateGsmSimCardBalanceNumber
    get_gsm_sim_card_balance: HubCommand.GetGsmSimCardBalance
    scan_wifi_networks: HubCommand.ScanWifiNetworks
    join_wifi_network: HubCommand.JoinWifiNetwork
    join_wifi_network_advanced: HubCommand.JoinWifiNetworkAdvanced
    forget_wifi_network: HubCommand.ForgetWifiNetwork
    apply_update: HubCommand.ApplyUpdate
    create_scenario: HubCommand.CreateScenario
    update_scenario: HubCommand.UpdateScenario
    delete_scenario: HubCommand.DeleteScenario
    apply_updates: HubCommand.ApplyUpdates
    start_migration: HubCommand.StartMigration
    stop_migration: HubCommand.StopMigration
    add_access_card: HubCommand.AddAccessCard
    delete_access_card: HubCommand.DeleteAccessCard
    erase_access_card: HubCommand.EraseAccessCard
    exit_card_mode: HubCommand.ExitCardMode
    cancel_access_key_search: HubCommand.CancelAccessKeySearch
    register_access_key: HubCommand.RegisterAccessKey
    delete_access_key: HubCommand.DeleteAccessKey
    def __init__(
        self,
        hub_id: str | None = ...,
        arming: HubCommand.Arming | _Mapping | None = ...,
        panic: HubCommand.Panic | _Mapping | None = ...,
        drop_cache: HubCommand.DropCache | _Mapping | None = ...,
        cancel_search: HubCommand.CancelSearch | _Mapping | None = ...,
        start_firmware_update: HubCommand.StartFirmwareUpdate | _Mapping | None = ...,
        update_groups_mode: HubCommand.UpdateGroupsMode | _Mapping | None = ...,
        reset_sim_traffic_counter: HubCommand.ResetSimTrafficCounter
        | _Mapping
        | None = ...,
        mute_fire_detectors: HubCommand.MuteFireDetectors | _Mapping | None = ...,
        reset_alarm_condition: HubCommand.ResetAlarmCondition | _Mapping | None = ...,
        delay_interconnect: HubCommand.DelayInterconnect | _Mapping | None = ...,
        update_card_state: HubCommand.UpdateCardState | _Mapping | None = ...,
        group_arming: HubCommand.GroupArming | _Mapping | None = ...,
        drop_logs: HubCommand.DropLogs | _Mapping | None = ...,
        invite_users: HubCommand.InviteUsers | _Mapping | None = ...,
        revoke_user_invite: HubCommand.RevokeUserInvite | _Mapping | None = ...,
        profi_hub_access_request: HubCommand.ProfiHubAccessRequest
        | _Mapping
        | None = ...,
        detach_user: HubCommand.DetachUser | _Mapping | None = ...,
        change_user_role: ChangeUserRole | _Mapping | None = ...,
        change_user_permissions: ChangeUserPermissions | _Mapping | None = ...,
        request_arming_reset: HubCommand.RequestArmingReset | _Mapping | None = ...,
        engineer_attendance_required: HubCommand.EngineerAttendanceRequired
        | _Mapping
        | None = ...,
        create_new_room: HubCommand.CreateNewRoom | _Mapping | None = ...,
        delete_room: HubCommand.DeleteRoom | _Mapping | None = ...,
        create_new_group: HubCommand.CreateNewGroup | _Mapping | None = ...,
        delete_group: HubCommand.DeleteGroup | _Mapping | None = ...,
        link_camera: HubCommand.LinkCamera | _Mapping | None = ...,
        unlink_camera: HubCommand.UnlinkCamera | _Mapping | None = ...,
        edit_stream_data: HubCommand.EditStreamData | _Mapping | None = ...,
        link_device: HubCommand.LinkDevice | _Mapping | None = ...,
        unlink_device: HubCommand.UnlinkDevice | _Mapping | None = ...,
        device_command: DeviceCommand | _Mapping | None = ...,
        scan_fibra_devices: HubCommand.ScanFibraDevices | _Mapping | None = ...,
        get_scanned_fibra_devices: HubCommand.GetScannedFibraDevices
        | _Mapping
        | None = ...,
        create_security_company_binding: HubCommand.CreateSecurityCompanyBinding
        | _Mapping
        | None = ...,
        delete_security_company_binding: HubCommand.DeleteSecurityCompanyBinding
        | _Mapping
        | None = ...,
        cancel_delete_security_company_binding: HubCommand.CancelDeleteSecurityCompanyBinding
        | _Mapping
        | None = ...,
        update_network_channel_state: HubCommand.UpdateNetworkChannelState
        | _Mapping
        | None = ...,
        update_ethernet_settings: HubCommand.UpdateEthernetSettings
        | _Mapping
        | None = ...,
        update_wifi_settings: HubCommand.UpdateWifiSettings | _Mapping | None = ...,
        update_gsm_sim_card_settings: HubCommand.UpdateGsmSimCardSettings
        | _Mapping
        | None = ...,
        update_gsm_sim_card_balance_number: HubCommand.UpdateGsmSimCardBalanceNumber
        | _Mapping
        | None = ...,
        get_gsm_sim_card_balance: HubCommand.GetGsmSimCardBalance
        | _Mapping
        | None = ...,
        scan_wifi_networks: HubCommand.ScanWifiNetworks | _Mapping | None = ...,
        join_wifi_network: HubCommand.JoinWifiNetwork | _Mapping | None = ...,
        join_wifi_network_advanced: HubCommand.JoinWifiNetworkAdvanced
        | _Mapping
        | None = ...,
        forget_wifi_network: HubCommand.ForgetWifiNetwork | _Mapping | None = ...,
        apply_update: HubCommand.ApplyUpdate | _Mapping | None = ...,
        create_scenario: HubCommand.CreateScenario | _Mapping | None = ...,
        update_scenario: HubCommand.UpdateScenario | _Mapping | None = ...,
        delete_scenario: HubCommand.DeleteScenario | _Mapping | None = ...,
        apply_updates: HubCommand.ApplyUpdates | _Mapping | None = ...,
        start_migration: HubCommand.StartMigration | _Mapping | None = ...,
        stop_migration: HubCommand.StopMigration | _Mapping | None = ...,
        add_access_card: HubCommand.AddAccessCard | _Mapping | None = ...,
        delete_access_card: HubCommand.DeleteAccessCard | _Mapping | None = ...,
        erase_access_card: HubCommand.EraseAccessCard | _Mapping | None = ...,
        exit_card_mode: HubCommand.ExitCardMode | _Mapping | None = ...,
        cancel_access_key_search: HubCommand.CancelAccessKeySearch
        | _Mapping
        | None = ...,
        register_access_key: HubCommand.RegisterAccessKey | _Mapping | None = ...,
        delete_access_key: HubCommand.DeleteAccessKey | _Mapping | None = ...,
    ) -> None: ...

class DeviceCommand(_message.Message):
    __slots__ = (
        "chimes_group_status",
        "chimes_status",
        "device_id",
        "device_type",
        "type",
    )
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_DEVICE_COMMAND_TYPE_INFO: _ClassVar[DeviceCommand.Type]
        CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        CONNECTION_TEST_STOP: _ClassVar[DeviceCommand.Type]
        DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        DETECTION_TEST_STOP: _ClassVar[DeviceCommand.Type]
        MUTE: _ClassVar[DeviceCommand.Type]
        SWITCH_ON: _ClassVar[DeviceCommand.Type]
        SWITCH_OFF: _ClassVar[DeviceCommand.Type]
        SOUND_TEST_START: _ClassVar[DeviceCommand.Type]
        UNLOCK_DEVICE: _ClassVar[DeviceCommand.Type]
        FIRE_SENSOR_TEST: _ClassVar[DeviceCommand.Type]
        MOTION_OUTDOOR_DETECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_OUTDOOR_UPPER_MOTION_SENSOR_DETECTION_TEST_START: _ClassVar[
            DeviceCommand.Type
        ]
        MOTION_OUTDOOR_LOWER_MOTION_SENSOR_DETECTION_TEST_START: _ClassVar[
            DeviceCommand.Type
        ]
        MOTION_OUTDOOR_ANTIMASKING_MOTION_SENSOR_DETECTION_TEST_START: _ClassVar[
            DeviceCommand.Type
        ]
        GROUP_MODE_OFF: _ClassVar[DeviceCommand.Type]
        GROUP_MODE_ON: _ClassVar[DeviceCommand.Type]
        GSM_TRAFFIC_RESET_SIM1: _ClassVar[DeviceCommand.Type]
        GSM_TRAFFIC_RESET_SIM2: _ClassVar[DeviceCommand.Type]
        DEVICE_BYPASS_OFF: _ClassVar[DeviceCommand.Type]
        DEVICE_BYPASS_WHOLE: _ClassVar[DeviceCommand.Type]
        DEVICE_BYPASS_TAMPER: _ClassVar[DeviceCommand.Type]
        MULTI_TRANSMITTER_POWER_RESET: _ClassVar[DeviceCommand.Type]
        MOTION_CAM_FIFTH_FREQUENCY_CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        MOTION_CAM_ZERO_OR_FIRST_FREQUENCY_CONNECTION_TEST_START: _ClassVar[
            DeviceCommand.Type
        ]
        MOTION_CAM_DATA_CHANNEL_CONNECTION_TEST_START: _ClassVar[DeviceCommand.Type]
        CHIMES_MODE: _ClassVar[DeviceCommand.Type]
        MAKE_PHOTO: _ClassVar[DeviceCommand.Type]
        INDICATION_OFF: _ClassVar[DeviceCommand.Type]
        INDICATION_ON: _ClassVar[DeviceCommand.Type]
        BUS_POWER_OFF: _ClassVar[DeviceCommand.Type]
        BUS_POWER_ON: _ClassVar[DeviceCommand.Type]
        MAX_POWER_TEST_OFF: _ClassVar[DeviceCommand.Type]
        MAX_POWER_TEST_ON: _ClassVar[DeviceCommand.Type]

    NO_DEVICE_COMMAND_TYPE_INFO: DeviceCommand.Type
    CONNECTION_TEST_START: DeviceCommand.Type
    CONNECTION_TEST_STOP: DeviceCommand.Type
    DETECTION_TEST_START: DeviceCommand.Type
    DETECTION_TEST_STOP: DeviceCommand.Type
    MUTE: DeviceCommand.Type
    SWITCH_ON: DeviceCommand.Type
    SWITCH_OFF: DeviceCommand.Type
    SOUND_TEST_START: DeviceCommand.Type
    UNLOCK_DEVICE: DeviceCommand.Type
    FIRE_SENSOR_TEST: DeviceCommand.Type
    MOTION_OUTDOOR_DETECTION_TEST_START: DeviceCommand.Type
    MOTION_OUTDOOR_UPPER_MOTION_SENSOR_DETECTION_TEST_START: DeviceCommand.Type
    MOTION_OUTDOOR_LOWER_MOTION_SENSOR_DETECTION_TEST_START: DeviceCommand.Type
    MOTION_OUTDOOR_ANTIMASKING_MOTION_SENSOR_DETECTION_TEST_START: DeviceCommand.Type
    GROUP_MODE_OFF: DeviceCommand.Type
    GROUP_MODE_ON: DeviceCommand.Type
    GSM_TRAFFIC_RESET_SIM1: DeviceCommand.Type
    GSM_TRAFFIC_RESET_SIM2: DeviceCommand.Type
    DEVICE_BYPASS_OFF: DeviceCommand.Type
    DEVICE_BYPASS_WHOLE: DeviceCommand.Type
    DEVICE_BYPASS_TAMPER: DeviceCommand.Type
    MULTI_TRANSMITTER_POWER_RESET: DeviceCommand.Type
    MOTION_CAM_FIFTH_FREQUENCY_CONNECTION_TEST_START: DeviceCommand.Type
    MOTION_CAM_ZERO_OR_FIRST_FREQUENCY_CONNECTION_TEST_START: DeviceCommand.Type
    MOTION_CAM_DATA_CHANNEL_CONNECTION_TEST_START: DeviceCommand.Type
    CHIMES_MODE: DeviceCommand.Type
    MAKE_PHOTO: DeviceCommand.Type
    INDICATION_OFF: DeviceCommand.Type
    INDICATION_ON: DeviceCommand.Type
    BUS_POWER_OFF: DeviceCommand.Type
    BUS_POWER_ON: DeviceCommand.Type
    MAX_POWER_TEST_OFF: DeviceCommand.Type
    MAX_POWER_TEST_ON: DeviceCommand.Type
    class ChimesGroupStatus(_message.Message):
        __slots__ = ("group_ids",)
        class GroupIdsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: bool
            def __init__(self, key: str | None = ..., value: bool = ...) -> None: ...

        GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
        group_ids: _containers.ScalarMap[str, bool]
        def __init__(self, group_ids: _Mapping[str, bool] | None = ...) -> None: ...

    class ChimesStatus(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHIMES_GROUP_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHIMES_STATUS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    type: DeviceCommand.Type
    device_type: _object_type_pb2.ObjectType
    chimes_group_status: DeviceCommand.ChimesGroupStatus
    chimes_status: DeviceCommand.ChimesStatus
    def __init__(
        self,
        device_id: str | None = ...,
        type: DeviceCommand.Type | str | None = ...,
        device_type: _object_type_pb2.ObjectType | str | None = ...,
        chimes_group_status: DeviceCommand.ChimesGroupStatus | _Mapping | None = ...,
        chimes_status: DeviceCommand.ChimesStatus | _Mapping | None = ...,
    ) -> None: ...

class ChangeUserRole(_message.Message):
    __slots__ = ("user_id", "user_role")
    class UserRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER: _ClassVar[ChangeUserRole.UserRole]
        MASTER: _ClassVar[ChangeUserRole.UserRole]

    USER: ChangeUserRole.UserRole
    MASTER: ChangeUserRole.UserRole
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_role: ChangeUserRole.UserRole
    def __init__(
        self,
        user_id: str | None = ...,
        user_role: ChangeUserRole.UserRole | str | None = ...,
    ) -> None: ...

class ChangeUserPermissions(_message.Message):
    __slots__ = ("user_id", "user_permission")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_permission: _containers.RepeatedScalarFieldContainer[_user_pb2.User.Permission]
    def __init__(
        self,
        user_id: str | None = ...,
        user_permission: _Iterable[_user_pb2.User.Permission | str] | None = ...,
    ) -> None: ...
