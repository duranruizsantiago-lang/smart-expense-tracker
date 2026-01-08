from __future__ import annotations
from datetime import datetime


def parse_month(month_str: str) -> tuple[int, int]:
    """Parse YYYY-MM into (year, month)."""
    try:
        dt = datetime.strptime(month_str, "%Y-%m")
        return dt.year, dt.month
    except ValueError as e:
        raise ValueError("Month must be in format YYYY-MM (e.g. 2026-01)") from e


def to_float(value: str) -> float:
    try:
        return float(value)
    except ValueError as e:
        raise ValueError(f"Invalid numeric value: {value}") from e
