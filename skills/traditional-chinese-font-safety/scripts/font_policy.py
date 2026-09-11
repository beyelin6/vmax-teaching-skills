"""Shared registry, identity and Unicode coverage checks."""
from pathlib import Path
import re

REGISTRY = Path(__file__).resolve().parents[1] / 'font-registry.yaml'
BOPOMOFO = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩˉˊˇˋ˙'

def read_registry(path=REGISTRY):
    import yaml
    data = yaml.safe_load(Path(path).read_text(encoding='utf-8'))
    fonts = {f['id']: f for f in data['fonts']}
    for role in data['roles'].values():
        for fid in [role['preferred'], *role.get('fallback', [])]:
            if fid not in fonts:
                raise ValueError(f'Undefined font ID: {fid}')
    return data, fonts

def font_metadata(path):
    from fontTools.ttLib import TTFont
    with TTFont(str(path), fontNumber=0) as font:
        names = font['name'].names
        ps = [n.toUnicode() for n in names if n.nameID == 6]
        versions = [n.toUnicode() for n in names if n.nameID == 5]
        cmap = font.getBestCmap() or {}
        coverage = {cp for cp, glyph in cmap.items() if font.getGlyphID(glyph) != 0}
        return ps, versions[0] if versions else None, coverage

def identify_font(path, fonts):
    ps, version, coverage = font_metadata(path)
    for fid, cfg in fonts.items():
        pattern = cfg.get('postscript_pattern')
        if pattern and ps and all(re.fullmatch(pattern, name) for name in ps):
            return fid, version, coverage
    return None, version, coverage

def has_bopomofo(text):
    return any('\u3100' <= c <= '\u312f' or '\u31a0' <= c <= '\u31bf' for c in text)
