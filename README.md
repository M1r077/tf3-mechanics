# TF3 Mechanics

How Transport Fever 3 really works, explained from the game's own Lua / Teal scripts and checked against the
[official wiki](https://wiki.transportfever3.com). English, French and German.

Fan project. Not affiliated with Urban Games.

## What is published

- `docs/`: the site (GitHub Pages, static HTML, no build step on GitHub).
- `content/<lang>/*.md`: the explanations, written by hand. Game code is never copied: pages give values and
  `file:line` references only.
- The tools that build and check the site.

`data/index.json` and `cache/` are derived from the game files and the official wiki: they stay local
(`.gitignore`).

## Tools

Python 3.12 with `markdown`. The game folder is read in place, zips included, nothing is extracted
(`TF3_GAME` environment variable, default `A:\SteamLibrary\steamapps\common\Transport Fever 3`).

| Script | Does |
|---|---|
| `scan.py` | indexes every .lua / .tl file of `base/content` (zips included) into `data/index.json`; after a game update, lists the changed files and the pages that cite them |
| `grep.py REGEX [PATH]` | searches the game sources |
| `gamestrings.py MSGID` | the game's own translation of a label in en / fr / de |
| `official.py` | reads the official wiki's Game Manual pages (ids from its navigation) into `cache/official/` |
| `build.py` | builds `docs/` from `content/`, `data/domains.json` and the diagrams of `diagrams.py` |
| `check.py` | same pages and references in every language, references exist, no long code copies, no broken links |

    python scan.py
    python build.py
    python check.py

## Writing a page

`content/en/<slug>.md`, then the same slug in `fr` and `de`, with the same references and diagrams:

    ---
    title: ...
    summary: one sentence for the index card
    domain: industries          (id from data/domains.json)
    official: gamemanual:simulation:industriescargos#booster
    status: verified            (verified | draft | engine)
    updated: 2026-11-14
    ---

- `` `file.tl:12-20` `` is a source reference (checked by `check.py`);
- ` ```diagram NAME ``` ` inserts a diagram of `diagrams.py`;
- ` ```engine ``` ` marks what the engine decides (not visible in the scripts);
- ` ```tip ``` ` is a gold box with a practical tip measured in game;
- ` ```check ``` ` is the box comparing the official wiki and the scripts (`official:`, `scripts:`,
  `result: agrees | refines | differs`).

Quote in-game labels with the game's own translation (`gamestrings.py`).

## Licence

- Texts and images (`content/`, `docs/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), see
  `LICENSE-CONTENT`.
- Tools (`*.py`): GPL-3.0, see `LICENSE`.
- Transport Fever 3 and its code are © Urban Games GmbH.
