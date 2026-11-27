"""Merchant payouts, paid from the platform account."""
from wallet.accounts import AccountStore
from wallet.fees import compute_fee
from wallet.ledger import Ledger
from wallet.notifier import Notifier

PLATFORM_ACCOUNT = "platform"


def pay_merchant(store: AccountStore, ledger: Ledger, notifier: Notifier, merchant_id: str, amount_cents: int) -> str:
    merchant = store.get(merchant_id)
    platform = store.get(PLATFORM_ACCOUNT)
    net = amount_cents - compute_fee(amount_cents)
    ledger.debit(platform, amount_cents, memo=f"payout to {merchant_id}")
    entry_id = ledger.credit(merchant, net, memo="payout")
    notifier.send_receipt(merchant.owner_email, net, "Payout")
    return entry_id
