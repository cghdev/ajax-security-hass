from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class MainChanelConnectionPart(_message.Message):
    __slots__ = ("main_chanel_connection_status",)
    class MainChanelConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MAIN_CHANEL_CONNECTION_STATUS_UNSPECIFIED: _ClassVar[
            MainChanelConnectionPart.MainChanelConnectionStatus
        ]
        MAIN_CHANEL_CONNECTION_STATUS_OFFLINE: _ClassVar[
            MainChanelConnectionPart.MainChanelConnectionStatus
        ]
        MAIN_CHANEL_CONNECTION_STATUS_ONLINE: _ClassVar[
            MainChanelConnectionPart.MainChanelConnectionStatus
        ]

    MAIN_CHANEL_CONNECTION_STATUS_UNSPECIFIED: (
        MainChanelConnectionPart.MainChanelConnectionStatus
    )
    MAIN_CHANEL_CONNECTION_STATUS_OFFLINE: (
        MainChanelConnectionPart.MainChanelConnectionStatus
    )
    MAIN_CHANEL_CONNECTION_STATUS_ONLINE: (
        MainChanelConnectionPart.MainChanelConnectionStatus
    )
    MAIN_CHANEL_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    main_chanel_connection_status: MainChanelConnectionPart.MainChanelConnectionStatus
    def __init__(
        self,
        main_chanel_connection_status: MainChanelConnectionPart.MainChanelConnectionStatus
        | str
        | None = ...,
    ) -> None: ...
