"""Monthly statement lines."""
from wallet.fees import compute_fee
from wallet.money import format_cents


def statement_line(description: str, amount_cents: int) -> str:
    fee = compute_fee(amount_cents)
    return f"{description}: {format_cents(amount_cents)} (fee {format_cents(fee)})"


def statement_total(lines: list[dict]) -> int:
    return sum(item["amount_cents"] + compute_fee(item["amount_cents"]) for item in lines)
