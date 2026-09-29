"""Verify bundle bytes and internal module references; no network or dependencies."""
import argparse
import hashlib
import json
import re
from pathlib import Path


# Claude limits follow the reported upload rejection; other targets have no verified limit.
TARGET_PROFILES = {
    "claude": {"max_files": 200, "build_budget": 190, "compact_markdown": True},
    "chatgpt": {"max_files": None, "build_budget": None, "compact_markdown": False},
    "antigravity": {"max_files": None, "build_budget": None, "compact_markdown": False},
    "codex": {"max_files": None, "build_budget": None, "compact_markdown": False},
}


def verify(root):
    root = Path(root).resolve()
    manifest = json.loads((root / "bundle-manifest.json").read_text(encoding="utf-8"))
    files = manifest["files"]
    profile = TARGET_PROFILES[manifest["target"]]
    count = len([p for p in root.rglob("*") if p.is_file()])
    if profile["build_budget"] is not None and count > profile["build_budget"]:
        raise ValueError(f"Target file budget exceeded: {count} > {profile['build_budget']} (platform maximum {profile['max_files']})")
    for name, digest in files.items():
        path = (root / name).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f"Missing or unsafe bundle file: {name}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f"Bundle hash mismatch: {name}")
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
              and "__pycache__" not in p.parts and p.name != "bundle-manifest.json"}
    if actual != set(files):
        raise ValueError("Unlisted bundle files")
    for original, info in manifest.get("relocated_references", {}).items():
        filename, anchor = info["destination"].split("#", 1)
        path = (root / filename).resolve()
        if not path.is_relative_to(root) or filename not in files:
            raise ValueError("Unsafe relocated reference")
        text = path.read_text(encoding="utf-8")
        start, end = f"<!-- BEGIN {original} -->\n", f"\n<!-- END {original} -->"
        if text.count(start) != 1 or text.count(end) != 1 or f'id="{anchor}"' not in text:
            raise ValueError(f"Missing reference section: {original}")
        content = text.split(start, 1)[1].split(end, 1)[0]
        if hashlib.sha256(content.encode("utf-8")).hexdigest() != info["content_sha256"]:
            raise ValueError(f"Reference section hash mismatch: {original}")
    entries = list(root.rglob("SKILL.md"))
    if entries != [root / "SKILL.md"]:
        raise ValueError("Bundle must expose exactly one SKILL.md")
    entry = (root / "SKILL.md").read_text(encoding="utf-8")
    name = re.search(r"^name: (.+)$", entry, re.M).group(1)
    if root.name != name:
        raise ValueError("Skill folder/name mismatch")
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for filename, anchor in re.findall(r"([\w/-]+/BUNDLE_REFERENCE\.md)#(ref-[\w-]+)", text):
            dest = root / filename
            if not dest.is_file() or f'id="{anchor}"' not in dest.read_text(encoding="utf-8"):
                raise ValueError(f"Missing reference anchor: {filename}#{anchor}")
        for ref in re.findall(r"(?:skills|chatgpt-work)/[\w-]+/MODULE\.md", text):
            if not (root / ref).is_file():
                raise ValueError(f"Missing module reference {ref} in {path.name}")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    info = verify(args.root)
    print(f"Bundle integrity passed: {info['target']} {info['version']}")
