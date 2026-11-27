"""Fee schedule."""
from decimal import Decimal

FLAT_FEE_CENTS = 25
PERCENT_FEE_BPS = 150  # 1.5%


def compute_fee(amount_cents: int) -> Decimal:
    """Fee for moving amount_cents, in dollars with two decimals, ready to show on receipts."""
    cents = FLAT_FEE_CENTS + (amount_cents * PERCENT_FEE_BPS) // 10_000
    return (Decimal(cents) / 100).quantize(Decimal("0.01"))
