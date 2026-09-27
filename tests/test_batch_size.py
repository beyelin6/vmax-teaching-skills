from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/vmax-image-renderer/scripts/validate_batch_size.py"
SPEC = importlib.util.spec_from_file_location("validate_batch_size", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class BatchSizeTests(unittest.TestCase):
    def test_standard_batch_accepts_four_through_eight(self) -> None:
        for count in (4, 5, 6, 7, 8):
            with self.subTest(count=count):
                MODULE.validate_batch_size(count)

    def test_standard_batch_rejects_fewer_than_four(self) -> None:
        with self.assertRaisesRegex(ValueError, "STANDARD_BATCH_MIN_4"):
            MODULE.validate_batch_size(3)

    def test_no_batch_may_exceed_eight(self) -> None:
        with self.assertRaisesRegex(ValueError, "BATCH_SIZE_EXCEEDS_MAX_8"):
            MODULE.validate_batch_size(9, "tail", "remaining")

    def test_exception_batch_can_be_smaller_with_reason(self) -> None:
        for batch_type in ("tail", "correction", "teacher-request"):
            with self.subTest(batch_type=batch_type):
                MODULE.validate_batch_size(1, batch_type, "documented reason")

    def test_exception_batch_requires_reason(self) -> None:
        with self.assertRaisesRegex(ValueError, "BATCH_EXCEPTION_REASON_REQUIRED"):
            MODULE.validate_batch_size(2, "correction")


if __name__ == "__main__":
    unittest.main()
