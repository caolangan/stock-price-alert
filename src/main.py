"""Main entry point for the Stock Price Alert application."""

from __future__ import annotations
import logging
import os
import datetime

LOG_FILE = "../logs/stock_price_alert.log"


def log_msg(msg: str, level: int = 1) -> None:
    """Log a message with the specified level.

    Args:
        msg (str): The message to log.
        level (int): The logging level (1 for INFO, 2 for WARNING, 3 for ERROR).
    """
    match level:
        case 1:
            level = logging.INFO
        case 2:
            level = logging.WARNING
        case 3:
            level = logging.ERROR
        case _:
            level = logging.DEBUG


def main() -> None:
    """Main function to run the Stock Price Alert application."""

    logging.basicConfig(
        format="%(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        filename=LOG_FILE,
        level=logging.INFO,
    )
    logging.info("Starting Stock Price Alert application...")

    logger = logging.getLogger(__name__)

    # Placeholder for the main logic of the application
    # This could include initializing services, starting a web server, etc.
    # For example:
    # from stock_price_alert import app
    # app.run()


if __name__ == "__main__":
    main()
