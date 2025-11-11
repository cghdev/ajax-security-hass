from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayMemberPushPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_UNSPECIFIED: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_ALARM: _ClassVar[DisplayMemberPushPreference]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_MALFUNCTION: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_SECURITY: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_SYSTEM_EVENT: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_NON_SECURITY_ALERT: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_AUTOMATION: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_SMART_LOCK: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_MOTION: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_HUMAN: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_PET: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_VEHICLE: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_SCENARIO_EXECUTED: _ClassVar[
        DisplayMemberPushPreference
    ]
    DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_RING_BUTTON_PRESSED: _ClassVar[
        DisplayMemberPushPreference
    ]

class DisplayMemberSmsPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_UNSPECIFIED: _ClassVar[
        DisplayMemberSmsPreference
    ]
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_ALARM: _ClassVar[DisplayMemberSmsPreference]
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_MALFUNCTION: _ClassVar[
        DisplayMemberSmsPreference
    ]
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_SECURITY: _ClassVar[DisplayMemberSmsPreference]
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_SYSTEM_EVENT: _ClassVar[
        DisplayMemberSmsPreference
    ]
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_NON_SECURITY_ALERT: _ClassVar[
        DisplayMemberSmsPreference
    ]
    DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_AUTOMATION: _ClassVar[
        DisplayMemberSmsPreference
    ]

class DisplayMemberCallPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_CALL_PREFERENCE_UNSPECIFIED: _ClassVar[
        DisplayMemberCallPreference
    ]
    DISPLAY_SPACE_MEMBER_CALL_PREFERENCE_ALARM: _ClassVar[DisplayMemberCallPreference]

class DisplayMemberFolderPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_UNSPECIFIED: _ClassVar[
        DisplayMemberFolderPreference
    ]
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_ALARM: _ClassVar[
        DisplayMemberFolderPreference
    ]
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_MALFUNCTION: _ClassVar[
        DisplayMemberFolderPreference
    ]
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_USER_AUTOMATION: _ClassVar[
        DisplayMemberFolderPreference
    ]
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_HOME_AUTOMATION: _ClassVar[
        DisplayMemberFolderPreference
    ]
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_SYSTEM: _ClassVar[
        DisplayMemberFolderPreference
    ]
    DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_VIDEO: _ClassVar[
        DisplayMemberFolderPreference
    ]

DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_UNSPECIFIED: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_ALARM: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_MALFUNCTION: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_SECURITY: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_SYSTEM_EVENT: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_NON_SECURITY_ALERT: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_AUTOMATION: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_SMART_LOCK: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_MOTION: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_HUMAN: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_PET: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_VEHICLE: DisplayMemberPushPreference
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_SCENARIO_EXECUTED: (
    DisplayMemberPushPreference
)
DISPLAY_SPACE_MEMBER_PUSH_PREFERENCE_VIDEO_RING_BUTTON_PRESSED: (
    DisplayMemberPushPreference
)
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_UNSPECIFIED: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_ALARM: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_MALFUNCTION: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_SECURITY: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_SYSTEM_EVENT: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_NON_SECURITY_ALERT: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_SMS_PREFERENCE_AUTOMATION: DisplayMemberSmsPreference
DISPLAY_SPACE_MEMBER_CALL_PREFERENCE_UNSPECIFIED: DisplayMemberCallPreference
DISPLAY_SPACE_MEMBER_CALL_PREFERENCE_ALARM: DisplayMemberCallPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_UNSPECIFIED: DisplayMemberFolderPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_ALARM: DisplayMemberFolderPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_MALFUNCTION: DisplayMemberFolderPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_USER_AUTOMATION: DisplayMemberFolderPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_HOME_AUTOMATION: DisplayMemberFolderPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_SYSTEM: DisplayMemberFolderPreference
DISPLAY_SPACE_MEMBER_FOLDER_PREFERENCE_VIDEO: DisplayMemberFolderPreference

class DisplayMemberNotificationPreferences(_message.Message):
    __slots__ = (
        "folder_preferences",
        "member_call_preferences",
        "member_push_preferences",
        "member_push_preferences_v2",
        "member_sms_preferences",
    )
    MEMBER_PUSH_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SMS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CALL_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    MEMBER_PUSH_PREFERENCES_V2_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    member_push_preferences: DisplayMemberPushPreferences
    member_sms_preferences: DisplayMemberSmsPreferences
    member_call_preferences: DisplayMemberCallPreferences
    member_push_preferences_v2: DisplayMemberPushPreferencesV2
    folder_preferences: DisplayMemberFolderPreferences
    def __init__(
        self,
        member_push_preferences: DisplayMemberPushPreferences | _Mapping | None = ...,
        member_sms_preferences: DisplayMemberSmsPreferences | _Mapping | None = ...,
        member_call_preferences: DisplayMemberCallPreferences | _Mapping | None = ...,
        member_push_preferences_v2: DisplayMemberPushPreferencesV2
        | _Mapping
        | None = ...,
        folder_preferences: DisplayMemberFolderPreferences | _Mapping | None = ...,
    ) -> None: ...

class DisplayMemberPushPreferences(_message.Message):
    __slots__ = ("push_preferences",)
    PUSH_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    push_preferences: _containers.RepeatedScalarFieldContainer[
        DisplayMemberPushPreference
    ]
    def __init__(
        self,
        push_preferences: _Iterable[DisplayMemberPushPreference | str] | None = ...,
    ) -> None: ...

class DisplayMemberPushPreferencesV2(_message.Message):
    __slots__ = (
        "alarm",
        "automation",
        "doorbell_ringing",
        "malfunction",
        "non_security_alert",
        "security",
        "smart_lock",
        "system_event",
        "video",
    )
    class DoorbellRingingPushPreferenceState(
        int, metaclass=_enum_type_wrapper.EnumTypeWrapper
    ):
        __slots__ = ()
        DOORBELL_RINGING_PUSH_PREFERENCE_STATE_UNSPECIFIED: _ClassVar[
            DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
        ]
        DOORBELL_RINGING_PUSH_PREFERENCE_STATE_DISABLE: _ClassVar[
            DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
        ]
        DOORBELL_RINGING_PUSH_PREFERENCE_STATE_NORMAL: _ClassVar[
            DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
        ]
        DOORBELL_RINGING_PUSH_PREFERENCE_STATE_CRITICAL: _ClassVar[
            DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
        ]
        DOORBELL_RINGING_PUSH_PREFERENCE_STATE_PHONE_CALL: _ClassVar[
            DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
        ]

    DOORBELL_RINGING_PUSH_PREFERENCE_STATE_UNSPECIFIED: (
        DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
    )
    DOORBELL_RINGING_PUSH_PREFERENCE_STATE_DISABLE: (
        DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
    )
    DOORBELL_RINGING_PUSH_PREFERENCE_STATE_NORMAL: (
        DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
    )
    DOORBELL_RINGING_PUSH_PREFERENCE_STATE_CRITICAL: (
        DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
    )
    DOORBELL_RINGING_PUSH_PREFERENCE_STATE_PHONE_CALL: (
        DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
    )
    class PushPreferenceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUSH_PREFERENCE_STATE_UNSPECIFIED: _ClassVar[
            DisplayMemberPushPreferencesV2.PushPreferenceState
        ]
        PUSH_PREFERENCE_STATE_DISABLE: _ClassVar[
            DisplayMemberPushPreferencesV2.PushPreferenceState
        ]
        PUSH_PREFERENCE_STATE_NORMAL: _ClassVar[
            DisplayMemberPushPreferencesV2.PushPreferenceState
        ]
        PUSH_PREFERENCE_STATE_CRITICAL: _ClassVar[
            DisplayMemberPushPreferencesV2.PushPreferenceState
        ]

    PUSH_PREFERENCE_STATE_UNSPECIFIED: (
        DisplayMemberPushPreferencesV2.PushPreferenceState
    )
    PUSH_PREFERENCE_STATE_DISABLE: DisplayMemberPushPreferencesV2.PushPreferenceState
    PUSH_PREFERENCE_STATE_NORMAL: DisplayMemberPushPreferencesV2.PushPreferenceState
    PUSH_PREFERENCE_STATE_CRITICAL: DisplayMemberPushPreferencesV2.PushPreferenceState
    class Alarm(_message.Message):
        __slots__ = ("fire", "intrusion", "leakage", "panic", "video")
        class Intrusion(_message.Message):
            __slots__ = ("state",)
            STATE_FIELD_NUMBER: _ClassVar[int]
            state: DisplayMemberPushPreferencesV2.PushPreferenceState
            def __init__(
                self,
                state: DisplayMemberPushPreferencesV2.PushPreferenceState
                | str
                | None = ...,
            ) -> None: ...

        class Panic(_message.Message):
            __slots__ = ("state",)
            STATE_FIELD_NUMBER: _ClassVar[int]
            state: DisplayMemberPushPreferencesV2.PushPreferenceState
            def __init__(
                self,
                state: DisplayMemberPushPreferencesV2.PushPreferenceState
                | str
                | None = ...,
            ) -> None: ...

        class Fire(_message.Message):
            __slots__ = ("state",)
            STATE_FIELD_NUMBER: _ClassVar[int]
            state: DisplayMemberPushPreferencesV2.PushPreferenceState
            def __init__(
                self,
                state: DisplayMemberPushPreferencesV2.PushPreferenceState
                | str
                | None = ...,
            ) -> None: ...

        class Leakage(_message.Message):
            __slots__ = ("state",)
            STATE_FIELD_NUMBER: _ClassVar[int]
            state: DisplayMemberPushPreferencesV2.PushPreferenceState
            def __init__(
                self,
                state: DisplayMemberPushPreferencesV2.PushPreferenceState
                | str
                | None = ...,
            ) -> None: ...

        class Video(_message.Message):
            __slots__ = ("state",)
            STATE_FIELD_NUMBER: _ClassVar[int]
            state: DisplayMemberPushPreferencesV2.PushPreferenceState
            def __init__(
                self,
                state: DisplayMemberPushPreferencesV2.PushPreferenceState
                | str
                | None = ...,
            ) -> None: ...

        INTRUSION_FIELD_NUMBER: _ClassVar[int]
        PANIC_FIELD_NUMBER: _ClassVar[int]
        FIRE_FIELD_NUMBER: _ClassVar[int]
        LEAKAGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_FIELD_NUMBER: _ClassVar[int]
        intrusion: DisplayMemberPushPreferencesV2.Alarm.Intrusion
        panic: DisplayMemberPushPreferencesV2.Alarm.Panic
        fire: DisplayMemberPushPreferencesV2.Alarm.Fire
        leakage: DisplayMemberPushPreferencesV2.Alarm.Leakage
        video: DisplayMemberPushPreferencesV2.Alarm.Video
        def __init__(
            self,
            intrusion: DisplayMemberPushPreferencesV2.Alarm.Intrusion
            | _Mapping
            | None = ...,
            panic: DisplayMemberPushPreferencesV2.Alarm.Panic | _Mapping | None = ...,
            fire: DisplayMemberPushPreferencesV2.Alarm.Fire | _Mapping | None = ...,
            leakage: DisplayMemberPushPreferencesV2.Alarm.Leakage
            | _Mapping
            | None = ...,
            video: DisplayMemberPushPreferencesV2.Alarm.Video | _Mapping | None = ...,
        ) -> None: ...

    class Malfunction(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class Security(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class SystemEvent(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class NonSecurityAlert(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class Automation(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class SmartLock(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class DoorbellRinging(_message.Message):
        __slots__ = ("enabled", "state")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        state: DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
        def __init__(
            self,
            enabled: bool = ...,
            state: DisplayMemberPushPreferencesV2.DoorbellRingingPushPreferenceState
            | str
            | None = ...,
        ) -> None: ...

    class Video(_message.Message):
        __slots__ = ("human", "motion", "pet", "scenario_executed", "vehicle")
        class Motion(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...

        class Human(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...

        class Pet(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...

        class Vehicle(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...

        class ScenarioExecuted(_message.Message):
            __slots__ = ("enabled",)
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            enabled: bool
            def __init__(self, enabled: bool = ...) -> None: ...

        MOTION_FIELD_NUMBER: _ClassVar[int]
        HUMAN_FIELD_NUMBER: _ClassVar[int]
        PET_FIELD_NUMBER: _ClassVar[int]
        VEHICLE_FIELD_NUMBER: _ClassVar[int]
        SCENARIO_EXECUTED_FIELD_NUMBER: _ClassVar[int]
        motion: DisplayMemberPushPreferencesV2.Video.Motion
        human: DisplayMemberPushPreferencesV2.Video.Human
        pet: DisplayMemberPushPreferencesV2.Video.Pet
        vehicle: DisplayMemberPushPreferencesV2.Video.Vehicle
        scenario_executed: DisplayMemberPushPreferencesV2.Video.ScenarioExecuted
        def __init__(
            self,
            motion: DisplayMemberPushPreferencesV2.Video.Motion | _Mapping | None = ...,
            human: DisplayMemberPushPreferencesV2.Video.Human | _Mapping | None = ...,
            pet: DisplayMemberPushPreferencesV2.Video.Pet | _Mapping | None = ...,
            vehicle: DisplayMemberPushPreferencesV2.Video.Vehicle
            | _Mapping
            | None = ...,
            scenario_executed: DisplayMemberPushPreferencesV2.Video.ScenarioExecuted
            | _Mapping
            | None = ...,
        ) -> None: ...

    ALARM_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_EVENT_FIELD_NUMBER: _ClassVar[int]
    NON_SECURITY_ALERT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    DOORBELL_RINGING_FIELD_NUMBER: _ClassVar[int]
    alarm: DisplayMemberPushPreferencesV2.Alarm
    malfunction: DisplayMemberPushPreferencesV2.Malfunction
    security: DisplayMemberPushPreferencesV2.Security
    system_event: DisplayMemberPushPreferencesV2.SystemEvent
    non_security_alert: DisplayMemberPushPreferencesV2.NonSecurityAlert
    automation: DisplayMemberPushPreferencesV2.Automation
    smart_lock: DisplayMemberPushPreferencesV2.SmartLock
    video: DisplayMemberPushPreferencesV2.Video
    doorbell_ringing: DisplayMemberPushPreferencesV2.DoorbellRinging
    def __init__(
        self,
        alarm: DisplayMemberPushPreferencesV2.Alarm | _Mapping | None = ...,
        malfunction: DisplayMemberPushPreferencesV2.Malfunction | _Mapping | None = ...,
        security: DisplayMemberPushPreferencesV2.Security | _Mapping | None = ...,
        system_event: DisplayMemberPushPreferencesV2.SystemEvent
        | _Mapping
        | None = ...,
        non_security_alert: DisplayMemberPushPreferencesV2.NonSecurityAlert
        | _Mapping
        | None = ...,
        automation: DisplayMemberPushPreferencesV2.Automation | _Mapping | None = ...,
        smart_lock: DisplayMemberPushPreferencesV2.SmartLock | _Mapping | None = ...,
        video: DisplayMemberPushPreferencesV2.Video | _Mapping | None = ...,
        doorbell_ringing: DisplayMemberPushPreferencesV2.DoorbellRinging
        | _Mapping
        | None = ...,
    ) -> None: ...

class DisplayMemberSmsPreferences(_message.Message):
    __slots__ = ("sms_preferences",)
    SMS_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    sms_preferences: _containers.RepeatedScalarFieldContainer[
        DisplayMemberSmsPreference
    ]
    def __init__(
        self, sms_preferences: _Iterable[DisplayMemberSmsPreference | str] | None = ...
    ) -> None: ...

class DisplayMemberCallPreferences(_message.Message):
    __slots__ = ("call_preferences",)
    CALL_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    call_preferences: _containers.RepeatedScalarFieldContainer[
        DisplayMemberCallPreference
    ]
    def __init__(
        self,
        call_preferences: _Iterable[DisplayMemberCallPreference | str] | None = ...,
    ) -> None: ...

class DisplayMemberFolderPreferences(_message.Message):
    __slots__ = ("folder_preferences",)
    FOLDER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    folder_preferences: _containers.RepeatedScalarFieldContainer[
        DisplayMemberFolderPreference
    ]
    def __init__(
        self,
        folder_preferences: _Iterable[DisplayMemberFolderPreference | str] | None = ...,
    ) -> None: ...
