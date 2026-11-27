"""Withdrawals to an external bank account."""
from wallet.accounts import AccountStore
from wallet.fees import compute_fee
from wallet.ledger import Ledger


def withdraw(store: AccountStore, ledger: Ledger, account_id: str, amount_cents: int) -> dict:
    account = store.get(account_id)
    fee = compute_fee(amount_cents)
    total = amount_cents + fee
    ledger.debit(account, total, memo="withdrawal")
    return {"withdrawn_cents": amount_cents, "fee_cents": fee, "total_cents": total}
