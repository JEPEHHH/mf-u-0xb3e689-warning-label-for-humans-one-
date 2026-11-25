#!/usr/bin/env python3
"""Local validation suite for the Warning Label for Humans program/v1 entry."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import main as entry_main

REPO_ROOT = Path(__file__).resolve().parent


class TestWarningLabelEntry(unittest.TestCase):
    def test_default_output_path_is_competition_target(self) -> None:
        self.assertEqual(entry_main.DEFAULT_OUTPUT_PATH, Path("/output/entry.txt"))

    def test_cli_execution_and_determinism(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            first_out = Path(tmpdir) / "run1" / "entry.txt"
            second_out = Path(tmpdir) / "run2" / "entry.txt"

            for target in (first_out, second_out):
                result = subprocess.run(
                    [sys.executable, str(REPO_ROOT / "main.py"), "--output", str(target)],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, msg=result.stderr)
                self.assertTrue(target.is_file(), msg=f"Missing output file: {target}")

            raw_first = first_out.read_bytes()
            raw_second = second_out.read_bytes()
            self.assertEqual(raw_first, raw_second, "Entry output must be deterministic across runs")

            text = raw_first.decode("utf-8")
            self.assertTrue(text.strip(), "Entry must not be empty or whitespace-only")
            self.assertNotIn("\n", text, "Entry must be a single line without newlines")
            self.assertNotIn("\r", text, "Entry must not contain carriage returns")
            self.assertGreaterEqual(len(text), 1)
            self.assertLessEqual(len(text), 160)

    def test_default_invocation_writes_to_default_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_default = Path(tmpdir) / "output" / "entry.txt"
            with mock.patch.object(entry_main, "DEFAULT_OUTPUT_PATH", fake_default):
                exit_code = entry_main.main([])
            self.assertEqual(exit_code, 0)
            self.assertTrue(fake_default.is_file())
            self.assertEqual(
                fake_default.read_text(encoding="utf-8"),
                entry_main.get_warning_label(),
            )

    def test_validate_label_rejects_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            entry_main.validate_label("")
        with self.assertRaises(ValueError):
            entry_main.validate_label("   \t  ")
        with self.assertRaises(ValueError):
            entry_main.validate_label("Line one\nLine two")
        with self.assertRaises(ValueError):
            entry_main.validate_label("X" * 161)

    def test_license_present_and_osi_spdx(self) -> None:
        license_path = REPO_ROOT / "LICENSE"
        self.assertTrue(license_path.is_file(), "LICENSE file must exist at repo root")
        content = license_path.read_text(encoding="utf-8")
        self.assertIn("SPDX-License-Identifier: MIT", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
