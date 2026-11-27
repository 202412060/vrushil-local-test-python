"""Customer notifications."""
import logging

logger = logging.getLogger(__name__)


class Notifier:
    def __init__(self, mailer):
        self.mailer = mailer

    def send_receipt(self, owner_email: str, amount_cents: int, memo: str) -> None:
        """Email a receipt. Sends a new email on every call."""
        self.mailer.send(to=owner_email, subject="Payment receipt", body=f"{memo}: {amount_cents} cents")
        logger.info("Receipt sent to %s", owner_email)
