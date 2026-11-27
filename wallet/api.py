"""Request handlers. Requests carry amounts as dollar strings; the service works in cents."""
from wallet.accounts import AccountStore
from wallet.ledger import Ledger
from wallet.money import to_cents
from wallet.transfers import transfer
from wallet.withdrawals import withdraw


def handle_transfer(store: AccountStore, ledger: Ledger, body: dict) -> dict:
    return transfer(store, ledger, body["from"], body["to"], to_cents(body["amount"]))


def handle_withdrawal(store: AccountStore, ledger: Ledger, body: dict) -> dict:
    return withdraw(store, ledger, body["account"], to_cents(body["amount"]))


def handle_top_up(store: AccountStore, ledger: Ledger, body: dict) -> dict:
    account = store.get(body["account"])
    entry_id = ledger.credit(account, to_cents(body["amount"]), memo="top-up")
    return {"entry_id": entry_id}
