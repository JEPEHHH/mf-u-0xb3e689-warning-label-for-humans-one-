#!/usr/bin/env python3
"""Program/v1 entrypoint for Warning Label for Humans: One Line, Big Laugh."""

from pathlib import Path
import sys

DEFAULT_OUTPUT_PATH = Path("/output/entry.txt")

MAX_LABEL_CHARS = 160

WARNING_LABEL = (
    "WARNING: Do not leave unattended; in the absence of real danger, "
    "unit will manufacture its own."
)


def get_warning_label() -> str:
    """Return the single-line human safety warning label."""
    return WARNING_LABEL


def validate_label(label: str) -> str:
    """Ensure the label satisfies the competition gate before writing."""
    if not label or not label.strip():
        raise ValueError("Warning label must not be empty or whitespace-only.")
    if "\n" in label or "\r" in label:
        raise ValueError("Warning label must be a single line.")
    if len(label) > MAX_LABEL_CHARS:
        raise ValueError(f"Warning label exceeds {MAX_LABEL_CHARS} characters.")
    label.encode("utf-8")
    return label


def write_entry(output_path: Path = DEFAULT_OUTPUT_PATH) -> Path:
    """Write the warning label deterministically as UTF-8 text."""
    label = validate_label(get_warning_label())
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(label, encoding="utf-8")
    return output_path


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) == 2 and args[0] == "--output":
        target = Path(args[1])
    elif len(args) == 0:
        target = DEFAULT_OUTPUT_PATH
    else:
        print("Usage: main.py [--output PATH]", file=sys.stderr)
        return 2

    write_entry(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
