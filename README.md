# makefun-news-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/Fauziwildan0856/makefun-news-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/Fauziwildan0856/makefun-news-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A one-page newspaper image summing up Friday 27 November 2026's world news: 19 stories on a single page, with 16 pictured panels — the Okinawa floods, the India–New Zealand Test, Australia's DFAT audit, and a $150M Powerball jackpot among them. The page carries a realistic Earth-globe map, a UTC timeline, confidence chips on the pictured panels, and notebook-ruled briefs for the text-only stories, all drawn in a 3D style on bright white paper.

## Run it

```sh
python3 main.py
# or, to choose the output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## How it works

`main.py` (Python standard library only) verifies the stored image's SHA-256 against the approved digest, copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), then reads the copy back and verifies its hash again. It exits 0 only when both the stored image and the delivered copy match exactly.

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=z63ha401&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
