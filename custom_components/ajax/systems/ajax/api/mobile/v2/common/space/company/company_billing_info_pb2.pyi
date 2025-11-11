from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyBillingInfo(_message.Message):
    __slots__ = ("billing_status", "hub_billing_info")
    class Blocked(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCKED_UNSPECIFIED: _ClassVar[CompanyBillingInfo.Blocked]
        BLOCKED_FALSE: _ClassVar[CompanyBillingInfo.Blocked]
        BLOCKED_TRUE: _ClassVar[CompanyBillingInfo.Blocked]

    BLOCKED_UNSPECIFIED: CompanyBillingInfo.Blocked
    BLOCKED_FALSE: CompanyBillingInfo.Blocked
    BLOCKED_TRUE: CompanyBillingInfo.Blocked
    class BillingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BILLING_STATUS_UNSPECIFIED: _ClassVar[CompanyBillingInfo.BillingStatus]
        BILLING_STATUS_ENABLED: _ClassVar[CompanyBillingInfo.BillingStatus]
        BILLING_STATUS_DISABLED: _ClassVar[CompanyBillingInfo.BillingStatus]

    BILLING_STATUS_UNSPECIFIED: CompanyBillingInfo.BillingStatus
    BILLING_STATUS_ENABLED: CompanyBillingInfo.BillingStatus
    BILLING_STATUS_DISABLED: CompanyBillingInfo.BillingStatus
    class HubBillingInfo(_message.Message):
        __slots__ = (
            "balance",
            "blocked",
            "company_hex_id",
            "currency",
            "hub_hex_id",
            "payment_date",
            "subscription_fee",
        )
        HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_FEE_FIELD_NUMBER: _ClassVar[int]
        BLOCKED_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_DATE_FIELD_NUMBER: _ClassVar[int]
        hub_hex_id: str
        company_hex_id: str
        balance: float
        subscription_fee: float
        blocked: CompanyBillingInfo.Blocked
        currency: str
        payment_date: str
        def __init__(
            self,
            hub_hex_id: str | None = ...,
            company_hex_id: str | None = ...,
            balance: float | None = ...,
            subscription_fee: float | None = ...,
            blocked: CompanyBillingInfo.Blocked | str | None = ...,
            currency: str | None = ...,
            payment_date: str | None = ...,
        ) -> None: ...

    HUB_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    BILLING_STATUS_FIELD_NUMBER: _ClassVar[int]
    hub_billing_info: CompanyBillingInfo.HubBillingInfo
    billing_status: CompanyBillingInfo.BillingStatus
    def __init__(
        self,
        hub_billing_info: CompanyBillingInfo.HubBillingInfo | _Mapping | None = ...,
        billing_status: CompanyBillingInfo.BillingStatus | str | None = ...,
    ) -> None: ...
