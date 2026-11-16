"""Scan every Lua / Teal file of the game and write data/index.json.

For each file: domain, size, sha1, functions it defines and the numeric constants it sets (name = number).
Run again after a game update: files whose sha1 changed are listed, with the wiki pages that cite them
(pages must then be checked again).

Every scan also keeps a snapshot of the game build it read (cache/builds/<build>/: the sha1 of every file and
a copy of every file a page cites; local only, game code is never published). Two snapshots can then be
compared reference by reference:

    python scan.py                    scan the installed game (build read from the game's log, or TF3_BUILD)
    python scan.py --diff 40425 40438 every cited reference whose lines changed between two builds, by page,
                                      with the new line numbers when the code only moved
    ... --diff A B --renumber         also rewrites the moved references in every language
"""
import difflib
import hashlib
import json
import os
import re
import sys

import sources

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "data", "index.json")
CONTENT_DIR = os.path.join(HERE, "content")
SNAPSHOTS = os.path.join(HERE, "cache", "builds")
GAME_LOG = os.environ.get("TF3_LOG", os.path.join(
    os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"), "Steam", "userdata"))
RX_REF = re.compile(r"`([\w./-]+\.(?:lua|tl)):(\d+)(?:-(\d+))?`")


def game_build():
    """Build number of the installed game: TF3_BUILD, else the newest "Starting up build version" in a log.

    The log is userdata/<id>/3493540/local/crash_dump/stdout.txt (rewritten at every start of the game)."""
    if os.environ.get("TF3_BUILD"):
        return int(os.environ["TF3_BUILD"])
    best = None
    if os.path.isdir(GAME_LOG):
        for uid in os.listdir(GAME_LOG):
            p = os.path.join(GAME_LOG, uid, "3493540", "local", "crash_dump", "stdout.txt")
            if os.path.exists(p):
                with open(p, encoding="utf-8", errors="replace") as f:
                    m = re.search(r"Starting up build version:\s*(\d+)", f.read(20000))
                if m and (best is None or os.path.getmtime(p) > best[0]):
                    best = (os.path.getmtime(p), int(m.group(1)))
    return best[1] if best else None


def page_refs():
    """[(page, file, first, last)] of every line reference in the English pages (the other languages
    carry the same references, check.py enforces it)."""
    out = []
    d = os.path.join(CONTENT_DIR, "en")
    for f in sorted(os.listdir(d)):
        if f.endswith(".md"):
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                for m in RX_REF.finditer(fh.read()):
                    a = int(m.group(2))
                    out.append((f[:-3], m.group(1), a, int(m.group(3) or a)))
    return out


def write_snapshot(build, files):
    """cache/builds/<build>/: hashes.json (every file) and src/ (the cited files, as read)."""
    root = os.path.join(SNAPSHOTS, str(build))
    os.makedirs(os.path.join(root, "src"), exist_ok=True)
    with open(os.path.join(root, "hashes.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"build": build, "game": sources.GAME,
                   "files": {k: v["sha1"] for k, v in files.items()}}, f, indent=0)
    cited = {name for _p, name, _a, _b in page_refs()}
    kept = 0
    for sid in files:
        if sources.short(sid) in cited or sources.short(sid).split("/")[-1] in cited:
            dest = os.path.join(root, "src", sid.replace("!", "__").replace("/", "__"))
            with open(dest, "w", encoding="utf-8", newline="\n") as f:
                f.write(sources.read(sid))
            kept += 1
    return root, kept


def snapshot_text(build, name):
    """{source id: lines} of the cited file `name` (a path or a bare file name) in a snapshot."""
    src = os.path.join(SNAPSHOTS, str(build), "src")
    if not os.path.isdir(src):
        raise SystemExit(f"no snapshot of build {build} in {os.path.relpath(SNAPSHOTS, HERE)} (run scan.py on it)")
    out = {}
    for fn in os.listdir(src):
        sid = fn.replace("__", "/")
        if sid.endswith("/" + name) or sid == name:
            with open(os.path.join(src, fn), encoding="utf-8") as f:
                out[sid] = f.read().splitlines()
    return out


def moved_to(old, new, a, b):
    """New line range of old[a-1:b] in new, when those lines are unchanged and only moved; else None."""
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    for tag, i1, i2, j1, _j2 in sm.get_opcodes():
        if tag == "equal" and i1 <= a - 1 and b <= i2:
            return j1 + (a - 1 - i1) + 1, j1 + (b - 1 - i1) + 1
    return None


def diff(build_a, build_b):
    """Prints, page by page, the references whose lines differ between two snapshots."""
    by_page, n_ok = {}, 0
    cache = {}
    for page, name, a, b in page_refs():
        for build in (build_a, build_b):
            if (build, name) not in cache:
                cache[(build, name)] = snapshot_text(build, name)
        old_all, new_all = cache[(build_a, name)], cache[(build_b, name)]
        if not old_all:
            continue  # not a game file of this snapshot (check.py reports unknown files)
        if not new_all:
            by_page.setdefault(page, []).append(f"{name}:{a}-{b}  file gone in {build_b}")
            continue
        sid = next(iter(old_all))
        old, new = old_all[sid], new_all.get(sid) or next(iter(new_all.values()))
        if old[a - 1:b] == new[a - 1:b]:
            n_ok += 1
            continue
        mv = moved_to(old, new, a, b)
        if mv:
            by_page.setdefault(page, []).append(
                f"{name}:{a}-{b}  same code, moved to {mv[0]}" + (f"-{mv[1]}" if mv[1] != mv[0] else ""))
        else:
            by_page.setdefault(page, []).append(f"{name}:{a}-{b}  CHANGED: read it again")
    print(f"references: {n_ok} unchanged, {sum(len(v) for v in by_page.values())} to look at "
          f"({build_a} -> {build_b})")
    for page in sorted(by_page):
        print(f"\n  {page}")
        for line in by_page[page]:
            print(f"    {line}")
    if "--renumber" in sys.argv:
        renumber(by_page)
    elif any("moved to" in l for v in by_page.values() for l in v):
        print("\n  moved references can be renumbered in every language: add --renumber")
    return 0


def renumber(by_page):
    """Rewrites the references whose code only moved, in every language of the page."""
    rx = re.compile(r"^(\S+):(\d+)-(\d+)  same code, moved to (\d+)(?:-(\d+))?$")
    n = 0
    for page, lines in by_page.items():
        moves = {}
        for line in lines:
            m = rx.match(line)
            if m:
                name, a, b, c, d = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)
                d = int(d) if d else c
                old = [f"`{name}:{a}`"] if a == b else [f"`{name}:{a}-{b}`"]
                moves[old[0]] = f"`{name}:{c}`" if c == d else f"`{name}:{c}-{d}`"
        if not moves:
            continue
        rx_any = re.compile("|".join(re.escape(k) for k in moves))
        for lang in os.listdir(CONTENT_DIR):
            p = os.path.join(CONTENT_DIR, lang, page + ".md")
            if os.path.exists(p):
                with open(p, encoding="utf-8", newline="") as f:
                    t = f.read()
                t2, k = rx_any.subn(lambda m: moves[m.group(0)], t)  # one pass: a new number is never moved again
                if k:
                    with open(p, "w", encoding="utf-8", newline="") as f:
                        f.write(t2)
                    n += k
    print(f"\n  renumbered {n} reference(s) in every language; the CHANGED ones must be read again by hand")

RX_FUNC = [
    re.compile(r"^\s*(?:local\s+)?function\s+([A-Za-z_][\w.:]*)\s*\("),
    re.compile(r"^\s*(?:local\s+)?([A-Za-z_][\w.]*)\s*(?::[^=]+)?=\s*function\s*\("),
]
RX_CONST = re.compile(
    r"^\s*(?:local\s+)?([A-Za-z_][\w.]*)\s*(?:<const>)?\s*(?::\s*[\w.]+\s*)?=\s*(-?\d+(?:\.\d+)?(?:e-?\d+)?)\s*,?\s*(?:--\s*(.*))?$")


def domain_of(source_id):
    """Group files by subsystem: <zip or folder>/<first meaningful folder>."""
    if "!" in source_id:
        zname, inner = source_id.split("!", 1)
        parts = inner.split("/")
        top = zname[:-4]  # name of the zip
        # zips keep everything under a folder of the same name (game_mechanics/towns/...)
        if parts and parts[0] == top:
            parts = parts[1:]
        sub = parts[0] if len(parts) > 1 else "(root)"
        return f"{top}/{sub}"
    parts = source_id.split("/")
    return f"{parts[0]}/(loose)"


def scan_file(text):
    funcs, consts = [], []
    for n, line in enumerate(text.splitlines(), 1):
        for rx in RX_FUNC:
            m = rx.match(line)
            if m:
                funcs.append([m.group(1), n])
                break
        m = RX_CONST.match(line)
        if m:
            consts.append([m.group(1), m.group(2), n] + ([m.group(3).strip()[:80]] if m.group(3) else []))
    return funcs, consts


def cited_sources():
    """source id -> wiki pages that cite it (content/<lang>/<page>.md, 'src:' lines and inline refs)."""
    cites = {}
    rx = re.compile(r"`([\w./-]+\.(?:lua|tl))(?::\d+(?:-\d+)?)?`")
    for root, _d, files in os.walk(CONTENT_DIR):
        for f in files:
            if f.endswith(".md"):
                page = os.path.splitext(f)[0]
                with open(os.path.join(root, f), encoding="utf-8") as fh:
                    for m in rx.finditer(fh.read()):
                        cites.setdefault(m.group(1), set()).add(page)
    return cites


def main():
    if "--diff" in sys.argv:
        i = sys.argv.index("--diff")
        return diff(int(sys.argv[i + 1]), int(sys.argv[i + 2]))
    old = {}
    if os.path.exists(INDEX):
        with open(INDEX, encoding="utf-8") as f:
            old = {k: v["sha1"] for k, v in json.load(f)["files"].items()}
    files, domains = {}, {}
    for sid, size in sources.iter_sources():
        text = sources.read(sid)
        funcs, consts = scan_file(text)
        dom = domain_of(sid)
        files[sid] = {
            "domain": dom, "size": size, "lines": text.count("\n") + 1,
            "sha1": hashlib.sha1(text.encode("utf-8")).hexdigest(),
            "functions": funcs, "constants": consts,
        }
        d = domains.setdefault(dom, {"files": 0, "bytes": 0})
        d["files"] += 1
        d["bytes"] += size
    build = game_build()
    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump({"game": sources.GAME, "build": build, "domains": domains, "files": files}, f, indent=1,
                  ensure_ascii=False)
    print(f"{len(files)} files in {len(domains)} domains -> {os.path.relpath(INDEX, HERE)}")
    if build:
        root, kept = write_snapshot(build, files)
        print(f"build {build}: snapshot of {len(files)} hashes and {kept} cited files -> {os.path.relpath(root, HERE)}")
    else:
        print("  ! game build unknown (no game log, set TF3_BUILD): no snapshot written")
    if old:
        changed = sorted(k for k in files if k in old and old[k] != files[k]["sha1"])
        added = sorted(k for k in files if k not in old)
        removed = sorted(k for k in old if k not in files)
        cites = cited_sources()
        for label, lst in (("changed", changed), ("added", added), ("removed", removed)):
            for k in lst:
                pages = cites.get(sources.short(k), set())
                print(f"  {label:8} {k}" + (f"   <- check pages: {', '.join(sorted(pages))}" if pages else ""))
        if not (changed or added or removed):
            print("  no change since the last scan")
    return 0


if __name__ == "__main__":
    sys.exit(main())
