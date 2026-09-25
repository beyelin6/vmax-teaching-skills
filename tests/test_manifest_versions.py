"""Exercise manifest validation against temporary repositories, not policy wording."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from scripts import validate_repository as validator


class ManifestVersionsTest(unittest.TestCase):
    def check_manifest(self, entries, files, header="1.0", field="1.0"):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "V-MAX_MANIFEST.md").write_text(
                f"# V-MAX Manifest {header}\n\n```yaml\nvmax_manifest_version: {field}\n{entries}\n```\n",
                encoding="utf-8",
            )
            for name, content in files.items():
                (root / name).write_text(content, encoding="utf-8")
            with patch.object(validator, "ROOT", root), patch.object(validator, "ERRORS", []):
                validator.validate_manifest_paths()
                validator.validate_manifest_module_versions()
                return list(validator.ERRORS)

    def test_inline_versions_preserve_minor_digits(self):
        entries = 'workflow: { path: workflow.md, current_version: "2.10" }'
        self.assertEqual([], self.check_manifest(entries, {"workflow.md": "# Main Workflow 2.10\n"}))
        self.assertTrue(self.check_manifest(entries, {"workflow.md": "# Main Workflow 2.1\n"}))

    def test_multiline_and_english_version(self):
        entries = "handoff:\n  path: handoff.md\n  current_version: 1.2"
        self.assertEqual([], self.check_manifest(entries, {"handoff.md": "# Handoff\nVersion: 1.2\n"}))

    def test_missing_inline_path_and_missing_declaration(self):
        entries = "module: { path: absent.md, current_version: 1.0 }"
        self.assertTrue(self.check_manifest(entries, {}))
        self.assertTrue(self.check_manifest(entries, {"absent.md": "# No version\n"}))

    def test_manifest_heading_mismatch(self):
        self.assertTrue(self.check_manifest("module: { path: m.md, current_version: 1.0 }", {"m.md": "版本：1.0\n"}, field="1.1"))


if __name__ == "__main__":
    unittest.main()
