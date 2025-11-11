from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommandTurnEthernetRequest(_message.Message):
    __slots__ = ("hub_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[HubCommandTurnEthernetRequest.State]
        STATE_OFF: _ClassVar[HubCommandTurnEthernetRequest.State]
        STATE_ON: _ClassVar[HubCommandTurnEthernetRequest.State]

    STATE_UNSPECIFIED: HubCommandTurnEthernetRequest.State
    STATE_OFF: HubCommandTurnEthernetRequest.State
    STATE_ON: HubCommandTurnEthernetRequest.State
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    state: HubCommandTurnEthernetRequest.State
    def __init__(
        self,
        hub_id: str | None = ...,
        state: HubCommandTurnEthernetRequest.State | str | None = ...,
    ) -> None: ...
