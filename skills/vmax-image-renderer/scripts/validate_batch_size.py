"""Validate V-MAX presentation batch size against the shared policy."""

from __future__ import annotations

import argparse
import sys


EXCEPTION_TYPES = {"tail", "correction", "teacher-request"}


def validate_batch_size(count: int, batch_type: str = "standard", reason: str = "") -> None:
    if batch_type not in EXCEPTION_TYPES | {"standard"}:
        raise ValueError("BATCH_TYPE_INVALID")
    if count > 8:
        raise ValueError("BATCH_SIZE_EXCEEDS_MAX_8")
    if count < 1:
        raise ValueError("BATCH_SIZE_MUST_BE_POSITIVE")
    if batch_type == "standard" and count < 4:
        raise ValueError("STANDARD_BATCH_MIN_4; use tail/correction/teacher-request with a reason")
    if batch_type in EXCEPTION_TYPES and not reason.strip():
        raise ValueError("BATCH_EXCEPTION_REASON_REQUIRED")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count", type=int, required=True, help="number of pages in this batch")
    parser.add_argument("--batch-type", choices=("standard", "tail", "correction", "teacher-request"), default="standard")
    parser.add_argument("--reason", default="", help="required for non-standard batches and saved with Runtime")
    args = parser.parse_args()
    try:
        validate_batch_size(args.count, args.batch_type, args.reason)
    except ValueError as exc:
        print(f"BATCH_SIZE_INVALID: {exc}", file=sys.stderr)
        return 1
    print(f"BATCH_SIZE_PASS: count={args.count}; type={args.batch_type}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
