from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class HubEvent(_message.Message):
    __slots__ = (
        "additional_data",
        "code",
        "event_id",
        "hub_id",
        "hub_name",
        "hub_sub_type",
        "id",
        "server_received_timestamp",
        "source_id",
        "source_name",
        "source_room_id",
        "source_room_name",
        "source_type",
        "type",
    )
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALARM: _ClassVar[HubEvent.Type]
        ALARM_RECOVERED: _ClassVar[HubEvent.Type]
        MALFUNCTION: _ClassVar[HubEvent.Type]
        FUNCTION_RECOVERED: _ClassVar[HubEvent.Type]
        SECURITY: _ClassVar[HubEvent.Type]
        COMMON: _ClassVar[HubEvent.Type]
        USER: _ClassVar[HubEvent.Type]
        LIFECYCLE: _ClassVar[HubEvent.Type]
        FIBRA_SCAN_ALARM: _ClassVar[HubEvent.Type]

    ALARM: HubEvent.Type
    ALARM_RECOVERED: HubEvent.Type
    MALFUNCTION: HubEvent.Type
    FUNCTION_RECOVERED: HubEvent.Type
    SECURITY: HubEvent.Type
    COMMON: HubEvent.Type
    USER: HubEvent.Type
    LIFECYCLE: HubEvent.Type
    FIBRA_SCAN_ALARM: HubEvent.Type
    class AdditionalData(_message.Message):
        __slots__ = (
            "access_request",
            "approve_permissions_permanently_additional_data",
            "approve_permissions_temporary_additional_data",
            "claim_permissions_request_permanent_additional_data",
            "claim_permissions_request_temporary_additional_data",
            "coordinates",
            "device_malfunctions",
            "firmware_version",
            "initiator_additional_data",
            "malfunction_additional_data",
            "reject_permissions_additional_data",
            "resource_description",
        )
        class AccessRequest(_message.Message):
            __slots__ = (
                "access_time_hours",
                "owner_email",
                "owner_id",
                "owner_name",
                "pro_company_id",
                "pro_email",
                "pro_id",
                "pro_name",
                "request_id",
                "requested_access_rights",
            )
            class AccessRights(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FULL_ACCESS: _ClassVar[
                    HubEvent.AdditionalData.AccessRequest.AccessRights
                ]

            FULL_ACCESS: HubEvent.AdditionalData.AccessRequest.AccessRights
            REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
            PRO_ID_FIELD_NUMBER: _ClassVar[int]
            PRO_NAME_FIELD_NUMBER: _ClassVar[int]
            PRO_EMAIL_FIELD_NUMBER: _ClassVar[int]
            PRO_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
            OWNER_ID_FIELD_NUMBER: _ClassVar[int]
            OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
            OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
            REQUESTED_ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
            request_id: int
            pro_id: str
            pro_name: str
            pro_email: str
            pro_company_id: str
            owner_id: str
            owner_name: str
            owner_email: str
            requested_access_rights: HubEvent.AdditionalData.AccessRequest.AccessRights
            access_time_hours: int
            def __init__(
                self,
                request_id: int | None = ...,
                pro_id: str | None = ...,
                pro_name: str | None = ...,
                pro_email: str | None = ...,
                pro_company_id: str | None = ...,
                owner_id: str | None = ...,
                owner_name: str | None = ...,
                owner_email: str | None = ...,
                requested_access_rights: HubEvent.AdditionalData.AccessRequest.AccessRights
                | str
                | None = ...,
                access_time_hours: int | None = ...,
            ) -> None: ...

        class Coordinates(_message.Message):
            __slots__ = ("latitude", "longitude")
            LATITUDE_FIELD_NUMBER: _ClassVar[int]
            LONGITUDE_FIELD_NUMBER: _ClassVar[int]
            latitude: float
            longitude: float
            def __init__(
                self, latitude: float | None = ..., longitude: float | None = ...
            ) -> None: ...

        class DeviceMalfunctions(_message.Message):
            __slots__ = ("items",)
            class DeviceMalfunction(_message.Message):
                __slots__ = (
                    "hub_name",
                    "obj_id",
                    "obj_name",
                    "obj_room_id",
                    "obj_room_name",
                    "obj_type",
                    "text",
                )
                OBJ_ID_FIELD_NUMBER: _ClassVar[int]
                OBJ_TYPE_FIELD_NUMBER: _ClassVar[int]
                OBJ_NAME_FIELD_NUMBER: _ClassVar[int]
                OBJ_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
                OBJ_ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
                HUB_NAME_FIELD_NUMBER: _ClassVar[int]
                TEXT_FIELD_NUMBER: _ClassVar[int]
                obj_id: str
                obj_type: str
                obj_name: str
                obj_room_id: str
                obj_room_name: str
                hub_name: str
                text: str
                def __init__(
                    self,
                    obj_id: str | None = ...,
                    obj_type: str | None = ...,
                    obj_name: str | None = ...,
                    obj_room_id: str | None = ...,
                    obj_room_name: str | None = ...,
                    hub_name: str | None = ...,
                    text: str | None = ...,
                ) -> None: ...

            ITEMS_FIELD_NUMBER: _ClassVar[int]
            items: _containers.RepeatedCompositeFieldContainer[
                HubEvent.AdditionalData.DeviceMalfunctions.DeviceMalfunction
            ]
            def __init__(
                self,
                items: _Iterable[
                    HubEvent.AdditionalData.DeviceMalfunctions.DeviceMalfunction
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class ResourceDescription(_message.Message):
            __slots__ = ("link_expiration_timestamp", "ordered_resource_links")
            class ResourceLink(_message.Message):
                __slots__ = ("status", "url")
                class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    IN_PROGRESS: _ClassVar[
                        HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                    ]
                    READY: _ClassVar[
                        HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                    ]
                    FAILED: _ClassVar[
                        HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                    ]

                IN_PROGRESS: (
                    HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                )
                READY: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                FAILED: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                URL_FIELD_NUMBER: _ClassVar[int]
                STATUS_FIELD_NUMBER: _ClassVar[int]
                url: str
                status: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                def __init__(
                    self,
                    url: str | None = ...,
                    status: HubEvent.AdditionalData.ResourceDescription.ResourceLink.Status
                    | str
                    | None = ...,
                ) -> None: ...

            ORDERED_RESOURCE_LINKS_FIELD_NUMBER: _ClassVar[int]
            LINK_EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            ordered_resource_links: _containers.RepeatedCompositeFieldContainer[
                HubEvent.AdditionalData.ResourceDescription.ResourceLink
            ]
            link_expiration_timestamp: _timestamp_pb2.Timestamp
            def __init__(
                self,
                ordered_resource_links: _Iterable[
                    HubEvent.AdditionalData.ResourceDescription.ResourceLink | _Mapping
                ]
                | None = ...,
                link_expiration_timestamp: _timestamp_pb2.Timestamp
                | _Mapping
                | None = ...,
            ) -> None: ...

        class FirmwareVersion(_message.Message):
            __slots__ = ("version",)
            VERSION_FIELD_NUMBER: _ClassVar[int]
            version: str
            def __init__(self, version: str | None = ...) -> None: ...

        class MalfunctionAdditionalData(_message.Message):
            __slots__ = ("device_malfunction",)
            class DeviceMalfunctionInfo(
                int, metaclass=_enum_type_wrapper.EnumTypeWrapper
            ):
                __slots__ = ()
                NO_MALFUNCTION_INFO: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                CABLE_BREAK_ISSUE: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                VOLTAGE_INSTABILITY: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                SIREN_VOLUME_TEST_REQUIRED: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                CO_SENSOR_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                CO_SENSOR_LEVEL_EXCEEDED: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                SMOKE_DETECTOR_CAMERA_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                MICROWAVE_SENSOR_CALIBRATION_ERROR: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                ACCELEROMETER_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                BAD_INPUT_RESISTANCE: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                MODEM_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                WIFI_CONNECTION_FAIL: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                BATTERY_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                BATTERY_CHARGE_ERROR: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                SOFTWARE_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]
                FLASH_MALFUNCTION: _ClassVar[
                    HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                ]

            NO_MALFUNCTION_INFO: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            CABLE_BREAK_ISSUE: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            VOLTAGE_INSTABILITY: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            SIREN_VOLUME_TEST_REQUIRED: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            CO_SENSOR_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            CO_SENSOR_LEVEL_EXCEEDED: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            SMOKE_DETECTOR_CAMERA_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            MICROWAVE_SENSOR_CALIBRATION_ERROR: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            ACCELEROMETER_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            BAD_INPUT_RESISTANCE: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            MODEM_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            WIFI_CONNECTION_FAIL: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            BATTERY_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            BATTERY_CHARGE_ERROR: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            SOFTWARE_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            FLASH_MALFUNCTION: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            DEVICE_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
            device_malfunction: (
                HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
            )
            def __init__(
                self,
                device_malfunction: HubEvent.AdditionalData.MalfunctionAdditionalData.DeviceMalfunctionInfo
                | str
                | None = ...,
            ) -> None: ...

        class Initiator(_message.Message):
            __slots__ = ("initiator_name",)
            INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
            initiator_name: str
            def __init__(self, initiator_name: str | None = ...) -> None: ...

        class ApprovePermissionsRequestPermanentlyAdditionalData(_message.Message):
            __slots__ = ("email", "name")
            NAME_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            name: str
            email: str
            def __init__(
                self, name: str | None = ..., email: str | None = ...
            ) -> None: ...

        class RejectPermissionsRequestAdditionalData(_message.Message):
            __slots__ = ("email", "name")
            NAME_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            name: str
            email: str
            def __init__(
                self, name: str | None = ..., email: str | None = ...
            ) -> None: ...

        class ApprovePermissionsRequestTemporaryAdditionalData(_message.Message):
            __slots__ = ("access_time_hours", "email", "name")
            NAME_FIELD_NUMBER: _ClassVar[int]
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
            name: str
            email: str
            access_time_hours: int
            def __init__(
                self,
                name: str | None = ...,
                email: str | None = ...,
                access_time_hours: int | None = ...,
            ) -> None: ...

        class ClaimPermissionsRequestTemporaryAdditionalData(_message.Message):
            __slots__ = ("access_time_hours", "claimID", "emailCompany")
            CLAIMID_FIELD_NUMBER: _ClassVar[int]
            EMAILCOMPANY_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TIME_HOURS_FIELD_NUMBER: _ClassVar[int]
            claimID: str
            emailCompany: str
            access_time_hours: int
            def __init__(
                self,
                claimID: str | None = ...,
                emailCompany: str | None = ...,
                access_time_hours: int | None = ...,
            ) -> None: ...

        class ClaimPermissionsRequestPermanentAdditionalData(_message.Message):
            __slots__ = ("claimID", "emailCompany")
            CLAIMID_FIELD_NUMBER: _ClassVar[int]
            EMAILCOMPANY_FIELD_NUMBER: _ClassVar[int]
            claimID: str
            emailCompany: str
            def __init__(
                self, claimID: str | None = ..., emailCompany: str | None = ...
            ) -> None: ...

        ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
        COORDINATES_FIELD_NUMBER: _ClassVar[int]
        DEVICE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTION_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        INITIATOR_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        APPROVE_PERMISSIONS_PERMANENTLY_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        REJECT_PERMISSIONS_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        APPROVE_PERMISSIONS_TEMPORARY_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        CLAIM_PERMISSIONS_REQUEST_TEMPORARY_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        CLAIM_PERMISSIONS_REQUEST_PERMANENT_ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
        access_request: HubEvent.AdditionalData.AccessRequest
        coordinates: HubEvent.AdditionalData.Coordinates
        device_malfunctions: HubEvent.AdditionalData.DeviceMalfunctions
        resource_description: HubEvent.AdditionalData.ResourceDescription
        firmware_version: HubEvent.AdditionalData.FirmwareVersion
        malfunction_additional_data: HubEvent.AdditionalData.MalfunctionAdditionalData
        initiator_additional_data: HubEvent.AdditionalData.Initiator
        approve_permissions_permanently_additional_data: (
            HubEvent.AdditionalData.ApprovePermissionsRequestPermanentlyAdditionalData
        )
        reject_permissions_additional_data: (
            HubEvent.AdditionalData.RejectPermissionsRequestAdditionalData
        )
        approve_permissions_temporary_additional_data: (
            HubEvent.AdditionalData.ApprovePermissionsRequestTemporaryAdditionalData
        )
        claim_permissions_request_temporary_additional_data: (
            HubEvent.AdditionalData.ClaimPermissionsRequestTemporaryAdditionalData
        )
        claim_permissions_request_permanent_additional_data: (
            HubEvent.AdditionalData.ClaimPermissionsRequestPermanentAdditionalData
        )
        def __init__(
            self,
            access_request: HubEvent.AdditionalData.AccessRequest
            | _Mapping
            | None = ...,
            coordinates: HubEvent.AdditionalData.Coordinates | _Mapping | None = ...,
            device_malfunctions: HubEvent.AdditionalData.DeviceMalfunctions
            | _Mapping
            | None = ...,
            resource_description: HubEvent.AdditionalData.ResourceDescription
            | _Mapping
            | None = ...,
            firmware_version: HubEvent.AdditionalData.FirmwareVersion
            | _Mapping
            | None = ...,
            malfunction_additional_data: HubEvent.AdditionalData.MalfunctionAdditionalData
            | _Mapping
            | None = ...,
            initiator_additional_data: HubEvent.AdditionalData.Initiator
            | _Mapping
            | None = ...,
            approve_permissions_permanently_additional_data: HubEvent.AdditionalData.ApprovePermissionsRequestPermanentlyAdditionalData
            | _Mapping
            | None = ...,
            reject_permissions_additional_data: HubEvent.AdditionalData.RejectPermissionsRequestAdditionalData
            | _Mapping
            | None = ...,
            approve_permissions_temporary_additional_data: HubEvent.AdditionalData.ApprovePermissionsRequestTemporaryAdditionalData
            | _Mapping
            | None = ...,
            claim_permissions_request_temporary_additional_data: HubEvent.AdditionalData.ClaimPermissionsRequestTemporaryAdditionalData
            | _Mapping
            | None = ...,
            claim_permissions_request_permanent_additional_data: HubEvent.AdditionalData.ClaimPermissionsRequestPermanentAdditionalData
            | _Mapping
            | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_RECEIVED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    HUB_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    hub_id: str
    hub_name: str
    source_id: str
    source_name: str
    code: str
    type: HubEvent.Type
    source_room_name: str
    event_id: str
    server_received_timestamp: _timestamp_pb2.Timestamp
    source_type: str
    source_room_id: str
    additional_data: HubEvent.AdditionalData
    hub_sub_type: str
    def __init__(
        self,
        id: str | None = ...,
        hub_id: str | None = ...,
        hub_name: str | None = ...,
        source_id: str | None = ...,
        source_name: str | None = ...,
        code: str | None = ...,
        type: HubEvent.Type | str | None = ...,
        source_room_name: str | None = ...,
        event_id: str | None = ...,
        server_received_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        source_type: str | None = ...,
        source_room_id: str | None = ...,
        additional_data: HubEvent.AdditionalData | _Mapping | None = ...,
        hub_sub_type: str | None = ...,
    ) -> None: ...
