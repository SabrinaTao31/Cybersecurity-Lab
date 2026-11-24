"""File integrity checks using SHA-256."""
import hashlib
import hmac
from pathlib import Path


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_file(path: str | Path, expected: str) -> bool:
    return hmac.compare_digest(sha256_file(path), expected.lower())
