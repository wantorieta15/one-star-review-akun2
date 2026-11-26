"""One-Star Review of Something Essential -- Akun 2 (@wantorieta15).

Writes exactly one line to entry.txt: a deadpan one-star review of
the duvet, an everyday essential everyone relies on. Pure stdlib,
deterministic, no network access.

The entry text is frozen: it must be written byte-for-byte, with no
trailing newline, so the scored file is exactly 111 bytes.
"""

import os


ENTRY_TEXT = (
    "One star. The duvet is exactly wide enough for one person and a half, "
    "and every night I discover I am the half."
)


def build_entry():
    """Return the frozen one-line entry text, exactly as specified."""
    return ENTRY_TEXT


def write_entry():
    """Write the entry text directly to <out_dir>/entry.txt.

    Writes straight to the destination file (no temp file, no rename)
    and sets mode 0644 explicitly so the grader can read it.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(build_entry())
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("wrote " + path)


if __name__ == "__main__":
    main()
