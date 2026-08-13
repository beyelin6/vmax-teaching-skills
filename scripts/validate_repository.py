#!/usr/bin/env python3
"""Validate repository structure without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def validate_versions() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    plugin = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("version") != version:
        fail(f"VERSION {version!r} != plugin version {plugin.get('version')!r}")


def validate_skills() -> None:
    skills_root = ROOT / "skills"
    for child in sorted(skills_root.iterdir()):
        if not child.is_dir():
            continue
        files = [p for p in child.rglob("*") if p.is_file()]
        if files and not (child / "SKILL.md").is_file():
            fail(f"orphan skill directory without SKILL.md: {child.relative_to(ROOT)}")

    names: dict[str, Path] = {}
    for skill_file in sorted(ROOT.rglob("SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"missing YAML front matter: {skill_file.relative_to(ROOT)}")
            continue
        match = re.search(r"(?m)^name:\s*([^\n]+)$", text[:2000])
        description = re.search(r"(?m)^description:\s*([^\n]+)$", text[:4000])
        if not match or not description:
            fail(f"missing name/description: {skill_file.relative_to(ROOT)}")
            continue
        name = match.group(1).strip().strip('"\'')
        if name in names:
            fail(f"duplicate skill name {name}: {names[name].relative_to(ROOT)} and {skill_file.relative_to(ROOT)}")
        names[name] = skill_file


def validate_manifest_paths() -> None:
    text = (ROOT / "V-MAX_MANIFEST.md").read_text(encoding="utf-8")
    keys = (
        "path|contract|report_schema|lesson_master_index_schema|lkb_patch_schema|"
        "task_requirement_registry|regression|request_schema|runtime_contract|bootstrap"
    )
    pattern = re.compile(rf"(?m)^\s*(?:{keys}):\s*([^\r\n]+)$")
    for raw in pattern.findall(text):
        value = raw.strip().strip('"\'')
        if value.startswith(("http://", "https://")):
            continue
        if not (ROOT / value).exists():
            fail(f"manifest path does not exist: {value}")


def validate_manifest_module_versions() -> None:
    text = (ROOT / "V-MAX_MANIFEST.md").read_text(encoding="utf-8")
    entries = re.finditer(
        r"(?m)^([a-z0-9_]+):\s*\n\s+path:\s*([^\n]+)\n\s+current_version:\s*([^\n]+)",
        text,
    )
    for entry in entries:
        module, raw_path, expected = entry.groups()
        path = ROOT / raw_path.strip()
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        found = re.search(r"(?m)^(?:版本：|# .*? v)(\d+(?:\.\d+)+)\s*$", content)
        if found and found.group(1) != expected.strip():
            fail(
                f"manifest version mismatch for {module}: "
                f"{expected.strip()} != {found.group(1)} in {path.relative_to(ROOT)}"
            )


def validate_drive_id_locations() -> None:
    allowed = {
        Path("V-MAX_MANIFEST.md"),
        Path("runtime/lesson-state.md"),
        Path("skills/google-drive-lesson-archive/SKILL.md"),
    }
    # Split literals so the validator does not itself become a fourth ID store.
    ids = (
        "1AOjYwALGVNWu99b" + "-SnjBUSALEDrlReMt",
        "1q4vgqiRFbrvcMeZ7B102rY_" + "kZVF7Z4LcqR8iL8vPKmQ",
        "1d1vCEw-BzFiR_DyGYDM1f3" + "aovrKODIaA",
    )
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if relative in allowed:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if any(value in text for value in ids):
            fail(f"fixed Drive ID outside governance allowlist: {relative}")


def validate_removed_skill_names() -> None:
    forbidden = ("vmax-chinese-preview-worksheet", "vmax-chinese-short-writing-worksheet")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".yaml", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name in forbidden:
            if name in text:
                fail(f"legacy skill reference {name!r}: {path.relative_to(ROOT)}")


def main() -> int:
    validate_versions()
    validate_skills()
    validate_manifest_paths()
    validate_manifest_module_versions()
    validate_drive_id_locations()
    validate_removed_skill_names()
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        return 1
    print("Repository validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
