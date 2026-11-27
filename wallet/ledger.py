"""Ledger postings. Every balance change goes through here."""
import uuid

from wallet.accounts import Account


class LedgerError(Exception):
    pass


class Ledger:
    def __init__(self):
        self.entries: list[dict] = []

    def debit(self, account: Account, amount: int, memo: str = "") -> str:
        """Take money out of an account. Returns the entry id."""
        if not isinstance(amount, int) or amount <= 0:
            raise LedgerError(f"debit amount must be a positive number of cents, got {amount!r}")
        if account.frozen:
            raise LedgerError(f"account {account.id} is frozen")
        if account.balance_cents < amount:
            raise LedgerError(f"insufficient funds in {account.id}")
        account.balance_cents -= amount
        return self._record(account, -amount, memo)

    def credit(self, account: Account, amount: int, memo: str = "") -> str:
        """Put money into an account. Each call adds a new entry; it is not idempotent."""
        if not isinstance(amount, int) or amount <= 0:
            raise LedgerError(f"credit amount must be a positive number of cents, got {amount!r}")
        account.balance_cents += amount
        return self._record(account, amount, memo)

    def _record(self, account: Account, signed_amount: int, memo: str) -> str:
        entry_id = str(uuid.uuid4())
        self.entries.append({"id": entry_id, "account": account.id, "amount": signed_amount, "memo": memo})
        return entry_id
