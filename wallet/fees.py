"""Fee schedule. Fees are integer cents, like every other amount in the service."""

FLAT_FEE_CENTS = 25
PERCENT_FEE_BPS = 150  # 1.5%


def compute_fee(amount_cents: int) -> int:
    """Fee for moving amount_cents, in integer cents."""
    return FLAT_FEE_CENTS + (amount_cents * PERCENT_FEE_BPS) // 10_000
