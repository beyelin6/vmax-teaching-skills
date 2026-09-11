#!/usr/bin/env python3
"""Measured, paginated font QA samples; visual approval remains manual."""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from font_policy import BOPOMOFO, font_metadata

W, H = 2560, 1440

def wrap_text(draw, text, font, width):
    lines = []
    for paragraph in text.split('\n'):
        line = ''
        for char in paragraph:
            box = draw.textbbox((0, 0), line + char, font=font)
            if box[2] - box[0] > width:
                if not line:
                    raise ValueError('One glyph exceeds column width')
                lines.append(line)
                line = char
            else:
                line += char
        lines.append(line)
    return lines

def render(args):
    body, title = (args.body_font, 46), (args.title_font, 64)
    character = (args.character_font, 100)
    lesson = args.lesson_text
    if args.lesson_text_file:
        lesson += Path(args.lesson_text_file).read_text(encoding='utf-8')
    blocks = [(title, '繁中文字型檢查'), (body, '請目視確認字形、標點、行距及換行。'),
              (title, '繁體中文與臺灣字形'),
              (body, '臺灣的孩子在課堂上閱讀、討論，也練習把想法說清楚。'),
              (character, '麥齒醫衛獻灣臺邊學夢'),
              (title, '本課目標字與關鍵詞'), (character, lesson),
              (title, '標點與閱讀'), (body, '「老師說：『讀一讀、想一想。』」'),
              (title, '字級階層'), (body, '正文範例：閱讀、討論與觀察。')]
    if args.bopomofo_font:
        blocks += [(title, '注音與聲調'), ((args.bopomofo_font, 48), BOPOMOFO),
                   ((args.bopomofo_font, 48), 'ㄍㄨㄛˊ ㄩˇ ㄒㄩㄝˊ ㄒㄧˊ')]
    blocks += [(title, '最終人工檢查'), (body, '確認無方框、缺字、錯誤字形或遮擋。\n確認聲調位置與基線。\n字型替換後重新檢查最終成品。')]
    pages, boxes = [], []
    image = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(image)
    column, y = 0, 100
    for (path, size), text in blocks:
        _, _, coverage = font_metadata(Path(path))
        missing = sorted({c for c in text if not c.isspace() and ord(c) not in coverage})
        if missing:
            raise ValueError(f'{path}: missing glyphs {missing}')
        font = ImageFont.truetype(path, size)
        for line in wrap_text(draw, text, font, 1100):
            b = draw.textbbox((0, 0), line or ' ', font=font)
            height = max(size, b[3] - b[1]) + 16
            reserve = 146 if size == 64 else 0
            if y + height + reserve > H - 100:
                column += 1
                y = 100
                if column == 2:
                    pages.append(image)
                    image = Image.new('RGB', (W, H), 'white')
                    draw = ImageDraw.Draw(image)
                    column = 0
            x = 100 + column * 1260
            draw.text((x-b[0], y-b[1]), line, font=font, fill='black')
            boxes.append({'page': len(pages)+1, 'bbox': [x, y, x+b[2]-b[0], y+b[3]-b[1]]})
            y += height
        y += 30
    pages.append(image)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    outputs = []
    for i, image in enumerate(pages):
        target = out if i == 0 else out.with_name(f'{out.stem}-{i+1:02d}{out.suffix}')
        image.save(target, 'PNG')
        outputs.append(str(target))
    report = {'pages': outputs, 'text_boxes': boxes, 'visual_qa': 'not_run'}
    out.with_suffix('.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return report

def main():
    p = argparse.ArgumentParser(description=__doc__)
    for role in ('body', 'title', 'character'):
        p.add_argument(f'--{role}-font', required=True)
    p.add_argument('--bopomofo-font')
    p.add_argument('--lesson-text', default='')
    p.add_argument('--lesson-text-file')
    p.add_argument('--output', default='bee-font-qa-2560x1440.png')
    print(json.dumps(render(p.parse_args()), ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
