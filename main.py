#!/usr/bin/env python3
"""Program/v1 entrypoint for Warning Label for Humans: One Line, Big Laugh."""

from pathlib import Path
import sys

DEFAULT_OUTPUT_PATH = Path("/output/entry.txt")

WARNING_LABEL = (
    "WARNING: Do not leave idle; in the absence of real danger, "
    "unit will manufacture its own."
)


def get_warning_label() -> str:
    """Return the single-line human safety warning label."""
    return WARNING_LABEL


def write_entry(output_path: Path = DEFAULT_OUTPUT_PATH) -> Path:
    """Write the warning label deterministically as UTF-8 text."""
    label = get_warning_label()
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
