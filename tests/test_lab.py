import hashlib
import tempfile
import unittest
from pathlib import Path
from lab.integrity import sha256_file, verify_file
from lab.encoding import encode_text, decode_text
from lab.validation import valid_project_id


class LabTests(unittest.TestCase):
    def test_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(b"hello")
            expected = hashlib.sha256(b"hello").hexdigest()
            self.assertEqual(sha256_file(path), expected)
            self.assertTrue(verify_file(path, expected))
            path.write_bytes(b"changed")
            self.assertFalse(verify_file(path, expected))

    def test_encoding(self):
        self.assertEqual(encode_text("hello"), "aGVsbG8=")
        self.assertEqual(decode_text(encode_text("bonjour")), "bonjour")

    def test_validation(self):
        self.assertTrue(valid_project_id("AB-1234"))
        for value in ["ab-1234", "AB-123", "AB-1234\n", "AB-12345"]:
            self.assertFalse(valid_project_id(value))
