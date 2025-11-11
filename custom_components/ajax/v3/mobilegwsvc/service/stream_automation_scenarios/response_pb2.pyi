from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.scheduled_acesss import (
    scheduled_access_pb2 as _scheduled_access_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubAutomationScenariosResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("created", "deleted", "snapshot", "updated")
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamHubAutomationScenariosResponse.Snapshot
        created: StreamHubAutomationScenariosResponse.Created
        updated: StreamHubAutomationScenariosResponse.Updated
        deleted: StreamHubAutomationScenariosResponse.Deleted
        def __init__(
            self,
            snapshot: StreamHubAutomationScenariosResponse.Snapshot
            | _Mapping
            | None = ...,
            created: StreamHubAutomationScenariosResponse.Created
            | _Mapping
            | None = ...,
            updated: StreamHubAutomationScenariosResponse.Updated
            | _Mapping
            | None = ...,
            deleted: StreamHubAutomationScenariosResponse.Deleted
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Snapshot(_message.Message):
        __slots__ = ("automation_scenarios",)
        AUTOMATION_SCENARIOS_FIELD_NUMBER: _ClassVar[int]
        automation_scenarios: _containers.RepeatedCompositeFieldContainer[
            StreamHubAutomationScenariosResponse.AutomationScenarioObject
        ]
        def __init__(
            self,
            automation_scenarios: _Iterable[
                StreamHubAutomationScenariosResponse.AutomationScenarioObject | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Created(_message.Message):
        __slots__ = ("automation_scenario",)
        AUTOMATION_SCENARIO_FIELD_NUMBER: _ClassVar[int]
        automation_scenario: (
            StreamHubAutomationScenariosResponse.AutomationScenarioObject
        )
        def __init__(
            self,
            automation_scenario: StreamHubAutomationScenariosResponse.AutomationScenarioObject
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Updated(_message.Message):
        __slots__ = ("automation_scenario",)
        AUTOMATION_SCENARIO_FIELD_NUMBER: _ClassVar[int]
        automation_scenario: (
            StreamHubAutomationScenariosResponse.AutomationScenarioObject
        )
        def __init__(
            self,
            automation_scenario: StreamHubAutomationScenariosResponse.AutomationScenarioObject
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Deleted(_message.Message):
        __slots__ = ("scheduled_access_id",)
        SCHEDULED_ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
        scheduled_access_id: int
        def __init__(self, scheduled_access_id: int | None = ...) -> None: ...

    class AutomationScenarioObject(_message.Message):
        __slots__ = ("scheduled_access",)
        SCHEDULED_ACCESS_FIELD_NUMBER: _ClassVar[int]
        scheduled_access: _scheduled_access_pb2.ScheduledAccess
        def __init__(
            self,
            scheduled_access: _scheduled_access_pb2.ScheduledAccess
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_not_found",
            "permission_denied",
            "request_timeout",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        REQUEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        request_timeout: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
            request_timeout: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamHubAutomationScenariosResponse.Success
    failure: StreamHubAutomationScenariosResponse.Failure
    def __init__(
        self,
        success: StreamHubAutomationScenariosResponse.Success | _Mapping | None = ...,
        failure: StreamHubAutomationScenariosResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
