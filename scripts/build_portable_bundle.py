"""Build single-entry V-MAX bundles from a Git checkout or extracted source archive; never install automatically."""
import argparse
import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path

from verify_portable_bundle import verify

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ("claude", "chatgpt", "antigravity", "codex")
TEXT_EXT = {".md", ".py", ".json", ".yaml", ".yml", ".txt", ".ps1"}


def rewrite(text, modules):
    # Published URLs still point to the repository; only local paths are relocated.
    parts = re.split(r"(https?://[^\s<>`\"')]+)", text)
    for index in range(0, len(parts), 2):
        for old, new in modules.items():
            parts[index] = parts[index].replace(old, new)
    return "".join(parts)


# Include only published runtime trees; never sweep arbitrary local files into a zip.
RUNTIME_DIRS = {"adapters", "chatgpt-work", "core", "docs", "launchers", "runtime", "schemas", "scripts", "skills", "resources", "assets", "libraries", "tests"}
ROOT_FILES = {"AGENTS.md", "README.md", "VERSION", "V-MAX_BOOTSTRAP.md", "V-MAX_MANIFEST.md"}


def included(name):
    p = Path(name)
    if any(part.startswith(".") or part == "__pycache__" for part in p.parts):
        return False
    if p.suffix in {".pyc", ".pyo"} or name.startswith("docs/visual-validation/"):
        return False
    if p.parts[0] == "tests" and p.suffix != ".md":
        return False
    return name in ROOT_FILES or (len(p.parts) > 1 and p.parts[0] in RUNTIME_DIRS)


def source_inventory(source):
    # A ZIP extracted inside another checkout must not inherit that parent's Git metadata.
    if (source / ".git").exists():
        names = subprocess.check_output(["git", "ls-files", "-z"], cwd=source).decode().split("\0")
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=source))
        kind = "git"
    else:
        names = []
        def walk(folder):
            for path in sorted(folder.iterdir()):
                if path.name.startswith(".") or path.name == "__pycache__":
                    continue
                if path.is_symlink():
                    raise ValueError(f"Unsafe source: {path}")
                if path.is_dir():
                    if folder != source or path.name in RUNTIME_DIRS:
                        walk(path)
                elif path.is_file():
                    names.append(path.relative_to(source).as_posix())
        walk(source)
        commit, dirty, kind = "unknown", None, "archive"
    return sorted(n for n in names if n and included(n)), commit, dirty, kind


def build(output, target, source=ROOT):
    source, output = Path(source).resolve(), Path(output).resolve()
    if target not in TARGETS:
        raise ValueError("Unsupported target")
    if output == source or source in output.parents:
        raise ValueError("Build outside the source repository")
    names, commit, dirty, kind = source_inventory(source)
    root = output / target / "vmax-chinese-teaching"
    root.mkdir(parents=True, exist_ok=False)
    modules = {n: n[:-8] + "MODULE.md" for n in names if n.endswith("/SKILL.md")}
    for name in names:
        path = source / name
        if path.is_symlink() or not path.resolve().is_relative_to(source):
            raise ValueError(f"Unsafe source: {name}")
        dest = root / modules.get(name, name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        content = path.read_bytes()
        if path.suffix in TEXT_EXT:
            text = content.decode("utf-8")
            text = rewrite(text, modules)
            content = text.replace("\r\n", "\n").encode("utf-8")
        dest.write_bytes(content)
    entry = (source / "packaging/portable-entry.md").read_text(encoding="utf-8").replace("{target}", target)
    for old, new in modules.items():
        entry = entry.replace(old, new)
    (root / "SKILL.md").write_bytes(entry.encode("utf-8"))
    version = (root / "VERSION").read_text().strip()
    info = {
        "format_version": 1, "target": target, "version": version,
        "source_commit": commit,
        "source_dirty": dirty,
        "source_kind": kind,
        "verification_scope": "Packaged file integrity and module references, not live platform behavior",
        "files": {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(root.rglob("*")) if p.is_file()},
    }
    (root / "bundle-manifest.json").write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    verify(root)
    archive = root.parent / f"vmax-chinese-teaching-{target}-{version}.zip"
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
        for p in sorted(root.rglob("*")):
            if p.is_file():
                bundle.write(p, p.relative_to(root.parent).as_posix())
    return root, archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--target", choices=TARGETS + ("all",), default="all")
    args = parser.parse_args()
    for target in TARGETS if args.target == "all" else (args.target,):
        _, archive = build(args.output, target)
        print(archive)
