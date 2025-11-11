from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureTargetSuspendedByDealer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FeatureTargetRestoredByDealer(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaidServiceAssigned(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaidServiceDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrepaidServiceDeactivated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SimCardCommissioningPeriodStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SimCardCommissioningPeriodEnded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrepaidServiceDeactivatedByReseller(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaidServiceDeactivatedByReseller(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FeatureTargetRestoredByReseller(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaymentFailedInvalidCardState(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaymentFailedTerminal(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PaymentFailedTechnical(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RetryPaymentFailedInvalidCardState(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RetryPaymentFailedTechnical(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscriptionRenewedAfterFailure(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubscriptionCanceledOnGracePeriodEnd(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AccountingEventTag(_message.Message):
    __slots__ = (
        "feature_target_restored_by_dealer",
        "feature_target_restored_by_reseller",
        "feature_target_suspended_by_dealer",
        "paid_service_assigned",
        "paid_service_deactivated",
        "paid_service_deactivated_by_reseller",
        "payment_failed_invalid_card_state",
        "payment_failed_technical",
        "payment_failed_terminal",
        "prepaid_service_deactivated",
        "prepaid_service_deactivated_by_reseller",
        "retry_payment_failed_invalid_card_state",
        "retry_payment_failed_technical",
        "sim_card_commissioning_period_ended",
        "sim_card_commissioning_period_started",
        "subscription_canceled_on_grace_period_end",
        "subscription_renewed_after_failure",
    )
    FEATURE_TARGET_SUSPENDED_BY_DEALER_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_RESTORED_BY_DEALER_FIELD_NUMBER: _ClassVar[int]
    PAID_SERVICE_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    PAID_SERVICE_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    PREPAID_SERVICE_DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    SIM_CARD_COMMISSIONING_PERIOD_STARTED_FIELD_NUMBER: _ClassVar[int]
    SIM_CARD_COMMISSIONING_PERIOD_ENDED_FIELD_NUMBER: _ClassVar[int]
    PREPAID_SERVICE_DEACTIVATED_BY_RESELLER_FIELD_NUMBER: _ClassVar[int]
    PAID_SERVICE_DEACTIVATED_BY_RESELLER_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_RESTORED_BY_RESELLER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FAILED_INVALID_CARD_STATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FAILED_TERMINAL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FAILED_TECHNICAL_FIELD_NUMBER: _ClassVar[int]
    RETRY_PAYMENT_FAILED_INVALID_CARD_STATE_FIELD_NUMBER: _ClassVar[int]
    RETRY_PAYMENT_FAILED_TECHNICAL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_RENEWED_AFTER_FAILURE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_CANCELED_ON_GRACE_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    feature_target_suspended_by_dealer: FeatureTargetSuspendedByDealer
    feature_target_restored_by_dealer: FeatureTargetRestoredByDealer
    paid_service_assigned: PaidServiceAssigned
    paid_service_deactivated: PaidServiceDeactivated
    prepaid_service_deactivated: PrepaidServiceDeactivated
    sim_card_commissioning_period_started: SimCardCommissioningPeriodStarted
    sim_card_commissioning_period_ended: SimCardCommissioningPeriodEnded
    prepaid_service_deactivated_by_reseller: PrepaidServiceDeactivatedByReseller
    paid_service_deactivated_by_reseller: PaidServiceDeactivatedByReseller
    feature_target_restored_by_reseller: FeatureTargetRestoredByReseller
    payment_failed_invalid_card_state: PaymentFailedInvalidCardState
    payment_failed_terminal: PaymentFailedTerminal
    payment_failed_technical: PaymentFailedTechnical
    retry_payment_failed_invalid_card_state: RetryPaymentFailedInvalidCardState
    retry_payment_failed_technical: RetryPaymentFailedTechnical
    subscription_renewed_after_failure: SubscriptionRenewedAfterFailure
    subscription_canceled_on_grace_period_end: SubscriptionCanceledOnGracePeriodEnd
    def __init__(
        self,
        feature_target_suspended_by_dealer: FeatureTargetSuspendedByDealer
        | _Mapping
        | None = ...,
        feature_target_restored_by_dealer: FeatureTargetRestoredByDealer
        | _Mapping
        | None = ...,
        paid_service_assigned: PaidServiceAssigned | _Mapping | None = ...,
        paid_service_deactivated: PaidServiceDeactivated | _Mapping | None = ...,
        prepaid_service_deactivated: PrepaidServiceDeactivated | _Mapping | None = ...,
        sim_card_commissioning_period_started: SimCardCommissioningPeriodStarted
        | _Mapping
        | None = ...,
        sim_card_commissioning_period_ended: SimCardCommissioningPeriodEnded
        | _Mapping
        | None = ...,
        prepaid_service_deactivated_by_reseller: PrepaidServiceDeactivatedByReseller
        | _Mapping
        | None = ...,
        paid_service_deactivated_by_reseller: PaidServiceDeactivatedByReseller
        | _Mapping
        | None = ...,
        feature_target_restored_by_reseller: FeatureTargetRestoredByReseller
        | _Mapping
        | None = ...,
        payment_failed_invalid_card_state: PaymentFailedInvalidCardState
        | _Mapping
        | None = ...,
        payment_failed_terminal: PaymentFailedTerminal | _Mapping | None = ...,
        payment_failed_technical: PaymentFailedTechnical | _Mapping | None = ...,
        retry_payment_failed_invalid_card_state: RetryPaymentFailedInvalidCardState
        | _Mapping
        | None = ...,
        retry_payment_failed_technical: RetryPaymentFailedTechnical
        | _Mapping
        | None = ...,
        subscription_renewed_after_failure: SubscriptionRenewedAfterFailure
        | _Mapping
        | None = ...,
        subscription_canceled_on_grace_period_end: SubscriptionCanceledOnGracePeriodEnd
        | _Mapping
        | None = ...,
    ) -> None: ...
