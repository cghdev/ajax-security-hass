from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.space.integration import (
    space_integration_type_pb2 as _space_integration_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetSpaceIntegrationOAuthAuthorizationCodeUrlRequest(_message.Message):
    __slots__ = ("integration_type", "space_id")
    INTEGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    integration_type: _space_integration_type_pb2.SpaceIntegrationType
    space_id: str
    def __init__(
        self,
        integration_type: _space_integration_type_pb2.SpaceIntegrationType
        | str
        | None = ...,
        space_id: str | None = ...,
    ) -> None: ...
