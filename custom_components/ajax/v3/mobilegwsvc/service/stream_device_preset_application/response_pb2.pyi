from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.company.templates import (
    company_template_type_pb2 as _company_template_type_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.space.device.light import (
    light_device_id_pb2 as _light_device_id_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDevicePresetApplicationResponse(_message.Message):
    __slots__ = ("failure", "success")
    class SettingsApplyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SETTINGS_APPLY_STATUS_UNSPECIFIED: _ClassVar[
            StreamDevicePresetApplicationResponse.SettingsApplyStatus
        ]
        SETTINGS_APPLY_STATUS_SUCCESS: _ClassVar[
            StreamDevicePresetApplicationResponse.SettingsApplyStatus
        ]
        SETTINGS_APPLY_STATUS_FAILURE: _ClassVar[
            StreamDevicePresetApplicationResponse.SettingsApplyStatus
        ]
        SETTINGS_APPLY_STATUS_FAILED_TO_START: _ClassVar[
            StreamDevicePresetApplicationResponse.SettingsApplyStatus
        ]

    SETTINGS_APPLY_STATUS_UNSPECIFIED: (
        StreamDevicePresetApplicationResponse.SettingsApplyStatus
    )
    SETTINGS_APPLY_STATUS_SUCCESS: (
        StreamDevicePresetApplicationResponse.SettingsApplyStatus
    )
    SETTINGS_APPLY_STATUS_FAILURE: (
        StreamDevicePresetApplicationResponse.SettingsApplyStatus
    )
    SETTINGS_APPLY_STATUS_FAILED_TO_START: (
        StreamDevicePresetApplicationResponse.SettingsApplyStatus
    )
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDevicePresetApplicationResponse.Snapshot
        update: StreamDevicePresetApplicationResponse.Update
        def __init__(
            self,
            snapshot: StreamDevicePresetApplicationResponse.Snapshot
            | _Mapping
            | None = ...,
            update: StreamDevicePresetApplicationResponse.Update
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Snapshot(_message.Message):
        __slots__ = (
            "company_template_metadata",
            "errors",
            "total_num_of_targets",
            "total_processed",
        )
        TOTAL_NUM_OF_TARGETS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        ERRORS_FIELD_NUMBER: _ClassVar[int]
        COMPANY_TEMPLATE_METADATA_FIELD_NUMBER: _ClassVar[int]
        total_num_of_targets: int
        total_processed: int
        errors: _containers.RepeatedCompositeFieldContainer[
            StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget
        ]
        company_template_metadata: (
            StreamDevicePresetApplicationResponse.TemplateMetadata
        )
        def __init__(
            self,
            total_num_of_targets: int | None = ...,
            total_processed: int | None = ...,
            errors: _Iterable[
                StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget
                | _Mapping
            ]
            | None = ...,
            company_template_metadata: StreamDevicePresetApplicationResponse.TemplateMetadata
            | _Mapping
            | None = ...,
        ) -> None: ...

    class TemplateMetadata(_message.Message):
        __slots__ = ("company_template_name", "company_template_type")
        COMPANY_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        COMPANY_TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        company_template_name: str
        company_template_type: _company_template_type_pb2.CompanyTemplateType
        def __init__(
            self,
            company_template_name: str | None = ...,
            company_template_type: _company_template_type_pb2.CompanyTemplateType
            | str
            | None = ...,
        ) -> None: ...

    class Update(_message.Message):
        __slots__ = ("application_result",)
        APPLICATION_RESULT_FIELD_NUMBER: _ClassVar[int]
        application_result: (
            StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget
        )
        def __init__(
            self,
            application_result: StreamDevicePresetApplicationResponse.SettingsApplyResultOnTarget
            | _Mapping
            | None = ...,
        ) -> None: ...

    class SettingsApplyResultOnTarget(_message.Message):
        __slots__ = ("apply_status", "target")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        APPLY_STATUS_FIELD_NUMBER: _ClassVar[int]
        target: StreamDevicePresetApplicationResponse.SettingTarget
        apply_status: StreamDevicePresetApplicationResponse.SettingsApplyStatus
        def __init__(
            self,
            target: StreamDevicePresetApplicationResponse.SettingTarget
            | _Mapping
            | None = ...,
            apply_status: StreamDevicePresetApplicationResponse.SettingsApplyStatus
            | str
            | None = ...,
        ) -> None: ...

    class SettingTarget(_message.Message):
        __slots__ = ("light_device_id",)
        LIGHT_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        light_device_id: _light_device_id_pb2.LightDeviceId
        def __init__(
            self,
            light_device_id: _light_device_id_pb2.LightDeviceId | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "permission_denied")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDevicePresetApplicationResponse.Success
    failure: StreamDevicePresetApplicationResponse.Failure
    def __init__(
        self,
        success: StreamDevicePresetApplicationResponse.Success | _Mapping | None = ...,
        failure: StreamDevicePresetApplicationResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
