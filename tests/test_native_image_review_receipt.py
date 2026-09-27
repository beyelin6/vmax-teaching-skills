from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/vmax-image-renderer/scripts/validate_native_image_review_receipt.py"
SPEC = importlib.util.spec_from_file_location("validate_native_image_review_receipt", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class NativeImageReviewReceiptTests(unittest.TestCase):
    def setUp(self) -> None:
        self.available = {
            "object_type": "NATIVE_IMAGE_REVIEW_RECEIPT",
            "status": "AVAILABLE",
            "provider": "CHATGPT_NATIVE_IMAGE",
            "tool_operation": "EDIT",
            "source_image_ref": "image:approved-source",
            "output_image_ref": "image:edited-output",
            "page_ids": ["P05"],
            "page_spec_sha256": "sha256:page",
            "review_revision": "r2",
            "editable_entry_available": True,
        }

    def write_receipt(self, value: dict) -> Path:
        temp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False)
        with temp:
            json.dump(value, temp)
        self.addCleanup(Path(temp.name).unlink, missing_ok=True)
        return Path(temp.name)

    def test_native_edit_entry_is_valid(self) -> None:
        MODULE.validate(self.write_receipt(self.available))

    def test_preview_only_cannot_claim_native_edit_entry(self) -> None:
        preview_only = {**self.available, "editable_entry_available": False}
        with self.assertRaisesRegex(ValueError, "NATIVE_IMAGE_EDIT_ENTRY_MISSING"):
            MODULE.validate(self.write_receipt(preview_only))

    def test_unavailable_native_tool_requires_reason(self) -> None:
        unavailable = {"object_type": "NATIVE_IMAGE_REVIEW_RECEIPT", "status": "UNAVAILABLE"}
        with self.assertRaisesRegex(ValueError, "NATIVE_IMAGE_REVIEW_UNAVAILABLE_REASON_MISSING"):
            MODULE.validate(self.write_receipt(unavailable))
        unavailable["unavailable_reason"] = "Platform has preview only"
        MODULE.validate(self.write_receipt(unavailable))


if __name__ == "__main__":
    unittest.main()
