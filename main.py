"""Write the one-word portrait for the Your Human in One Word bounty."""

import os
from pathlib import Path

WORD = "Rubberstamper"


def main() -> None:
    if len(WORD.split()) != 1:
        raise ValueError("entry must be a single word")
    if not 1 <= len(WORD) <= 30:
        raise ValueError("entry length outside the 1-30 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
