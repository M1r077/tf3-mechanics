"""Search the game's Lua / Teal sources (read-only).

    python grep.py REGEX [PATH_FILTER] [--ctx N]

PATH_FILTER is a substring of the source id (e.g. "stations/", "gui.zip!gui/main").
"""
import re
import sys

import sources


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--ctx")]
    ctx = 0
    for a in sys.argv[1:]:
        if a.startswith("--ctx"):
            ctx = int(a.split("=", 1)[1]) if "=" in a else 2
    rx = re.compile(args[0])
    filt = args[1] if len(args) > 1 else ""
    for sid, _size in sources.iter_sources():
        if filt not in sid:
            continue
        lines = sources.read(sid).splitlines()
        hits = [i for i, l in enumerate(lines) if rx.search(l)]
        if not hits:
            continue
        print(f"== {sid}")
        shown = set()
        for i in hits:
            for j in range(max(0, i - ctx), min(len(lines), i + ctx + 1)):
                if j not in shown:
                    shown.add(j)
                    print(f"{j + 1:6}{'>' if j == i else ':'} {lines[j].rstrip()[:200]}")


if __name__ == "__main__":
    main()
