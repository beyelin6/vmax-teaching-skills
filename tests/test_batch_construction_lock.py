from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/vmax-image-renderer/scripts/validate_batch_lock.py"
SPEC = importlib.util.spec_from_file_location("validate_batch_lock", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class BatchConstructionLockTests(unittest.TestCase):
    def make_fixture(self, root: Path) -> tuple[Path, Path, Path, Path]:
        page = {
            "page_id": "S001",
            "sequence_index": 1,
            "page_family": "IDIOM",
            "source_refs": ["LKB:S001"],
            "layout_spec": {"composition": "SCENE"},
        }
        page["page_spec_sha256"] = MODULE.page_spec_hash(page)
        page_detail = {
            "page_detail_confirmation": {
                "status": "approved",
                "batch_lock_mode": "EXACT_PAGE_DETAIL",
                "pages": [page],
            }
        }
        style_selection = {
            "object_type": "STYLE_SELECTION_PROFILE",
            "status": "CONFIRMED",
            "teacher_confirmation_status": "CONFIRMED",
            "style_core": {"style_core_id": "STYLE-WARM-001"},
        }
        page_detail_path = root / "page-detail.json"
        style_path = root / "style-selection.json"
        role_path = root / "role-selection.json"
        registry_path = root / "ROLE-NEW-001.md"
        slide_path = root / "slide-script.json"
        page_detail_path.write_text(json.dumps(page_detail, ensure_ascii=False), encoding="utf-8")
        style_path.write_text(json.dumps(style_selection, ensure_ascii=False), encoding="utf-8")
        registry_path.write_text("character_id: ROLE-NEW-001\nreuse_level: LESSON_ONLY\ncore_dna_ref: ROLE-NEW-001:CORE-DNA\napproved_asset_refs: [asset-001]\n", encoding="utf-8")
        role_selection = {
            "status": "CONFIRMED",
            "teacher_confirmation_status": "CONFIRMED",
            "character_origin": "NEW_CHARACTER",
            "base_character_id": "ROLE-NEW-001",
            "core_dna_ref": "ROLE-NEW-001:CORE-DNA",
            "registry_writeback": {
                "status": "COMPLETE",
                "registry_ref": registry_path.name,
                "registry_sha256": MODULE.file_hash(registry_path),
                "reuse_level": "LESSON_ONLY",
                "approved_asset_refs": ["asset-001"],
                "teacher_confirmation_ref": "TEACHER-ROLE-001",
            },
        }
        role_path.write_text(json.dumps(role_selection, ensure_ascii=False), encoding="utf-8")
        page_hash = MODULE.page_spec_hash(page)
        detail_hash = MODULE.file_hash(page_detail_path)
        style_hash = MODULE.file_hash(style_path)
        role_hash = MODULE.file_hash(role_path)
        slide = {
            "slide_id": "S001",
            "sequence": 1,
            "page_family": "IDIOM",
            "style_core_id": "STYLE-WARM-001",
            "source_refs": ["LKB:S001"],
            "page_detail_page_sha256": page_hash,
            "page_detail_confirmation_sha256": detail_hash,
            "render_request": {
                "page_detail_page_sha256": page_hash,
                "page_detail_confirmation_sha256": detail_hash,
                "style_core_id": "STYLE-WARM-001",
            },
        }
        slide_script = {
            "batch_lock": {
                "status": "LOCKED",
                "mode": "EXACT_PAGE_DETAIL",
                "page_detail_confirmation_ref": "page-detail.json",
                "page_detail_confirmation_sha256": detail_hash,
                "style_selection_ref": "style-selection.json",
                "style_selection_sha256": style_hash,
                "selected_style_id": "STYLE-WARM-001",
                "role_selection_ref": "role-selection.json",
                "role_selection_sha256": role_hash,
                "pages": [{"slide_id": "S001", "page_detail_page_id": "S001", "page_spec_sha256": page_hash}],
            },
            "slides": [slide],
        }
        slide_path.write_text(json.dumps(slide_script, ensure_ascii=False), encoding="utf-8")
        return slide_path, page_detail_path, style_path, role_path

    def test_exact_page_and_style_lock_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            paths = self.make_fixture(Path(temp))
            MODULE.validate(*paths)

    def test_unconfirmed_style_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            slide, page_detail, style, role = self.make_fixture(Path(temp))
            payload = json.loads(style.read_text(encoding="utf-8"))
            payload["status"] = "TEACHER_REVIEW"
            style.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "STYLE_SELECTION_REQUIRED"):
                MODULE.validate(slide, page_detail, style, role)

    def test_page_detail_change_invalidates_batch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            slide, page_detail, style, role = self.make_fixture(Path(temp))
            payload = json.loads(page_detail.read_text(encoding="utf-8"))
            payload["page_detail_confirmation"]["pages"][0]["layout_spec"]["composition"] = "OTHER"
            page_detail.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "PAGE_DETAIL_HASH_MISMATCH"):
                MODULE.validate(slide, page_detail, style, role)


if __name__ == "__main__":
    unittest.main()
