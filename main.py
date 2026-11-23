#!/usr/bin/env python3
"""Write entry.png to the output directory.

The entry image (a front page summing up the world news of Monday
23 November 2026) is stored in this repository as entry.png; this
program copies it to $MAKEFUN_OUTPUT_DIR/entry.png (or /output when
unset). Standard library only, no network, deterministic output.
"""

import hashlib
import os
from pathlib import Path

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _read_entry(source: Path) -> bytes:
    """Read and validate the entry image, returning its exact bytes."""
    if not source.is_file():
        raise SystemExit(f"entry image missing: {source}")
    data = source.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(
            f"entry image too large: {len(data)} bytes (limit {MAX_BYTES})"
        )
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry image is not a PNG file")
    return data


def main() -> None:
    here = Path(__file__).resolve().parent
    data = _read_entry(here / "entry.png")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    # Determinism guard: what landed on disk must be exactly the
    # validated source bytes, so repeated runs stay byte-identical.
    if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(data).digest():
        raise SystemExit("output does not match source")


if __name__ == "__main__":
    main()
