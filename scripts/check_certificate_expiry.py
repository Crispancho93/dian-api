"""Ejecuta una revisión de certificados para usar desde cron."""

import logging
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from application.use_cases.client.notify_expiring_certificates_case import (  # noqa: E402
    NotifyExpiringCertificatesCase,
)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    NotifyExpiringCertificatesCase().execute()


if __name__ == "__main__":
    main()
