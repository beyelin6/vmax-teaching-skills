#!/usr/bin/env python3
"""Render a 2560x1440 V-MAX Traditional Chinese font QA page.

The page is intentionally text-heavy and includes Traditional Chinese, Bopomofo,
lesson-character samples, punctuation, multiple sizes, and paired role examples.
Use it after font preflight and before representative-page production.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 2560, 1440
BG = "white"
TEXT = "black"


def load_font(path: str, size: int):
    return ImageFont.truetype(path, size=size)


def draw_text(draw, xy, text, font, fill=TEXT, spacing=8):
    draw.multiline_text(xy, text, font=font, fill=fill, spacing=spacing)


def main() -> int:
    p = argparse.ArgumentParser(description="Render Bee teacher font QA page")
    p.add_argument("--body-font", required=True)
    p.add_argument("--title-font", required=True)
    p.add_argument("--character-font", required=True)
    p.add_argument("--bopomofo-font", required=True)
    p.add_argument("--lesson-text", default="奉獻 良方 居家衛生 捐錢 食宿 永遠的馬偕")
    p.add_argument("--output", default="bee-font-qa-2560x1440.png")
    args = p.parse_args()

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    title = load_font(args.title_font, 84)
    body = load_font(args.body_font, 46)
    body_small = load_font(args.body_font, 36)
    char_big = load_font(args.character_font, 112)
    bop = load_font(args.bopomofo_font, 48)

    # Header
    draw_text(d, (110, 70), "Bee老師教材字型 QA｜2560×1440", title)
    draw_text(d, (115, 180), "用途：正式簡報／PNG／PDF 批次輸出前的繁中與注音目視檢查", body_small)

    # Section 1
    draw_text(d, (120, 290), "① 繁體中文與臺灣常用字形", title)
    draw_text(d, (140, 400), "永遠的馬偕｜學習重點｜臺灣｜醫療教育｜體驗與觀察", body)
    draw_text(d, (140, 470), "麥 齒 醫 衛 獻 灣 臺 邊 學 夢", char_big)

    # Section 2
    draw_text(d, (120, 650), "② 注音與聲調", title)
    draw_text(d, (140, 765), "國語  ㄍㄨㄛˊ  ㄩˇ    學習  ㄒㄩㄝˊ  ㄒㄧˊ", bop)
    draw_text(d, (140, 835), "ㄅ ㄆ ㄇ ㄈ ㄉ ㄊ ㄋ ㄌ ㄍ ㄎ ㄏ ㄐ ㄑ ㄒ ㄓ ㄔ ㄕ ㄖ ㄗ ㄘ ㄙ", bop)

    # Section 3
    draw_text(d, (120, 950), "③ 本課目標字／關鍵詞", title)
    draw_text(d, (140, 1065), args.lesson_text, body)

    # Section 4
    draw_text(d, (1450, 290), "④ 標點與閱讀密度", title)
    sample = "「老師說：『讀一讀、想一想。』」\n臺灣的孩子在課堂上閱讀、討論，也練習把想法說清楚。"
    draw_text(d, (1470, 410), sample, body)

    draw_text(d, (1450, 650), "⑤ 字級階層", title)
    draw_text(d, (1470, 770), "主標題 84 px", title)
    draw_text(d, (1470, 885), "正文 46 px｜適合中年級簡報", body)
    draw_text(d, (1470, 955), "補充說明 36 px｜僅用於次要資訊", body_small)

    draw_text(d, (1450, 1080), "⑥ 最終人工檢查", title)
    checklist = "□ 無方框／缺字   □ 注音位置正常\n□ 標點正常       □ 行距清楚\n□ fallback 未造成換行崩壞\n□ 學生可見文字清楚、不遮圖"
    draw_text(d, (1470, 1190), checklist, body_small)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
