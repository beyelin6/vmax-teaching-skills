"""Validate presentation contracts; semantic review remains a separate gate."""
import argparse
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'core/schemas/vmax'


COMMON_CHECKS = {'source_fidelity', 'traditional_chinese_exact', 'inspect_final_asset',
                 'object_composition_pass', 'protected_zone_pass',
                 'planned_overlap_pass', 'monolithic_background_pass'}
IDIOM_CHECKS = {'idiom_text_pass', 'idiom_hierarchy_pass', 'idiom_example_readability_pass',
                'idiom_example_naturalness_pass', 'idiom_example_visual_match_pass',
                'idiom_object_composition_pass'}
VOCAB_CHECKS = {'vocab_anchor_pass', 'vocab_reflow_pass', 'vocab_mark_alignment_pass',
                'vocab_mark_span_pass', 'vocab_mark_layer_pass', 'term_color_consistency_pass'}


def request_digest(request):
    return hashlib.sha256(json.dumps(request, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode('utf-8')).hexdigest()


def validate_result(request, result, base_dir):
    """Verify a local result receipt is bound to the request and actual bytes."""
    errors = []
    if not isinstance(result, dict):
        return ['RESULT_NOT_OBJECT']
    if result.get('request_id') != request['request_id'] or result.get('request_sha256') != request_digest(request):
        errors.append('STALE_OR_WRONG_RENDER_RESULT')
    checks = COMMON_CHECKS | (IDIOM_CHECKS if request['page_family'] == 'IDIOM' else set())
    checks |= VOCAB_CHECKS if request.get('vocab_mark_plan') else set()
    statuses = result.get('checks', {})
    if not isinstance(statuses, dict):
        return errors + ['RESULT_CHECKS_NOT_OBJECT']
    for name in sorted(checks):
        if statuses.get(name) is not True:
            errors.append(f'FINAL_CHECK_NOT_PASSED: {name}')
    if any(value is False for value in statuses.values()):
        errors.append('FINAL_CHECK_FAILED')
    for key in ['asset_path', 'asset_sha256', 'review_ref']:
        if not isinstance(result.get(key), str) or not result[key].strip():
            errors.append(f'RESULT_EVIDENCE_MISSING: {key}')
    if errors:
        return errors
    asset = Path(base_dir) / result['asset_path']
    try:
        if not asset.is_file() or hashlib.sha256(asset.read_bytes()).hexdigest() != result['asset_sha256']:
            errors.append('ASSET_MISSING_OR_CHANGED')
    except OSError as exc:
        errors.append(f'ASSET_UNREADABLE: {exc}')
    return errors


def validate_ready_text(request):
    errors = []
    layers = request['verified_text']
    by_id = {layer['layer_id']: layer for layer in layers}
    if len(by_id) != len(layers):
        errors.append('DUPLICATE_TEXT_LAYER_ID')
    if any(not layer['text'].strip() for layer in layers):
        errors.append('EMPTY_VERIFIED_TEXT')
    if any(layer['source_ref'] not in request['source_refs'] for layer in layers):
        errors.append('TEXT_SOURCE_NOT_IN_REQUEST')
    if request.get('textless') and layers:
        errors.append('TEXTLESS_WITH_TEXT')
    if any(value is False for value in request['acceptance_checks'].values()):
        errors.append('PRE_RENDER_CHECK_FAILED')
    if request['page_family'] == 'IDIOM':
        plan = request['idiom_application_plan']
        for key in ['idiom', 'student_friendly_meaning', 'example_sentence']:
            if not any(plan[key] in layer['text'] for layer in layers):
                errors.append(f'IDIOM_VERIFIED_TEXT_MISMATCH: {key}')
        if not set(plan['source_refs']).issubset(request['source_refs']):
            errors.append('IDIOM_SOURCE_NOT_IN_REQUEST')
        if request['acceptance_checks'].get('idiom_text_pass') is not True:
            errors.append('IDIOM_TEXT_NOT_REVIEWED')
    width, height = request['output_spec']['width_px'], request['output_spec']['height_px']
    for mark in request.get('vocab_mark_plan', []):
        layer = by_id.get(mark['text_layer_id'])
        if layer is None:
            errors.append('VOCAB_TEXT_LAYER_NOT_FOUND')
            continue
        text = layer['text']
        start, end = mark['start_char_index'], mark['end_char_index']
        term = mark['term_text']
        occurrences = [i for i in range(len(text)) if text.startswith(term, i)] if term else []
        occurrence = mark['occurrence_index'] - 1
        if (end <= start or end > len(text) or text[start:end] != term or occurrence >= len(occurrences)
                or occurrences[occurrence] != start):
            errors.append('VOCAB_TEXT_SPAN_MISMATCH')
        if mark['source_ref'] != layer['source_ref']:
            errors.append('VOCAB_SOURCE_MISMATCH')
        if mark['text_layout_revision'] != request['text_layout_revision']:
            errors.append('STALE_VOCAB_MARK_ANCHOR')
        glyph, underline = mark['glyph_bbox'], mark['mark_bbox']
        for box in [glyph, underline]:
            if box['x'] < 0 or box['y'] < 0 or box['x'] + box['width'] > width or box['y'] + box['height'] > height:
                errors.append('ANCHOR_OUTSIDE_CANVAS')
        if not glyph['y'] <= mark['baseline_y'] <= glyph['y'] + glyph['height']:
            errors.append('BASELINE_OUTSIDE_GLYPH')
        # One pixel permits raster rounding; measured boxes, not estimated locations.
        clearance = underline['y'] - glyph['y'] - glyph['height']
        if (abs(underline['x'] - glyph['x']) > 1 or abs(underline['width'] - glyph['width']) > 1
                or clearance < max(0, glyph['height'] * .08 - 1)
                or clearance > glyph['height'] * .12 + 1
                or not max(0, glyph['height'] * .10 - 1) <= underline['height'] <= glyph['height'] * .16 + 1):
            errors.append('UNDERLINE_GEOMETRY_MISMATCH')
    return errors


def validate(data, kind='slide-script', require_ready=False):
    try:
        json.dumps(data, allow_nan=False)
    except ValueError:
        return ['NON_FINITE_NUMBER']
    schema = json.loads((SCHEMAS / 'slide-script.schema.json').read_text(encoding='utf-8'))
    registry = Registry().with_resource(schema['$id'], Resource.from_contents(schema))
    selected = schema if kind == 'slide-script' else json.loads((SCHEMAS / 'render-request.schema.json').read_text(encoding='utf-8'))
    errors = [f'{list(e.absolute_path)}: {e.message}' for e in Draft202012Validator(selected, registry=registry).iter_errors(data)]
    if errors:
        return errors
    pairs = [(s, s.get('render_request')) for s in data['slides']] if kind == 'slide-script' else [(None, data)]
    for slide, request in pairs:
        if request is None:
            if require_ready:
                errors.append('RENDER_REQUEST_MISSING')
            continue
        if require_ready and request['request_state'] != 'RENDER_READY':
            errors.append('RENDER_REQUEST_NOT_READY')
        if slide:
            for key in ['page_family', 'idiom_application_plan', 'vocab_mark_plan', 'text_layout_revision', 'object_composition_plan', 'character_plan', 'key_line_plan']:
                default = [] if key == 'vocab_mark_plan' else None
                if slide.get(key, default) != request.get(key, default):
                    errors.append(f'SLIDE_RENDER_MISMATCH: {key}')
            if data['canvas_lock'] != request.get('canvas_lock'):
                errors.append('CANVAS_LOCK_MISMATCH')
        if request['request_state'] == 'RENDER_READY':
            errors.extend(validate_ready_text(request))
            if slide:
                if data['lesson_id'] != request['lesson_id']:
                    errors.append('LESSON_ID_MISMATCH')
                if set(slide.get('source_refs', [])) != set(request['source_refs']):
                    errors.append('SLIDE_SOURCE_MISMATCH')
                formal = [{k: layer[k] for k in ['layer_id', 'text', 'source_ref']}
                          for layer in slide.get('text_rendering', {}).get('layers', [])
                          if layer['visibility'] == 'STUDENT']
                if formal != request['verified_text']:
                    errors.append('SLIDE_VERIFIED_TEXT_MISMATCH')
                for key in ['title', 'student_visible_text']:
                    visible = slide['student_layer'].get(key)
                    if isinstance(visible, str) and visible and not any(visible in layer['text'] for layer in formal):
                        errors.append(f'STUDENT_TEXT_NOT_RENDERED: {key}')
            canvas = request.get('canvas_lock')
            if canvas and (any(request['output_spec'][k] != canvas[k] for k in ['width_px', 'height_px'])
                           or request['output_spec']['format'] not in canvas['output_formats']):
                errors.append('OUTPUT_CANVAS_MISMATCH')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--kind', choices=['slide-script', 'render-request'], default='slide-script')
    parser.add_argument('--require-ready', action='store_true')
    parser.add_argument('--result', type=Path, help='Final receipt for a single render-request; implies --require-ready')
    parser.add_argument('--digest', action='store_true', help='Print canonical request hash after validation')
    args = parser.parse_args()
    if (args.result or args.digest) and args.kind != 'render-request':
        parser.error('--result and --digest require --kind render-request')
    try:
        data = json.loads(args.path.read_text(encoding='utf-8-sig'))
        errors = validate(data, args.kind, args.require_ready or bool(args.result))
        if args.result and not errors:
            errors.extend(validate_result(data, json.loads(args.result.read_text(encoding='utf-8-sig')), args.result.parent))
    except (OSError, ValueError) as exc:
        print(f'INPUT_ERROR: {exc}')
        return 2
    if errors:
        print('\n'.join(errors))
    elif args.digest:
        print(request_digest(data))
    else:
        print('Presentation contract validation passed')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
