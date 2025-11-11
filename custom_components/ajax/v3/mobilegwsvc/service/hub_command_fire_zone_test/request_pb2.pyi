from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class HubCommandFireZoneTestRequest(_message.Message):
    __slots__ = (
        "add_fire_zone_to_test",
        "fire_zone_id",
        "hub_id",
        "remove_fire_zone_from_test",
        "start_fire_zone_test",
    )
    class StartFireZoneTest(_message.Message):
        __slots__ = ("output_devices", "type_of_output_activate")
        class TypeOfOutputActivate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_OF_OUTPUT_ACTIVATE_UNSPECIFIED: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
            ]
            TYPE_OF_OUTPUT_ACTIVATE_DO_NOT_ACTIVATE_OUTPUTS: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
            ]
            TYPE_OF_OUTPUT_ACTIVATE_ACTIVATE_ONLY_IN_TESTED_ZONES: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
            ]
            TYPE_OF_OUTPUT_ACTIVATE_ACTIVATE_IN_ALL_ZONES: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
            ]

        TYPE_OF_OUTPUT_ACTIVATE_UNSPECIFIED: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
        )
        TYPE_OF_OUTPUT_ACTIVATE_DO_NOT_ACTIVATE_OUTPUTS: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
        )
        TYPE_OF_OUTPUT_ACTIVATE_ACTIVATE_ONLY_IN_TESTED_ZONES: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
        )
        TYPE_OF_OUTPUT_ACTIVATE_ACTIVATE_IN_ALL_ZONES: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
        )
        class OutputDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OUTPUT_DEVICE_UNSPECIFIED: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
            ]
            OUTPUT_DEVICE_SOUNDERS: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
            ]
            OUTPUT_DEVICE_VADS: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
            ]
            OUTPUT_DEVICE_RELAYS: _ClassVar[
                HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
            ]

        OUTPUT_DEVICE_UNSPECIFIED: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
        )
        OUTPUT_DEVICE_SOUNDERS: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
        )
        OUTPUT_DEVICE_VADS: HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
        OUTPUT_DEVICE_RELAYS: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
        )
        TYPE_OF_OUTPUT_ACTIVATE_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_DEVICES_FIELD_NUMBER: _ClassVar[int]
        type_of_output_activate: (
            HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
        )
        output_devices: _containers.RepeatedScalarFieldContainer[
            HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice
        ]
        def __init__(
            self,
            type_of_output_activate: HubCommandFireZoneTestRequest.StartFireZoneTest.TypeOfOutputActivate
            | str
            | None = ...,
            output_devices: _Iterable[
                HubCommandFireZoneTestRequest.StartFireZoneTest.OutputDevice | str
            ]
            | None = ...,
        ) -> None: ...

    class AddFireZoneToTest(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class RemoveFireZoneFromTest(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIRE_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    ADD_FIRE_ZONE_TO_TEST_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIRE_ZONE_FROM_TEST_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    fire_zone_id: str
    start_fire_zone_test: HubCommandFireZoneTestRequest.StartFireZoneTest
    add_fire_zone_to_test: HubCommandFireZoneTestRequest.AddFireZoneToTest
    remove_fire_zone_from_test: HubCommandFireZoneTestRequest.RemoveFireZoneFromTest
    def __init__(
        self,
        hub_id: str | None = ...,
        fire_zone_id: str | None = ...,
        start_fire_zone_test: HubCommandFireZoneTestRequest.StartFireZoneTest
        | _Mapping
        | None = ...,
        add_fire_zone_to_test: HubCommandFireZoneTestRequest.AddFireZoneToTest
        | _Mapping
        | None = ...,
        remove_fire_zone_from_test: HubCommandFireZoneTestRequest.RemoveFireZoneFromTest
        | _Mapping
        | None = ...,
    ) -> None: ...
