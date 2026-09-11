#!/usr/bin/env python3
"""Bootstrap approved V-MAX teaching fonts from official GitHub releases.

Security / licensing policy:
- Only repositories hard-coded in APPROVED_SOURCES may be downloaded.
- Downloads come from official GitHub release assets only.
- The script never scrapes third-party font sites.
- Font files are installed into a project-local directory (default: assets/fonts),
  not globally into the operating system.
- Source Han downloads use the Taiwan region-specific subset OTF package and retain
  only TW font files, reducing accidental use of JP/CN/HK glyph variants.

Automatic set:
- Iansui / 芫荽
- jf open huninn / jf open 粉圓
- Source Han Sans TW / 思源黑體 TW
- Source Han Serif TW / 思源宋體 TW
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Dict, List, Optional

GITHUB_API = "https://api.github.com/repos/{repo}/releases/latest"
USER_AGENT = "V-MAX-Font-Bootstrap/1.1"
FONT_EXTS = {".ttf", ".otf", ".ttc", ".otc"}
LICENSE_NAMES = {"license", "license.txt", "license.md", "ofl.txt", "ofl.md", "copyright.txt"}

APPROVED_SOURCES: Dict[str, Dict[str, object]] = {
    "iansui": {
        "repo": "ButTaiwan/iansui",
        "asset_regex": r"(?i)^iansui.*\.zip$",
        "license": "SIL Open Font License 1.1",
    },
    "huninn": {
        "repo": "justfont/open-huninn-font",
        "asset_regex": r"(?i)^jf-openhuninn.*\.ttf$",
        "license": "SIL Open Font License 1.1",
    },
    "source_han_sans_tw": {
        "repo": "adobe-fonts/source-han-sans",
        "asset_regex": r"(?i)^05_SourceHanSansSubsetOTF\.zip$",
        "font_regex": r"(?i)^SourceHanSansTW-.*\.otf$",
        "license": "SIL Open Font License 1.1 (verify bundled official license)",
        "region": "Traditional Chinese — Taiwan (TW)",
    },
    "source_han_serif_tw": {
        "repo": "adobe-fonts/source-han-serif",
        "asset_regex": r"(?i)^05_SourceHanSerifSubsetOTF\.zip$",
        "font_regex": r"(?i)^SourceHanSerifTW-.*\.otf$",
        "license": "SIL Open Font License 1.1 (verify bundled official license)",
        "region": "Traditional Chinese — Taiwan (TW)",
    },
}


def request_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=300) as resp, dest.open("wb") as f:
        shutil.copyfileobj(resp, f)


def pick_asset(release: dict, pattern: str) -> dict:
    rx = re.compile(pattern)
    for asset in release.get("assets", []):
        if rx.match(asset.get("name", "")):
            return asset
    raise RuntimeError(f"No approved release asset matched: {pattern}")


def copy_font(src: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    shutil.copy2(src, dest)
    return dest


def install_zip(zip_path: Path, dest_dir: Path, source_id: str, font_regex: Optional[str] = None) -> List[Path]:
    installed: List[Path] = []
    font_rx = re.compile(font_regex) if font_regex else None
    license_dir = dest_dir / "licenses" / source_id
    license_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            zf.extractall(root)
            for p in root.rglob("*"):
                if not p.is_file():
                    continue
                if p.suffix.lower() in FONT_EXTS:
                    if font_rx and not font_rx.match(p.name):
                        continue
                    installed.append(copy_font(p, dest_dir))
                elif p.name.lower() in LICENSE_NAMES or "license" in p.name.lower() or p.name.lower().startswith("ofl"):
                    shutil.copy2(p, license_dir / p.name)
    return installed


def install_one(source_id: str, dest_dir: Path) -> dict:
    cfg = APPROVED_SOURCES[source_id]
    release = request_json(GITHUB_API.format(repo=cfg["repo"]))
    asset = pick_asset(release, str(cfg["asset_regex"]))
    url = asset["browser_download_url"]
    name = asset["name"]

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / name
        download(url, tmp)
        if tmp.suffix.lower() == ".zip":
            installed = install_zip(tmp, dest_dir, source_id, cfg.get("font_regex"))
        elif tmp.suffix.lower() in FONT_EXTS:
            installed = [copy_font(tmp, dest_dir)]
        else:
            raise RuntimeError(f"Unexpected asset type: {name}")

    if not installed:
        raise RuntimeError(f"No approved font files were found in asset: {name}")

    return {
        "source_id": source_id,
        "repo": cfg["repo"],
        "release": release.get("tag_name"),
        "asset": name,
        "region": cfg.get("region"),
        "license_policy": cfg["license"],
        "installed_files": [str(p) for p in installed],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Install approved V-MAX Traditional Chinese teaching fonts")
    parser.add_argument("--dest", default="assets/fonts", help="Project-local destination directory")
    parser.add_argument("--font", action="append", choices=sorted(APPROVED_SOURCES), help="Install only selected approved font. Repeatable.")
    parser.add_argument("--report", default="font-bootstrap-report.json", help="JSON report path")
    args = parser.parse_args()

    dest = Path(args.dest)
    targets = args.font or list(APPROVED_SOURCES.keys())
    results = []
    errors = []

    for source_id in targets:
        try:
            results.append(install_one(source_id, dest))
        except Exception as exc:
            errors.append({"source_id": source_id, "error": str(exc)})

    report = {
        "schema": "vmax-font-bootstrap/1.1",
        "destination": str(dest),
        "installed": results,
        "errors": errors,
        "status": "pass" if results and not errors else ("partial" if results else "fail"),
        "next_step": "Run check_fonts.py against installed files before rendering; require Bopomofo when the page contains Zhuyin.",
    }
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
