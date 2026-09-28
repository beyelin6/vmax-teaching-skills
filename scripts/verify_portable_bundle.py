"""Verify bundle bytes and internal module references; no network or dependencies."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def verify(root):
    root = Path(root).resolve()
    manifest = json.loads((root / "bundle-manifest.json").read_text(encoding="utf-8"))
    files = manifest["files"]
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
    entries = list(root.rglob("SKILL.md"))
    if entries != [root / "SKILL.md"]:
        raise ValueError("Bundle must expose exactly one SKILL.md")
    entry = (root / "SKILL.md").read_text(encoding="utf-8")
    name = re.search(r"^name: (.+)$", entry, re.M).group(1)
    if root.name != name:
        raise ValueError("Skill folder/name mismatch")
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
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
