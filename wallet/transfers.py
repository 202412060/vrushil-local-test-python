"""Account-to-account transfers."""
from wallet.accounts import AccountStore
from wallet.fees import compute_fee
from wallet.ledger import Ledger


def transfer(store: AccountStore, ledger: Ledger, source_id: str, target_id: str, amount_cents: int) -> dict:
    source = store.get(source_id)
    target = store.get(target_id)
    fee = compute_fee(amount_cents)
    ledger.debit(source, amount_cents + fee, memo=f"transfer to {target_id}")
    ledger.credit(target, amount_cents, memo=f"transfer from {source_id}")
    return {"amount_cents": amount_cents, "fee_cents": fee}
