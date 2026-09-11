#!/usr/bin/env python3
"""V-MAX Traditional Chinese font preflight.

Checks candidate font files for Traditional Chinese and Bopomofo glyph coverage.
The script intentionally does not auto-download fonts. It validates fonts that are
already present in the workspace or installed on the system, then emits a JSON
report suitable for a render gate.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

TC_TEST = "永遠的馬偕｜學習重點｜臺灣｜醫療教育｜體驗與觀察｜麥齒醫衛獻灣臺邊學夢"
from font_policy import read_registry, identify_font, BOPOMOFO, has_bopomofo

BOPOMOFO_TEST = BOPOMOFO

FONT_EXTS = {".ttf", ".otf", ".ttc", ".otc"}

DEFAULT_SEARCH_DIRS = [
    Path("assets/fonts"),
    Path("fonts"),
    Path.home() / ".fonts",
    Path.home() / ".local/share/fonts",
    Path("/usr/share/fonts"),
    Path("/usr/local/share/fonts"),
]

if platform.system() == "Windows":
    windir = os.environ.get("WINDIR", r"C:\\Windows")
    DEFAULT_SEARCH_DIRS.append(Path(windir) / "Fonts")
elif platform.system() == "Darwin":
    DEFAULT_SEARCH_DIRS += [
        Path("/System/Library/Fonts"),
        Path("/Library/Fonts"),
        Path.home() / "Library/Fonts",
    ]


def iter_font_files(search_dirs: Iterable[Path]) -> Iterable[Path]:
    seen: Set[str] = set()
    for root in search_dirs:
        try:
            if not root.exists():
                continue
            for p in root.rglob("*"):
                if p.is_file() and p.suffix.lower() in FONT_EXTS:
                    key = str(p.resolve())
                    if key not in seen:
                        seen.add(key)
                        yield p
        except (PermissionError, OSError):
            continue


def load_cmap(path: Path, face_index: int = 0) -> Optional[Set[int]]:
    try:
        from fontTools.ttLib import TTFont  # type: ignore
    except ImportError:
        return None

    try:
        font = TTFont(str(path), fontNumber=face_index, lazy=True)
        cmap = {cp for cp, glyph in (font.getBestCmap() or {}).items()
                if font.getGlyphID(glyph) != 0}
        font.close()
        return cmap
    except Exception:
        return set()


def missing_chars(cmap: Set[int], text: str) -> List[str]:
    out: List[str] = []
    for ch in text:
        if ch.isspace():
            continue
        if ord(ch) not in cmap and ch not in out:
            out.append(ch)
    return out


def pillow_loadable(path: Path, size: int = 42) -> bool:
    try:
        from PIL import ImageFont  # type: ignore
        ImageFont.truetype(str(path), size=size)
        return True
    except Exception:
        return False


def inspect_font(path: Path, extra_text: str, require_bopomofo: bool) -> Dict[str, object]:
    cmap = load_cmap(path)
    result: Dict[str, object] = {
        "path": str(path),
        "pillow_loadable": pillow_loadable(path),
        "cmap_check_available": cmap is not None,
    }

    if cmap is None:
        result.update({
            "traditional_chinese_test": "unknown",
            "bopomofo_test": "unknown" if require_bopomofo else "not_required",
            "missing_glyphs": [],
            "pass": False,
            "reason": "fontTools is not installed; install fonttools to perform glyph coverage checks",
        })
        return result

    if not cmap:
        result.update({
            "traditional_chinese_test": "fail",
            "bopomofo_test": "fail" if require_bopomofo else "not_required",
            "missing_glyphs": [],
            "pass": False,
            "reason": "font file could not be parsed or no Unicode cmap was found",
        })
        return result

    tc_missing = missing_chars(cmap, TC_TEST + extra_text)
    bop_missing = missing_chars(cmap, BOPOMOFO_TEST) if require_bopomofo else []
    all_missing = list(dict.fromkeys(tc_missing + bop_missing))

    tc_ok = not tc_missing
    bop_ok = (not bop_missing) if require_bopomofo else True
    load_ok = bool(result["pillow_loadable"])

    result.update({
        "traditional_chinese_test": "pass" if tc_ok else "fail",
        "bopomofo_test": ("pass" if bop_ok else "fail") if require_bopomofo else "not_required",
        "missing_glyphs": all_missing,
        "pass": bool(tc_ok and bop_ok and load_ok),
    })
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="V-MAX Traditional Chinese font preflight")
    parser.add_argument("--font", action="append", default=[], help="Explicit font file path. Repeatable.")
    parser.add_argument("--font-dir", action="append", default=[], help="Additional font directory. Repeatable.")
    parser.add_argument("--match", action="append", default=[], help="Only inspect discovered font filenames containing this text. Repeatable.")
    parser.add_argument("--extra-text", default="", help="Lesson-specific target characters/phrases to require.")
    parser.add_argument("--require-bopomofo", action="store_true", help="Require Bopomofo glyph coverage.")
    parser.add_argument("--report", default="font-preflight-report.json", help="Output JSON report path.")
    parser.add_argument('--role', default='body_sans', help='Registry role; run once for each font role used.')
    parser.add_argument('--text-file', help='UTF-8 file containing all visible text for this role.')
    parser.add_argument('--include-system-fonts', action='store_true', help='Also search system directories; approval policy still applies.')
    args = parser.parse_args()
    registry, font_configs = read_registry()
    if args.role not in registry['roles']:
        parser.error('Unknown registry role: ' + args.role)
    global TC_TEST
    TC_TEST = registry['render_test']['traditional_chinese']
    if args.text_file:
        args.extra_text += Path(args.text_file).read_text(encoding='utf-8')
    args.require_bopomofo = args.require_bopomofo or args.role == 'bopomofo_safe' or has_bopomofo(args.extra_text)
    role = registry['roles'][args.role]
    chain = [role['preferred'], *role.get('fallback', [])]

    candidates: List[Path] = [Path(p) for p in args.font]
    search_dirs = [Path(p) for p in args.font_dir] + DEFAULT_SEARCH_DIRS[:2]
    if args.include_system_fonts:
        search_dirs += DEFAULT_SEARCH_DIRS[2:]

    if not candidates:
        matches = [m.lower() for m in args.match]
        for p in iter_font_files(search_dirs):
            if matches and not any(m in p.name.lower() for m in matches):
                continue
            candidates.append(p)

    existing = sorted(set(p.resolve() for p in candidates if p.is_file()), key=str)
    inspected = []
    for path in existing:
        result = inspect_font(path, args.extra_text, args.require_bopomofo)
        try:
            fid, version, _ = identify_font(path, font_configs)
            approved = fid in chain
            cfg = font_configs.get(fid, {})
            result.update(font_id=fid, version=version, region=cfg.get('region'),
                          source=cfg.get('official_source'), policy_pass=approved)
            if not approved:
                result['reason'] = 'Font identity is not approved for this role; filename alone is not evidence.'
            result['pass'] = bool(result['pass'] and approved)
        except Exception as exc:
            result.update({'pass': False, 'policy_pass': False, 'reason': str(exc)})
        inspected.append(result)
    passed = sorted((r for r in inspected if r.get('pass')),
                    key=lambda r: (chain.index(r['font_id']), str(r['path'])))
    selected = passed[0] if passed else None
    fallback = bool(selected and selected['font_id'] != chain[0])

    report = {
        "schema": "vmax-font-preflight/1.1",
        "platform": platform.platform(),
        "require_bopomofo": args.require_bopomofo,
        "extra_text": args.extra_text,
        "candidate_count": len(existing),
        "status": "pass" if passed else "fail",
        "selected_font_file": passed[0]["path"] if passed else None,
        "fallback_used": fallback,
        "fallback_reason": 'Preferred font unavailable or failed preflight' if fallback else None,
        "selected_font_role": args.role,
        "selected_font_id": selected['font_id'] if selected else None,
        "selected_font_region": selected.get('region') if selected else None,
        "selected_font_source": selected.get('source') if selected else None,
        "selected_font_version": selected.get('version') if selected else None,
        "missing_glyphs": selected['missing_glyphs'] if selected else list(dict.fromkeys(c for r in inspected for c in r['missing_glyphs'])),
        "font_qa_page": "not_run",
        "final_render_QA": "not_run",
        "traditional_chinese_test": "pass" if passed else "fail",
        "bopomofo_test": ("pass" if passed else "fail") if args.require_bopomofo else "not_required",
        "fonts": inspected,
    }

    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not existing:
        print("ERROR: no font files found. Provide --font or --font-dir.", file=sys.stderr)
        return 2
    if not passed:
        print("ERROR: no candidate font passed the V-MAX Traditional Chinese preflight.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
