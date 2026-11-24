"""Validate a fictional project identifier."""
import re


def valid_project_id(value: str) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[A-Z]{2}-[0-9]{4}", value) is not None
