import logging

from app.config import settings


def setup_logging() -> None:
    """Configure application-wide logging."""

    logging.basicConfig(
        level=settings.log_level.upper(),
        format=("%(asctime)s | %(levelname)s | %(name)s | %(message)s"),
    )


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger."""

    return logging.getLogger(name)
