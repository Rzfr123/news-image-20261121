# Run notes — news-image-20261121

Entry title: **21 November 2026 — The World's News in One Image**

## Stories chosen (all from Saturday 21 November 2026 unless noted)

| Slot | Story | Note |
|---|---|---|
| Lead | UK and EU strike a 'landmark' deal to rebuild ties after Brexit; PM Burnham says the UK will explore even closer ties with the EU | Masthead names the day: "21 NOVEMBER 2026" |
| Panel 1 | Russia fires 100+ missiles and 400 drones at Ukraine; a Russian missile and a drone enter Polish airspace (PM Tusk confirms); Russia hits 3 Kyiv bridges days after Ukraine hit the Crimean Bridge; 2 killed, 42 injured in Kryvyi Rih; EU agrees €1 billion more for Ukraine drones and air defence; UK to deliver 1,000+ long-range drones | Kryvyi Rih casualties and the Crimean Bridge context did not fit the panel caption; recorded here |
| Panel 2 | ICJ finds Myanmar guilty of Rohingya genocide (9–6, verdict 20 Nov) — follow-up: UK expels Myanmar's diplomat; Rohingya rejoice | Verdict dated 20 Nov, follow-up on 21 Nov |
| Panel 3 | Trump–Xi–Putin first three-way talks in Shenzhen (19 Nov) + joint peace declaration; Trump says 'no immediate hurry' on Iran, 'We've got time', Iran war could continue into 2027; Trump threatens a tax/ban on US firms building AI data centres abroad; Nvidia's accounting is a target of a US SEC investigation | Iran 'no hurry' / into-2027 detail did not fit the panel caption; recorded here |
| Panel 4 | Markets — tech stock sell-off drags markets down as Anthropic shares slide (Anthropic debuted +34% on 20 Nov) | |
| Brief (on page) | Mamdani announces plan to close New York's Rikers Island jail by 2032 | |
| Brief (on page) | US declassifies more UFO footage filmed in the Middle East | |
| Brief (on page) | Denmark accuses Russia of plotting to assassinate a US-Ukrainian rapper | |
| Brief (on page) | California proposes emergency powers to disable risky AI models | |
| Brief (notes only) | Nearly 600 women killed in South Africa within three months | Fifth brief; front page holds four, this one is recorded here |

Design: newspaper front page, masthead "21 NOVEMBER 2026", drawn programmatically
with `render.py` (Python + Pillow, DejaVu/Liberation fonts). No AI image generation,
so all text is exact. Simple drawn icons per story (UK + EU flags over a skyline
and an intact bridge, broken Kyiv bridge, scales of justice, three flags over a
globe, falling market chart).

## Image

- File: `entry.png`
- Dimensions: 1024 x 1024 px
- Size: 141,056 bytes (limit 1,048,576)
- SHA-256: `6294b88e40e40b684bd8b3f4c222c29fad7a0e71441eb255e453a9f3921e67ae`

## Local tests (2026-11-21 ~13:30 WIB)

- `python3 render.py` — rendered cleanly. Image visually checked twice:
  first render had the Shenzhen panel caption spilling a 5th line ("Nvidia.")
  onto the footer rule — shortened the caption to "Trump eyes AI-centre tax"
  and removed a stray green arc from the lead art, added windows to the
  lead skyline towers. Re-checked: no overlaps, no clipped text, all icons
  recognisable, legible at small size.
- `main.ts` v1 tested first (magic-bytes + size check only):
  `MAKEFUN_OUTPUT_DIR=/tmp/n21-out1 node main.ts` from the repo dir —
  exit 0, digest matches source, `cmp` clean.
- `main.ts` v2 is a genuine revision of v1: added IHDR dimension validation
  (exactly 1024x1024) and bit-depth 8 / colour-type 2 validation, and the
  `1024x1024` dimensions in the success line. The file in the repo is the
  tested v2.
- `MAKEFUN_OUTPUT_DIR=/tmp/n21-out1 node main.ts` (v2, from the repo dir) —
  exit 0, digest `6294b88e...1e67ae`. Run again from /tmp with the absolute
  path (`/tmp/n21-out2`) — exit 0, same digest, `cmp` clean both ways.
- Default-output test: `cd /tmp && env -u MAKEFUN_OUTPUT_DIR node
  <repo>/main.ts` → exit 0, wrote `/output/entry.png`, byte-identical
  (`cmp` clean).
- Negative tests: non-PNG file → exit 1 ("not a PNG (bad magic bytes)");
  forged IHDR (height patched 1024 → 1280) → exit 1 ("IHDR dimensions
  1024x1280, expected exactly 1024x1024").
- PIL verified `/tmp/n21-out1/entry.png`: valid PNG, 1024x1024 RGB,
  141,056 bytes.
- README 2,405 bytes (< 4096), carries the 3 live make.fun badges +
  bounty link. LICENSE carries `SPDX-License-Identifier: MIT`.
  `.makefun/owner.json` is exactly
  `{"wallet": "bDXdfcW6wZ1hmDZnnH4eJLhXEbYUkV7AAKZHagdnoPg"}`.

## Files in repo

`main.ts`, `package.json`, `entry.png`, `render.py`, `README.md`, `LICENSE`,
`.makefun/owner.json`, `run-notes.md`, `.gitignore`

## Bundle notes (for the parent's later step — NOT acted on here)

- DO NOT bundle/submit from this session; parent bundles/submits only
  after the user's approval. Competition close time not verified in this
  session — re-check before any submit (daily pattern suggests
  2026-11-23T00:00:00Z / 23 Nov 07:00 WIB, unconfirmed).
- This session built the entry only; no `makefun` submit/record commands
  were run.
