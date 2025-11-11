from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class DoorOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExtContactOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollerShutterAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollerShutterOffline(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShockDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TiltDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutomaticBypassByNumber(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutomaticBypassByRestoreTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutomaticBypassOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FirmwareUpdateInProgress(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Malfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ObjectAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperBypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TurnOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnregisteredDeviceEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArcFaultDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Button1On(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Button2On(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentHighDevice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentHighUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayCurrentOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayNotResponding(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByArming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByButton(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByDevice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByDisarming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOverheatingDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayVoltageHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayVoltageOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DataChannelCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetectedLeft(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetectedRight(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioUnsuccessfulWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemand(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandUnsuccessfulWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandWithName(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedLeft(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedRight(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoBySchedule(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScheduleUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CameraDirty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireAlarmMuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HighCoLevelDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HighCoLevelDetectedEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReserveBatteryLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeChamberTestNotPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeChamberTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeDetectedEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureHighEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureRiseDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureRiseDetectedEarlyWarning(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireProtectMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeatTestNotPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeatTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HighCcoLevelDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CoTestNotPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CoTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Co2High(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumidityHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumidityLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumidityOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemperatureOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Arm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmingIncomplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Disarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressNightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupArmAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupDuressDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOnAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NightModeOnWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PanicButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PasswordAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SecurityStateTransitionProgressUpdated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressAuthorization(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArmDuringUpgradeAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CellularSignalLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CmsConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DonorChosen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EthernetConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FactoryReset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldUpAlarmConfirmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IncorrectCms(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarmConfirmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrationStart(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServerConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrationOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrationFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TargetChosen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TurnOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WalkTestStart(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WiFiConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsNoiseHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SettingsChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessDeniedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessDeniedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccessRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChimeActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChimeActivatedInGroup(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentAccessGrantedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentAccessGrantedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoByScenarioOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemRestored(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemRestoreDenied(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemRestoreRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryAccessGrantedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryAccessGrantedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BridgeNotResponding(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CardDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CodeDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeactivatedCardAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetectorShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceMoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EthernetCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactLost(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactOk(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalPowerLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDetectorShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FrontTamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GasDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GlassBreakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldUpLongPress(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldUpShortPress(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JewellerNoiseHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MedicalAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MonitoringStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentAccessRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class S1Alarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class S3Alarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScenarioNotExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryAccessRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackTamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperBoardDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHigh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LineSabotage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FuseBreak(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TimezoneChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RingBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusConflict(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndOfLife(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DevFWUpgradeStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DevFWUpgradeFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DevFWUpgradeFinished(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusPowerDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnetimeFullBypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnetimeTamperBypassOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LifeQualityMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByButton(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByArming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByDisarming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByDevice(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveOpenedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UndefinedValvePosition(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChargerError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OverheatingDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadBlocked(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadUnblockedByTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeypadUnblockedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByArming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayUnableToSwitchByDisarming(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeyarmBlocked(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class KeyarmUnblockedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusesBreak(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusesConflict(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusesUnregistered(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReedSwitchBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccelerometerBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MagneticSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CalibrationRequired(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ActivationRRUCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeactivationRRUCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImproperKeyarmUsage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoScenarioTriggered(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeActivation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PeriodicTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExitError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecentClosing(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuitSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHighSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLowSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusPowerDisabledSingleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockViolation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SeismicAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TempSensorHighTemperature(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TempSensorLowTemperature(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocalExitError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AbortBurglary(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BurglaryCancel(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceSupervisionFailure(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfTestFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingDetectedMalfunction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SurveillanceScenarioExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeActivationFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnvacatedPremises(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PasswordReset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInAllowedDirection(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInForbiddenDirection(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInAllowedDirectionTimerStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedInAllowedDirectionTimerActive(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AllowedDirectionTimerEnded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoArchiveExportPrepared(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoArchiveExportFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExtSrcLowVoltage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JwlAntennaDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JwlAntennaConnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsAntennaDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsAntennaConnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmAntennaDisconnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmAntennaConnect(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JwlAntennaDamaged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WingsAntennaDamaged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GsmAntennaDamaged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSmokeDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CallbackRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallNoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallTimeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallMissed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallTimeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CallbackDenied(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarmConfirmedGeneral(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IntrusionAlarmConfirmedDetailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnverifiedAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartBracketOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PirSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MicrowaveSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IncorrectDeviceInstallation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MaskingSensorCalibrationFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukhoorEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukhoorDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BukhoorDisabledByTimeout(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SipConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartHomeMotionDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumanDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PetDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RingButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CaseBreakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelfTestDeviceDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SeismoSensorBroken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VorfChannelCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayShortCircuit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BoltSwitchContactOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BlockingElementOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveStuckPreventionNotExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValveStuckPreventionExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuitSingleOutput1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHighSingleOutput1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLowSingleOutput1(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShortCircuitSingleOutput2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageHighSingleOutput2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BusVoltageLowSingleOutput2(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LineConnectError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandForDetectionArea(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PhotoOnDemandForDetectionAreaUnsuccessful(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54FireAlarmReset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceDoesNotRespond(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SounderFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VADFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HeatDetectionFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmokeDetectionFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetectedDuringTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryTemperatureOutOfRange(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExitDelayComplete(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoArmAttempt(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GroupAutoDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoArmNotExecuted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoArmWithMalfunctions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoSelfTestPassed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoSelfTestFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoSelfTestError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54Silence(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54Resound(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TriggerGroupNotArmed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTestByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTestByCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmAnnunciationTestByCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WiFiModuleUpgradeStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WiFiModuleUpgradeFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HubModuleUpgradeFinished(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutPowerOverload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeWakeupSMS(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointDisabledByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointDisabledByCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EndpointDisabledByCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InCallTimeoutBSM(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutCallTimeoutBSM(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatterySavingModeWakeupByScheduled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutputFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54TamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54PowerLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54DeviceCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54FireAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54MedicalAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54PanicButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54GasDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54ExternalFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54LeakDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactHardFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FaultAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByAccessCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByAccessCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByTimer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByAccessCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByAccessCard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Evacuation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomAlarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AudioRecord(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOnByFailSafe(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayOffByFailSafe(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DelaysOverride(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SoftwareSystemFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MemorySystemFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArcReportingOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDelaysOn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDelaysOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireZoneTest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CmsDeliveryFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DayAlarmTemporaryBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressDayAlarmTemporaryBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DayAlarmBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DuressDayAlarmBypassActivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DayAlarmBypassNotRestored(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalContactResistanceFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmsToCmsDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlarmsToCmsEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FaultsToCmsDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FaultsToCmsEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DetectorVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FireDetectorVoltageLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ZoneTestSystemExit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CmsConnectionLost(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByKnob(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByCode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByTag(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByUser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByScenario(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByArm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByDisarm(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockUnlockedByKeyboard(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockModuleLockedAutomatically(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockDoorOpen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockDoorbellButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockKeyboardLocked(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModuleInsertedIntoDifferentLock(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialAddingError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialRemoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialRemovingError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockLockedWithConfirmation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialActivatedDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SmartLockCredentialActivationDeactivationError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54ExternalPowerLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EN54EthernetCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HubEventTag(_message.Message):
    __slots__ = (
        "CardDeactivated",
        "abort_burglary",
        "accelerometer_broken",
        "access_denied_to_company",
        "access_denied_to_pro",
        "access_request",
        "activation_rru_code",
        "alarm_annunciation_test",
        "alarm_annunciation_test_by_card",
        "alarm_annunciation_test_by_code",
        "alarm_annunciation_test_by_user",
        "alarms_to_cms_disabled",
        "alarms_to_cms_enabled",
        "allowed_direction_timer_ended",
        "arc_fault_detected",
        "arc_reporting_off",
        "arm",
        "arm_attempt",
        "arm_during_upgrade_attempt",
        "arm_with_malfunctions",
        "arming_incomplete",
        "audio_record",
        "auto_arm",
        "auto_arm_not_executed",
        "auto_arm_with_malfunctions",
        "auto_disarm",
        "auto_self_test_error",
        "auto_self_test_failed",
        "auto_self_test_passed",
        "automatic_bypass_by_number",
        "automatic_bypass_by_restore_timer",
        "automatic_bypass_off",
        "back_tamper_opened",
        "battery_disconnected",
        "battery_error",
        "battery_fault",
        "battery_low",
        "battery_saving_mode_activation",
        "battery_saving_mode_activation_failed",
        "battery_saving_mode_wakeup_by_scheduled",
        "battery_saving_mode_wakeup_sms",
        "battery_temperature_out_of_range",
        "blocking_element_opened",
        "bolt_switch_contact_opened",
        "bridge_not_responding",
        "bukhoor_disabled",
        "bukhoor_disabled_by_timeout",
        "bukhoor_enabled",
        "burglary_cancel",
        "bus_conflict",
        "bus_power_disabled",
        "bus_power_disabled_single_output",
        "bus_short_circuit",
        "bus_voltage_high",
        "bus_voltage_high_single_output",
        "bus_voltage_high_single_output1",
        "bus_voltage_high_single_output2",
        "bus_voltage_low",
        "bus_voltage_low_single_output",
        "bus_voltage_low_single_output1",
        "bus_voltage_low_single_output2",
        "buses_break",
        "buses_conflict",
        "buses_unregistered",
        "button_1_on",
        "button_2_on",
        "bypass_on",
        "calibration_required",
        "callback_denied",
        "callback_request",
        "camera_dirty",
        "car_detected",
        "case_break_detected",
        "cellular_signal_low",
        "charger_error",
        "chime_activated",
        "chime_activated_in_group",
        "cms_connection_loss",
        "cms_connection_lost",
        "cms_delivery_failed",
        "co_2_high",
        "co_test_not_passed",
        "co_test_passed",
        "code_deactivated",
        "csmoke_detected",
        "custom_alarm",
        "custom_event",
        "data_channel_communication_loss",
        "day_alarm_bypass_activated",
        "day_alarm_bypass_not_restored",
        "day_alarm_temporary_bypass_activated",
        "deactivated_card_attempt",
        "deactivation_rru_code",
        "delays_override",
        "detector_short_circuit",
        "detector_voltage_low",
        "dev_fw_upgrade_failed",
        "dev_fw_upgrade_finished",
        "dev_fw_upgrade_started",
        "device_communication_loss",
        "device_does_not_respond",
        "device_moved",
        "device_supervision_failure",
        "disarm",
        "donor_chosen",
        "door_opened",
        "duress_authorization",
        "duress_code",
        "duress_day_alarm_bypass_activated",
        "duress_day_alarm_temporary_bypass_activated",
        "duress_disarm",
        "duress_night_mode_off",
        "en54_device_communication_loss",
        "en54_ethernet_communication_loss",
        "en54_external_fault",
        "en54_external_power_loss",
        "en54_fire_alarm",
        "en54_fire_alarm_reset",
        "en54_gas_detected",
        "en54_leak_detected",
        "en54_medical_alarm",
        "en54_panic_button_pressed",
        "en54_power_low",
        "en54_resound",
        "en54_silence",
        "en54_tamper_opened",
        "end_of_life",
        "endpoint_disabled_by_card",
        "endpoint_disabled_by_code",
        "endpoint_disabled_by_user",
        "ethernet_communication_loss",
        "ethernet_connection_loss",
        "evacuation",
        "exit_delay_complete",
        "exit_error",
        "ext_contact_opened",
        "ext_src_low_voltage",
        "external_contact_hard_fault",
        "external_contact_lost",
        "external_contact_ok",
        "external_contact_resistance_fault",
        "external_contact_short_circuit",
        "external_malfunction",
        "external_power_loss",
        "factory_reset",
        "fault_alarm",
        "faults_to_cms_disabled",
        "faults_to_cms_enabled",
        "fire_alarm",
        "fire_alarm_muted",
        "fire_delays_off",
        "fire_delays_on",
        "fire_detector_short_circuit",
        "fire_detector_voltage_low",
        "fire_protect_malfunction",
        "fire_zone_test",
        "firmware_update_in_progress",
        "front_tamper_opened",
        "fuse_break",
        "gas_detected",
        "glass_break_detected",
        "group_arm",
        "group_arm_attempt",
        "group_arm_with_malfunctions",
        "group_auto_arm",
        "group_auto_arm_attempt",
        "group_auto_arm_with_malfunctions",
        "group_auto_disarm",
        "group_disarm",
        "group_duress_disarm",
        "gsm_antenna_connect",
        "gsm_antenna_damaged",
        "gsm_antenna_disconnect",
        "gsm_connection_loss",
        "heat_detection_fault",
        "heat_test_not_passed",
        "heat_test_passed",
        "high_cco_level_detected",
        "high_co_level_detected",
        "high_co_level_detected_early_warning",
        "hold_up_alarm_confirmed",
        "hold_up_long_press",
        "hold_up_short_press",
        "hub_module_upgrade_finished",
        "human_detected",
        "humidity_high",
        "humidity_low",
        "humidity_ok",
        "improper_keyarm_usage",
        "in_call",
        "in_call_error",
        "in_call_missed",
        "in_call_timeout",
        "in_call_timeout_bsm",
        "incorrect_cms",
        "incorrect_device_installation",
        "intrusion_alarm",
        "intrusion_alarm_confirmed",
        "intrusion_alarm_confirmed_detailed",
        "intrusion_alarm_confirmed_general",
        "jeweller_noise_high",
        "jwl_antenna_connect",
        "jwl_antenna_damaged",
        "jwl_antenna_disconnect",
        "keyarm_blocked",
        "keyarm_unblocked_by_user",
        "keypad_blocked",
        "keypad_unblocked_by_timer",
        "keypad_unblocked_by_user",
        "leak_detected",
        "life_quality_malfunction",
        "line_connect_error",
        "line_sabotage",
        "local_exit_error",
        "lock_violation",
        "magnetic_sensor_broken",
        "malfunction",
        "masking_detected",
        "masking_detected_left",
        "masking_detected_malfunction",
        "masking_detected_right",
        "masking_sensor_broken",
        "masking_sensor_calibration_failed",
        "medical_alarm",
        "memory_system_fault",
        "microwave_sensor_broken",
        "migration_failed",
        "migration_ok",
        "migration_start",
        "module_inserted_into_different_lock",
        "monitoring_started",
        "motion_detected",
        "motion_detected_during_test",
        "motion_detected_in_allowed_direction",
        "motion_detected_in_allowed_direction_timer_active",
        "motion_detected_in_allowed_direction_timer_started",
        "motion_detected_in_forbidden_direction",
        "motion_detected_left",
        "motion_detected_right",
        "night_mode_off",
        "night_mode_on",
        "night_mode_on_attempt",
        "night_mode_on_with_malfunctions",
        "object_added",
        "onetime_full_bypass_on",
        "onetime_tamper_bypass_on",
        "out_call",
        "out_call_error",
        "out_call_no_response",
        "out_call_timeout",
        "out_call_timeout_bsm",
        "out_power_overload",
        "output_fault",
        "overheating_detected",
        "panic_button_pressed",
        "password_attempt",
        "password_reset",
        "periodic_test",
        "permanent_access_granted_to_company",
        "permanent_access_granted_to_pro",
        "permanent_access_request",
        "pet_detected",
        "photo_by_scenario",
        "photo_by_scenario_on",
        "photo_by_scenario_unsuccessful",
        "photo_by_scenario_unsuccessful_with_name",
        "photo_by_scenario_with_name",
        "photo_by_schedule",
        "photo_by_schedule_unsuccessful",
        "photo_on_demand",
        "photo_on_demand_for_detection_area",
        "photo_on_demand_for_detection_area_unsuccessful",
        "photo_on_demand_on",
        "photo_on_demand_unsuccessful",
        "photo_on_demand_unsuccessful_with_name",
        "photo_on_demand_with_name",
        "pir_sensor_broken",
        "power_low",
        "recent_closing",
        "reed_switch_broken",
        "relay_current_high",
        "relay_current_high_device",
        "relay_current_high_user",
        "relay_current_low",
        "relay_current_ok",
        "relay_not_responding",
        "relay_off_by_access_card",
        "relay_off_by_access_code",
        "relay_off_by_fail_safe",
        "relay_off_by_user",
        "relay_off_bytimer",
        "relay_on",
        "relay_on_by_access_card",
        "relay_on_by_access_code",
        "relay_on_by_arming",
        "relay_on_by_button",
        "relay_on_by_device",
        "relay_on_by_disarming",
        "relay_on_by_fail_safe",
        "relay_on_by_scenario",
        "relay_on_by_timer",
        "relay_on_by_user",
        "relay_overheating_detected",
        "relay_short_circuit",
        "relay_unable_to_switch_by_arming",
        "relay_unable_to_switch_by_disarming",
        "relay_unable_to_switch_by_scenario",
        "relay_unable_to_switch_by_user",
        "relay_unable_to_switch_off",
        "relay_voltage_high",
        "relay_voltage_low",
        "relay_voltage_ok",
        "reserve_battery_low",
        "restore_request",
        "ring_broken",
        "ring_button_pressed",
        "roller_shutter_alarm",
        "roller_shutter_offline",
        "s_1_alarm",
        "s_3_alarm",
        "scenario_not_executed",
        "security_state_transition_progress_updated",
        "seismic_alarm",
        "seismo_sensor_broken",
        "self_test_device_disconnected",
        "self_test_failed",
        "self_test_passed",
        "server_connection_loss",
        "settings_changed",
        "shock_detected",
        "short_circuit",
        "short_circuit_single_output",
        "short_circuit_single_output1",
        "short_circuit_single_output2",
        "sip_connection_loss",
        "smart_bracket_opened",
        "smart_home_motion_detected",
        "smart_lock_credential_activated_deactivated",
        "smart_lock_credential_activation_deactivation_error",
        "smart_lock_credential_added",
        "smart_lock_credential_adding_error",
        "smart_lock_credential_removed",
        "smart_lock_credential_removing_error",
        "smart_lock_door_open",
        "smart_lock_doorbell_button_pressed",
        "smart_lock_keyboard_locked",
        "smart_lock_locked_with_confirmation",
        "smart_lock_module_locked_automatically",
        "smart_lock_unlocked_by_arm",
        "smart_lock_unlocked_by_code",
        "smart_lock_unlocked_by_disarm",
        "smart_lock_unlocked_by_keyboard",
        "smart_lock_unlocked_by_knob",
        "smart_lock_unlocked_by_scenario",
        "smart_lock_unlocked_by_tag",
        "smart_lock_unlocked_by_user",
        "smoke_chamber_test_not_passed",
        "smoke_chamber_test_passed",
        "smoke_detected",
        "smoke_detected_early_warning",
        "smoke_detection_fault",
        "software_system_fault",
        "sounder_fault",
        "surveillance_scenario_executed",
        "system_restore_denied",
        "system_restore_request",
        "system_restored",
        "tamper_board_disconnect",
        "tamper_bypass_on",
        "tamper_opened",
        "target_chosen",
        "temp_sensor_high_temperature",
        "temp_sensor_low_temperature",
        "temperature_high",
        "temperature_high_early_warning",
        "temperature_low",
        "temperature_ok",
        "temperature_rise_detected",
        "temperature_rise_detected_early_warning",
        "temporary_access_granted_to_company",
        "temporary_access_granted_to_pro",
        "temporary_access_request",
        "tilt_detected",
        "timezone_changed",
        "trigger_group_not_armed",
        "turn_off",
        "turn_on",
        "undefined_valve_position",
        "unregistered_device_event",
        "unvacated_premises",
        "unverified_alarm",
        "vad_fault",
        "valve_opened_by_arming",
        "valve_opened_by_button",
        "valve_opened_by_device",
        "valve_opened_by_disarming",
        "valve_opened_by_scenario",
        "valve_opened_by_user",
        "valve_stuck_prevention_executed",
        "valve_stuck_prevention_not_executed",
        "video_archive_export_failed",
        "video_archive_export_prepared",
        "video_scenario_triggered",
        "vorf_channel_communication_loss",
        "walk_test_start",
        "wi_fi_connection_loss",
        "wifi_module_upgrade_failed",
        "wifi_module_upgrade_started",
        "wings_antenna_connect",
        "wings_antenna_damaged",
        "wings_antenna_disconnect",
        "wings_noise_high",
        "zone_test_system_exit",
    )
    DOOR_OPENED_FIELD_NUMBER: _ClassVar[int]
    EXT_CONTACT_OPENED_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_ALARM_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    SHOCK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TILT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_BYPASS_BY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_BYPASS_BY_RESTORE_TIMER_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_BYPASS_OFF_FIELD_NUMBER: _ClassVar[int]
    POWER_LOW_FIELD_NUMBER: _ClassVar[int]
    BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_UPDATE_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ADDED_FIELD_NUMBER: _ClassVar[int]
    TAMPER_BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    TURN_OFF_FIELD_NUMBER: _ClassVar[int]
    UNREGISTERED_DEVICE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ARC_FAULT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    BUTTON_1_ON_FIELD_NUMBER: _ClassVar[int]
    BUTTON_2_ON_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_HIGH_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_HIGH_DEVICE_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_HIGH_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_LOW_FIELD_NUMBER: _ClassVar[int]
    RELAY_CURRENT_OK_FIELD_NUMBER: _ClassVar[int]
    RELAY_NOT_RESPONDING_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BYTIMER_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_ARMING_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_BUTTON_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_DEVICE_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_DISARMING_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_OVERHEATING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_OFF_FIELD_NUMBER: _ClassVar[int]
    RELAY_VOLTAGE_HIGH_FIELD_NUMBER: _ClassVar[int]
    RELAY_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    RELAY_VOLTAGE_OK_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_LEFT_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_UNSUCCESSFUL_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_LEFT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_RIGHT_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCHEDULE_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_DIRTY_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_MUTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_CO_LEVEL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_CO_LEVEL_DETECTED_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    RESERVE_BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    SMOKE_CHAMBER_TEST_NOT_PASSED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_CHAMBER_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTED_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_HIGH_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_HIGH_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_RISE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_RISE_DETECTED_EARLY_WARNING_FIELD_NUMBER: _ClassVar[int]
    FIRE_PROTECT_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    HEAT_TEST_NOT_PASSED_FIELD_NUMBER: _ClassVar[int]
    HEAT_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    HIGH_CCO_LEVEL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CO_TEST_NOT_PASSED_FIELD_NUMBER: _ClassVar[int]
    CO_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    CO_2_HIGH_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_HIGH_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_LOW_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_OK_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_LOW_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_OK_FIELD_NUMBER: _ClassVar[int]
    ARM_FIELD_NUMBER: _ClassVar[int]
    ARM_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ARMING_INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    DISARM_FIELD_NUMBER: _ClassVar[int]
    DURESS_DISARM_FIELD_NUMBER: _ClassVar[int]
    DURESS_NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARM_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARM_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_DISARM_FIELD_NUMBER: _ClassVar[int]
    GROUP_DURESS_DISARM_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_OFF_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ON_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ON_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ON_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    PANIC_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_STATE_TRANSITION_PROGRESS_UPDATED_FIELD_NUMBER: _ClassVar[int]
    DURESS_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    ARM_DURING_UPGRADE_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    BUS_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_SIGNAL_LOW_FIELD_NUMBER: _ClassVar[int]
    CMS_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    DONOR_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    FACTORY_RESET_FIELD_NUMBER: _ClassVar[int]
    GSM_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    HOLD_UP_ALARM_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    INCORRECT_CMS_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_START_FIELD_NUMBER: _ClassVar[int]
    SERVER_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_OK_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    TURN_ON_FIELD_NUMBER: _ClassVar[int]
    WALK_TEST_START_FIELD_NUMBER: _ClassVar[int]
    WI_FI_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    WINGS_NOISE_HIGH_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DENIED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_DENIED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CHIME_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CHIME_ACTIVATED_IN_GROUP_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_ACCESS_GRANTED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_ACCESS_GRANTED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_ON_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_ON_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTORED_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTORE_DENIED_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTORE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ACCESS_GRANTED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ACCESS_GRANTED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    BATTERY_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_NOT_RESPONDING_FIELD_NUMBER: _ClassVar[int]
    CARDDEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CODE_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EVENT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_CARD_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MOVED_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_LOST_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_OK_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_LOSS_FIELD_NUMBER: _ClassVar[int]
    FIRE_DETECTOR_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    FRONT_TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    GAS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HOLD_UP_LONG_PRESS_FIELD_NUMBER: _ClassVar[int]
    HOLD_UP_SHORT_PRESS_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_FIELD_NUMBER: _ClassVar[int]
    JEWELLER_NOISE_HIGH_FIELD_NUMBER: _ClassVar[int]
    LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    MEDICAL_ALARM_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STARTED_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    S_1_ALARM_FIELD_NUMBER: _ClassVar[int]
    S_3_ALARM_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_NOT_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ACCESS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LOW_FIELD_NUMBER: _ClassVar[int]
    BACK_TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    TAMPER_BOARD_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_FIELD_NUMBER: _ClassVar[int]
    LINE_SABOTAGE_FIELD_NUMBER: _ClassVar[int]
    FUSE_BREAK_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    RING_BROKEN_FIELD_NUMBER: _ClassVar[int]
    BUS_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    DEV_FW_UPGRADE_STARTED_FIELD_NUMBER: _ClassVar[int]
    DEV_FW_UPGRADE_FAILED_FIELD_NUMBER: _ClassVar[int]
    DEV_FW_UPGRADE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    BUS_POWER_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ONETIME_FULL_BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    ONETIME_TAMPER_BYPASS_ON_FIELD_NUMBER: _ClassVar[int]
    LIFE_QUALITY_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_BUTTON_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_ARMING_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_DISARMING_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VALVE_OPENED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    UNDEFINED_VALVE_POSITION_FIELD_NUMBER: _ClassVar[int]
    BATTERY_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESTORE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    CHARGER_ERROR_FIELD_NUMBER: _ClassVar[int]
    OVERHEATING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_UNBLOCKED_BY_TIMER_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_UNBLOCKED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_ARMING_FIELD_NUMBER: _ClassVar[int]
    RELAY_UNABLE_TO_SWITCH_BY_DISARMING_FIELD_NUMBER: _ClassVar[int]
    KEYARM_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    KEYARM_UNBLOCKED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    BUSES_BREAK_FIELD_NUMBER: _ClassVar[int]
    BUSES_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    BUSES_UNREGISTERED_FIELD_NUMBER: _ClassVar[int]
    REED_SWITCH_BROKEN_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMETER_BROKEN_FIELD_NUMBER: _ClassVar[int]
    MAGNETIC_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_RRU_CODE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATION_RRU_CODE_FIELD_NUMBER: _ClassVar[int]
    IMPROPER_KEYARM_USAGE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TEST_FIELD_NUMBER: _ClassVar[int]
    EXIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    RECENT_CLOSING_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    BUS_POWER_DISABLED_SINGLE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    LOCK_VIOLATION_FIELD_NUMBER: _ClassVar[int]
    DURESS_CODE_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_ALARM_FIELD_NUMBER: _ClassVar[int]
    TEMP_SENSOR_HIGH_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TEMP_SENSOR_LOW_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_EXIT_ERROR_FIELD_NUMBER: _ClassVar[int]
    ABORT_BURGLARY_FIELD_NUMBER: _ClassVar[int]
    BURGLARY_CANCEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SUPERVISION_FAILURE_FIELD_NUMBER: _ClassVar[int]
    SELF_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    SELF_TEST_FAILED_FIELD_NUMBER: _ClassVar[int]
    MASKING_DETECTED_MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    SURVEILLANCE_SCENARIO_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_ACTIVATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BY_SCENARIO_UNSUCCESSFUL_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    UNVACATED_PREMISES_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_ALLOWED_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_FORBIDDEN_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_ALLOWED_DIRECTION_TIMER_STARTED_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_IN_ALLOWED_DIRECTION_TIMER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DIRECTION_TIMER_ENDED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_EXPORT_PREPARED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ARCHIVE_EXPORT_FAILED_FIELD_NUMBER: _ClassVar[int]
    EXT_SRC_LOW_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    JWL_ANTENNA_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    JWL_ANTENNA_CONNECT_FIELD_NUMBER: _ClassVar[int]
    WINGS_ANTENNA_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    WINGS_ANTENNA_CONNECT_FIELD_NUMBER: _ClassVar[int]
    GSM_ANTENNA_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    GSM_ANTENNA_CONNECT_FIELD_NUMBER: _ClassVar[int]
    JWL_ANTENNA_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    WINGS_ANTENNA_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    GSM_ANTENNA_DAMAGED_FIELD_NUMBER: _ClassVar[int]
    CSMOKE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_ERROR_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_ERROR_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_NO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_MISSED_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_DENIED_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_CONFIRMED_GENERAL_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_ALARM_CONFIRMED_DETAILED_FIELD_NUMBER: _ClassVar[int]
    UNVERIFIED_ALARM_FIELD_NUMBER: _ClassVar[int]
    SMART_BRACKET_OPENED_FIELD_NUMBER: _ClassVar[int]
    PIR_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    MICROWAVE_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    INCORRECT_DEVICE_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_CALIBRATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_DISABLED_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_DISABLED_BY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SIP_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    SMART_HOME_MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HUMAN_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PET_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CAR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    CASE_BREAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    SELF_TEST_DEVICE_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    SEISMO_SENSOR_BROKEN_FIELD_NUMBER: _ClassVar[int]
    VORF_CHANNEL_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    RELAY_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    BOLT_SWITCH_CONTACT_OPENED_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_ELEMENT_OPENED_FIELD_NUMBER: _ClassVar[int]
    VALVE_STUCK_PREVENTION_NOT_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    VALVE_STUCK_PREVENTION_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_SINGLE_OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_SINGLE_OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_SINGLE_OUTPUT1_FIELD_NUMBER: _ClassVar[int]
    SHORT_CIRCUIT_SINGLE_OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_HIGH_SINGLE_OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    BUS_VOLTAGE_LOW_SINGLE_OUTPUT2_FIELD_NUMBER: _ClassVar[int]
    LINE_CONNECT_ERROR_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_FOR_DETECTION_AREA_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_FOR_DETECTION_AREA_UNSUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
    EN54_FIRE_ALARM_RESET_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DOES_NOT_RESPOND_FIELD_NUMBER: _ClassVar[int]
    SOUNDER_FAULT_FIELD_NUMBER: _ClassVar[int]
    VAD_FAULT_FIELD_NUMBER: _ClassVar[int]
    HEAT_DETECTION_FAULT_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTION_FAULT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_DURING_TEST_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMPERATURE_OUT_OF_RANGE_FIELD_NUMBER: _ClassVar[int]
    EXIT_DELAY_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_ARM_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    GROUP_AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_NOT_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_WITH_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELF_TEST_PASSED_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELF_TEST_FAILED_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELF_TEST_ERROR_FIELD_NUMBER: _ClassVar[int]
    EN54_SILENCE_FIELD_NUMBER: _ClassVar[int]
    EN54_RESOUND_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GROUP_NOT_ARMED_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_BY_USER_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_BY_CARD_FIELD_NUMBER: _ClassVar[int]
    ALARM_ANNUNCIATION_TEST_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    WIFI_MODULE_UPGRADE_STARTED_FIELD_NUMBER: _ClassVar[int]
    WIFI_MODULE_UPGRADE_FAILED_FIELD_NUMBER: _ClassVar[int]
    HUB_MODULE_UPGRADE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    OUT_POWER_OVERLOAD_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_WAKEUP_SMS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISABLED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISABLED_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISABLED_BY_CARD_FIELD_NUMBER: _ClassVar[int]
    IN_CALL_TIMEOUT_BSM_FIELD_NUMBER: _ClassVar[int]
    OUT_CALL_TIMEOUT_BSM_FIELD_NUMBER: _ClassVar[int]
    BATTERY_SAVING_MODE_WAKEUP_BY_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FAULT_FIELD_NUMBER: _ClassVar[int]
    EN54_TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    EN54_POWER_LOW_FIELD_NUMBER: _ClassVar[int]
    EN54_DEVICE_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    EN54_FIRE_ALARM_FIELD_NUMBER: _ClassVar[int]
    EN54_MEDICAL_ALARM_FIELD_NUMBER: _ClassVar[int]
    EN54_PANIC_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    EN54_GAS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    EN54_EXTERNAL_FAULT_FIELD_NUMBER: _ClassVar[int]
    EN54_LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_HARD_FAULT_FIELD_NUMBER: _ClassVar[int]
    FAULT_ALARM_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_ACCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_TIMER_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_USER_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_ACCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_ACCESS_CARD_FIELD_NUMBER: _ClassVar[int]
    EVACUATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ALARM_FIELD_NUMBER: _ClassVar[int]
    AUDIO_RECORD_FIELD_NUMBER: _ClassVar[int]
    RELAY_ON_BY_FAIL_SAFE_FIELD_NUMBER: _ClassVar[int]
    RELAY_OFF_BY_FAIL_SAFE_FIELD_NUMBER: _ClassVar[int]
    DELAYS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_SYSTEM_FAULT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SYSTEM_FAULT_FIELD_NUMBER: _ClassVar[int]
    ARC_REPORTING_OFF_FIELD_NUMBER: _ClassVar[int]
    FIRE_DELAYS_ON_FIELD_NUMBER: _ClassVar[int]
    FIRE_DELAYS_OFF_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FAULT_FIELD_NUMBER: _ClassVar[int]
    FIRE_ZONE_TEST_FIELD_NUMBER: _ClassVar[int]
    CMS_DELIVERY_FAILED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_TEMPORARY_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DURESS_DAY_ALARM_TEMPORARY_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DURESS_DAY_ALARM_BYPASS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    DAY_ALARM_BYPASS_NOT_RESTORED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_RESISTANCE_FAULT_FIELD_NUMBER: _ClassVar[int]
    ALARMS_TO_CMS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    ALARMS_TO_CMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FAULTS_TO_CMS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    FAULTS_TO_CMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    FIRE_DETECTOR_VOLTAGE_LOW_FIELD_NUMBER: _ClassVar[int]
    ZONE_TEST_SYSTEM_EXIT_FIELD_NUMBER: _ClassVar[int]
    CMS_CONNECTION_LOST_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_KNOB_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_CODE_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_TAG_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_SCENARIO_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_ARM_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_DISARM_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_UNLOCKED_BY_KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_MODULE_LOCKED_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_DOOR_OPEN_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_DOORBELL_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_KEYBOARD_LOCKED_FIELD_NUMBER: _ClassVar[int]
    MODULE_INSERTED_INTO_DIFFERENT_LOCK_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ADDED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ADDING_ERROR_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_REMOVED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_REMOVING_ERROR_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_LOCKED_WITH_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ACTIVATED_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_CREDENTIAL_ACTIVATION_DEACTIVATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    EN54_EXTERNAL_POWER_LOSS_FIELD_NUMBER: _ClassVar[int]
    EN54_ETHERNET_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    door_opened: DoorOpened
    ext_contact_opened: ExtContactOpened
    roller_shutter_alarm: RollerShutterAlarm
    roller_shutter_offline: RollerShutterOffline
    shock_detected: ShockDetected
    tilt_detected: TiltDetected
    automatic_bypass_by_number: AutomaticBypassByNumber
    automatic_bypass_by_restore_timer: AutomaticBypassByRestoreTimer
    automatic_bypass_off: AutomaticBypassOff
    power_low: PowerLow
    bypass_on: BypassOn
    device_communication_loss: DeviceCommunicationLoss
    firmware_update_in_progress: FirmwareUpdateInProgress
    malfunction: Malfunction
    object_added: ObjectAdded
    tamper_bypass_on: TamperBypassOn
    tamper_opened: TamperOpened
    turn_off: TurnOff
    unregistered_device_event: UnregisteredDeviceEvent
    arc_fault_detected: ArcFaultDetected
    button_1_on: Button1On
    button_2_on: Button2On
    relay_current_high: RelayCurrentHigh
    relay_current_high_device: RelayCurrentHighDevice
    relay_current_high_user: RelayCurrentHighUser
    relay_current_low: RelayCurrentLow
    relay_current_ok: RelayCurrentOk
    relay_not_responding: RelayNotResponding
    relay_off_bytimer: RelayOffByTimer
    relay_on: RelayOn
    relay_on_by_arming: RelayOnByArming
    relay_on_by_button: RelayOnByButton
    relay_on_by_device: RelayOnByDevice
    relay_on_by_disarming: RelayOnByDisarming
    relay_on_by_scenario: RelayOnByScenario
    relay_on_by_user: RelayOnByUser
    relay_overheating_detected: RelayOverheatingDetected
    relay_unable_to_switch_off: RelayUnableToSwitchOff
    relay_voltage_high: RelayVoltageHigh
    relay_voltage_low: RelayVoltageLow
    relay_voltage_ok: RelayVoltageOk
    data_channel_communication_loss: DataChannelCommunicationLoss
    masking_detected: MaskingDetected
    masking_detected_left: MaskingDetectedLeft
    masking_detected_right: MaskingDetectedRight
    motion_detected: MotionDetected
    photo_by_scenario: PhotoByScenario
    photo_by_scenario_unsuccessful: PhotoByScenarioUnsuccessful
    photo_on_demand: PhotoOnDemand
    photo_on_demand_unsuccessful: PhotoOnDemandUnsuccessful
    photo_on_demand_unsuccessful_with_name: PhotoOnDemandUnsuccessfulWithName
    photo_on_demand_with_name: PhotoOnDemandWithName
    motion_detected_left: MotionDetectedLeft
    motion_detected_right: MotionDetectedRight
    photo_by_schedule: PhotoBySchedule
    photo_by_schedule_unsuccessful: PhotoByScheduleUnsuccessful
    camera_dirty: CameraDirty
    fire_alarm: FireAlarm
    fire_alarm_muted: FireAlarmMuted
    high_co_level_detected: HighCoLevelDetected
    high_co_level_detected_early_warning: HighCoLevelDetectedEarlyWarning
    reserve_battery_low: ReserveBatteryLow
    smoke_chamber_test_not_passed: SmokeChamberTestNotPassed
    smoke_chamber_test_passed: SmokeChamberTestPassed
    smoke_detected: SmokeDetected
    smoke_detected_early_warning: SmokeDetectedEarlyWarning
    temperature_high: TemperatureHigh
    temperature_high_early_warning: TemperatureHighEarlyWarning
    temperature_rise_detected: TemperatureRiseDetected
    temperature_rise_detected_early_warning: TemperatureRiseDetectedEarlyWarning
    fire_protect_malfunction: FireProtectMalfunction
    heat_test_not_passed: HeatTestNotPassed
    heat_test_passed: HeatTestPassed
    high_cco_level_detected: HighCcoLevelDetected
    co_test_not_passed: CoTestNotPassed
    co_test_passed: CoTestPassed
    co_2_high: Co2High
    humidity_high: HumidityHigh
    humidity_low: HumidityLow
    humidity_ok: HumidityOk
    temperature_low: TemperatureLow
    temperature_ok: TemperatureOk
    arm: Arm
    arm_attempt: ArmAttempt
    arming_incomplete: ArmingIncomplete
    arm_with_malfunctions: ArmWithMalfunctions
    disarm: Disarm
    duress_disarm: DuressDisarm
    duress_night_mode_off: DuressNightModeOff
    group_arm: GroupArm
    group_arm_attempt: GroupArmAttempt
    group_arm_with_malfunctions: GroupArmWithMalfunctions
    group_disarm: GroupDisarm
    group_duress_disarm: GroupDuressDisarm
    night_mode_off: NightModeOff
    night_mode_on: NightModeOn
    night_mode_on_attempt: NightModeOnAttempt
    night_mode_on_with_malfunctions: NightModeOnWithMalfunctions
    panic_button_pressed: PanicButtonPressed
    password_attempt: PasswordAttempt
    security_state_transition_progress_updated: SecurityStateTransitionProgressUpdated
    duress_authorization: DuressAuthorization
    arm_during_upgrade_attempt: ArmDuringUpgradeAttempt
    bus_short_circuit: BusShortCircuit
    cellular_signal_low: CellularSignalLow
    cms_connection_loss: CmsConnectionLoss
    donor_chosen: DonorChosen
    ethernet_connection_loss: EthernetConnectionLoss
    factory_reset: FactoryReset
    gsm_connection_loss: GsmConnectionLoss
    hold_up_alarm_confirmed: HoldUpAlarmConfirmed
    incorrect_cms: IncorrectCms
    intrusion_alarm_confirmed: IntrusionAlarmConfirmed
    migration_start: MigrationStart
    server_connection_loss: ServerConnectionLoss
    migration_ok: MigrationOk
    migration_failed: MigrationFailed
    target_chosen: TargetChosen
    turn_on: TurnOn
    walk_test_start: WalkTestStart
    wi_fi_connection_loss: WiFiConnectionLoss
    wings_noise_high: WingsNoiseHigh
    settings_changed: SettingsChanged
    access_denied_to_company: AccessDeniedToCompany
    access_denied_to_pro: AccessDeniedToPro
    access_request: AccessRequest
    chime_activated: ChimeActivated
    chime_activated_in_group: ChimeActivatedInGroup
    permanent_access_granted_to_company: PermanentAccessGrantedToCompany
    permanent_access_granted_to_pro: PermanentAccessGrantedToPro
    photo_by_scenario_on: PhotoByScenarioOn
    photo_on_demand_on: PhotoOnDemandOn
    system_restored: SystemRestored
    system_restore_denied: SystemRestoreDenied
    system_restore_request: SystemRestoreRequest
    temporary_access_granted_to_company: TemporaryAccessGrantedToCompany
    temporary_access_granted_to_pro: TemporaryAccessGrantedToPro
    battery_disconnected: BatteryDisconnected
    bridge_not_responding: BridgeNotResponding
    CardDeactivated: CardDeactivated
    code_deactivated: CodeDeactivated
    custom_event: CustomEvent
    deactivated_card_attempt: DeactivatedCardAttempt
    detector_short_circuit: DetectorShortCircuit
    device_moved: DeviceMoved
    ethernet_communication_loss: EthernetCommunicationLoss
    external_contact_lost: ExternalContactLost
    external_contact_ok: ExternalContactOk
    external_contact_short_circuit: ExternalContactShortCircuit
    external_malfunction: ExternalMalfunction
    external_power_loss: ExternalPowerLoss
    fire_detector_short_circuit: FireDetectorShortCircuit
    front_tamper_opened: FrontTamperOpened
    gas_detected: GasDetected
    glass_break_detected: GlassBreakDetected
    hold_up_long_press: HoldUpLongPress
    hold_up_short_press: HoldUpShortPress
    intrusion_alarm: IntrusionAlarm
    jeweller_noise_high: JewellerNoiseHigh
    leak_detected: LeakDetected
    medical_alarm: MedicalAlarm
    monitoring_started: MonitoringStarted
    permanent_access_request: PermanentAccessRequest
    s_1_alarm: S1Alarm
    s_3_alarm: S3Alarm
    scenario_not_executed: ScenarioNotExecuted
    temporary_access_request: TemporaryAccessRequest
    battery_low: BatteryLow
    back_tamper_opened: BackTamperOpened
    short_circuit: ShortCircuit
    tamper_board_disconnect: TamperBoardDisconnect
    bus_voltage_high: BusVoltageHigh
    line_sabotage: LineSabotage
    fuse_break: FuseBreak
    timezone_changed: TimezoneChanged
    ring_broken: RingBroken
    bus_conflict: BusConflict
    end_of_life: EndOfLife
    dev_fw_upgrade_started: DevFWUpgradeStarted
    dev_fw_upgrade_failed: DevFWUpgradeFailed
    dev_fw_upgrade_finished: DevFWUpgradeFinished
    bus_power_disabled: BusPowerDisabled
    onetime_full_bypass_on: OnetimeFullBypassOn
    onetime_tamper_bypass_on: OnetimeTamperBypassOn
    life_quality_malfunction: LifeQualityMalfunction
    valve_opened_by_button: ValveOpenedByButton
    valve_opened_by_scenario: ValveOpenedByScenario
    valve_opened_by_arming: ValveOpenedByArming
    valve_opened_by_disarming: ValveOpenedByDisarming
    valve_opened_by_device: ValveOpenedByDevice
    valve_opened_by_user: ValveOpenedByUser
    undefined_valve_position: UndefinedValvePosition
    battery_error: BatteryError
    restore_request: RestoreRequest
    bus_voltage_low: BusVoltageLow
    charger_error: ChargerError
    overheating_detected: OverheatingDetected
    keypad_blocked: KeypadBlocked
    keypad_unblocked_by_timer: KeypadUnblockedByTimer
    keypad_unblocked_by_user: KeypadUnblockedByUser
    relay_unable_to_switch_by_user: RelayUnableToSwitchByUser
    relay_unable_to_switch_by_scenario: RelayUnableToSwitchByScenario
    relay_unable_to_switch_by_arming: RelayUnableToSwitchByArming
    relay_unable_to_switch_by_disarming: RelayUnableToSwitchByDisarming
    keyarm_blocked: KeyarmBlocked
    keyarm_unblocked_by_user: KeyarmUnblockedByUser
    buses_break: BusesBreak
    buses_conflict: BusesConflict
    buses_unregistered: BusesUnregistered
    reed_switch_broken: ReedSwitchBroken
    accelerometer_broken: AccelerometerBroken
    magnetic_sensor_broken: MagneticSensorBroken
    calibration_required: CalibrationRequired
    activation_rru_code: ActivationRRUCode
    deactivation_rru_code: DeactivationRRUCode
    improper_keyarm_usage: ImproperKeyarmUsage
    video_scenario_triggered: VideoScenarioTriggered
    battery_saving_mode_activation: BatterySavingModeActivation
    periodic_test: PeriodicTest
    exit_error: ExitError
    recent_closing: RecentClosing
    short_circuit_single_output: ShortCircuitSingleOutput
    bus_voltage_high_single_output: BusVoltageHighSingleOutput
    bus_voltage_low_single_output: BusVoltageLowSingleOutput
    bus_power_disabled_single_output: BusPowerDisabledSingleOutput
    lock_violation: LockViolation
    duress_code: DuressCode
    seismic_alarm: SeismicAlarm
    temp_sensor_high_temperature: TempSensorHighTemperature
    temp_sensor_low_temperature: TempSensorLowTemperature
    local_exit_error: LocalExitError
    abort_burglary: AbortBurglary
    burglary_cancel: BurglaryCancel
    device_supervision_failure: DeviceSupervisionFailure
    self_test_passed: SelfTestPassed
    self_test_failed: SelfTestFailed
    masking_detected_malfunction: MaskingDetectedMalfunction
    surveillance_scenario_executed: SurveillanceScenarioExecuted
    battery_saving_mode_activation_failed: BatterySavingModeActivationFailed
    photo_by_scenario_with_name: PhotoByScenarioWithName
    photo_by_scenario_unsuccessful_with_name: PhotoByScenarioUnsuccessfulWithName
    unvacated_premises: UnvacatedPremises
    password_reset: PasswordReset
    motion_detected_in_allowed_direction: MotionDetectedInAllowedDirection
    motion_detected_in_forbidden_direction: MotionDetectedInForbiddenDirection
    motion_detected_in_allowed_direction_timer_started: (
        MotionDetectedInAllowedDirectionTimerStarted
    )
    motion_detected_in_allowed_direction_timer_active: (
        MotionDetectedInAllowedDirectionTimerActive
    )
    allowed_direction_timer_ended: AllowedDirectionTimerEnded
    video_archive_export_prepared: VideoArchiveExportPrepared
    video_archive_export_failed: VideoArchiveExportFailed
    ext_src_low_voltage: ExtSrcLowVoltage
    jwl_antenna_disconnect: JwlAntennaDisconnect
    jwl_antenna_connect: JwlAntennaConnect
    wings_antenna_disconnect: WingsAntennaDisconnect
    wings_antenna_connect: WingsAntennaConnect
    gsm_antenna_disconnect: GsmAntennaDisconnect
    gsm_antenna_connect: GsmAntennaConnect
    jwl_antenna_damaged: JwlAntennaDamaged
    wings_antenna_damaged: WingsAntennaDamaged
    gsm_antenna_damaged: GsmAntennaDamaged
    csmoke_detected: CSmokeDetected
    in_call: InCall
    out_call: OutCall
    in_call_error: InCallError
    out_call_error: OutCallError
    callback_request: CallbackRequest
    out_call_no_response: OutCallNoResponse
    out_call_timeout: OutCallTimeout
    in_call_missed: InCallMissed
    in_call_timeout: InCallTimeout
    callback_denied: CallbackDenied
    intrusion_alarm_confirmed_general: IntrusionAlarmConfirmedGeneral
    intrusion_alarm_confirmed_detailed: IntrusionAlarmConfirmedDetailed
    unverified_alarm: UnverifiedAlarm
    smart_bracket_opened: SmartBracketOpened
    pir_sensor_broken: PirSensorBroken
    microwave_sensor_broken: MicrowaveSensorBroken
    incorrect_device_installation: IncorrectDeviceInstallation
    masking_sensor_broken: MaskingSensorBroken
    masking_sensor_calibration_failed: MaskingSensorCalibrationFailed
    bukhoor_enabled: BukhoorEnabled
    bukhoor_disabled: BukhoorDisabled
    bukhoor_disabled_by_timeout: BukhoorDisabledByTimeout
    sip_connection_loss: SipConnectionLoss
    smart_home_motion_detected: SmartHomeMotionDetected
    human_detected: HumanDetected
    pet_detected: PetDetected
    car_detected: CarDetected
    ring_button_pressed: RingButtonPressed
    case_break_detected: CaseBreakDetected
    self_test_device_disconnected: SelfTestDeviceDisconnected
    seismo_sensor_broken: SeismoSensorBroken
    vorf_channel_communication_loss: VorfChannelCommunicationLoss
    relay_short_circuit: RelayShortCircuit
    bolt_switch_contact_opened: BoltSwitchContactOpened
    blocking_element_opened: BlockingElementOpened
    valve_stuck_prevention_not_executed: ValveStuckPreventionNotExecuted
    valve_stuck_prevention_executed: ValveStuckPreventionExecuted
    short_circuit_single_output1: ShortCircuitSingleOutput1
    bus_voltage_high_single_output1: BusVoltageHighSingleOutput1
    bus_voltage_low_single_output1: BusVoltageLowSingleOutput1
    short_circuit_single_output2: ShortCircuitSingleOutput2
    bus_voltage_high_single_output2: BusVoltageHighSingleOutput2
    bus_voltage_low_single_output2: BusVoltageLowSingleOutput2
    line_connect_error: LineConnectError
    photo_on_demand_for_detection_area: PhotoOnDemandForDetectionArea
    photo_on_demand_for_detection_area_unsuccessful: (
        PhotoOnDemandForDetectionAreaUnsuccessful
    )
    en54_fire_alarm_reset: EN54FireAlarmReset
    device_does_not_respond: DeviceDoesNotRespond
    sounder_fault: SounderFault
    vad_fault: VADFault
    heat_detection_fault: HeatDetectionFault
    smoke_detection_fault: SmokeDetectionFault
    motion_detected_during_test: MotionDetectedDuringTest
    alarm_annunciation_test: AlarmAnnunciationTest
    battery_temperature_out_of_range: BatteryTemperatureOutOfRange
    exit_delay_complete: ExitDelayComplete
    group_auto_arm: GroupAutoArm
    group_auto_arm_with_malfunctions: GroupAutoArmWithMalfunctions
    group_auto_arm_attempt: GroupAutoArmAttempt
    group_auto_disarm: GroupAutoDisarm
    auto_arm_not_executed: AutoArmNotExecuted
    auto_arm: AutoArm
    auto_arm_with_malfunctions: AutoArmWithMalfunctions
    auto_disarm: AutoDisarm
    auto_self_test_passed: AutoSelfTestPassed
    auto_self_test_failed: AutoSelfTestFailed
    auto_self_test_error: AutoSelfTestError
    en54_silence: EN54Silence
    en54_resound: EN54Resound
    trigger_group_not_armed: TriggerGroupNotArmed
    alarm_annunciation_test_by_user: AlarmAnnunciationTestByUser
    alarm_annunciation_test_by_card: AlarmAnnunciationTestByCard
    alarm_annunciation_test_by_code: AlarmAnnunciationTestByCode
    wifi_module_upgrade_started: WiFiModuleUpgradeStarted
    wifi_module_upgrade_failed: WiFiModuleUpgradeFailed
    hub_module_upgrade_finished: HubModuleUpgradeFinished
    out_power_overload: OutPowerOverload
    battery_saving_mode_wakeup_sms: BatterySavingModeWakeupSMS
    endpoint_disabled_by_user: EndpointDisabledByUser
    endpoint_disabled_by_code: EndpointDisabledByCode
    endpoint_disabled_by_card: EndpointDisabledByCard
    in_call_timeout_bsm: InCallTimeoutBSM
    out_call_timeout_bsm: OutCallTimeoutBSM
    battery_saving_mode_wakeup_by_scheduled: BatterySavingModeWakeupByScheduled
    output_fault: OutputFault
    en54_tamper_opened: EN54TamperOpened
    en54_power_low: EN54PowerLow
    en54_device_communication_loss: EN54DeviceCommunicationLoss
    en54_fire_alarm: EN54FireAlarm
    en54_medical_alarm: EN54MedicalAlarm
    en54_panic_button_pressed: EN54PanicButtonPressed
    en54_gas_detected: EN54GasDetected
    en54_external_fault: EN54ExternalFault
    en54_leak_detected: EN54LeakDetected
    external_contact_hard_fault: ExternalContactHardFault
    fault_alarm: FaultAlarm
    relay_on_by_access_code: RelayOnByAccessCode
    relay_on_by_access_card: RelayOnByAccessCard
    relay_on_by_timer: RelayOnByTimer
    relay_off_by_user: RelayOffByUser
    relay_off_by_access_code: RelayOffByAccessCode
    relay_off_by_access_card: RelayOffByAccessCard
    evacuation: Evacuation
    custom_alarm: CustomAlarm
    audio_record: AudioRecord
    relay_on_by_fail_safe: RelayOnByFailSafe
    relay_off_by_fail_safe: RelayOffByFailSafe
    delays_override: DelaysOverride
    software_system_fault: SoftwareSystemFault
    memory_system_fault: MemorySystemFault
    arc_reporting_off: ArcReportingOff
    fire_delays_on: FireDelaysOn
    fire_delays_off: FireDelaysOff
    battery_fault: BatteryFault
    fire_zone_test: FireZoneTest
    cms_delivery_failed: CmsDeliveryFailed
    day_alarm_temporary_bypass_activated: DayAlarmTemporaryBypassActivated
    duress_day_alarm_temporary_bypass_activated: DuressDayAlarmTemporaryBypassActivated
    day_alarm_bypass_activated: DayAlarmBypassActivated
    duress_day_alarm_bypass_activated: DuressDayAlarmBypassActivated
    day_alarm_bypass_not_restored: DayAlarmBypassNotRestored
    external_contact_resistance_fault: ExternalContactResistanceFault
    alarms_to_cms_disabled: AlarmsToCmsDisabled
    alarms_to_cms_enabled: AlarmsToCmsEnabled
    faults_to_cms_disabled: FaultsToCmsDisabled
    faults_to_cms_enabled: FaultsToCmsEnabled
    detector_voltage_low: DetectorVoltageLow
    fire_detector_voltage_low: FireDetectorVoltageLow
    zone_test_system_exit: ZoneTestSystemExit
    cms_connection_lost: CmsConnectionLost
    smart_lock_unlocked_by_knob: SmartLockUnlockedByKnob
    smart_lock_unlocked_by_code: SmartLockUnlockedByCode
    smart_lock_unlocked_by_tag: SmartLockUnlockedByTag
    smart_lock_unlocked_by_user: SmartLockUnlockedByUser
    smart_lock_unlocked_by_scenario: SmartLockUnlockedByScenario
    smart_lock_unlocked_by_arm: SmartLockUnlockedByArm
    smart_lock_unlocked_by_disarm: SmartLockUnlockedByDisarm
    smart_lock_unlocked_by_keyboard: SmartLockUnlockedByKeyboard
    smart_lock_module_locked_automatically: SmartLockModuleLockedAutomatically
    smart_lock_door_open: SmartLockDoorOpen
    smart_lock_doorbell_button_pressed: SmartLockDoorbellButtonPressed
    smart_lock_keyboard_locked: SmartLockKeyboardLocked
    module_inserted_into_different_lock: ModuleInsertedIntoDifferentLock
    smart_lock_credential_added: SmartLockCredentialAdded
    smart_lock_credential_adding_error: SmartLockCredentialAddingError
    smart_lock_credential_removed: SmartLockCredentialRemoved
    smart_lock_credential_removing_error: SmartLockCredentialRemovingError
    smart_lock_locked_with_confirmation: SmartLockLockedWithConfirmation
    smart_lock_credential_activated_deactivated: SmartLockCredentialActivatedDeactivated
    smart_lock_credential_activation_deactivation_error: (
        SmartLockCredentialActivationDeactivationError
    )
    en54_external_power_loss: EN54ExternalPowerLoss
    en54_ethernet_communication_loss: EN54EthernetCommunicationLoss
    def __init__(
        self,
        door_opened: DoorOpened | _Mapping | None = ...,
        ext_contact_opened: ExtContactOpened | _Mapping | None = ...,
        roller_shutter_alarm: RollerShutterAlarm | _Mapping | None = ...,
        roller_shutter_offline: RollerShutterOffline | _Mapping | None = ...,
        shock_detected: ShockDetected | _Mapping | None = ...,
        tilt_detected: TiltDetected | _Mapping | None = ...,
        automatic_bypass_by_number: AutomaticBypassByNumber | _Mapping | None = ...,
        automatic_bypass_by_restore_timer: AutomaticBypassByRestoreTimer
        | _Mapping
        | None = ...,
        automatic_bypass_off: AutomaticBypassOff | _Mapping | None = ...,
        power_low: PowerLow | _Mapping | None = ...,
        bypass_on: BypassOn | _Mapping | None = ...,
        device_communication_loss: DeviceCommunicationLoss | _Mapping | None = ...,
        firmware_update_in_progress: FirmwareUpdateInProgress | _Mapping | None = ...,
        malfunction: Malfunction | _Mapping | None = ...,
        object_added: ObjectAdded | _Mapping | None = ...,
        tamper_bypass_on: TamperBypassOn | _Mapping | None = ...,
        tamper_opened: TamperOpened | _Mapping | None = ...,
        turn_off: TurnOff | _Mapping | None = ...,
        unregistered_device_event: UnregisteredDeviceEvent | _Mapping | None = ...,
        arc_fault_detected: ArcFaultDetected | _Mapping | None = ...,
        button_1_on: Button1On | _Mapping | None = ...,
        button_2_on: Button2On | _Mapping | None = ...,
        relay_current_high: RelayCurrentHigh | _Mapping | None = ...,
        relay_current_high_device: RelayCurrentHighDevice | _Mapping | None = ...,
        relay_current_high_user: RelayCurrentHighUser | _Mapping | None = ...,
        relay_current_low: RelayCurrentLow | _Mapping | None = ...,
        relay_current_ok: RelayCurrentOk | _Mapping | None = ...,
        relay_not_responding: RelayNotResponding | _Mapping | None = ...,
        relay_off_bytimer: RelayOffByTimer | _Mapping | None = ...,
        relay_on: RelayOn | _Mapping | None = ...,
        relay_on_by_arming: RelayOnByArming | _Mapping | None = ...,
        relay_on_by_button: RelayOnByButton | _Mapping | None = ...,
        relay_on_by_device: RelayOnByDevice | _Mapping | None = ...,
        relay_on_by_disarming: RelayOnByDisarming | _Mapping | None = ...,
        relay_on_by_scenario: RelayOnByScenario | _Mapping | None = ...,
        relay_on_by_user: RelayOnByUser | _Mapping | None = ...,
        relay_overheating_detected: RelayOverheatingDetected | _Mapping | None = ...,
        relay_unable_to_switch_off: RelayUnableToSwitchOff | _Mapping | None = ...,
        relay_voltage_high: RelayVoltageHigh | _Mapping | None = ...,
        relay_voltage_low: RelayVoltageLow | _Mapping | None = ...,
        relay_voltage_ok: RelayVoltageOk | _Mapping | None = ...,
        data_channel_communication_loss: DataChannelCommunicationLoss
        | _Mapping
        | None = ...,
        masking_detected: MaskingDetected | _Mapping | None = ...,
        masking_detected_left: MaskingDetectedLeft | _Mapping | None = ...,
        masking_detected_right: MaskingDetectedRight | _Mapping | None = ...,
        motion_detected: MotionDetected | _Mapping | None = ...,
        photo_by_scenario: PhotoByScenario | _Mapping | None = ...,
        photo_by_scenario_unsuccessful: PhotoByScenarioUnsuccessful
        | _Mapping
        | None = ...,
        photo_on_demand: PhotoOnDemand | _Mapping | None = ...,
        photo_on_demand_unsuccessful: PhotoOnDemandUnsuccessful | _Mapping | None = ...,
        photo_on_demand_unsuccessful_with_name: PhotoOnDemandUnsuccessfulWithName
        | _Mapping
        | None = ...,
        photo_on_demand_with_name: PhotoOnDemandWithName | _Mapping | None = ...,
        motion_detected_left: MotionDetectedLeft | _Mapping | None = ...,
        motion_detected_right: MotionDetectedRight | _Mapping | None = ...,
        photo_by_schedule: PhotoBySchedule | _Mapping | None = ...,
        photo_by_schedule_unsuccessful: PhotoByScheduleUnsuccessful
        | _Mapping
        | None = ...,
        camera_dirty: CameraDirty | _Mapping | None = ...,
        fire_alarm: FireAlarm | _Mapping | None = ...,
        fire_alarm_muted: FireAlarmMuted | _Mapping | None = ...,
        high_co_level_detected: HighCoLevelDetected | _Mapping | None = ...,
        high_co_level_detected_early_warning: HighCoLevelDetectedEarlyWarning
        | _Mapping
        | None = ...,
        reserve_battery_low: ReserveBatteryLow | _Mapping | None = ...,
        smoke_chamber_test_not_passed: SmokeChamberTestNotPassed
        | _Mapping
        | None = ...,
        smoke_chamber_test_passed: SmokeChamberTestPassed | _Mapping | None = ...,
        smoke_detected: SmokeDetected | _Mapping | None = ...,
        smoke_detected_early_warning: SmokeDetectedEarlyWarning | _Mapping | None = ...,
        temperature_high: TemperatureHigh | _Mapping | None = ...,
        temperature_high_early_warning: TemperatureHighEarlyWarning
        | _Mapping
        | None = ...,
        temperature_rise_detected: TemperatureRiseDetected | _Mapping | None = ...,
        temperature_rise_detected_early_warning: TemperatureRiseDetectedEarlyWarning
        | _Mapping
        | None = ...,
        fire_protect_malfunction: FireProtectMalfunction | _Mapping | None = ...,
        heat_test_not_passed: HeatTestNotPassed | _Mapping | None = ...,
        heat_test_passed: HeatTestPassed | _Mapping | None = ...,
        high_cco_level_detected: HighCcoLevelDetected | _Mapping | None = ...,
        co_test_not_passed: CoTestNotPassed | _Mapping | None = ...,
        co_test_passed: CoTestPassed | _Mapping | None = ...,
        co_2_high: Co2High | _Mapping | None = ...,
        humidity_high: HumidityHigh | _Mapping | None = ...,
        humidity_low: HumidityLow | _Mapping | None = ...,
        humidity_ok: HumidityOk | _Mapping | None = ...,
        temperature_low: TemperatureLow | _Mapping | None = ...,
        temperature_ok: TemperatureOk | _Mapping | None = ...,
        arm: Arm | _Mapping | None = ...,
        arm_attempt: ArmAttempt | _Mapping | None = ...,
        arming_incomplete: ArmingIncomplete | _Mapping | None = ...,
        arm_with_malfunctions: ArmWithMalfunctions | _Mapping | None = ...,
        disarm: Disarm | _Mapping | None = ...,
        duress_disarm: DuressDisarm | _Mapping | None = ...,
        duress_night_mode_off: DuressNightModeOff | _Mapping | None = ...,
        group_arm: GroupArm | _Mapping | None = ...,
        group_arm_attempt: GroupArmAttempt | _Mapping | None = ...,
        group_arm_with_malfunctions: GroupArmWithMalfunctions | _Mapping | None = ...,
        group_disarm: GroupDisarm | _Mapping | None = ...,
        group_duress_disarm: GroupDuressDisarm | _Mapping | None = ...,
        night_mode_off: NightModeOff | _Mapping | None = ...,
        night_mode_on: NightModeOn | _Mapping | None = ...,
        night_mode_on_attempt: NightModeOnAttempt | _Mapping | None = ...,
        night_mode_on_with_malfunctions: NightModeOnWithMalfunctions
        | _Mapping
        | None = ...,
        panic_button_pressed: PanicButtonPressed | _Mapping | None = ...,
        password_attempt: PasswordAttempt | _Mapping | None = ...,
        security_state_transition_progress_updated: SecurityStateTransitionProgressUpdated
        | _Mapping
        | None = ...,
        duress_authorization: DuressAuthorization | _Mapping | None = ...,
        arm_during_upgrade_attempt: ArmDuringUpgradeAttempt | _Mapping | None = ...,
        bus_short_circuit: BusShortCircuit | _Mapping | None = ...,
        cellular_signal_low: CellularSignalLow | _Mapping | None = ...,
        cms_connection_loss: CmsConnectionLoss | _Mapping | None = ...,
        donor_chosen: DonorChosen | _Mapping | None = ...,
        ethernet_connection_loss: EthernetConnectionLoss | _Mapping | None = ...,
        factory_reset: FactoryReset | _Mapping | None = ...,
        gsm_connection_loss: GsmConnectionLoss | _Mapping | None = ...,
        hold_up_alarm_confirmed: HoldUpAlarmConfirmed | _Mapping | None = ...,
        incorrect_cms: IncorrectCms | _Mapping | None = ...,
        intrusion_alarm_confirmed: IntrusionAlarmConfirmed | _Mapping | None = ...,
        migration_start: MigrationStart | _Mapping | None = ...,
        server_connection_loss: ServerConnectionLoss | _Mapping | None = ...,
        migration_ok: MigrationOk | _Mapping | None = ...,
        migration_failed: MigrationFailed | _Mapping | None = ...,
        target_chosen: TargetChosen | _Mapping | None = ...,
        turn_on: TurnOn | _Mapping | None = ...,
        walk_test_start: WalkTestStart | _Mapping | None = ...,
        wi_fi_connection_loss: WiFiConnectionLoss | _Mapping | None = ...,
        wings_noise_high: WingsNoiseHigh | _Mapping | None = ...,
        settings_changed: SettingsChanged | _Mapping | None = ...,
        access_denied_to_company: AccessDeniedToCompany | _Mapping | None = ...,
        access_denied_to_pro: AccessDeniedToPro | _Mapping | None = ...,
        access_request: AccessRequest | _Mapping | None = ...,
        chime_activated: ChimeActivated | _Mapping | None = ...,
        chime_activated_in_group: ChimeActivatedInGroup | _Mapping | None = ...,
        permanent_access_granted_to_company: PermanentAccessGrantedToCompany
        | _Mapping
        | None = ...,
        permanent_access_granted_to_pro: PermanentAccessGrantedToPro
        | _Mapping
        | None = ...,
        photo_by_scenario_on: PhotoByScenarioOn | _Mapping | None = ...,
        photo_on_demand_on: PhotoOnDemandOn | _Mapping | None = ...,
        system_restored: SystemRestored | _Mapping | None = ...,
        system_restore_denied: SystemRestoreDenied | _Mapping | None = ...,
        system_restore_request: SystemRestoreRequest | _Mapping | None = ...,
        temporary_access_granted_to_company: TemporaryAccessGrantedToCompany
        | _Mapping
        | None = ...,
        temporary_access_granted_to_pro: TemporaryAccessGrantedToPro
        | _Mapping
        | None = ...,
        battery_disconnected: BatteryDisconnected | _Mapping | None = ...,
        bridge_not_responding: BridgeNotResponding | _Mapping | None = ...,
        CardDeactivated: CardDeactivated | _Mapping | None = ...,
        code_deactivated: CodeDeactivated | _Mapping | None = ...,
        custom_event: CustomEvent | _Mapping | None = ...,
        deactivated_card_attempt: DeactivatedCardAttempt | _Mapping | None = ...,
        detector_short_circuit: DetectorShortCircuit | _Mapping | None = ...,
        device_moved: DeviceMoved | _Mapping | None = ...,
        ethernet_communication_loss: EthernetCommunicationLoss | _Mapping | None = ...,
        external_contact_lost: ExternalContactLost | _Mapping | None = ...,
        external_contact_ok: ExternalContactOk | _Mapping | None = ...,
        external_contact_short_circuit: ExternalContactShortCircuit
        | _Mapping
        | None = ...,
        external_malfunction: ExternalMalfunction | _Mapping | None = ...,
        external_power_loss: ExternalPowerLoss | _Mapping | None = ...,
        fire_detector_short_circuit: FireDetectorShortCircuit | _Mapping | None = ...,
        front_tamper_opened: FrontTamperOpened | _Mapping | None = ...,
        gas_detected: GasDetected | _Mapping | None = ...,
        glass_break_detected: GlassBreakDetected | _Mapping | None = ...,
        hold_up_long_press: HoldUpLongPress | _Mapping | None = ...,
        hold_up_short_press: HoldUpShortPress | _Mapping | None = ...,
        intrusion_alarm: IntrusionAlarm | _Mapping | None = ...,
        jeweller_noise_high: JewellerNoiseHigh | _Mapping | None = ...,
        leak_detected: LeakDetected | _Mapping | None = ...,
        medical_alarm: MedicalAlarm | _Mapping | None = ...,
        monitoring_started: MonitoringStarted | _Mapping | None = ...,
        permanent_access_request: PermanentAccessRequest | _Mapping | None = ...,
        s_1_alarm: S1Alarm | _Mapping | None = ...,
        s_3_alarm: S3Alarm | _Mapping | None = ...,
        scenario_not_executed: ScenarioNotExecuted | _Mapping | None = ...,
        temporary_access_request: TemporaryAccessRequest | _Mapping | None = ...,
        battery_low: BatteryLow | _Mapping | None = ...,
        back_tamper_opened: BackTamperOpened | _Mapping | None = ...,
        short_circuit: ShortCircuit | _Mapping | None = ...,
        tamper_board_disconnect: TamperBoardDisconnect | _Mapping | None = ...,
        bus_voltage_high: BusVoltageHigh | _Mapping | None = ...,
        line_sabotage: LineSabotage | _Mapping | None = ...,
        fuse_break: FuseBreak | _Mapping | None = ...,
        timezone_changed: TimezoneChanged | _Mapping | None = ...,
        ring_broken: RingBroken | _Mapping | None = ...,
        bus_conflict: BusConflict | _Mapping | None = ...,
        end_of_life: EndOfLife | _Mapping | None = ...,
        dev_fw_upgrade_started: DevFWUpgradeStarted | _Mapping | None = ...,
        dev_fw_upgrade_failed: DevFWUpgradeFailed | _Mapping | None = ...,
        dev_fw_upgrade_finished: DevFWUpgradeFinished | _Mapping | None = ...,
        bus_power_disabled: BusPowerDisabled | _Mapping | None = ...,
        onetime_full_bypass_on: OnetimeFullBypassOn | _Mapping | None = ...,
        onetime_tamper_bypass_on: OnetimeTamperBypassOn | _Mapping | None = ...,
        life_quality_malfunction: LifeQualityMalfunction | _Mapping | None = ...,
        valve_opened_by_button: ValveOpenedByButton | _Mapping | None = ...,
        valve_opened_by_scenario: ValveOpenedByScenario | _Mapping | None = ...,
        valve_opened_by_arming: ValveOpenedByArming | _Mapping | None = ...,
        valve_opened_by_disarming: ValveOpenedByDisarming | _Mapping | None = ...,
        valve_opened_by_device: ValveOpenedByDevice | _Mapping | None = ...,
        valve_opened_by_user: ValveOpenedByUser | _Mapping | None = ...,
        undefined_valve_position: UndefinedValvePosition | _Mapping | None = ...,
        battery_error: BatteryError | _Mapping | None = ...,
        restore_request: RestoreRequest | _Mapping | None = ...,
        bus_voltage_low: BusVoltageLow | _Mapping | None = ...,
        charger_error: ChargerError | _Mapping | None = ...,
        overheating_detected: OverheatingDetected | _Mapping | None = ...,
        keypad_blocked: KeypadBlocked | _Mapping | None = ...,
        keypad_unblocked_by_timer: KeypadUnblockedByTimer | _Mapping | None = ...,
        keypad_unblocked_by_user: KeypadUnblockedByUser | _Mapping | None = ...,
        relay_unable_to_switch_by_user: RelayUnableToSwitchByUser
        | _Mapping
        | None = ...,
        relay_unable_to_switch_by_scenario: RelayUnableToSwitchByScenario
        | _Mapping
        | None = ...,
        relay_unable_to_switch_by_arming: RelayUnableToSwitchByArming
        | _Mapping
        | None = ...,
        relay_unable_to_switch_by_disarming: RelayUnableToSwitchByDisarming
        | _Mapping
        | None = ...,
        keyarm_blocked: KeyarmBlocked | _Mapping | None = ...,
        keyarm_unblocked_by_user: KeyarmUnblockedByUser | _Mapping | None = ...,
        buses_break: BusesBreak | _Mapping | None = ...,
        buses_conflict: BusesConflict | _Mapping | None = ...,
        buses_unregistered: BusesUnregistered | _Mapping | None = ...,
        reed_switch_broken: ReedSwitchBroken | _Mapping | None = ...,
        accelerometer_broken: AccelerometerBroken | _Mapping | None = ...,
        magnetic_sensor_broken: MagneticSensorBroken | _Mapping | None = ...,
        calibration_required: CalibrationRequired | _Mapping | None = ...,
        activation_rru_code: ActivationRRUCode | _Mapping | None = ...,
        deactivation_rru_code: DeactivationRRUCode | _Mapping | None = ...,
        improper_keyarm_usage: ImproperKeyarmUsage | _Mapping | None = ...,
        video_scenario_triggered: VideoScenarioTriggered | _Mapping | None = ...,
        battery_saving_mode_activation: BatterySavingModeActivation
        | _Mapping
        | None = ...,
        periodic_test: PeriodicTest | _Mapping | None = ...,
        exit_error: ExitError | _Mapping | None = ...,
        recent_closing: RecentClosing | _Mapping | None = ...,
        short_circuit_single_output: ShortCircuitSingleOutput | _Mapping | None = ...,
        bus_voltage_high_single_output: BusVoltageHighSingleOutput
        | _Mapping
        | None = ...,
        bus_voltage_low_single_output: BusVoltageLowSingleOutput
        | _Mapping
        | None = ...,
        bus_power_disabled_single_output: BusPowerDisabledSingleOutput
        | _Mapping
        | None = ...,
        lock_violation: LockViolation | _Mapping | None = ...,
        duress_code: DuressCode | _Mapping | None = ...,
        seismic_alarm: SeismicAlarm | _Mapping | None = ...,
        temp_sensor_high_temperature: TempSensorHighTemperature | _Mapping | None = ...,
        temp_sensor_low_temperature: TempSensorLowTemperature | _Mapping | None = ...,
        local_exit_error: LocalExitError | _Mapping | None = ...,
        abort_burglary: AbortBurglary | _Mapping | None = ...,
        burglary_cancel: BurglaryCancel | _Mapping | None = ...,
        device_supervision_failure: DeviceSupervisionFailure | _Mapping | None = ...,
        self_test_passed: SelfTestPassed | _Mapping | None = ...,
        self_test_failed: SelfTestFailed | _Mapping | None = ...,
        masking_detected_malfunction: MaskingDetectedMalfunction
        | _Mapping
        | None = ...,
        surveillance_scenario_executed: SurveillanceScenarioExecuted
        | _Mapping
        | None = ...,
        battery_saving_mode_activation_failed: BatterySavingModeActivationFailed
        | _Mapping
        | None = ...,
        photo_by_scenario_with_name: PhotoByScenarioWithName | _Mapping | None = ...,
        photo_by_scenario_unsuccessful_with_name: PhotoByScenarioUnsuccessfulWithName
        | _Mapping
        | None = ...,
        unvacated_premises: UnvacatedPremises | _Mapping | None = ...,
        password_reset: PasswordReset | _Mapping | None = ...,
        motion_detected_in_allowed_direction: MotionDetectedInAllowedDirection
        | _Mapping
        | None = ...,
        motion_detected_in_forbidden_direction: MotionDetectedInForbiddenDirection
        | _Mapping
        | None = ...,
        motion_detected_in_allowed_direction_timer_started: MotionDetectedInAllowedDirectionTimerStarted
        | _Mapping
        | None = ...,
        motion_detected_in_allowed_direction_timer_active: MotionDetectedInAllowedDirectionTimerActive
        | _Mapping
        | None = ...,
        allowed_direction_timer_ended: AllowedDirectionTimerEnded
        | _Mapping
        | None = ...,
        video_archive_export_prepared: VideoArchiveExportPrepared
        | _Mapping
        | None = ...,
        video_archive_export_failed: VideoArchiveExportFailed | _Mapping | None = ...,
        ext_src_low_voltage: ExtSrcLowVoltage | _Mapping | None = ...,
        jwl_antenna_disconnect: JwlAntennaDisconnect | _Mapping | None = ...,
        jwl_antenna_connect: JwlAntennaConnect | _Mapping | None = ...,
        wings_antenna_disconnect: WingsAntennaDisconnect | _Mapping | None = ...,
        wings_antenna_connect: WingsAntennaConnect | _Mapping | None = ...,
        gsm_antenna_disconnect: GsmAntennaDisconnect | _Mapping | None = ...,
        gsm_antenna_connect: GsmAntennaConnect | _Mapping | None = ...,
        jwl_antenna_damaged: JwlAntennaDamaged | _Mapping | None = ...,
        wings_antenna_damaged: WingsAntennaDamaged | _Mapping | None = ...,
        gsm_antenna_damaged: GsmAntennaDamaged | _Mapping | None = ...,
        csmoke_detected: CSmokeDetected | _Mapping | None = ...,
        in_call: InCall | _Mapping | None = ...,
        out_call: OutCall | _Mapping | None = ...,
        in_call_error: InCallError | _Mapping | None = ...,
        out_call_error: OutCallError | _Mapping | None = ...,
        callback_request: CallbackRequest | _Mapping | None = ...,
        out_call_no_response: OutCallNoResponse | _Mapping | None = ...,
        out_call_timeout: OutCallTimeout | _Mapping | None = ...,
        in_call_missed: InCallMissed | _Mapping | None = ...,
        in_call_timeout: InCallTimeout | _Mapping | None = ...,
        callback_denied: CallbackDenied | _Mapping | None = ...,
        intrusion_alarm_confirmed_general: IntrusionAlarmConfirmedGeneral
        | _Mapping
        | None = ...,
        intrusion_alarm_confirmed_detailed: IntrusionAlarmConfirmedDetailed
        | _Mapping
        | None = ...,
        unverified_alarm: UnverifiedAlarm | _Mapping | None = ...,
        smart_bracket_opened: SmartBracketOpened | _Mapping | None = ...,
        pir_sensor_broken: PirSensorBroken | _Mapping | None = ...,
        microwave_sensor_broken: MicrowaveSensorBroken | _Mapping | None = ...,
        incorrect_device_installation: IncorrectDeviceInstallation
        | _Mapping
        | None = ...,
        masking_sensor_broken: MaskingSensorBroken | _Mapping | None = ...,
        masking_sensor_calibration_failed: MaskingSensorCalibrationFailed
        | _Mapping
        | None = ...,
        bukhoor_enabled: BukhoorEnabled | _Mapping | None = ...,
        bukhoor_disabled: BukhoorDisabled | _Mapping | None = ...,
        bukhoor_disabled_by_timeout: BukhoorDisabledByTimeout | _Mapping | None = ...,
        sip_connection_loss: SipConnectionLoss | _Mapping | None = ...,
        smart_home_motion_detected: SmartHomeMotionDetected | _Mapping | None = ...,
        human_detected: HumanDetected | _Mapping | None = ...,
        pet_detected: PetDetected | _Mapping | None = ...,
        car_detected: CarDetected | _Mapping | None = ...,
        ring_button_pressed: RingButtonPressed | _Mapping | None = ...,
        case_break_detected: CaseBreakDetected | _Mapping | None = ...,
        self_test_device_disconnected: SelfTestDeviceDisconnected
        | _Mapping
        | None = ...,
        seismo_sensor_broken: SeismoSensorBroken | _Mapping | None = ...,
        vorf_channel_communication_loss: VorfChannelCommunicationLoss
        | _Mapping
        | None = ...,
        relay_short_circuit: RelayShortCircuit | _Mapping | None = ...,
        bolt_switch_contact_opened: BoltSwitchContactOpened | _Mapping | None = ...,
        blocking_element_opened: BlockingElementOpened | _Mapping | None = ...,
        valve_stuck_prevention_not_executed: ValveStuckPreventionNotExecuted
        | _Mapping
        | None = ...,
        valve_stuck_prevention_executed: ValveStuckPreventionExecuted
        | _Mapping
        | None = ...,
        short_circuit_single_output1: ShortCircuitSingleOutput1 | _Mapping | None = ...,
        bus_voltage_high_single_output1: BusVoltageHighSingleOutput1
        | _Mapping
        | None = ...,
        bus_voltage_low_single_output1: BusVoltageLowSingleOutput1
        | _Mapping
        | None = ...,
        short_circuit_single_output2: ShortCircuitSingleOutput2 | _Mapping | None = ...,
        bus_voltage_high_single_output2: BusVoltageHighSingleOutput2
        | _Mapping
        | None = ...,
        bus_voltage_low_single_output2: BusVoltageLowSingleOutput2
        | _Mapping
        | None = ...,
        line_connect_error: LineConnectError | _Mapping | None = ...,
        photo_on_demand_for_detection_area: PhotoOnDemandForDetectionArea
        | _Mapping
        | None = ...,
        photo_on_demand_for_detection_area_unsuccessful: PhotoOnDemandForDetectionAreaUnsuccessful
        | _Mapping
        | None = ...,
        en54_fire_alarm_reset: EN54FireAlarmReset | _Mapping | None = ...,
        device_does_not_respond: DeviceDoesNotRespond | _Mapping | None = ...,
        sounder_fault: SounderFault | _Mapping | None = ...,
        vad_fault: VADFault | _Mapping | None = ...,
        heat_detection_fault: HeatDetectionFault | _Mapping | None = ...,
        smoke_detection_fault: SmokeDetectionFault | _Mapping | None = ...,
        motion_detected_during_test: MotionDetectedDuringTest | _Mapping | None = ...,
        alarm_annunciation_test: AlarmAnnunciationTest | _Mapping | None = ...,
        battery_temperature_out_of_range: BatteryTemperatureOutOfRange
        | _Mapping
        | None = ...,
        exit_delay_complete: ExitDelayComplete | _Mapping | None = ...,
        group_auto_arm: GroupAutoArm | _Mapping | None = ...,
        group_auto_arm_with_malfunctions: GroupAutoArmWithMalfunctions
        | _Mapping
        | None = ...,
        group_auto_arm_attempt: GroupAutoArmAttempt | _Mapping | None = ...,
        group_auto_disarm: GroupAutoDisarm | _Mapping | None = ...,
        auto_arm_not_executed: AutoArmNotExecuted | _Mapping | None = ...,
        auto_arm: AutoArm | _Mapping | None = ...,
        auto_arm_with_malfunctions: AutoArmWithMalfunctions | _Mapping | None = ...,
        auto_disarm: AutoDisarm | _Mapping | None = ...,
        auto_self_test_passed: AutoSelfTestPassed | _Mapping | None = ...,
        auto_self_test_failed: AutoSelfTestFailed | _Mapping | None = ...,
        auto_self_test_error: AutoSelfTestError | _Mapping | None = ...,
        en54_silence: EN54Silence | _Mapping | None = ...,
        en54_resound: EN54Resound | _Mapping | None = ...,
        trigger_group_not_armed: TriggerGroupNotArmed | _Mapping | None = ...,
        alarm_annunciation_test_by_user: AlarmAnnunciationTestByUser
        | _Mapping
        | None = ...,
        alarm_annunciation_test_by_card: AlarmAnnunciationTestByCard
        | _Mapping
        | None = ...,
        alarm_annunciation_test_by_code: AlarmAnnunciationTestByCode
        | _Mapping
        | None = ...,
        wifi_module_upgrade_started: WiFiModuleUpgradeStarted | _Mapping | None = ...,
        wifi_module_upgrade_failed: WiFiModuleUpgradeFailed | _Mapping | None = ...,
        hub_module_upgrade_finished: HubModuleUpgradeFinished | _Mapping | None = ...,
        out_power_overload: OutPowerOverload | _Mapping | None = ...,
        battery_saving_mode_wakeup_sms: BatterySavingModeWakeupSMS
        | _Mapping
        | None = ...,
        endpoint_disabled_by_user: EndpointDisabledByUser | _Mapping | None = ...,
        endpoint_disabled_by_code: EndpointDisabledByCode | _Mapping | None = ...,
        endpoint_disabled_by_card: EndpointDisabledByCard | _Mapping | None = ...,
        in_call_timeout_bsm: InCallTimeoutBSM | _Mapping | None = ...,
        out_call_timeout_bsm: OutCallTimeoutBSM | _Mapping | None = ...,
        battery_saving_mode_wakeup_by_scheduled: BatterySavingModeWakeupByScheduled
        | _Mapping
        | None = ...,
        output_fault: OutputFault | _Mapping | None = ...,
        en54_tamper_opened: EN54TamperOpened | _Mapping | None = ...,
        en54_power_low: EN54PowerLow | _Mapping | None = ...,
        en54_device_communication_loss: EN54DeviceCommunicationLoss
        | _Mapping
        | None = ...,
        en54_fire_alarm: EN54FireAlarm | _Mapping | None = ...,
        en54_medical_alarm: EN54MedicalAlarm | _Mapping | None = ...,
        en54_panic_button_pressed: EN54PanicButtonPressed | _Mapping | None = ...,
        en54_gas_detected: EN54GasDetected | _Mapping | None = ...,
        en54_external_fault: EN54ExternalFault | _Mapping | None = ...,
        en54_leak_detected: EN54LeakDetected | _Mapping | None = ...,
        external_contact_hard_fault: ExternalContactHardFault | _Mapping | None = ...,
        fault_alarm: FaultAlarm | _Mapping | None = ...,
        relay_on_by_access_code: RelayOnByAccessCode | _Mapping | None = ...,
        relay_on_by_access_card: RelayOnByAccessCard | _Mapping | None = ...,
        relay_on_by_timer: RelayOnByTimer | _Mapping | None = ...,
        relay_off_by_user: RelayOffByUser | _Mapping | None = ...,
        relay_off_by_access_code: RelayOffByAccessCode | _Mapping | None = ...,
        relay_off_by_access_card: RelayOffByAccessCard | _Mapping | None = ...,
        evacuation: Evacuation | _Mapping | None = ...,
        custom_alarm: CustomAlarm | _Mapping | None = ...,
        audio_record: AudioRecord | _Mapping | None = ...,
        relay_on_by_fail_safe: RelayOnByFailSafe | _Mapping | None = ...,
        relay_off_by_fail_safe: RelayOffByFailSafe | _Mapping | None = ...,
        delays_override: DelaysOverride | _Mapping | None = ...,
        software_system_fault: SoftwareSystemFault | _Mapping | None = ...,
        memory_system_fault: MemorySystemFault | _Mapping | None = ...,
        arc_reporting_off: ArcReportingOff | _Mapping | None = ...,
        fire_delays_on: FireDelaysOn | _Mapping | None = ...,
        fire_delays_off: FireDelaysOff | _Mapping | None = ...,
        battery_fault: BatteryFault | _Mapping | None = ...,
        fire_zone_test: FireZoneTest | _Mapping | None = ...,
        cms_delivery_failed: CmsDeliveryFailed | _Mapping | None = ...,
        day_alarm_temporary_bypass_activated: DayAlarmTemporaryBypassActivated
        | _Mapping
        | None = ...,
        duress_day_alarm_temporary_bypass_activated: DuressDayAlarmTemporaryBypassActivated
        | _Mapping
        | None = ...,
        day_alarm_bypass_activated: DayAlarmBypassActivated | _Mapping | None = ...,
        duress_day_alarm_bypass_activated: DuressDayAlarmBypassActivated
        | _Mapping
        | None = ...,
        day_alarm_bypass_not_restored: DayAlarmBypassNotRestored
        | _Mapping
        | None = ...,
        external_contact_resistance_fault: ExternalContactResistanceFault
        | _Mapping
        | None = ...,
        alarms_to_cms_disabled: AlarmsToCmsDisabled | _Mapping | None = ...,
        alarms_to_cms_enabled: AlarmsToCmsEnabled | _Mapping | None = ...,
        faults_to_cms_disabled: FaultsToCmsDisabled | _Mapping | None = ...,
        faults_to_cms_enabled: FaultsToCmsEnabled | _Mapping | None = ...,
        detector_voltage_low: DetectorVoltageLow | _Mapping | None = ...,
        fire_detector_voltage_low: FireDetectorVoltageLow | _Mapping | None = ...,
        zone_test_system_exit: ZoneTestSystemExit | _Mapping | None = ...,
        cms_connection_lost: CmsConnectionLost | _Mapping | None = ...,
        smart_lock_unlocked_by_knob: SmartLockUnlockedByKnob | _Mapping | None = ...,
        smart_lock_unlocked_by_code: SmartLockUnlockedByCode | _Mapping | None = ...,
        smart_lock_unlocked_by_tag: SmartLockUnlockedByTag | _Mapping | None = ...,
        smart_lock_unlocked_by_user: SmartLockUnlockedByUser | _Mapping | None = ...,
        smart_lock_unlocked_by_scenario: SmartLockUnlockedByScenario
        | _Mapping
        | None = ...,
        smart_lock_unlocked_by_arm: SmartLockUnlockedByArm | _Mapping | None = ...,
        smart_lock_unlocked_by_disarm: SmartLockUnlockedByDisarm
        | _Mapping
        | None = ...,
        smart_lock_unlocked_by_keyboard: SmartLockUnlockedByKeyboard
        | _Mapping
        | None = ...,
        smart_lock_module_locked_automatically: SmartLockModuleLockedAutomatically
        | _Mapping
        | None = ...,
        smart_lock_door_open: SmartLockDoorOpen | _Mapping | None = ...,
        smart_lock_doorbell_button_pressed: SmartLockDoorbellButtonPressed
        | _Mapping
        | None = ...,
        smart_lock_keyboard_locked: SmartLockKeyboardLocked | _Mapping | None = ...,
        module_inserted_into_different_lock: ModuleInsertedIntoDifferentLock
        | _Mapping
        | None = ...,
        smart_lock_credential_added: SmartLockCredentialAdded | _Mapping | None = ...,
        smart_lock_credential_adding_error: SmartLockCredentialAddingError
        | _Mapping
        | None = ...,
        smart_lock_credential_removed: SmartLockCredentialRemoved
        | _Mapping
        | None = ...,
        smart_lock_credential_removing_error: SmartLockCredentialRemovingError
        | _Mapping
        | None = ...,
        smart_lock_locked_with_confirmation: SmartLockLockedWithConfirmation
        | _Mapping
        | None = ...,
        smart_lock_credential_activated_deactivated: SmartLockCredentialActivatedDeactivated
        | _Mapping
        | None = ...,
        smart_lock_credential_activation_deactivation_error: SmartLockCredentialActivationDeactivationError
        | _Mapping
        | None = ...,
        en54_external_power_loss: EN54ExternalPowerLoss | _Mapping | None = ...,
        en54_ethernet_communication_loss: EN54EthernetCommunicationLoss
        | _Mapping
        | None = ...,
    ) -> None: ...
