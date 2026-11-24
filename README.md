# Cybersecurity Lab

A hands-on learning portfolio for defensive security and secure Python development.

## Modules

| Module | Objective |
|---|---|
| 01 — File integrity | Calculate SHA-256 and compare a file against a trusted digest |
| 02 — Encoding | Understand Base64 and why it is not encryption |
| 03 — Input validation | Validate structured data using explicit rules |

## Run locally

Requires Python 3.10+; no external dependencies.

```sh
git clone https://github.com/SabrinaTao31/Cybersecurity-Lab.git
cd Cybersecurity-Lab
python -m unittest discover -s tests -v
```

See [learning guide](docs/learning-guide.md) for exercises. Use only synthetic examples and files you own. Never commit credentials or personal data.

**Status:** starter implementation; exercises and tests are provided for independent practice. Future modules will cover secure application design and defensive log analysis.
