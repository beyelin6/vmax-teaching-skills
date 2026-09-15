from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/vmax-image-renderer/scripts/validate_representative_selection.py"
SPEC = importlib.util.spec_from_file_location("validate_representative_selection", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class RepresentativePageSelectionTests(unittest.TestCase):
    def fixture(self, root: Path) -> tuple[Path, Path]:
        page = {
            "page_id": "S001",
            "sequence_index": 1,
            "page_family": "IDIOM",
            "student_visible_text": {"body": ["例句"]},
            "image_spec": {"purpose": "理解成語", "scene": "教室", "text_in_image": False},
            "layout_spec": {"layout_id": "L1"},
        }
        page["page_spec_sha256"] = MODULE.page_spec_hash(page)
        page_detail = {"page_detail_confirmation": {"status": "approved", "pages": [page]}}
        page_detail_path = root / "page-detail.json"
        page_detail_path.write_text(json.dumps(page_detail, ensure_ascii=False), encoding="utf-8")
        selection = {
            "object_type": "REPRESENTATIVE_PAGE_SELECTION",
            "status": "CONFIRMED",
            "teacher_confirmation_status": "CONFIRMED",
            "selection_policy": "FROM_APPROVED_PAGE_DETAIL_ONLY",
            "page_detail_confirmation_ref": page_detail_path.name,
            "page_detail_confirmation_sha256": MODULE.file_hash(page_detail_path),
            "required_page_families": ["IDIOM"],
            "coverage_matrix": [{
                "page_family": "IDIOM",
                "contract_id": "IDIOM",
                "style_variant_id": "STYLE-WARM-001:IDIOM",
                "representative_id": "REP-001",
                "status": "PENDING_TEACHER_REVIEW",
            }],
            "selected_pages": [{
                "representative_id": "REP-001",
                "page_detail_page_id": "S001",
                "page_spec_sha256": page["page_spec_sha256"],
                "verification_scope": ["TEXT", "IMAGE", "LAYOUT"],
            }],
        }
        selection_path = root / "representative-selection.json"
        selection_path.write_text(json.dumps(selection, ensure_ascii=False), encoding="utf-8")
        return selection_path, page_detail_path

    def test_selection_must_reference_approved_page_detail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            selection, page_detail = self.fixture(Path(temp))
            MODULE.validate(selection, page_detail)

    def test_undeclared_page_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            selection, page_detail = self.fixture(Path(temp))
            payload = json.loads(selection.read_text(encoding="utf-8"))
            payload["selected_pages"][0]["page_detail_page_id"] = "S999"
            selection.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "REPRESENTATIVE_PAGE_SOURCE_CONFLICT"):
                MODULE.validate(selection, page_detail)

    def test_page_detail_change_invalidates_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            selection, page_detail = self.fixture(Path(temp))
            payload = json.loads(page_detail.read_text(encoding="utf-8"))
            payload["page_detail_confirmation"]["pages"][0]["layout_spec"]["layout_id"] = "L2"
            page_detail.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "REPRESENTATIVE_PAGE_DETAIL_HASH_MISMATCH"):
                MODULE.validate(selection, page_detail)


if __name__ == "__main__":
    unittest.main()
