"""Data-contract checks for grouped approvals, not a live model workflow test."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


class GroupedReviewContractTests(unittest.TestCase):
    def setUp(self):
        schema = json.loads((ROOT / "core/schemas/vmax/approved-teaching-selection.schema.json").read_text(encoding="utf-8"))
        self.validator = Draft202012Validator(schema)
        self.payload = {
            "object_type": "APPROVED_TEACHING_SELECTION",
            "lesson_id": "example-lesson",
            "source_master_version": "source-r1",
            "candidate_inventory_version": "candidate-r1",
            "version": "selection-r1",
            "status": "LESSON_LOCKED",
            "teacher_confirmation_status": "CONFIRMED",
            "selections": [
                {"candidate_id": item, "decision": "MUST_TEACH", "student_visible": True,
                 "confirmed_by_teacher": True, "teacher_confirmation_ref": "review:vp1:r1"}
                for item in ("text-P1", "idiom-C1", "reading-inference-Q1")
            ],
        }

    def test_one_review_event_can_confirm_multiple_explicit_items(self):
        self.validator.validate(self.payload)

    def test_unconfirmed_candidate_cannot_become_approved_selection(self):
        self.payload["selections"][1]["confirmed_by_teacher"] = False
        self.assertTrue(list(self.validator.iter_errors(self.payload)))


if __name__ == "__main__":
    unittest.main()
