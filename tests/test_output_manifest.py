"""Reject unsupported completion claims while preserving draft handoffs."""
import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1] / "core/schemas/vmax"


class OutputManifestTests(unittest.TestCase):
    def setUp(self):
        schema = json.loads((ROOT / "output-manifest.schema.json").read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.validator = Draft202012Validator(schema)
        self.manifest = json.loads((ROOT / "examples/output-manifest.example.json").read_text(encoding="utf-8"))

    def test_example_and_draft_handoff_are_valid(self):
        self.assertTrue(self.validator.is_valid(self.manifest))
        self.assertEqual(self.manifest["outputs"][0]["status"], "HANDOFF_READY")
        self.assertIsNone(self.manifest["outputs"][0]["asset_ref"])

    def test_verified_output_requires_asset_and_report(self):
        item = self.manifest["outputs"][0]
        item.update(format="PNG", status="RENDER_VERIFIED", asset_ref="assets/P01.png",
                    verification_report_ref="validation/P01.md")
        self.assertTrue(self.validator.is_valid(self.manifest))
        for field in ("asset_ref", "verification_report_ref"):
            for value in (None, "", "MISSING"):
                with self.subTest(field=field, value=value):
                    bad = copy.deepcopy(self.manifest)
                    if value == "MISSING":
                        del bad["outputs"][0][field]
                    else:
                        bad["outputs"][0][field] = value
                    self.assertFalse(self.validator.is_valid(bad))

    def test_approved_requires_confirmation_and_output(self):
        self.manifest["status"] = "APPROVED"
        for value in ("NOT_REVIEWED", "WAITING_TEACHER", "CHANGES_REQUESTED", None):
            with self.subTest(confirmation=value):
                bad = copy.deepcopy(self.manifest)
                if value is None:
                    del bad["teacher_confirmation_status"]
                else:
                    bad["teacher_confirmation_status"] = value
                self.assertFalse(self.validator.is_valid(bad))
        self.manifest["teacher_confirmation_status"] = "CONFIRMED"
        self.assertTrue(self.validator.is_valid(self.manifest))
        self.manifest["outputs"] = []
        self.assertFalse(self.validator.is_valid(self.manifest))

    def test_canvas_is_required(self):
        del self.manifest["canvas_lock"]
        self.assertFalse(self.validator.is_valid(self.manifest))


if __name__ == "__main__":
    unittest.main()
