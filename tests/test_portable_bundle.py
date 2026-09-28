"""Offline packaging and checkpoint contracts; does not simulate an LLM or platform UI."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_portable_bundle import build, rewrite, source_inventory
from verify_portable_bundle import verify


class PortableBundleTests(unittest.TestCase):
    def test_targets_have_one_entry_and_required_quality_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            for target in ("claude", "chatgpt", "antigravity", "codex"):
                with self.subTest(target=target):
                    root, archive = build(tmp, target)
                    manifest = verify(root)
                    self.assertEqual(manifest["target"], target)
                    self.assertTrue(archive.is_file())
                    self.assertTrue((root / "docs/V-MAX_Quality_Standard.md").is_file())
                    self.assertTrue((root / "docs/TEACHING_DNA.md").is_file())
                    self.assertTrue((root / "libraries").is_dir())
                    self.assertTrue((root / f"adapters/{target}.md").is_file())
                    self.assertEqual(len(list(root.rglob("SKILL.md"))), 1)
                    self.assertIn("skills/prestudy-worksheet/MODULE.md", (root / "SKILL.md").read_text(encoding="utf-8"))
                    # Extract elsewhere and run there: no repo-relative working directory.
                    unpack = Path(tmp) / "unpacked" / target
                    with zipfile.ZipFile(archive) as bundle:
                        bundle.extractall(unpack)
                    extracted = unpack / "vmax-chinese-teaching"
                    subprocess.run([sys.executable, str(extracted / "scripts/verify_portable_bundle.py"), str(extracted)], cwd=unpack, check=True, capture_output=True)
                    with self.assertRaises(FileExistsError):
                        build(tmp, target)

    def test_archive_without_git_matches_checkout_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "extracted"
            source.mkdir()
            names, _, _, _ = source_inventory(ROOT)
            for name in names + ["packaging/portable-entry.md"]:
                dest = source / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, dest)
            (source / ".env").write_text("secret")
            (source / "notes.txt").write_text("private")
            cache = source / "scripts/__pycache__"
            cache.mkdir()
            (cache / "junk.pyc").write_bytes(b"cache")
            before, _ = build(Path(tmp) / "git-output", "claude")
            after, _ = build(Path(tmp) / "archive-output", "claude", source)
            left, right = verify(before), verify(after)
            self.assertEqual(right["source_commit"], "unknown")
            self.assertIsNone(right["source_dirty"])
            self.assertEqual(right["source_kind"], "archive")
            self.assertEqual(left["files"], right["files"])
            self.assertFalse((after / "docs/visual-validation").exists())
            self.assertFalse(list((after / "tests").glob("*.py")))
            self.assertTrue((after / "tests/workflow-hold-regression-cases.md").is_file())

    def test_tampered_source_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, _ = build(tmp, "claude")
            (root / "VERSION").write_text("0.0.0")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                verify(root)

    def test_remote_urls_are_not_relocated(self):
        path = "skills/example/SKILL.md"
        text = f"`{path}` https://github.com/example/repo/blob/main/{path}"
        result = rewrite(text, {path: "skills/example/MODULE.md"})
        self.assertIn("`skills/example/MODULE.md`", result)
        self.assertIn("/main/skills/example/SKILL.md", result)


class PortableCheckpointTests(unittest.TestCase):
    def test_verified_requires_readback_and_approvals_require_revision(self):
        schema = json.loads((ROOT / "schemas/portable-checkpoint.schema.json").read_text())
        validator = Draft202012Validator(schema)
        payload = dict(lesson_id="test-lesson", revision="r2", previous_revision="r1", backend="LOCAL",
                       status="EXPORTED_UNACKNOWLEDGED", state={"current_stage": "VP3_PAGE_PLAN_REVIEW", "next_allowed_stage": []},
                       approval_scope=[], artifacts=[])
        self.assertTrue(validator.is_valid(payload))
        payload["status"] = "VERIFIED"
        self.assertFalse(validator.is_valid(payload))
        payload["readback_evidence"] = "readback:test-r2"
        self.assertTrue(validator.is_valid(payload))
        payload["approval_scope"] = [{"artifact_ref": "plan-v1", "teacher_event_ref": "event-1"}]
        self.assertFalse(validator.is_valid(payload))
        payload["approval_scope"][0]["revision"] = "v1"
        self.assertTrue(validator.is_valid(payload))
        payload["state"]["next_allowed_stage"] = ["VP4_CHARACTER_REVIEW", "VP5_BATCH_REVIEW"]
        self.assertFalse(validator.is_valid(payload))


if __name__ == "__main__":
    unittest.main()
