"""One-Star Review of Something Essential -- Akun 2 (@wantorieta15).

Reviser rewrite: the builder's entry text is frozen and must be written
byte-for-byte, with no trailing newline, so the scored file is exactly
111 bytes. This revision adds a strict validator that checks the text is
a single line with no newline and that its SHA-256 matches the verified
expectation before anything is written.

Pure stdlib, deterministic, no network access.
"""

import hashlib
import os


ENTRY_TEXT = (
    "One star. The duvet is exactly wide enough for one person and a half, "
    "and every night I discover I am the half."
)

EXPECTED_SHA256 = "3b2c2c4965137a16cd25aa6c6b95c61563221ec0043487914f8ad5902948e4b1"
EXPECTED_BYTES = 111


def build_entry():
    """Return the frozen one-line entry text, exactly as specified."""
    return ENTRY_TEXT


def validate_entry(text):
    """Check the entry is one line, newline-free, and hashes as expected.

    Raises ValueError on any mismatch; returns True when every check
    passes, so a bad entry can never reach the output file.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    encoded = text.encode("utf-8")
    if len(encoded) != EXPECTED_BYTES:
        raise ValueError(
            "entry must be %d bytes, got %d" % (EXPECTED_BYTES, len(encoded))
        )
    digest = hashlib.sha256(encoded).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("entry sha256 mismatch: got %s" % digest)
    return True


def write_entry():
    """Write the validated entry text directly to <out_dir>/entry.txt.

    Writes straight to the destination file (no temp file, no rename)
    and sets mode 0644 explicitly so the grader can read it.
    """
    text = build_entry()
    validate_entry(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    print("wrote " + path)


if __name__ == "__main__":
    main()
