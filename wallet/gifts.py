"""Customer-to-customer gifts."""
from wallet.accounts import AccountStore
from wallet.ledger import Ledger


def send_gift(store: AccountStore, ledger: Ledger, sender_id: str, recipient_id: str, amount_cents: int) -> dict:
    sender = store.get(sender_id)
    recipient = store.get(recipient_id)
    ledger.debit(sender, amount_cents, memo=f"gift to {recipient_id}")
    ledger.credit(recipient, amount_cents, memo=f"gift from {sender_id}")
    return {"sent_cents": amount_cents}
