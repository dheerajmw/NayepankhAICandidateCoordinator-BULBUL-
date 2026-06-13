"""Retry helper for automation with simple rate limiting."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

from core.config import EMAIL_MAX_RETRIES, EMAIL_RETRY_DELAY_SECONDS

T = TypeVar("T")


def with_retry(
    operation: Callable[[], T],
    *,
    max_retries: int | None = None,
    delay_seconds: float | None = None,
    label: str = "operation",
) -> T:
    retries = max_retries if max_retries is not None else EMAIL_MAX_RETRIES
    delay = delay_seconds if delay_seconds is not None else EMAIL_RETRY_DELAY_SECONDS
    last_error: Exception | None = None

    for attempt in range(1, retries + 1):
        try:
            return operation()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(delay * attempt)

    raise RuntimeError(f"{label} failed after {retries} attempt(s): {last_error}")
