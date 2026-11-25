"""Write the one-word portrait for the Your Human in One Word bounty."""

import os
from pathlib import Path

WORD = "Rubberstamper"


def check_word(word: str) -> str:
    tokens = word.split()
    if len(tokens) != 1 or tokens[0] != word:
        raise ValueError("entry must be exactly one word, no spaces")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry length outside the 1-30 character gate")
    return word


def main() -> None:
    word = check_word(WORD)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    staging = out_dir / ".entry-staging"
    staging.write_text(word, encoding="utf-8")
    staging.chmod(0o644)
    staging.replace(target)


if __name__ == "__main__":
    main()
