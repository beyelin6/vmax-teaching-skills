"""Behavioral regression tests for teacher approval and workflow gates."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class ApprovalContracts(unittest.TestCase):
    def valid(self, name, payload):
        schema = json.loads(read(f"core/schemas/vmax/{name}.schema.json"))
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema).is_valid(payload)

    def test_transition_requires_approval_evidence(self):
        for before, after in [("TEACHER_REVIEW", "LESSON_LOCKED"),
                              ("OUTPUT_QA", "APPROVED_OUTPUT")]:
            payload = dict(object_type="STATUS_TRANSITION", transition_id="t1",
                           object_id="o1", from_status=before, to_status=after,
                           trigger="approve", actor_type="TEACHER",
                           teacher_confirmation_ref="confirmation-1")
            if after == "APPROVED_OUTPUT":
                payload["qa_gate_summary"] = {"result": "PASS"}
            self.assertTrue(self.valid("status-transition", payload))
            for field in ["teacher_confirmation_ref"] + (
                    ["qa_gate_summary"] if after == "APPROVED_OUTPUT" else []):
                with self.subTest(after=after, field=field):
                    missing = {k: v for k, v in payload.items() if k != field}
                    self.assertFalse(self.valid("status-transition", missing))
                    self.assertFalse(self.valid("status-transition", dict(payload, **{field: None})))
            self.assertFalse(self.valid("status-transition", dict(payload, teacher_confirmation_ref="")))
            self.assertFalse(self.valid("status-transition", dict(payload, actor_type="AGENT")))

    def test_selection_status_lifecycle(self):
        payload = dict(object_type="APPROVED_TEACHING_SELECTION", lesson_id="l1",
                       source_master_version="1", candidate_inventory_version="1",
                       version="1", selections=[])
        cases = [
            ("TEACHER_REVIEW", None, True),
            ("TEACHER_REVIEW", "WAITING_TEACHER", True),
            ("TEACHER_REVIEW", "CONFIRMED", False),
            ("LESSON_LOCKED", None, False),
            ("LESSON_LOCKED", "WAITING_TEACHER", False),
            ("LESSON_LOCKED", "CONFIRMED", True),
            ("SUPERSEDED", "CONFIRMED", True),
        ]
        for status, confirmation, expected in cases:
            with self.subTest(status=status, confirmation=confirmation):
                candidate = dict(payload, status=status)
                if confirmation is not None:
                    candidate["teacher_confirmation_status"] = confirmation
                self.assertEqual(self.valid("approved-teaching-selection", candidate), expected)

    def test_repository_examples(self):
        for name in ("status-transition", "approved-teaching-selection"):
            with self.subTest(name=name):
                payload = json.loads(read(f"core/schemas/vmax/examples/{name}.example.json"))
                self.assertTrue(self.valid(name, payload))


class WorkflowContracts(unittest.TestCase):
    def test_style_gate_order_matches_main_workflow(self):
        def sequence(path):
            text = read(path)
            start = text.index("→ Visual Grammar / Slide Architecture")
            end = text.index("→ 代表頁驗證", start)
            return text[start:end].strip()
        self.assertEqual(sequence("core/governance/vmax-main-workflow.md"),
                         sequence("skills/vmax-golden-path-executor/SKILL.md"))

    def test_no_idiom_runtime_keeps_confirmation_gate(self):
        text = read("runtime/lesson-state.md")
        branch = text.split("→ STEP_2_6 = N/A_NO_IDIOM", 1)[1].split("```", 1)[0]
        self.assertEqual([line.strip() for line in branch.splitlines() if line.strip()],
                         ["→ HOLD_2_6", "→ HOLD_2_6 confirmed", "→ TEACHER_INTENT_LOCK"])

    def test_incomplete_coverage_is_not_reviewable(self):
        for path in ("core/governance/vmax-main-workflow.md",
                     "skills/vmax-golden-path-executor/SKILL.md"):
            with self.subTest(path=path):
                rule = next(line for line in read(path).splitlines()
                            if "STEP2.5_COVERAGE_INCOMPLETE" in line)
                self.assertIn("不得進入 HOLD 2.5", rule)


if __name__ == "__main__":
    unittest.main()
