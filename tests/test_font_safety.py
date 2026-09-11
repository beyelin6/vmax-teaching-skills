"""Behavioral regression tests using synthetic font files, without network access."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from argparse import Namespace

SCRIPTS = Path(__file__).resolve().parents[1] / 'skills/traditional-chinese-font-safety/scripts'
sys.path.insert(0, str(SCRIPTS))
import check_fonts as check
import font_policy
import render_font_qa_page as qa

def make_font(path, name, missing=''):
    from fontTools.fontBuilder import FontBuilder
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    fb = FontBuilder(1000, isTTF=True)
    fb.setupGlyphOrder(['.notdef', 'mark'])
    pen = TTGlyphPen(None)
    pen.moveTo((50, 0)); pen.lineTo((600, 0)); pen.lineTo((600, 700)); pen.lineTo((50, 700)); pen.closePath()
    fb.setupGlyf({'.notdef': TTGlyphPen(None).glyph(), 'mark': pen.glyph()})
    fb.setupHorizontalMetrics({'.notdef': (650, 0), 'mark': (650, 0)})
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    chars = set(check.TC_TEST + font_policy.BOPOMOFO + '教材測試') - set(missing)
    fb.setupCharacterMap({ord(c): 'mark' for c in chars})
    fb.setupNameTable({'familyName': name, 'styleName': 'Regular', 'psName': name, 'fullName': name, 'version': 'Version 1.0'})
    fb.setupOS2(); fb.setupPost(); fb.setupMaxp(); fb.save(path)

class FontSafetyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def run_check(self, *args):
        out = self.root/'nested'/'report.json'
        with patch.object(sys, 'argv', ['check', *args, '--report', str(out)]), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            code = check.main()
        return code, json.loads(out.read_text(encoding='utf-8'))

    def test_fallback_and_nested_report(self):
        a,b = self.root/'a.ttf',self.root/'b.ttf'
        make_font(a, 'Iansui-Regular', missing='臺'); make_font(b, 'SourceHanSansTW-Regular')
        code,r = self.run_check('--role','character_learning','--font',str(a),'--font',str(b))
        self.assertEqual(code,0); self.assertTrue(r['fallback_used'])
        self.assertEqual(r['selected_font_id'],'Source_Han_Sans_TW')
        self.assertEqual(r['final_render_QA'],'not_run')

    def test_role_order_overrides_argument_order(self):
        a,b = self.root/'a.ttf',self.root/'b.ttf'
        make_font(a,'Iansui-Regular'); make_font(b,'SourceHanSansTW-Regular')
        _,r = self.run_check('--role','character_learning','--font',str(b),'--font',str(a))
        self.assertEqual(r['selected_font_id'],'Iansui'); self.assertFalse(r['fallback_used'])

    def test_renamed_wrong_region_rejected(self):
        f=self.root/'SourceHanSansTW-Regular.ttf'; make_font(f,'SourceHanSansJP-Regular')
        code,r=self.run_check('--font',str(f))
        self.assertEqual(code,1); self.assertIsNone(r['selected_font_file'])

    def test_text_file_triggers_full_bopomofo_and_missing_tone(self):
        f=self.root/'font.ttf'; make_font(f,'Iansui-Regular',missing='˙')
        t=self.root/'text.txt'; t.write_text('ㄩ',encoding='utf-8')
        code,r=self.run_check('--role','character_learning','--font',str(f),'--text-file',str(t))
        self.assertEqual(code,1); self.assertTrue(r['require_bopomofo']); self.assertIn('˙',r['missing_glyphs'])

    def test_no_fonts_fail(self):
        code,r=self.run_check('--font',str(self.root/'missing.ttf'))
        self.assertEqual(code,2); self.assertEqual(r['status'],'fail')

    def test_registry_references_resolve(self):
        data,fonts=font_policy.read_registry()
        self.assertEqual(data['roles']['bopomofo_safe']['preferred'],'Iansui')
        self.assertIn('Source_Han_Sans_TW',fonts)

    def test_qa_long_text_paginated_inside_margins(self):
        from PIL import ImageFont
        font=ImageFont.truetype('DejaVuSans.ttf',46) if Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf').exists() else ImageFont.load_default(size=46)
        args=Namespace(body_font='test',title_font='test',character_font='test',bopomofo_font=None,lesson_text='long sample '*500,lesson_text_file=None,output=str(self.root/'qa.png'))
        with patch.object(qa,'font_metadata',return_value=([],None,set(range(0x110000)))), patch.object(qa.ImageFont,'truetype',return_value=font):
            r=qa.render(args)
        self.assertGreater(len(r['pages']),1)
        self.assertEqual(r['visual_qa'],'not_run')
        for item in r['text_boxes']:
            x,y,right,bottom=item['bbox']
            self.assertGreaterEqual(x,100); self.assertGreaterEqual(y,100)
            self.assertLessEqual(right,2460); self.assertLessEqual(bottom,1340)

if __name__ == '__main__':
    unittest.main()
