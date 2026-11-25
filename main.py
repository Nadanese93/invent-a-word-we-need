"""Write the Make.fun entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single invented word with its definition, exactly 65
characters, one line, no trailing newline.
"""

import os

ENTRY_TEXT = "verifright — the dread that a green check passed nothing real."
OUTPUT_FILENAME = "entry.txt"
MAX_LENGTH = 140


def main() -> None:
    text = ENTRY_TEXT
    if not text:
        raise ValueError("entry text must not be empty")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"entry text must be at most {MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back to /output/entry.txt
    # only when the variable is unset entirely.
    if "MAKEFUN_OUTPUT_DIR" not in os.environ:
        output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    data = text.encode("utf-8")
    tmp_path = output_path + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(data)
    os.replace(tmp_path, output_path)
    with open(output_path, "rb") as f:
        on_disk = f.read()
    if on_disk != data:
        raise ValueError(
            f"read-back verification failed for {output_path}: "
            f"expected {len(data)} bytes, found {len(on_disk)} bytes"
        )


if __name__ == "__main__":
    main()
