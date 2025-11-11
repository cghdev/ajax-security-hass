from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import (
    resource_status_pb2 as _resource_status_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import (
    visibility_pb2 as _visibility_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubAudioResource(_message.Message):
    __slots__ = ("initiator_name", "resources", "visibility")
    class Audio(_message.Message):
        __slots__ = ("status",)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: _resource_status_pb2.ResourceStatus
        def __init__(
            self, status: _resource_status_pb2.ResourceStatus | str | None = ...
        ) -> None: ...

    INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    initiator_name: str
    resources: _containers.RepeatedCompositeFieldContainer[HubAudioResource.Audio]
    visibility: _visibility_pb2.MediaVisibility
    def __init__(
        self,
        initiator_name: str | None = ...,
        resources: _Iterable[HubAudioResource.Audio | _Mapping] | None = ...,
        visibility: _visibility_pb2.MediaVisibility | _Mapping | None = ...,
    ) -> None: ...
