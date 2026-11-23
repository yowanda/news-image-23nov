#!/usr/bin/env python3
"""Write entry.png to the output directory.

The entry image (a front page summing up the world news of Monday
23 November 2026) is stored in this repository as entry.png; this
program copies it to $MAKEFUN_OUTPUT_DIR/entry.png (or /output when
unset). Standard library only, no network, deterministic output.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
