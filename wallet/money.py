"""Money helpers. All balances and amounts inside the service are integer cents."""
from decimal import Decimal, ROUND_HALF_UP


def to_cents(amount) -> int:
    """Convert a decimal amount in dollars (str, int or Decimal) to integer cents, rounding half up."""
    return int((Decimal(str(amount)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def format_cents(cents: int) -> str:
    """Render integer cents for display, e.g. 123456 -> '$1,234.56'."""
    sign = "-" if cents < 0 else ""
    return f"{sign}${abs(cents) / 100:,.2f}"
