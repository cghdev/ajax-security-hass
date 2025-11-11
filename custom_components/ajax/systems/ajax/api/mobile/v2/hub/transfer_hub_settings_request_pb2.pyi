from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TransferHubSettingsRequest(_message.Message):
    __slots__ = (
        "accept_snatch_hub",
        "donor_hub_id",
        "space_locator",
        "target_hub_qr_code",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    DONOR_HUB_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_HUB_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_SNATCH_HUB_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    donor_hub_id: str
    target_hub_qr_code: str
    accept_snatch_hub: bool
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        donor_hub_id: str | None = ...,
        target_hub_qr_code: str | None = ...,
        accept_snatch_hub: bool = ...,
    ) -> None: ...

class TransferHubSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "donor_hub_has_active_subscriptions",
            "donor_hub_has_active_subscriptions_for_member",
            "hub_already_in_space",
            "hub_busy",
            "hub_claim_error",
            "hub_error",
            "hub_in_use",
            "hub_locked_by_another_company",
            "hub_not_empty",
            "hub_qr_code_invalid",
            "hub_wrong_state",
            "illegal_donor_hub_service_state",
            "member_not_authorized_add_fibra_and_hybrid_hub",
            "member_not_authorized_add_hub",
            "member_not_support_add_fibra_and_hybrid_hub",
            "passive_hubs_limit_exceeded",
            "permission_denied",
            "space_locked",
            "space_not_found",
            "target_hub_has_active_subscriptions",
            "target_hub_has_active_subscriptions_for_member",
            "target_hub_not_found",
            "target_hub_space_on_monitoring",
            "transfer_hub_settings_validation_errors",
        )
        class TransferHubSettingsValidationErrors(_message.Message):
            __slots__ = ("error",)
            class TransferHubSettingsValidationError(_message.Message):
                __slots__ = (
                    "donor_firmware_lower_minimal",
                    "donor_in_migration",
                    "donor_online",
                    "donor_permission_denied",
                    "donor_state_fetch_failed",
                    "donor_target_incompatible_types",
                    "target_armed",
                    "target_firmware_lower_donor",
                    "target_firmware_lower_minimal",
                    "target_in_migration",
                    "target_offline",
                    "target_permission_denied",
                    "target_state_fetch_failed",
                    "target_users_limit_exceeded",
                )
                TARGET_PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
                TARGET_ARMED_FIELD_NUMBER: _ClassVar[int]
                TARGET_STATE_FETCH_FAILED_FIELD_NUMBER: _ClassVar[int]
                TARGET_OFFLINE_FIELD_NUMBER: _ClassVar[int]
                TARGET_IN_MIGRATION_FIELD_NUMBER: _ClassVar[int]
                TARGET_FIRMWARE_LOWER_MINIMAL_FIELD_NUMBER: _ClassVar[int]
                TARGET_FIRMWARE_LOWER_DONOR_FIELD_NUMBER: _ClassVar[int]
                TARGET_USERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
                DONOR_PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
                DONOR_STATE_FETCH_FAILED_FIELD_NUMBER: _ClassVar[int]
                DONOR_TARGET_INCOMPATIBLE_TYPES_FIELD_NUMBER: _ClassVar[int]
                DONOR_FIRMWARE_LOWER_MINIMAL_FIELD_NUMBER: _ClassVar[int]
                DONOR_IN_MIGRATION_FIELD_NUMBER: _ClassVar[int]
                DONOR_ONLINE_FIELD_NUMBER: _ClassVar[int]
                target_permission_denied: _response_pb2.DefaultError
                target_armed: _response_pb2.DefaultError
                target_state_fetch_failed: _response_pb2.DefaultError
                target_offline: _response_pb2.DefaultError
                target_in_migration: _response_pb2.DefaultError
                target_firmware_lower_minimal: _response_pb2.DefaultError
                target_firmware_lower_donor: _response_pb2.DefaultError
                target_users_limit_exceeded: _response_pb2.DefaultError
                donor_permission_denied: _response_pb2.DefaultError
                donor_state_fetch_failed: _response_pb2.DefaultError
                donor_target_incompatible_types: _response_pb2.DefaultError
                donor_firmware_lower_minimal: _response_pb2.DefaultError
                donor_in_migration: _response_pb2.DefaultError
                donor_online: _response_pb2.DefaultError
                def __init__(
                    self,
                    target_permission_denied: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    target_armed: _response_pb2.DefaultError | _Mapping | None = ...,
                    target_state_fetch_failed: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    target_offline: _response_pb2.DefaultError | _Mapping | None = ...,
                    target_in_migration: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    target_firmware_lower_minimal: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    target_firmware_lower_donor: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    target_users_limit_exceeded: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    donor_permission_denied: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    donor_state_fetch_failed: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    donor_target_incompatible_types: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    donor_firmware_lower_minimal: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    donor_in_migration: _response_pb2.DefaultError
                    | _Mapping
                    | None = ...,
                    donor_online: _response_pb2.DefaultError | _Mapping | None = ...,
                ) -> None: ...

            ERROR_FIELD_NUMBER: _ClassVar[int]
            error: _containers.RepeatedCompositeFieldContainer[
                TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors.TransferHubSettingsValidationError
            ]
            def __init__(
                self,
                error: _Iterable[
                    TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors.TransferHubSettingsValidationError
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        PASSIVE_HUBS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_IN_USE_FIELD_NUMBER: _ClassVar[int]
        HUB_ALREADY_IN_SPACE_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
        HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_EMPTY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_SUPPORT_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_BY_ANOTHER_COMPANY_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_SPACE_ON_MONITORING_FIELD_NUMBER: _ClassVar[int]
        TRANSFER_HUB_SETTINGS_VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
        DONOR_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        DONOR_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FOR_MEMBER_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        TARGET_HUB_HAS_ACTIVE_SUBSCRIPTIONS_FOR_MEMBER_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_DONOR_HUB_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        passive_hubs_limit_exceeded: _response_pb2.LimitExceededError
        hub_in_use: _response_pb2.DefaultError
        hub_already_in_space: _response_pb2.DefaultError
        target_hub_not_found: _response_pb2.DefaultError
        hub_qr_code_invalid: _response_pb2.DefaultError
        hub_claim_error: _response_pb2.DefaultError
        hub_not_empty: _response_pb2.DefaultError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        member_not_support_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
        member_not_authorized_add_hub: _response_pb2.DefaultError
        member_not_authorized_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
        hub_locked_by_another_company: _response_pb2.DefaultError
        target_hub_space_on_monitoring: _response_pb2.DefaultError
        transfer_hub_settings_validation_errors: (
            TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors
        )
        donor_hub_has_active_subscriptions: _response_pb2.DefaultError
        donor_hub_has_active_subscriptions_for_member: _response_pb2.DefaultError
        target_hub_has_active_subscriptions: _response_pb2.DefaultError
        target_hub_has_active_subscriptions_for_member: _response_pb2.DefaultError
        illegal_donor_hub_service_state: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            passive_hubs_limit_exceeded: _response_pb2.LimitExceededError
            | _Mapping
            | None = ...,
            hub_in_use: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_already_in_space: _response_pb2.DefaultError | _Mapping | None = ...,
            target_hub_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_qr_code_invalid: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_claim_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_not_empty: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            member_not_support_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            member_not_authorized_add_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            member_not_authorized_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_locked_by_another_company: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            target_hub_space_on_monitoring: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            transfer_hub_settings_validation_errors: TransferHubSettingsResponse.Failure.TransferHubSettingsValidationErrors
            | _Mapping
            | None = ...,
            donor_hub_has_active_subscriptions: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            donor_hub_has_active_subscriptions_for_member: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            target_hub_has_active_subscriptions: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            target_hub_has_active_subscriptions_for_member: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            illegal_donor_hub_service_state: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: TransferHubSettingsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: TransferHubSettingsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
