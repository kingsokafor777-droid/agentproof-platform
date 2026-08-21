from __future__ import annotations

import contextlib
import importlib.util
import io
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPOSITORY_ROOT / "scripts" / "validate_docs.py"
SPEC = importlib.util.spec_from_file_location("validate_docs", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class DocumentationValidatorTest(unittest.TestCase):
    def copied_repository(self) -> tempfile.TemporaryDirectory[str]:
        temporary = tempfile.TemporaryDirectory[str]()
        destination = Path(temporary.name) / "platform"
        shutil.copytree(
            REPOSITORY_ROOT,
            destination,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        self.addCleanup(temporary.cleanup)
        return temporary

    def run_validator(self, root: Path) -> tuple[int, str]:
        stream = io.StringIO()
        with patch.object(VALIDATOR, "ROOT", root), contextlib.redirect_stderr(stream):
            return VALIDATOR.main(), stream.getvalue()

    def test_current_repository_is_valid(self) -> None:
        temporary = self.copied_repository()
        status, output = self.run_validator(Path(temporary.name) / "platform")
        self.assertEqual(status, 0, output)

    def test_broken_relative_link_fails_closed(self) -> None:
        temporary = self.copied_repository()
        root = Path(temporary.name) / "platform"
        readme = root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n[broken](missing.md)\n", encoding="utf-8")
        status, output = self.run_validator(root)
        self.assertEqual(status, 1)
        self.assertIn("broken relative link", output)

    def test_mutable_workflow_pin_fails_closed(self) -> None:
        temporary = self.copied_repository()
        root = Path(temporary.name) / "platform"
        workflow = root / ".github" / "workflows" / "ci.yml"
        workflow.write_text(
            workflow.read_text(encoding="utf-8").replace(
                "actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
                "actions/checkout@v4",
            ),
            encoding="utf-8",
        )
        status, output = self.run_validator(root)
        self.assertEqual(status, 1)
        self.assertIn("mutable or malformed action pin", output)
