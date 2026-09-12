"""Validate that a batch Slide Script is bound to approved page and style profiles."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def canonical_hash(value: Any) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def page_spec_hash(page: dict[str, Any]) -> str:
    """Hash the page specification without its self-referential hash field."""
    value = dict(page)
    value.pop("page_spec_sha256", None)
    return canonical_hash(value)


def fail(message: str) -> None:
    raise ValueError(message)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read JSON {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"JSON root must be an object: {path}")
    return value


def validate(slide_script_path: Path, page_detail_path: Path, style_selection_path: Path, role_selection_path: Path) -> None:
    slide_script = load_json(slide_script_path)
    page_detail_root = load_json(page_detail_path)
    style_selection = load_json(style_selection_path)
    role_selection = load_json(role_selection_path)
    page_detail = page_detail_root.get("page_detail_confirmation", page_detail_root)
    if not isinstance(page_detail, dict):
        fail("page-detail root must contain page_detail_confirmation object")
    if page_detail.get("status") != "approved":
        fail("PAGE_DETAIL_CONFIRMATION status must be approved")
    if page_detail.get("batch_lock_mode") != "EXACT_PAGE_DETAIL":
        fail("PAGE_DETAIL_CONFIRMATION batch_lock_mode must be EXACT_PAGE_DETAIL")
    if style_selection.get("status") != "CONFIRMED" or style_selection.get("teacher_confirmation_status") != "CONFIRMED":
        fail("STYLE_SELECTION_REQUIRED: Style Selection Profile must be CONFIRMED")
    style_core = style_selection.get("style_core")
    if not isinstance(style_core, dict) or not style_core.get("style_core_id"):
        fail("STYLE_SELECTION_REQUIRED: selected style_core_id is missing")
    selected_style_id = style_core["style_core_id"]
    if role_selection.get("status") != "CONFIRMED" or role_selection.get("teacher_confirmation_status") != "CONFIRMED":
        fail("CHARACTER_REGISTRY_WRITEBACK_REQUIRED: Role Selection Profile must be CONFIRMED")
    role_origin = role_selection.get("character_origin")
    writeback = role_selection.get("registry_writeback") or {}
    registry_ref = writeback.get("registry_ref")
    registry_path: Path | None = None
    if role_origin == "NEW_CHARACTER":
        if writeback.get("status") != "COMPLETE" or writeback.get("reuse_level") not in {"LESSON_ONLY", "REUSABLE_CANDIDATE"}:
            fail("CHARACTER_REGISTRY_WRITEBACK_REQUIRED")
        if not registry_ref:
            fail("CHARACTER_REGISTRY_WRITEBACK_REQUIRED: registry_ref missing")
        registry_path = Path(registry_ref)
        if not registry_path.is_absolute():
            registry_path = role_selection_path.parent / registry_path
        if not registry_path.is_file():
            fail("CHARACTER_REGISTRY_WRITEBACK_REQUIRED: registry file missing")
        if writeback.get("registry_sha256") != file_hash(registry_path):
            fail("CHARACTER_REGISTRY_HASH_MISMATCH")
        base_character_id = role_selection.get("base_character_id")
        core_dna_ref = role_selection.get("core_dna_ref")
        asset_refs = writeback.get("approved_asset_refs") or []
        if not base_character_id or not core_dna_ref or not asset_refs:
            fail("CHARACTER_DNA_MISSING or CHARACTER_ASSET_UNBOUND")
        registry_text = registry_path.read_text(encoding="utf-8", errors="replace")
        if base_character_id not in registry_text or core_dna_ref not in registry_text or any(asset not in registry_text for asset in asset_refs):
            fail("CHARACTER_REGISTRY_WRITEBACK_REQUIRED: registry record is incomplete")

    batch_lock = slide_script.get("batch_lock")
    if not isinstance(batch_lock, dict):
        fail("BATCH_CONSTRUCTION_LOCK missing from Slide Script")
    if batch_lock.get("status") != "LOCKED" or batch_lock.get("mode") != "EXACT_PAGE_DETAIL":
        fail("batch_lock must be LOCKED with EXACT_PAGE_DETAIL mode")
    expected_file_hash = file_hash(page_detail_path)
    expected_style_hash = file_hash(style_selection_path)
    if batch_lock.get("page_detail_confirmation_sha256") != expected_file_hash:
        fail("PAGE_DETAIL_HASH_MISMATCH")
    if batch_lock.get("style_selection_sha256") != expected_style_hash:
        fail("STYLE_SELECTION_HASH_MISMATCH")
    expected_role_hash = file_hash(role_selection_path)
    if batch_lock.get("role_selection_sha256") != expected_role_hash:
        fail("CHARACTER_REGISTRY_HASH_MISMATCH")
    if batch_lock.get("selected_style_id") != selected_style_id:
        fail("STYLE_DRIFT: selected_style_id does not match confirmed Style Selection Profile")
    if not batch_lock.get("page_detail_confirmation_ref") or not batch_lock.get("style_selection_ref"):
        fail("batch_lock source references are required")

    pages = page_detail.get("pages")
    slides = slide_script.get("slides")
    lock_pages = batch_lock.get("pages")
    if not isinstance(pages, list) or not isinstance(slides, list) or not isinstance(lock_pages, list):
        fail("pages, slides and batch_lock.pages must be arrays")
    if len(slides) != len(pages) or len(lock_pages) != len(pages):
        fail("UNDECLARED_PAGE or missing page in batch lock")

    page_by_id = {page.get("page_id"): page for page in pages if isinstance(page, dict)}
    lock_by_slide = {entry.get("slide_id"): entry for entry in lock_pages if isinstance(entry, dict)}
    if len(page_by_id) != len(pages) or len(lock_by_slide) != len(lock_pages):
        fail("duplicate or missing page identifiers in PAGE_DETAIL_CONFIRMATION or batch lock")

    for expected_sequence, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            fail(f"slide {expected_sequence} must be an object")
        slide_id = slide.get("slide_id")
        if slide.get("sequence") != expected_sequence:
            fail(f"PAGE_ORDER_DRIFT at {slide_id or expected_sequence}")
        lock_entry = lock_by_slide.get(slide_id)
        if lock_entry is None:
            fail(f"UNDECLARED_PAGE: {slide_id}")
        page_id = lock_entry.get("page_detail_page_id")
        page = page_by_id.get(page_id)
        if page is None or page.get("sequence_index") != expected_sequence:
            fail(f"PAGE_ORDER_DRIFT at {page_id}")
        actual_page_hash = page_spec_hash(page)
        if page.get("page_spec_sha256") != actual_page_hash or lock_entry.get("page_spec_sha256") != actual_page_hash:
            fail(f"PAGE_SPEC_HASH_MISMATCH at {slide_id}")
        if slide.get("page_detail_page_sha256") != actual_page_hash:
            fail(f"PAGE_SPEC_HASH_MISMATCH at Slide Script {slide_id}")
        if slide.get("page_detail_confirmation_sha256") != expected_file_hash:
            fail(f"PAGE_DETAIL_HASH_MISMATCH at Slide Script {slide_id}")
        if slide.get("style_core_id") != selected_style_id:
            fail(f"STYLE_DRIFT at Slide Script {slide_id}")
        if page.get("page_family") and slide.get("page_family") != page.get("page_family"):
            fail(f"PAGE_FAMILY_DRIFT at {slide_id}")
        if slide.get("page_family") in {"TEXT_READING_PAGE", "PARAGRAPH_TEXT", "TEXT_AND_CONTEXT"} or str(page.get("section_id", "")).startswith("paragraph"):
            coverage = page.get("text_coverage")
            if not isinstance(coverage, dict):
                fail(f"PARAGRAPH_TEXT_INCOMPLETE at {slide_id}")
            if coverage.get("source_unit_type") not in {"NATURAL_PARAGRAPH", "POETRY_STANZA", "MEANING_UNIT"}:
                fail(f"PARAGRAPH_SOURCE_UNIT_DRIFT at {slide_id}")
            if not coverage.get("source_unit_ids") or coverage.get("text_integrity") != "COMPLETE_UNEDITED":
                fail(f"PARAGRAPH_TEXT_INCOMPLETE at {slide_id}")
            visible = page.get("student_visible_text") or {}
            body = visible.get("body") if isinstance(visible, dict) else None
            if not body:
                fail(f"PARAGRAPH_TEXT_INCOMPLETE at {slide_id}")
            vocabulary = coverage.get("vocabulary_coverage")
            if not isinstance(vocabulary, dict) or not isinstance(vocabulary.get("required_refs"), list):
                fail(f"PARAGRAPH_VOCABULARY_DROPPED at {slide_id}")
            if vocabulary.get("placement") not in {"INLINE_ADJACENT", "SIDE_BY_SIDE_ADJACENT", "CONTINUATION_ADJACENT"}:
                fail(f"PARAGRAPH_VOCABULARY_DETACHED at {slide_id}")
            if coverage.get("coverage_mode") == "SPLIT_CONTINUATION":
                if not coverage.get("split_group_id") or not coverage.get("split_reason"):
                    fail(f"PARAGRAPH_SPLIT_UNJUSTIFIED at {slide_id}")
        page_refs = set(page.get("source_refs") or [])
        slide_refs = set(slide.get("source_refs") or [])
        if page_refs and not page_refs.issubset(slide_refs):
            fail(f"PAGE_DETAIL_SOURCE_CONFLICT at {slide_id}")

        render_request = slide.get("render_request")
        if render_request is not None:
            if not isinstance(render_request, dict):
                fail(f"RENDER_REQUEST_UNBOUND at {slide_id}")
            if render_request.get("page_detail_page_sha256") != actual_page_hash or render_request.get("page_detail_confirmation_sha256") != expected_file_hash:
                fail(f"RENDER_REQUEST_UNBOUND at {slide_id}")
            if render_request.get("style_core_id") != selected_style_id:
                fail(f"STYLE_DRIFT in Render Request at {slide_id}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slide-script", required=True, type=Path)
    parser.add_argument("--page-detail", required=True, type=Path)
    parser.add_argument("--style-selection", required=True, type=Path)
    parser.add_argument("--role-selection", required=True, type=Path)
    args = parser.parse_args()
    try:
        validate(args.slide_script, args.page_detail, args.style_selection, args.role_selection)
    except ValueError as exc:
        print(f"BATCH_CONSTRUCTION_LOCK_FAIL: {exc}")
        return 1
    print("Batch construction lock passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
