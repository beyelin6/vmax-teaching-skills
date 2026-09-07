"""Decision evidence must precede resolving holds or approving revisions."""
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1] / "core/schemas/vmax"


class StateDecisionTests(unittest.TestCase):
    def valid(self, name, payload):
        schema = json.loads((ROOT / (name + ".schema.json")).read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        return Draft202012Validator(schema).is_valid(payload)

    def test_open_hold_example(self):
        payload = json.loads((ROOT / "examples/hold-event.example.json").read_text(encoding="utf-8"))
        self.assertTrue(self.valid("hold-event", payload))

    def test_terminal_hold_requires_decision(self):
        payload = json.loads((ROOT / "examples/hold-event.example.json").read_text(encoding="utf-8"))
        for status in ("TEACHER_DECIDED", "RESOLVED", "CANCELLED"):
            for event in (None, "", "decision-1"):
                with self.subTest(status=status, event=event):
                    candidate = dict(payload, status=status, teacher_decision_event=event)
                    self.assertEqual(self.valid("hold-event", candidate), event == "decision-1")
            candidate = dict(payload, status=status)
            del candidate["teacher_decision_event"]
            self.assertFalse(self.valid("hold-event", candidate))

    def revision(self):
        return dict(object_type="REVISION_EVENT", revision_id="r1", lesson_id="l1",
                    trigger="LOCAL_PAGE_PATCH", changed_object="SLIDE_SCRIPT:ss1",
                    affected_downstream=[], recommended_return_phase="PHASE_3",
                    unchanged_objects=[], teacher_decision_required="Confirm patch scope")

    def test_revision_requires_explicit_status(self):
        payload = self.revision()
        self.assertFalse(self.valid("revision-event", payload))
        for status in ("OPEN", "WAITING_TEACHER"):
            self.assertTrue(self.valid("revision-event", dict(payload, status=status)))

    def test_revision_approval_requires_version_and_decision(self):
        payload = dict(self.revision(), status="APPROVED", changed_version="ss2",
                       teacher_decision_event="decision-2")
        self.assertTrue(self.valid("revision-event", payload))
        for field in ("changed_version", "teacher_decision_event"):
            missing = {k: v for k, v in payload.items() if k != field}
            self.assertFalse(self.valid("revision-event", missing))
            for value in (None, ""):
                self.assertFalse(self.valid("revision-event", dict(payload, **{field: value})))

    def test_cancelled_revision_requires_decision_but_not_new_version(self):
        payload = dict(self.revision(), status="CANCELLED")
        self.assertFalse(self.valid("revision-event", payload))
        self.assertTrue(self.valid("revision-event", dict(payload, teacher_decision_event="cancel-1")))


if __name__ == "__main__":
    unittest.main()
