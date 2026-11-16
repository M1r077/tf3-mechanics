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
| `scan.py` | indexes every .lua / .tl file of `base/content` (zips included) into `data/index.json` and keeps a snapshot of the game build (`cache/builds/<build>/`); after a game update, lists the changed files and the pages that cite them |
| `scan.py --diff A B [--renumber]` | every page reference whose lines differ between two builds; references whose code only moved get their new line numbers (`--renumber` writes them in every language) |
| `notes.py` | reads the official release notes into `data/builds.json` and prints the task list: notes not triaged yet, pages to update, things to measure in game |
| `grep.py REGEX [PATH]` | searches the game sources |
| `gamestrings.py MSGID` | the game's own translation of a label in en / fr / de |
| `official.py` | reads the official wiki's Game Manual pages (ids from its navigation) into `cache/official/` |
| `build.py` | builds `docs/` from `content/`, `data/domains.json` and the diagrams of `diagrams.py` |
| `check.py` | same pages and references in every language, references exist, no long code copies, no broken links |

    python scan.py
    python build.py
    python check.py

## Game versions

The wiki describes the **stable** game. Each page says which build it was checked on (`game: 40425`), and
`check.py` refuses a preview build there.

Preview builds reach stable later, so their release notes are the to-do list. `python notes.py` reads the
[official release notes](https://wiki.transportfever3.com/doku.php?id=releasenotes) into `data/builds.json`;
every note gets a triage, written by hand in that file:

| status | meaning |
|---|---|
| `new` | not looked at yet |
| `todo` | pages to check or update (`pages`) |
| `watch` | to measure in game (`pages`, or `dashboard` for the companion mod) |
| `done` | handled, or already in the build the pages were checked on |
| `none` | nothing for the wiki |

A note keeps its triage when the same text appears again under a stable build. `notes.py` then warns that it
reached stable.

When a new stable build is installed:

1. `python scan.py`: snapshot of the new build (the build number comes from the game's log, or `TF3_BUILD`).
2. `python scan.py --diff OLD NEW --renumber`: moved references are renumbered; the changed ones are read again.
3. Update the pages of the `todo` / `watch` notes of that build, set them to `done`.
4. Set `game:` to the new build on every page checked, and add a `change:` line where a mechanic changed.
5. `git tag game-OLD` on the last commit that described the old build, so its text stays available.

A page header can carry the history of a mechanic, shown in a box at the end of the page:

    game: 40438
    change: 40438 | Building cargo stocks are kept when a street is upgraded.

## Writing a page

`content/en/<slug>.md`, then the same slug in `fr` and `de`, with the same references and diagrams:

    ---
    title: ...
    summary: one sentence for the index card
    domain: industries          (id from data/domains.json)
    official: gamemanual:simulation:industriescargos#booster
    status: verified            (verified | draft | engine)
    updated: 2026-11-14
    game: 40425                 (stable build the page was checked on)
    ---

- `` `file.tl:12-20` `` is a source reference (checked by `check.py`);
- ` ```diagram NAME ``` ` inserts a diagram of `diagrams.py`;
- ` ```engine ``` ` marks what the engine decides (not visible in the scripts);
- ` ```tip ``` ` is a gold box with a practical tip measured in game; ` ```tip scripts ``` ` is a tip that follows from the scripts (no "measured in game" subtitle). Pages with tips get a "Tips" button next to "Sources": tips are shown by default, the reader can hide them (kept in `localStorage` `tf3tips`);
- ` ```check ``` ` is the box comparing the official wiki and the scripts (`official:`, `scripts:`,
  `result: agrees | refines | differs`).

Quote in-game labels with the game's own translation (`gamestrings.py`).

## Licence

- Texts and images (`content/`, `docs/`): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), see
  `LICENSE-CONTENT`.
- Tools (`*.py`): GPL-3.0, see `LICENSE`.
- Transport Fever 3 and its code are © Urban Games GmbH.
