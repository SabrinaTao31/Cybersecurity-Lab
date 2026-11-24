"""Encoding is not encryption."""
import base64


def encode_text(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode_text(encoded: str) -> str:
    return base64.b64decode(encoded, validate=True).decode("utf-8")
