import copy
import hashlib
import subprocess
import tempfile
import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_presentation import validate, validate_result, request_digest, COMMON_CHECKS, IDIOM_CHECKS, VOCAB_CHECKS
from jsonschema import Draft202012Validator


class PresentationContracts(unittest.TestCase):
    def setUp(self):
        self.slide = json.loads((ROOT / 'core/schemas/vmax/examples/slide-script.example.json').read_text(encoding='utf-8'))
        self.request = dict(request_id='RR-1', request_state='RENDER_READY', lesson_id='example', asset_type='illustration', page_family='IDIOM', source_refs=['example:source'], approval_refs=['example:approval'], verified_text=[dict(layer_id='T1', text='example', source_ref='example:source')], output_spec=dict(width_px=1920, height_px=1080, format='PNG'), idiom_application_plan={k: 'example' for k in ['idiom', 'student_friendly_meaning', 'example_sentence', 'example_scene_subject', 'example_scene_action', 'semantic_relation', 'literal_image_risk']}, acceptance_checks={'source_fidelity': True, 'traditional_chinese_exact': True, 'idiom_text_pass': True, 'idiom_example_naturalness_pass': True}, idiom_naturalness_evidence=dict(grammar_pass=True, usage_pass=True, grade_context_pass=True, review_ref='example:review'))
        self.request['idiom_application_plan']['source_refs'] = ['example:source']
        self.mark = dict(text_layer_id='T1', term_text='example', source_ref='example:source', term_color_id='a', mark_mode='UNDERLINE_HIGHLIGHT', include_punctuation=False, layer_order='MARK_BELOW_TEXT', span_rule='TERM_ONLY', occurrence_index=1, start_char_index=0, end_char_index=7, text_layout_revision='r1', glyph_bbox=dict(x=0,y=0,width=70,height=10), baseline_y=9, mark_bbox=dict(x=0,y=11,width=70,height=2))

    def test_existing_example_and_legacy_fields(self):
        self.assertEqual(validate(self.slide), [])

    def test_schema_definitions(self):
        for name in ['slide-script', 'render-request']:
            Draft202012Validator.check_schema(json.loads((ROOT / f'core/schemas/vmax/{name}.schema.json').read_text(encoding='utf-8')))

    def test_restore_canvas_lineage_and_text_constraints(self):
        for mutate in [lambda d: d['canvas_lock'].update(width_px=0), lambda d: d.update(derived_from={}), lambda d: d['slides'][0]['text_rendering']['layers'][0].update(visibility='PUBLIC')]:
            d=copy.deepcopy(self.slide); mutate(d)
            self.assertTrue(validate(d))

    def test_idiom_slide_requires_plan_and_page_family(self):
        self.slide['slides'][0]['page_family']='IDIOM'
        self.assertTrue(validate(self.slide))
        del self.slide['slides'][0]['page_family']
        self.assertTrue(validate(self.slide))

    def test_ready_idiom(self):
        self.assertEqual(validate(self.request, 'render-request', True), [])
        for key in ['idiom_application_plan', 'idiom_naturalness_evidence', 'acceptance_checks', 'output_spec', 'request_state']:
            d=copy.deepcopy(self.request); del d[key]
            self.assertTrue(validate(d, 'render-request', True), key)
        self.request['acceptance_checks']['idiom_example_naturalness_pass']=False
        self.assertTrue(validate(self.request, 'render-request', True))

    def test_pre_layout_cannot_enter_renderer(self):
        self.request['request_state']='PRE_LAYOUT'
        self.request['vocab_mark_plan']=[dict(self.mark, glyph_bbox=None, baseline_y=None, mark_bbox=None)]
        self.assertEqual(validate(self.request, 'render-request'), [])
        self.assertTrue(validate(self.request, 'render-request', True))
        self.request['request_state']='RENDER_READY'
        self.assertTrue(validate(self.request, 'render-request', True))

    def test_anchor_shape_revision_span_and_layers(self):
        self.request.update(text_layout_revision='r1',vocab_mark_plan=[self.mark])
        self.assertEqual(validate(self.request, 'render-request', True), [])
        for change in [dict(glyph_bbox={}), dict(text_layout_revision='old'), dict(include_punctuation=True), dict(layer_order='MARK_ABOVE_TEXT'), dict(start_char_index=-1), dict(end_char_index=0), dict(stroke_height_ratio=0.9)]:
            d=copy.deepcopy(self.request); d['vocab_mark_plan'][0].update(change)
            self.assertTrue(validate(d, 'render-request', True), change)

    def test_slide_request_plan_drift_and_canvas(self):
        slide=self.slide['slides'][0]
        r=copy.deepcopy(self.request)
        r.update(asset_type='slide',page_family=slide['page_family'],canvas_lock=self.slide['canvas_lock'],
                 lesson_id=self.slide['lesson_id'], source_refs=slide['source_refs'],
                 verified_text=[{k: l[k] for k in ['layer_id','text','source_ref']} for l in slide['text_rendering']['layers']])
        r['source_refs'] = slide['source_refs']
        del r['idiom_application_plan']
        for k in ['object_composition_plan','character_plan','key_line_plan']: r[k]=copy.deepcopy(slide[k])
        slide['render_request']=r
        self.assertEqual(validate(self.slide, require_ready=True), [])
        r['character_plan']={'appear':True}
        self.assertTrue(validate(self.slide, require_ready=True))
        r['character_plan']=slide['character_plan']
        r['output_spec']['width_px']=1
        self.assertTrue(validate(self.slide, require_ready=True))

    def test_verified_text_and_failed_checks(self):
        for change in [dict(verified_text=[]), dict(verified_text=[dict(layer_id='T1',text='different',source_ref='example:source')]),
                       dict(verified_text=[dict(layer_id='T1',text='   ',source_ref='example:source')])]:
            d=copy.deepcopy(self.request); d.update(change)
            self.assertTrue(validate(d, 'render-request', True), change)
        for key in ['idiom_text_pass', 'source_fidelity', 'idiom_example_visual_match_pass']:
            d=copy.deepcopy(self.request); d['acceptance_checks'][key]=False
            self.assertTrue(validate(d, 'render-request', True), key)

    def test_pending_final_checks_do_not_block_construction(self):
        self.request['acceptance_checks']['idiom_example_visual_match_pass']=None
        self.assertEqual(validate(self.request, 'render-request', True), [])

    def test_textless_illustration_is_allowed_but_not_idiom(self):
        self.request.update(page_family='ILLUSTRATION', textless=True, verified_text=[])
        del self.request['idiom_application_plan']
        self.assertEqual(validate(self.request, 'render-request', True), [])
        self.request['page_family']='IDIOM'
        self.assertTrue(validate(self.request, 'render-request', True))

    def test_anchor_semantics_and_geometry(self):
        self.request.update(text_layout_revision='r1', vocab_mark_plan=[self.mark])
        for change in [dict(text_layer_id='missing'), dict(term_text='wrong'), dict(occurrence_index=2),
                       dict(end_char_index=100), dict(source_ref='wrong'),
                       dict(glyph_bbox=dict(x=99999,y=0,width=70,height=10)),
                       dict(mark_bbox=dict(x=0,y=5,width=70,height=2)), dict(baseline_y=999)]:
            d=copy.deepcopy(self.request); d['vocab_mark_plan'][0].update(change)
            self.assertTrue(validate(d, 'render-request', True), change)

    def test_final_receipt_and_changes_invalidate_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            asset=Path(tmp)/'synthetic.bin'; asset.write_bytes(b'synthetic test artifact, not rendered teaching material')
            receipt=dict(request_id=self.request['request_id'],request_sha256=request_digest(self.request),
                         asset_path=asset.name, asset_sha256=hashlib.sha256(asset.read_bytes()).hexdigest(),
                         review_ref='test:review',checks={k:True for k in COMMON_CHECKS | IDIOM_CHECKS})
            self.assertEqual(validate_result(self.request,receipt,tmp),[])
            for mutate in [lambda r:r['checks'].update(idiom_example_visual_match_pass=False),
                           lambda r:r['checks'].pop('idiom_hierarchy_pass'),
                           lambda r:r.update(request_sha256='old'),
                           lambda r:r.update(asset_path='missing')]:
                r=copy.deepcopy(receipt); mutate(r)
                self.assertTrue(validate_result(self.request,r,tmp))
            changed=copy.deepcopy(self.request); changed['verified_text'][0]['text']='revised'
            self.assertTrue(validate_result(changed,receipt,tmp))
            asset.write_bytes(b'changed')
            self.assertTrue(validate_result(self.request,receipt,tmp))

    def test_launcher_from_course_directory_and_sync_install(self):
        import shutil
        launcher=ROOT/'skills/vmax-image-renderer/scripts/validate_presentation.py'
        example=ROOT/'core/schemas/vmax/examples/slide-script.example.json'
        with tempfile.TemporaryDirectory() as tmp:
            lesson=Path(tmp)/'course'; lesson.mkdir()
            installed=Path(tmp)/'skills/vmax-image-renderer/scripts/validate_presentation.py'
            installed.parent.mkdir(parents=True)
            shutil.copyfile(launcher,installed)
            (Path(tmp)/'skills/.vmax-managed-skills.json').write_text(json.dumps({'cache_dir':str(ROOT)}),encoding='utf-8')
            for entry, extra in [(launcher,[]),(installed,[]),(installed,['--repo-root',str(ROOT)])]:
                result=subprocess.run([sys.executable,str(entry),str(example),*extra],cwd=lesson,capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr+result.stdout)
            result=subprocess.run([sys.executable,str(installed),str(example),'--repo-root',str(lesson)],cwd=lesson,capture_output=True,text=True)
            self.assertEqual(result.returncode,2)

    def test_full_cli_lifecycle(self):
        launcher = ROOT / 'skills/vmax-image-renderer/scripts/validate_presentation.py'
        with tempfile.TemporaryDirectory() as tmp:
            request_path = Path(tmp) / 'request.json'
            result_path = Path(tmp) / 'result.json'
            def run(*flags):
                return subprocess.run([sys.executable, str(launcher), str(request_path), '--kind', 'render-request', *flags], cwd=tmp, capture_output=True, text=True)
            draft = copy.deepcopy(self.request)
            draft['request_state'] = 'PRE_LAYOUT'
            request_path.write_text(json.dumps(draft), encoding='utf-8')
            self.assertEqual(run().returncode, 0)
            self.assertEqual(run('--require-ready').returncode, 1)
            request_path.write_text(json.dumps(self.request), encoding='utf-8')
            self.assertEqual(run('--require-ready').returncode, 0)
            digest = run('--require-ready', '--digest')
            self.assertEqual(digest.stdout.strip(), request_digest(self.request))
            # Synthetic bytes test transport/evidence only, not visual correctness.
            asset = Path(tmp) / 'synthetic.bin'
            asset.write_bytes(b'qa workflow fixture')
            receipt = dict(request_id=self.request['request_id'], request_sha256=digest.stdout.strip(), asset_path=asset.name, asset_sha256=hashlib.sha256(asset.read_bytes()).hexdigest(), review_ref='fixture:review', checks={k: True for k in COMMON_CHECKS | IDIOM_CHECKS})
            result_path.write_text(json.dumps(receipt), encoding='utf-8')
            self.assertEqual(run('--result', str(result_path)).returncode, 0)
            receipt['checks']['idiom_example_visual_match_pass'] = None
            result_path.write_text(json.dumps(receipt), encoding='utf-8')
            self.assertEqual(run('--result', str(result_path)).returncode, 1)
            request_path.write_text('{bad json', encoding='utf-8')
            self.assertEqual(run().returncode, 2)


if __name__ == '__main__':
    unittest.main()
