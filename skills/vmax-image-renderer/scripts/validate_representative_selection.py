"""Validate that representative pages are selected only from approved page details."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

PAGE_FAMILY_CONTRACTS = {
    "OPENING": "OPENING", "COVER": "OPENING",
    "OVERVIEW": "OVERVIEW", "LESSON_OVERVIEW": "OVERVIEW",
    "VISUAL_MIND_MAP": "VISUAL_MIND_MAP", "LESSON_VISUAL_MAP": "VISUAL_MIND_MAP",
    "TEXT_READING_PAGE": "TEXT_READING", "PARAGRAPH_TEXT": "TEXT_READING", "TEXT_AND_CONTEXT": "TEXT_READING",
    "COMPREHENSION": "COMPREHENSION", "MEANING_COMPREHENSION": "COMPREHENSION",
    "RHETORIC": "RHETORIC", "RHETORIC_DISCOVERY": "RHETORIC",
    "SENTENCE_PATTERN": "SENTENCE_PATTERN",
    "CHARACTER_COMPARISON_PAGE": "SHAPE_NEAR", "SHAPE_NEAR": "SHAPE_NEAR",
    "POLYPHONIC": "POLYPHONIC", "POLYPHONIC_PAGE": "POLYPHONIC",
    "IDIOM": "IDIOM", "IDIOM_APPLICATION": "IDIOM",
    "LANGUAGE_ACTIVITY": "LANGUAGE_ACTIVITY", "TEXTBOOK_ACTIVITY": "LANGUAGE_ACTIVITY", "ACTIVITY": "LANGUAGE_ACTIVITY",
    "SUMMARY_TRANSFER": "SUMMARY_TRANSFER", "SUMMARY": "SUMMARY_TRANSFER", "TRANSFER": "SUMMARY_TRANSFER",
}


def canonical_hash(value: Any) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_spec_hash(page: dict[str, Any]) -> str:
    value = dict(page)
    value.pop("page_spec_sha256", None)
    return canonical_hash(value)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return value


def validate(selection_path: Path, page_detail_path: Path) -> None:
    selection = load_json(selection_path)
    page_detail_root = load_json(page_detail_path)
    page_detail = page_detail_root.get("page_detail_confirmation", page_detail_root)
    if not isinstance(page_detail, dict):
        raise ValueError("page-detail root must contain page_detail_confirmation object")
    if page_detail.get("status") != "approved":
        raise ValueError("PAGE_DETAIL_CONFIRMATION status must be approved")
    if selection.get("object_type") != "REPRESENTATIVE_PAGE_SELECTION":
        raise ValueError("REPRESENTATIVE_PAGE_SELECTION object_type is required")
    if selection.get("status") != "CONFIRMED" or selection.get("teacher_confirmation_status") != "CONFIRMED":
        raise ValueError("REPRESENTATIVE_PAGE_HOLD must be teacher-confirmed")
    if selection.get("selection_policy") != "FROM_APPROVED_PAGE_DETAIL_ONLY":
        raise ValueError("REPRESENTATIVE_PAGE_SOURCE_CONFLICT: selection policy is not locked")
    if selection.get("page_detail_confirmation_sha256") != file_hash(page_detail_path):
        raise ValueError("REPRESENTATIVE_PAGE_DETAIL_HASH_MISMATCH")
    page_number_system = page_detail.get("page_number_system")
    section_marker_system = page_detail.get("section_marker_system")
    navigation_confirmation = selection.get("navigation_system_confirmation")
    if not isinstance(page_number_system, dict) or not isinstance(section_marker_system, dict) or not isinstance(navigation_confirmation, dict) or navigation_confirmation.get("status") != "CONFIRMED":
        raise ValueError("PAGE_NAVIGATION_SYSTEM_UNCONFIRMED")
    page_number_hash = page_number_system.get("system_sha256")
    section_marker_hash = section_marker_system.get("system_sha256")
    if navigation_confirmation.get("page_number_system_sha256") != page_number_hash or navigation_confirmation.get("section_marker_system_sha256") != section_marker_hash:
        raise ValueError("PAGE_NAVIGATION_SYSTEM_HASH_MISMATCH")

    pages = page_detail.get("pages")
    selected = selection.get("selected_pages")
    required_families = selection.get("required_page_families")
    if not isinstance(pages, list) or not isinstance(selected, list) or not selected:
        raise ValueError("REPRESENTATIVE_PAGE_SELECTION_INCOMPLETE")
    if not isinstance(required_families, list) or not required_families:
        raise ValueError("REPRESENTATIVE_PAGE_FAMILY_COVERAGE_INCOMPLETE")
    coverage_matrix = selection.get("coverage_matrix")
    if not isinstance(coverage_matrix, list) or not coverage_matrix:
        raise ValueError("REPRESENTATIVE_PAGE_COVERAGE_MATRIX_MISSING")
    matrix_by_family = {}
    for row in coverage_matrix:
        if not isinstance(row, dict) or not row.get("page_family") or not row.get("contract_id") or not row.get("style_variant_id") or not row.get("representative_id"):
            raise ValueError("REPRESENTATIVE_PAGE_COVERAGE_MATRIX_INCOMPLETE")
        family = row["page_family"]
        if family in matrix_by_family:
            raise ValueError("REPRESENTATIVE_PAGE_COVERAGE_MATRIX_DUPLICATE")
        if PAGE_FAMILY_CONTRACTS.get(family) != row["contract_id"]:
            raise ValueError(f"REPRESENTATIVE_PAGE_COVERAGE_MATRIX_CONTRACT_MISMATCH: {family}")
        matrix_by_family[family] = row

    page_by_id = {page.get("page_id"): page for page in pages if isinstance(page, dict)}
    if len(page_by_id) != len(pages):
        raise ValueError("PAGE_DETAIL_PAGE_ID_DUPLICATE")
    actual_families = {page.get("page_family") for page in pages if page.get("page_family")}
    if not actual_families.issubset(set(required_families)):
        raise ValueError("REPRESENTATIVE_PAGE_FAMILY_COVERAGE_INCOMPLETE")

    selected_ids: set[str] = set()
    covered_families: set[str] = set()
    for entry in selected:
        if not isinstance(entry, dict):
            raise ValueError("REPRESENTATIVE_PAGE_SELECTION_INCOMPLETE")
        page_id = entry.get("page_detail_page_id")
        if not page_id or page_id in selected_ids:
            raise ValueError("REPRESENTATIVE_PAGE_ID_DUPLICATE")
        page = page_by_id.get(page_id)
        if page is None:
            raise ValueError(f"REPRESENTATIVE_PAGE_SOURCE_CONFLICT: undeclared page {page_id}")
        expected_hash = page_spec_hash(page)
        if page.get("page_spec_sha256") != expected_hash or entry.get("page_spec_sha256") != expected_hash:
            raise ValueError(f"REPRESENTATIVE_PAGE_SPEC_HASH_MISMATCH: {page_id}")
        if not entry.get("representative_id") or not isinstance(entry.get("verification_scope"), list) or not entry["verification_scope"]:
            raise ValueError(f"REPRESENTATIVE_PAGE_SELECTION_INCOMPLETE: {page_id}")
        selected_ids.add(page_id)
        covered_families.add(page.get("page_family"))
        matrix = matrix_by_family.get(page.get("page_family"))
        if matrix is None or matrix.get("representative_id") != entry.get("representative_id"):
            raise ValueError(f"REPRESENTATIVE_PAGE_COVERAGE_MATRIX_MISMATCH: {page_id}")

    missing = sorted(set(required_families) - covered_families)
    if missing:
        raise ValueError(f"REPRESENTATIVE_PAGE_FAMILY_COVERAGE_INCOMPLETE: {','.join(missing)}")
    if set(matrix_by_family) != set(required_families):
        raise ValueError("REPRESENTATIVE_PAGE_COVERAGE_MATRIX_FAMILY_DRIFT")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selection", required=True, type=Path)
    parser.add_argument("--page-detail", required=True, type=Path)
    args = parser.parse_args()
    try:
        validate(args.selection, args.page_detail)
    except ValueError as exc:
        print(f"REPRESENTATIVE_PAGE_SELECTION_FAIL: {exc}")
        return 1
    print("Representative page selection passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
