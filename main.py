"""Entry for make.fun bounty: The GPS Swears It Was a Shortcut.

Writes the entry line to entry.txt inside MAKEFUN_OUTPUT_DIR
(default: the current directory), with no trailing newline.
"""

import os

ENTRY = "Recalculating was never an option: that road had main-character energy, and honestly, you needed the scenic trauma to grow as a driver."
MAX_CHARS = 200


def main() -> None:
    # Validate the entry format before writing anything.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, max is {MAX_CHARS}"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
