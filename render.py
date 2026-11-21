#!/usr/bin/env python3
"""Render the news-image-20261121 entry: a newspaper front page summing up
Saturday 21 November 2026. Output: entry.png (1024x1024, deterministic).
Drawn programmatically with Pillow; no AI image generation, so every
headline is exact text."""
import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 229)
INK = (26, 26, 26)
RED = (176, 42, 32)
BLUE = (31, 58, 95)
GREY = (96, 96, 96)
SAND = (214, 196, 150)
SEA = (140, 180, 205)
SKY = (232, 236, 240)
ORANGE = (230, 120, 20)
GREEN = (60, 110, 50)
GOLD = (255, 204, 0)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(d, xy, s, f, fill=INK):
    d.text(xy, s, font=f, fill=fill)


def text_c(d, cx, y, s, f, fill=INK):
    w = d.textlength(s, font=f)
    d.text((cx - w / 2, y), s, font=f, fill=fill)


def wrap(d, s, f, max_w):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, s, f, max_w, fill=INK, leading=6):
    lines = wrap(d, s, f, max_w)
    lh = f.size + leading
    for i, line in enumerate(lines):
        d.text((x, y + i * lh), line, font=f, fill=fill)
    return y + len(lines) * lh


def starburst(d, cx, cy, r, fill):
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)


def flag_us(d, x, y, w, h):
    stripe = h / 13
    for i in range(13):
        d.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe],
                    fill=(178, 34, 52) if i % 2 == 0 else (255, 255, 255))
    d.rectangle([x, y, x + w * 0.4, y + stripe * 7], fill=(30, 50, 110))
    for r in range(4):
        for c in range(5):
            d.ellipse([x + 4 + c * 7, y + 3 + r * 6, x + 7 + c * 7,
                       y + 6 + r * 6], fill=(255, 255, 255))


def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    starburst(d, x + w * 0.28, y + h * 0.3, 9, (255, 222, 0))


def flag_ru(d, x, y, w, h):
    for i, col in enumerate([(255, 255, 255), (0, 60, 160), (210, 30, 30)]):
        d.rectangle([x, y + i * h / 3, x + w, y + (i + 1) * h / 3], fill=col)


def flag_eu(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 51, 153))
    cx, cy = x + w / 2, y + h / 2
    rx, ry = w * 0.32, h * 0.30
    for i in range(12):
        ang = math.pi / 2 + i * math.pi / 6
        sx = cx + rx * math.cos(ang)
        sy = cy - ry * math.sin(ang)
        d.ellipse([sx - 2.5, sy - 2.5, sx + 2.5, sy + 2.5], fill=GOLD)


def flag_uk(d, x, y, w, h):
    # Simplified Union Jack: blue field, white saltire, red cross.
    d.rectangle([x, y, x + w, y + h], fill=(0, 36, 125))
    d.line([(x, y), (x + w, y + h)], fill=(255, 255, 255), width=7)
    d.line([(x + w, y), (x, y + h)], fill=(255, 255, 255), width=7)
    d.line([(x, y), (x + w, y + h)], fill=(200, 16, 46), width=2)
    d.line([(x + w, y), (x, y + h)], fill=(200, 16, 46), width=2)
    d.line([(x + w / 2, y), (x + w / 2, y + h)], fill=(255, 255, 255),
           width=12)
    d.line([(x, y + h / 2), (x + w, y + h / 2)], fill=(255, 255, 255),
           width=12)
    d.line([(x + w / 2, y), (x + w / 2, y + h)], fill=(200, 16, 46), width=7)
    d.line([(x, y + h / 2), (x + w, y + h / 2)], fill=(200, 16, 46), width=7)


def draw_lead_art(d):
    # London and Brussels rebuild ties: UK and EU flags on either side of
    # an intact bridge deck joining them, sun rising above.
    # Art area: x 650..990, y 235..470.
    starburst(d, 820, 268, 26, GOLD)
    starburst(d, 820, 268, 14, ORANGE)
    # flag poles
    for fx in (680, 905):
        d.line([(fx, 300), (fx, 392)], fill=INK, width=3)
    flag_uk(d, 683, 302, 84, 48)
    flag_eu(d, 838, 302, 84, 48)
    # skyline silhouettes beneath the flags
    base = 440
    for bx, top, bw in [(655, 392, 40), (700, 372, 34), (742, 398, 30),
                        (838, 380, 32), (876, 362, 30), (912, 392, 36),
                        (952, 402, 30)]:
        d.rectangle([bx, top, bx + bw, base], fill=BLUE)
        for wy in range(top + 10, base - 8, 16):
            for wx in range(bx + 6, bx + bw - 6, 12):
                d.rectangle([wx, wy, wx + 4, wy + 6], fill=GOLD)
    d.line([(650, base), (990, base)], fill=INK, width=3)
    # intact bridge deck: the rebuilt tie, spanning the gap
    d.line([(660, 452), (985, 452)], fill=INK, width=6)
    d.line([(660, 464), (985, 464)], fill=SEA, width=2)


def draw_bridge(d, x, y, w, h):
    # Kyiv bridge hit overnight: deck with a broken gap, blast, smoke.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    water_y = y + 122
    d.rectangle([x, water_y, x + w, y + h], fill=SEA)
    d.rectangle([x + 22, y + 28, x + 30, water_y], fill=INK)
    d.rectangle([x + 118, y + 28, x + 126, water_y], fill=INK)
    d.line([(x, y + 52), (x + 60, y + 52)], fill=INK, width=7)
    d.line([(x + 92, y + 52), (x + w, y + 52)], fill=INK, width=7)
    d.line([(x + 62, y + 60), (x + 90, y + 108)], fill=INK, width=6)
    d.line([(x + 26, y + 30), (x + 60, y + 52)], fill=GREY, width=2)
    d.line([(x + 26, y + 30), (x + 4, y + 52)], fill=GREY, width=2)
    d.line([(x + 122, y + 30), (x + 92, y + 52)], fill=GREY, width=2)
    d.line([(x + 122, y + 30), (x + 148, y + 52)], fill=GREY, width=2)
    starburst(d, x + 76, y + 52, 22, ORANGE)
    starburst(d, x + 76, y + 52, 12, RED)
    d.ellipse([x + 52, y + 4, x + 82, y + 28], fill=(150, 150, 150))
    d.ellipse([x + 72, y - 2, x + 102, y + 20], fill=(180, 180, 180))


def draw_scales(d, x, y, w, h):
    # The scales of justice: the ICJ's genocide verdict.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    cx = x + w / 2
    base_y = y + h - 20
    d.rectangle([x + 18, base_y, x + w - 18, base_y + 8], fill=BLUE)
    d.rectangle([cx - 4, y + 22, cx + 4, base_y], fill=BLUE)
    d.ellipse([cx - 7, y + 12, cx + 7, y + 26], fill=BLUE)
    d.line([(cx - 58, y + 34), (cx + 58, y + 34)], fill=BLUE, width=5)
    for px in (cx - 58, cx + 58):
        d.line([(px, y + 34), (px - 24, y + 78)], fill=INK, width=2)
        d.line([(px, y + 34), (px + 24, y + 78)], fill=INK, width=2)
        d.line([(px, y + 34), (px, y + 78)], fill=INK, width=2)
        d.pieslice([px - 26, y + 76, px + 26, y + 104], 0, 180, fill=BLUE)
    d.rectangle([cx - 26, base_y - 14, cx + 26, base_y], fill=BLUE)


def draw_summit(d, x, y, w, h):
    # Three flags over a globe: the first Trump–Xi–Putin three-way talks.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    flag_us(d, x + 6, y + 12, 42, 28)
    flag_cn(d, x + 54, y + 12, 42, 28)
    flag_ru(d, x + 102, y + 12, 42, 28)
    cx, cy = x + w / 2, y + 108
    d.ellipse([cx - 42, cy - 42, cx + 42, cy + 42], fill=SEA,
              outline=BLUE, width=2)
    d.ellipse([cx - 18, cy - 42, cx + 18, cy + 42], outline=BLUE, width=2)
    d.line([(cx - 42, cy), (cx + 42, cy)], fill=BLUE, width=2)
    d.line([(cx - 36, cy - 24), (cx + 36, cy - 24)], fill=BLUE, width=1)
    d.line([(cx - 36, cy + 24), (cx + 36, cy + 24)], fill=BLUE, width=1)
    d.line([(x + 14, y + h - 34), (x + w - 14, y + h - 62)], fill=GREEN,
           width=4)
    for lx, ly in [(x + 38, y + h - 44), (x + 68, y + h - 52),
                   (x + 98, y + h - 60)]:
        d.ellipse([lx, ly, lx + 22, ly + 10], fill=GREEN)


def draw_fall(d, x, y, w, h):
    # A market sell-off: falling bars and a descending arrow.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    f = font(SANS_B, 26)
    text_w(d, (x + 8, y + 8), "DOWN", f, fill=RED)
    base_y = y + h - 26
    d.line([(x + 12, y + 34), (x + 12, base_y)], fill=INK, width=2)
    d.line([(x + 12, base_y), (x + w - 8, base_y)], fill=INK, width=2)
    bars = [(26, 112), (52, 84), (78, 62), (104, 42)]
    for bx, bh in bars:
        d.rectangle([x + bx, base_y - bh, x + bx + 18, base_y], fill=RED)
    d.line([(x + 24, y + 44), (x + 128, base_y - 34)], fill=RED, width=4)
    d.polygon([(x + 128, base_y - 34), (x + 112, base_y - 34),
               (x + 128, base_y - 50)], fill=RED)


def panel(d, x, y, w, h, kicker, headline, caption, art):
    art(d, x + 8, y + 8, 148, h - 16)
    tx = x + 164
    f_k = font(SANS_B, 20)
    f_h = font(SANS_B, 26)
    f_c = font(SANS, 20)
    text_w(d, (tx, y + 10), kicker, f_k, fill=RED)
    hl = wrap(d, headline, f_h, w - 172)
    hy = y + 36
    for i, line in enumerate(hl):
        d.text((tx, hy + i * 31), line, font=f_h, fill=INK)
    cy = hy + len(hl) * 31 + 4
    para(d, tx, cy, caption, f_c, w - 172, leading=4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # frames
    d.rectangle([10, 10, 1014, 1014], outline=INK, width=5)
    d.rectangle([20, 20, 1004, 1004], outline=INK, width=2)

    # ---- masthead ----
    f_small = font(SANS_B, 24)
    text_w(d, (38, 36), "SATURDAY", f_small)
    wr = d.textlength("WORLD NEWS", font=f_small)
    text_w(d, (986 - wr, 36), "WORLD NEWS", f_small)
    f_mast = font(SERIF_B, 92)
    text_c(d, 512, 66, "21 NOVEMBER 2026", f_mast)
    f_sub = font(SANS_B, 25)
    text_c(d, 512, 168, "THE WORLD'S NEWS IN ONE IMAGE", f_sub, fill=GREY)
    d.line([(36, 208), (988, 208)], fill=INK, width=4)
    d.line([(36, 216), (988, 216)], fill=INK, width=2)

    # ---- lead story: UK–EU landmark deal ----
    f_k = font(SANS_B, 22)
    f_h = font(SANS_B, 34)
    f_c = font(SANS, 25)
    text_w(d, (36, 236), "LONDON  ·  BREXIT RESET", f_k, fill=RED)
    text_w(d, (36, 264), "UK AND EU STRIKE 'LANDMARK'", f_h)
    text_w(d, (36, 300), "DEAL TO REBUILD TIES", f_h)
    para(d, 36, 344, "PM Burnham says the UK will explore even closer ties "
       "with the EU after the landmark deal to rebuild relations "
       "following Brexit.", f_c, 600, leading=5)
    draw_lead_art(d)
    d.line([(36, 478), (988, 478)], fill=INK, width=3)

    # ---- 2x2 grid ----
    gx, gy = 36, 488
    cw, ch = 466, 200
    panel(d, gx, gy, cw, ch, "KYIV · WAR", "MISSILES RAIN ON UKRAINE",
          "100+ missiles, 400 drones; Polish airspace entered; 3 Kyiv "
          "bridges hit; EU adds €1bn, UK 1,000+ drones.", draw_bridge)
    panel(d, gx + cw + 20, gy, cw, ch, "THE HAGUE · JUSTICE",
          "MYANMAR GUILTY OF GENOCIDE",
          "ICJ rules 9–6 on 20 Nov; UK expels Myanmar's diplomat; "
          "Rohingya rejoice.", draw_scales)
    d.line([(36, gy + ch + 6), (988, gy + ch + 6)], fill=GREY, width=1)
    panel(d, gx, gy + ch + 12, cw, ch, "SHENZHEN · SUMMIT",
          "THREE-WAY PEACE TALKS",
          "Peace declaration after first Trump–Xi–Putin talks (19 Nov); "
          "Trump eyes AI-centre tax; SEC probes Nvidia.",
          draw_summit)
    panel(d, gx + cw + 20, gy + ch + 12, cw, ch, "WALL STREET · MARKETS",
          "TECH SELL-OFF DRAGS MARKETS",
          "Tech stocks slide as Anthropic shares fall, a day after "
          "debuting +34% on 20 Nov.", draw_fall)
    d.line([(36, 906), (988, 906)], fill=INK, width=3)

    # ---- footer briefs ticker ----
    f_b = font(SANS_B, 18)
    f_bt = font(SANS, 16)
    briefs = [
        ("RIKERS", "Mamdani plans to close Rikers Island jail by 2032."),
        ("UFO FILES", "US declassifies UFO footage filmed in the Mideast."),
        ("ASSASSINATION PLOT", "Denmark: Russia plotted to kill a US-Ukrainian rapper."),
        ("AI SAFETY", "California proposes powers to disable risky AI models."),
    ]
    bx = 36
    bw = 226
    for kicker, txt in briefs:
        text_w(d, (bx, 914), kicker, f_b, fill=RED)
        para(d, bx, 932, txt, f_bt, bw, leading=3)
        bx += bw + 16

    # ---- sources footer ----
    # Thin rule plus one small-type line crediting the news sources.
    # Briefs above end at y=970 (two 16px lines from y=932), so the rule
    # sits at 978 and the line at 984, clear of the inner frame at 1004.
    d.line([(36, 978), (988, 978)], fill=GREY, width=1)
    f_src = font(SANS, 13)
    text_c(d, 512, 984, "Sources: AP · BBC · CNN · Le Monde · The Times",
           f_src, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
