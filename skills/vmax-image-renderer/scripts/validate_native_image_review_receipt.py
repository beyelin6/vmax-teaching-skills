"""Validate the native image review receipt used for representative/batch inspection."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate(path: Path) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"NATIVE_IMAGE_REVIEW_RECEIPT_INVALID: {exc}") from exc
    if not isinstance(data, dict) or data.get("object_type") != "NATIVE_IMAGE_REVIEW_RECEIPT":
        raise ValueError("NATIVE_IMAGE_REVIEW_RECEIPT_INVALID")
    if data.get("status") == "UNAVAILABLE":
        if not data.get("unavailable_reason"):
            raise ValueError("NATIVE_IMAGE_REVIEW_UNAVAILABLE_REASON_MISSING")
        return
    required = ("provider", "tool_operation", "source_image_ref", "output_image_ref", "page_ids", "page_spec_sha256", "review_revision")
    if data.get("status") != "AVAILABLE" or any(not data.get(key) for key in required):
        raise ValueError("NATIVE_IMAGE_REVIEW_RECEIPT_INCOMPLETE")
    if data.get("provider") != "CHATGPT_NATIVE_IMAGE":
        raise ValueError("NATIVE_IMAGE_REVIEW_PROVIDER_INVALID")
    if data.get("tool_operation") not in {"GENERATE_OR_EDIT", "EDIT"}:
        raise ValueError("NATIVE_IMAGE_REVIEW_TOOL_INVALID")
    if data.get("editable_entry_available") is not True:
        raise ValueError("NATIVE_IMAGE_EDIT_ENTRY_MISSING")
    if not isinstance(data.get("page_ids"), list) or not data["page_ids"]:
        raise ValueError("NATIVE_IMAGE_REVIEW_PAGE_IDS_MISSING")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    try:
        validate(args.receipt)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print("Native image review receipt passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
