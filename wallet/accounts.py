"""Account records and lookup."""
from dataclasses import dataclass


class AccountNotFound(Exception):
    pass


@dataclass
class Account:
    id: str
    owner_email: str
    balance_cents: int = 0
    frozen: bool = False


class AccountStore:
    """In-memory account store used by the service and the tests."""

    def __init__(self):
        self._accounts: dict[str, Account] = {}

    def add(self, account: Account) -> None:
        self._accounts[account.id] = account

    def get(self, account_id: str) -> Account:
        """Return the account, or raise AccountNotFound. Never returns None."""
        try:
            return self._accounts[account_id]
        except KeyError:
            raise AccountNotFound(account_id) from None
