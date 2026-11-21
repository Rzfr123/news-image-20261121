# 21 November 2026 — The World's News in One Image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Rzfr123/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Rzfr123/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page summing up Saturday 21 November 2026. The masthead names the day; four panels plus four briefs cover the day's biggest stories.

Bounty: https://make.fun/bounty/news-image-20261121

## Stories

- **UK and EU strike a 'landmark' deal** — PM Burnham says the UK will explore even closer ties with the EU as the two sides rebuild relations after Brexit.
- **Missiles rain on Ukraine** — Russia fires 100+ missiles and 400 drones; a missile and a drone enter Polish airspace; 3 Kyiv bridges hit; the EU adds €1bn for drones and the UK 1,000+ drones.
- **Myanmar guilty of genocide** — The ICJ rules 9–6 (20 Nov); the UK expels Myanmar's diplomat; Rohingya rejoice.
- **Three-way peace talks** — Trump, Xi and Putin meet in Shenzhen (19 Nov) and declare peace; Trump eyes a tax on AI centres abroad; the SEC probes Nvidia.
- **Tech sell-off drags markets** — Tech stocks slide as Anthropic shares fall, a day after debuting +34% on 20 Nov.
- Briefs: Mamdani plans to close New York's Rikers Island jail by 2032; the US declassifies more UFO footage filmed in the Middle East; Denmark accuses Russia of plotting to kill a US-Ukrainian rapper; California proposes emergency powers to disable risky AI models.

## How it was made

`render.py` composites the front page over an AI-generated photo of Earth at night (`bg_photo.jpg`), dimmed and softly blurred under a translucent paper sheet; all headlines and panels are drawn programmatically with Pillow, so every headline is exact. `main.ts` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies its PNG magic bytes, IHDR dimensions (1024x1024), bit depth / colour type, size and SHA-256 digest.

## Sources

- Reporting of Saturday 21 November 2026 by AP, BBC, CNN, Le Monde and The Times, as summarised in `run-notes.md`.

## License

MIT — see LICENSE.
