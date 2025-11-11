from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    assigned_target_infos_pb2 as _assigned_target_infos_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    deactivated_target_infos_pb2 as _deactivated_target_infos_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    deactivation_date_pb2 as _deactivation_date_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    dealer_info_pb2 as _dealer_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    paid_service_pb2 as _paid_service_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    space_member_info_pb2 as _space_member_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company.additional.data import (
    company_permissions_claim_request_pb2 as _company_permissions_claim_request_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company.additional.data import (
    company_permissions_claim_response_pb2 as _company_permissions_claim_response_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company.additional.data import (
    initiator_info_pb2 as _initiator_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    action_source_object_pb2 as _action_source_object_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    alarm_suppress_info_pb2 as _alarm_suppress_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    company_permissions_claim_pb2 as _company_permissions_claim_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    company_permissions_claim_response_pb2 as _company_permissions_claim_response_pb2_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    confirmed_alarm_info_pb2 as _confirmed_alarm_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    custom_alarm_type_pb2 as _custom_alarm_type_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    day_alarm_zone_info_pb2 as _day_alarm_zone_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    device_location_info_pb2 as _device_location_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    display_groups_pb2 as _display_groups_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    en54_disablement_endpoints_pb2 as _en54_disablement_endpoints_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    endpoint_info_pb2 as _endpoint_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    error_code_info_pb2 as _error_code_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    fire_zone_info_pb2 as _fire_zone_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    firmware_id_pb2 as _firmware_id_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    firmware_version_pb2 as _firmware_version_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    hub_alarm_info_pb2 as _hub_alarm_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    hub_audio_resource_pb2 as _hub_audio_resource_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    hub_connection_info_pb2 as _hub_connection_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    image_resource_pb2 as _image_resource_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    initiator_info_pb2 as _initiator_info_pb2_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    initiator_name_pb2 as _initiator_name_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    location_info_pb2 as _location_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    malfunction_info_pb2 as _malfunction_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    offline_notifications_pb2 as _offline_notifications_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    pro_permissions_claim_pb2 as _pro_permissions_claim_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    pro_permissions_claim_response_pb2 as _pro_permissions_claim_response_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    self_test_status_pb2 as _self_test_status_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    slave_bus_id_pb2 as _slave_bus_id_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    timezone_info_pb2 as _timezone_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    troubled_devices_pb2 as _troubled_devices_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    video_archive_export_completed_data_pb2 as _video_archive_export_completed_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    video_edge_channel_media_data_info_pb2 as _video_edge_channel_media_data_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    video_edge_info_pb2 as _video_edge_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.additional.data import (
    video_scenario_resource_pb2 as _video_scenario_resource_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.smartlock.additional.data import (
    initiator_pb2 as _initiator_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    display_groups_pb2 as _display_groups_pb2_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    hub_info_pb2 as _hub_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    hub_troubled_devices_pb2 as _hub_troubled_devices_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    initiator_info_pb2 as _initiator_info_pb2_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    join_space_request_info_pb2 as _join_space_request_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    panic_location_pb2 as _panic_location_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    pro_permissions_claim_request_pb2 as _pro_permissions_claim_request_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    pro_permissions_claim_response_pb2 as _pro_permissions_claim_response_pb2_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    standalone_device_info_pb2 as _standalone_device_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    timezone_info_pb2 as _timezone_info_pb2_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data import (
    backup_connection_context_pb2 as _backup_connection_context_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data import (
    channel_media_data_info_pb2 as _channel_media_data_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data import (
    initiator_info_pb2 as _initiator_info_pb2_1_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data import (
    video_detection_timestamp_info_pb2 as _video_detection_timestamp_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data import (
    video_scenario_data_pb2 as _video_scenario_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.archive import (
    archive_export_completed_data_pb2 as _archive_export_completed_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.archive import (
    direct_export_requested_data_pb2 as _direct_export_requested_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.channel import (
    channel_added_data_pb2 as _channel_added_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.channel import (
    channel_disconnected_data_pb2 as _channel_disconnected_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.channel import (
    line_crossed_data_pb2 as _line_crossed_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.firmware import (
    firmware_update_finished_data_pb2 as _firmware_update_finished_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.firmware import (
    firmware_update_started_data_pb2 as _firmware_update_started_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    temporary_video_access_approved_to_company_data_pb2 as _temporary_video_access_approved_to_company_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    temporary_video_access_approved_to_pro_data_pb2 as _temporary_video_access_approved_to_pro_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    temporary_video_access_denied_for_company_data_pb2 as _temporary_video_access_denied_for_company_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    temporary_video_access_denied_for_pro_data_pb2 as _temporary_video_access_denied_for_pro_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    temporary_video_access_request_from_company_data_pb2 as _temporary_video_access_request_from_company_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    temporary_video_access_request_from_pro_data_pb2 as _temporary_video_access_request_from_pro_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.storage import (
    storage_device_info_pb2 as _storage_device_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.storage import (
    storage_error_detected_data_pb2 as _storage_error_detected_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.storage import (
    storage_powered_off_overheated_data_pb2 as _storage_powered_off_overheated_data_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.storage import (
    storage_write_error_detected_data_pb2 as _storage_write_error_detected_data_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationAdditionalData(_message.Message):
    __slots__ = (
        "archive_export_completed_data",
        "assigned_target_infos",
        "backup_connection_context",
        "channel_added_data",
        "channel_disconnected_data",
        "channel_media_data",
        "company_permission_claim_request",
        "company_permission_claim_response",
        "deactivated_target_infos",
        "deactivation_date",
        "dealer_info",
        "detection_timestamp_info",
        "direct_export_requested_data",
        "firmware_update_finished_data",
        "firmware_update_started_data",
        "hub_action_source_object",
        "hub_alarm_info",
        "hub_alarm_suppress_info",
        "hub_audio_resource",
        "hub_company_permission_claim",
        "hub_company_permission_claim_response",
        "hub_confirmed_alarm_info",
        "hub_connection_info",
        "hub_custom_alarm_type_info",
        "hub_day_alarm_zone_info",
        "hub_device_location_info",
        "hub_display_groups",
        "hub_en54_disablement_endpoints_list",
        "hub_endpoint_info",
        "hub_error_code_info",
        "hub_fire_zone_info",
        "hub_firmware_id_info",
        "hub_firmware_version",
        "hub_image_resource",
        "hub_in_space_info",
        "hub_in_space_troubled_devices",
        "hub_initiator_info",
        "hub_initiator_name",
        "hub_location_info",
        "hub_malfunction",
        "hub_pro_permission_claim",
        "hub_pro_permission_claim_response",
        "hub_self_test_status",
        "hub_slave_bus_id",
        "hub_timezone_info",
        "hub_troubled_devices",
        "hub_video_archive_export_completed_data",
        "hub_video_edge_info",
        "hub_video_scenario_resource",
        "initiator",
        "initiator_info",
        "join_space_request_info",
        "line_crossed_data",
        "offline_notifications",
        "paid_service",
        "space_display_groups",
        "space_initiator_info",
        "space_location_info",
        "space_member_info",
        "space_pro_permissions_claim_request",
        "space_pro_permissions_claim_response",
        "standalone_device_info",
        "storage_device_info",
        "storage_error_detected_data",
        "storage_powered_off_overheated_data",
        "storage_write_error_detected_data",
        "temporary_video_access_approved_to_company_data",
        "temporary_video_access_approved_to_pro_data",
        "temporary_video_access_denied_for_company_data",
        "temporary_video_access_denied_for_pro_data",
        "temporary_video_access_request_from_company_data",
        "temporary_video_access_request_from_pro_data",
        "timezone_info",
        "video_edge_channel_media_data",
        "video_initiator_info",
        "video_scenario_data",
    )
    HUB_DISPLAY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    HUB_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_TROUBLED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    HUB_INITIATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HUB_IMAGE_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HUB_COMPANY_PERMISSION_CLAIM_FIELD_NUMBER: _ClassVar[int]
    HUB_COMPANY_PERMISSION_CLAIM_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    HUB_INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    HUB_PRO_PERMISSION_CLAIM_FIELD_NUMBER: _ClassVar[int]
    HUB_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    HUB_PRO_PERMISSION_CLAIM_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    HUB_SLAVE_BUS_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_TIMEZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_ACTION_SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    HUB_FIRMWARE_ID_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_VIDEO_SCENARIO_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HUB_CUSTOM_ALARM_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_SELF_TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    HUB_VIDEO_ARCHIVE_EXPORT_COMPLETED_DATA_FIELD_NUMBER: _ClassVar[int]
    HUB_ALARM_SUPPRESS_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_VIDEO_EDGE_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_CONFIRMED_ALARM_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_ALARM_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_ERROR_CODE_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_FIRE_ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_EN54_DISABLEMENT_ENDPOINTS_LIST_FIELD_NUMBER: _ClassVar[int]
    HUB_AUDIO_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HUB_DEVICE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    HUB_DAY_ALARM_ZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_CHANNEL_MEDIA_DATA_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DISCONNECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ERROR_DETECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    STORAGE_WRITE_ERROR_DETECTED_DATA_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_EXPORT_COMPLETED_DATA_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_UPDATE_STARTED_DATA_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_UPDATE_FINISHED_DATA_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POWERED_OFF_OVERHEATED_DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ADDED_DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_MEDIA_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_REQUEST_FROM_PRO_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_REQUEST_FROM_COMPANY_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_DENIED_FOR_PRO_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_APPROVED_TO_COMPANY_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_APPROVED_TO_PRO_DATA_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_DENIED_FOR_COMPANY_DATA_FIELD_NUMBER: _ClassVar[int]
    DIRECT_EXPORT_REQUESTED_DATA_FIELD_NUMBER: _ClassVar[int]
    DETECTION_TIMESTAMP_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONNECTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_INITIATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSED_DATA_FIELD_NUMBER: _ClassVar[int]
    SPACE_DISPLAY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRO_PERMISSIONS_CLAIM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SPACE_PRO_PERMISSIONS_CLAIM_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    HUB_IN_SPACE_TROUBLED_DEVICES_FIELD_NUMBER: _ClassVar[int]
    HUB_IN_SPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    STANDALONE_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_INITIATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_INFO_FIELD_NUMBER: _ClassVar[int]
    JOIN_SPACE_REQUEST_INFO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_PERMISSION_CLAIM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    COMPANY_PERMISSION_CLAIM_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_INFO_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    DEALER_INFO_FIELD_NUMBER: _ClassVar[int]
    PAID_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATION_DATE_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_INFO_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    hub_display_groups: _display_groups_pb2.DisplayGroups
    hub_location_info: _location_info_pb2.LocationInfo
    hub_troubled_devices: _troubled_devices_pb2.TroubledDevices
    hub_initiator_info: _initiator_info_pb2_1.InitiatorInfo
    hub_endpoint_info: _endpoint_info_pb2.EndpointInfo
    hub_firmware_version: _firmware_version_pb2.FirmwareVersion
    hub_image_resource: _image_resource_pb2.ImageResource
    hub_company_permission_claim: _company_permissions_claim_pb2.CompanyPermissionsClaim
    hub_company_permission_claim_response: (
        _company_permissions_claim_response_pb2_1.CompanyPermissionsClaimResponse
    )
    hub_initiator_name: _initiator_name_pb2.InitiatorName
    hub_pro_permission_claim: _pro_permissions_claim_pb2.ProPermissionsClaim
    hub_malfunction: _malfunction_info_pb2.MalfunctionInfo
    hub_pro_permission_claim_response: (
        _pro_permissions_claim_response_pb2.ProPermissionsClaimResponse
    )
    hub_slave_bus_id: _slave_bus_id_pb2.SlaveBusId
    hub_timezone_info: _timezone_info_pb2.TimezoneInfo
    hub_connection_info: _hub_connection_info_pb2.HubConnectionInfo
    hub_action_source_object: _action_source_object_pb2.ActionSourceObject
    hub_firmware_id_info: _firmware_id_pb2.FirmwareIdInfo
    hub_video_scenario_resource: _video_scenario_resource_pb2.VideoScenarioResource
    hub_custom_alarm_type_info: _custom_alarm_type_pb2.CustomAlarmTypeInfo
    hub_self_test_status: _self_test_status_pb2.SelfTestStatus
    hub_video_archive_export_completed_data: (
        _video_archive_export_completed_data_pb2.VideoArchiveExportCompletedData
    )
    hub_alarm_suppress_info: _alarm_suppress_info_pb2.AlarmSuppressInfo
    hub_video_edge_info: _video_edge_info_pb2.VideoEdgeInfo
    hub_confirmed_alarm_info: _confirmed_alarm_info_pb2.ConfirmedAlarmInfo
    hub_alarm_info: _hub_alarm_info_pb2.HubAlarmInfo
    hub_error_code_info: _error_code_info_pb2.ErrorCodeInfo
    hub_fire_zone_info: _fire_zone_info_pb2.FireZoneInfo
    hub_en54_disablement_endpoints_list: (
        _en54_disablement_endpoints_pb2.En54DisablementEndpoints
    )
    hub_audio_resource: _hub_audio_resource_pb2.HubAudioResource
    hub_device_location_info: _device_location_info_pb2.DeviceLocationInfo
    hub_day_alarm_zone_info: _day_alarm_zone_info_pb2.DayAlarmZoneInfo
    offline_notifications: _offline_notifications_pb2.OfflineNotifications
    video_edge_channel_media_data: (
        _video_edge_channel_media_data_info_pb2.VideoEdgeChannelMediaDataInfo
    )
    video_scenario_data: _video_scenario_data_pb2.VideoScenarioData
    channel_disconnected_data: _channel_disconnected_data_pb2.ChannelDisconnectedData
    storage_error_detected_data: (
        _storage_error_detected_data_pb2.StorageErrorDetectedData
    )
    storage_write_error_detected_data: (
        _storage_write_error_detected_data_pb2.StorageWriteErrorDetectedData
    )
    archive_export_completed_data: (
        _archive_export_completed_data_pb2.ArchiveExportCompletedData
    )
    firmware_update_started_data: (
        _firmware_update_started_data_pb2.FirmwareUpdateStartedData
    )
    firmware_update_finished_data: (
        _firmware_update_finished_data_pb2.FirmwareUpdateFinishedData
    )
    storage_powered_off_overheated_data: (
        _storage_powered_off_overheated_data_pb2.StoragePoweredOffOverheatedData
    )
    channel_added_data: _channel_added_data_pb2.ChannelAddedData
    channel_media_data: _channel_media_data_info_pb2.ChannelMediaDataInfo
    temporary_video_access_request_from_pro_data: _temporary_video_access_request_from_pro_data_pb2.TemporaryVideoAccessRequestFromProData
    temporary_video_access_request_from_company_data: _temporary_video_access_request_from_company_data_pb2.TemporaryVideoAccessRequestFromCompanyData
    temporary_video_access_denied_for_pro_data: _temporary_video_access_denied_for_pro_data_pb2.TemporaryVideoAccessDeniedForProData
    temporary_video_access_approved_to_company_data: _temporary_video_access_approved_to_company_data_pb2.TemporaryVideoAccessApprovedToCompanyData
    temporary_video_access_approved_to_pro_data: _temporary_video_access_approved_to_pro_data_pb2.TemporaryVideoAccessApprovedToProData
    temporary_video_access_denied_for_company_data: _temporary_video_access_denied_for_company_data_pb2.TemporaryVideoAccessDeniedForCompanyData
    direct_export_requested_data: (
        _direct_export_requested_data_pb2.DirectExportRequestedData
    )
    detection_timestamp_info: (
        _video_detection_timestamp_info_pb2.VideoDetectionTimestampInfo
    )
    backup_connection_context: _backup_connection_context_pb2.BackupConnectionContext
    video_initiator_info: _initiator_info_pb2_1_1_1.InitiatorInfo
    storage_device_info: _storage_device_info_pb2.StorageDeviceInfo
    line_crossed_data: _line_crossed_data_pb2.LineCrossedData
    space_display_groups: _display_groups_pb2_1.DisplayGroups
    space_pro_permissions_claim_request: (
        _pro_permissions_claim_request_pb2.ProPermissionsClaimRequest
    )
    space_pro_permissions_claim_response: (
        _pro_permissions_claim_response_pb2_1.ProPermissionsClaimResponse
    )
    hub_in_space_troubled_devices: _hub_troubled_devices_pb2.HubInSpaceTroubledDevices
    hub_in_space_info: _hub_info_pb2.HubInSpaceInfo
    space_location_info: _panic_location_pb2.SpaceLocationInfo
    standalone_device_info: _standalone_device_info_pb2.StandaloneDeviceInfo
    space_initiator_info: _initiator_info_pb2_1_1.InitiatorInfo
    timezone_info: _timezone_info_pb2_1.TimezoneInfo
    join_space_request_info: _join_space_request_info_pb2.JoinSpaceRequestInfo
    company_permission_claim_request: (
        _company_permissions_claim_request_pb2.CompanyPermissionsClaimRequest
    )
    company_permission_claim_response: (
        _company_permissions_claim_response_pb2.CompanyPermissionsClaimResponse
    )
    initiator_info: _initiator_info_pb2.InitiatorInfo
    initiator: _initiator_pb2.Initiator
    dealer_info: _dealer_info_pb2.DealerInfo
    paid_service: _paid_service_pb2.PaidService
    deactivation_date: _deactivation_date_pb2.DeactivationDate
    space_member_info: _space_member_info_pb2.SpaceMemberInfo
    assigned_target_infos: _assigned_target_infos_pb2.AssignedTargetInfos
    deactivated_target_infos: _deactivated_target_infos_pb2.DeactivatedTargetInfos
    def __init__(
        self,
        hub_display_groups: _display_groups_pb2.DisplayGroups | _Mapping | None = ...,
        hub_location_info: _location_info_pb2.LocationInfo | _Mapping | None = ...,
        hub_troubled_devices: _troubled_devices_pb2.TroubledDevices
        | _Mapping
        | None = ...,
        hub_initiator_info: _initiator_info_pb2_1.InitiatorInfo | _Mapping | None = ...,
        hub_endpoint_info: _endpoint_info_pb2.EndpointInfo | _Mapping | None = ...,
        hub_firmware_version: _firmware_version_pb2.FirmwareVersion
        | _Mapping
        | None = ...,
        hub_image_resource: _image_resource_pb2.ImageResource | _Mapping | None = ...,
        hub_company_permission_claim: _company_permissions_claim_pb2.CompanyPermissionsClaim
        | _Mapping
        | None = ...,
        hub_company_permission_claim_response: _company_permissions_claim_response_pb2_1.CompanyPermissionsClaimResponse
        | _Mapping
        | None = ...,
        hub_initiator_name: _initiator_name_pb2.InitiatorName | _Mapping | None = ...,
        hub_pro_permission_claim: _pro_permissions_claim_pb2.ProPermissionsClaim
        | _Mapping
        | None = ...,
        hub_malfunction: _malfunction_info_pb2.MalfunctionInfo | _Mapping | None = ...,
        hub_pro_permission_claim_response: _pro_permissions_claim_response_pb2.ProPermissionsClaimResponse
        | _Mapping
        | None = ...,
        hub_slave_bus_id: _slave_bus_id_pb2.SlaveBusId | _Mapping | None = ...,
        hub_timezone_info: _timezone_info_pb2.TimezoneInfo | _Mapping | None = ...,
        hub_connection_info: _hub_connection_info_pb2.HubConnectionInfo
        | _Mapping
        | None = ...,
        hub_action_source_object: _action_source_object_pb2.ActionSourceObject
        | _Mapping
        | None = ...,
        hub_firmware_id_info: _firmware_id_pb2.FirmwareIdInfo | _Mapping | None = ...,
        hub_video_scenario_resource: _video_scenario_resource_pb2.VideoScenarioResource
        | _Mapping
        | None = ...,
        hub_custom_alarm_type_info: _custom_alarm_type_pb2.CustomAlarmTypeInfo
        | _Mapping
        | None = ...,
        hub_self_test_status: _self_test_status_pb2.SelfTestStatus
        | _Mapping
        | None = ...,
        hub_video_archive_export_completed_data: _video_archive_export_completed_data_pb2.VideoArchiveExportCompletedData
        | _Mapping
        | None = ...,
        hub_alarm_suppress_info: _alarm_suppress_info_pb2.AlarmSuppressInfo
        | _Mapping
        | None = ...,
        hub_video_edge_info: _video_edge_info_pb2.VideoEdgeInfo | _Mapping | None = ...,
        hub_confirmed_alarm_info: _confirmed_alarm_info_pb2.ConfirmedAlarmInfo
        | _Mapping
        | None = ...,
        hub_alarm_info: _hub_alarm_info_pb2.HubAlarmInfo | _Mapping | None = ...,
        hub_error_code_info: _error_code_info_pb2.ErrorCodeInfo | _Mapping | None = ...,
        hub_fire_zone_info: _fire_zone_info_pb2.FireZoneInfo | _Mapping | None = ...,
        hub_en54_disablement_endpoints_list: _en54_disablement_endpoints_pb2.En54DisablementEndpoints
        | _Mapping
        | None = ...,
        hub_audio_resource: _hub_audio_resource_pb2.HubAudioResource
        | _Mapping
        | None = ...,
        hub_device_location_info: _device_location_info_pb2.DeviceLocationInfo
        | _Mapping
        | None = ...,
        hub_day_alarm_zone_info: _day_alarm_zone_info_pb2.DayAlarmZoneInfo
        | _Mapping
        | None = ...,
        offline_notifications: _offline_notifications_pb2.OfflineNotifications
        | _Mapping
        | None = ...,
        video_edge_channel_media_data: _video_edge_channel_media_data_info_pb2.VideoEdgeChannelMediaDataInfo
        | _Mapping
        | None = ...,
        video_scenario_data: _video_scenario_data_pb2.VideoScenarioData
        | _Mapping
        | None = ...,
        channel_disconnected_data: _channel_disconnected_data_pb2.ChannelDisconnectedData
        | _Mapping
        | None = ...,
        storage_error_detected_data: _storage_error_detected_data_pb2.StorageErrorDetectedData
        | _Mapping
        | None = ...,
        storage_write_error_detected_data: _storage_write_error_detected_data_pb2.StorageWriteErrorDetectedData
        | _Mapping
        | None = ...,
        archive_export_completed_data: _archive_export_completed_data_pb2.ArchiveExportCompletedData
        | _Mapping
        | None = ...,
        firmware_update_started_data: _firmware_update_started_data_pb2.FirmwareUpdateStartedData
        | _Mapping
        | None = ...,
        firmware_update_finished_data: _firmware_update_finished_data_pb2.FirmwareUpdateFinishedData
        | _Mapping
        | None = ...,
        storage_powered_off_overheated_data: _storage_powered_off_overheated_data_pb2.StoragePoweredOffOverheatedData
        | _Mapping
        | None = ...,
        channel_added_data: _channel_added_data_pb2.ChannelAddedData
        | _Mapping
        | None = ...,
        channel_media_data: _channel_media_data_info_pb2.ChannelMediaDataInfo
        | _Mapping
        | None = ...,
        temporary_video_access_request_from_pro_data: _temporary_video_access_request_from_pro_data_pb2.TemporaryVideoAccessRequestFromProData
        | _Mapping
        | None = ...,
        temporary_video_access_request_from_company_data: _temporary_video_access_request_from_company_data_pb2.TemporaryVideoAccessRequestFromCompanyData
        | _Mapping
        | None = ...,
        temporary_video_access_denied_for_pro_data: _temporary_video_access_denied_for_pro_data_pb2.TemporaryVideoAccessDeniedForProData
        | _Mapping
        | None = ...,
        temporary_video_access_approved_to_company_data: _temporary_video_access_approved_to_company_data_pb2.TemporaryVideoAccessApprovedToCompanyData
        | _Mapping
        | None = ...,
        temporary_video_access_approved_to_pro_data: _temporary_video_access_approved_to_pro_data_pb2.TemporaryVideoAccessApprovedToProData
        | _Mapping
        | None = ...,
        temporary_video_access_denied_for_company_data: _temporary_video_access_denied_for_company_data_pb2.TemporaryVideoAccessDeniedForCompanyData
        | _Mapping
        | None = ...,
        direct_export_requested_data: _direct_export_requested_data_pb2.DirectExportRequestedData
        | _Mapping
        | None = ...,
        detection_timestamp_info: _video_detection_timestamp_info_pb2.VideoDetectionTimestampInfo
        | _Mapping
        | None = ...,
        backup_connection_context: _backup_connection_context_pb2.BackupConnectionContext
        | _Mapping
        | None = ...,
        video_initiator_info: _initiator_info_pb2_1_1_1.InitiatorInfo
        | _Mapping
        | None = ...,
        storage_device_info: _storage_device_info_pb2.StorageDeviceInfo
        | _Mapping
        | None = ...,
        line_crossed_data: _line_crossed_data_pb2.LineCrossedData
        | _Mapping
        | None = ...,
        space_display_groups: _display_groups_pb2_1.DisplayGroups
        | _Mapping
        | None = ...,
        space_pro_permissions_claim_request: _pro_permissions_claim_request_pb2.ProPermissionsClaimRequest
        | _Mapping
        | None = ...,
        space_pro_permissions_claim_response: _pro_permissions_claim_response_pb2_1.ProPermissionsClaimResponse
        | _Mapping
        | None = ...,
        hub_in_space_troubled_devices: _hub_troubled_devices_pb2.HubInSpaceTroubledDevices
        | _Mapping
        | None = ...,
        hub_in_space_info: _hub_info_pb2.HubInSpaceInfo | _Mapping | None = ...,
        space_location_info: _panic_location_pb2.SpaceLocationInfo
        | _Mapping
        | None = ...,
        standalone_device_info: _standalone_device_info_pb2.StandaloneDeviceInfo
        | _Mapping
        | None = ...,
        space_initiator_info: _initiator_info_pb2_1_1.InitiatorInfo
        | _Mapping
        | None = ...,
        timezone_info: _timezone_info_pb2_1.TimezoneInfo | _Mapping | None = ...,
        join_space_request_info: _join_space_request_info_pb2.JoinSpaceRequestInfo
        | _Mapping
        | None = ...,
        company_permission_claim_request: _company_permissions_claim_request_pb2.CompanyPermissionsClaimRequest
        | _Mapping
        | None = ...,
        company_permission_claim_response: _company_permissions_claim_response_pb2.CompanyPermissionsClaimResponse
        | _Mapping
        | None = ...,
        initiator_info: _initiator_info_pb2.InitiatorInfo | _Mapping | None = ...,
        initiator: _initiator_pb2.Initiator | _Mapping | None = ...,
        dealer_info: _dealer_info_pb2.DealerInfo | _Mapping | None = ...,
        paid_service: _paid_service_pb2.PaidService | _Mapping | None = ...,
        deactivation_date: _deactivation_date_pb2.DeactivationDate
        | _Mapping
        | None = ...,
        space_member_info: _space_member_info_pb2.SpaceMemberInfo
        | _Mapping
        | None = ...,
        assigned_target_infos: _assigned_target_infos_pb2.AssignedTargetInfos
        | _Mapping
        | None = ...,
        deactivated_target_infos: _deactivated_target_infos_pb2.DeactivatedTargetInfos
        | _Mapping
        | None = ...,
    ) -> None: ...
