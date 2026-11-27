"""Bulk merchant payouts uploaded by finance as a CSV (columns: merchant, amount_usd)."""
import csv

from wallet.accounts import AccountStore
from wallet.ledger import Ledger
from wallet.payouts import PLATFORM_ACCOUNT


def run_bulk_payouts(store: AccountStore, ledger: Ledger, csv_path: str) -> int:
    """Pay every merchant listed in the CSV. Returns the number of payouts made."""
    platform = store.get(PLATFORM_ACCOUNT)
    paid = 0
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            merchant = store.get(row["merchant"])
            amount = int(row["amount_usd"])
            ledger.debit(platform, amount, memo=f"bulk payout to {merchant.id}")
            ledger.credit(merchant, amount, memo="bulk payout")
            paid += 1
    return paid
