"""Finance reports built from raw ledger exports (amounts arrive as dollar strings)."""
from wallet.money import to_cents


def total_deposits(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "deposit")


def total_withdrawals(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "withdrawal")


def total_fees(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "fee")


def total_refunds(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "refund")


def total_chargebacks(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "chargeback")


def total_interest(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "interest")


def total_payouts(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "payout")


def total_adjustments(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "adjustment")


def total_rewards(rows: list[dict]) -> int:
    return sum(to_cents(r["amount"]) for r in rows if r["type"] == "reward")


def largest_single_amount(rows: list[dict]) -> int:
    return max((to_cents(r["amount"]) for r in rows), default=0)
