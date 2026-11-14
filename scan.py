"""Scan every Lua / Teal file of the game and write data/index.json.

For each file: domain, size, sha1, functions it defines and the numeric constants it sets (name = number).
Run again after a game update: files whose sha1 changed are listed, with the wiki pages that cite them
(pages must then be checked again).

    python scan.py
"""
import hashlib
import json
import os
import re
import sys

import sources

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, "data", "index.json")
CONTENT_DIR = os.path.join(HERE, "content")

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
    os.makedirs(os.path.dirname(INDEX), exist_ok=True)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump({"game": sources.GAME, "domains": domains, "files": files}, f, indent=1, ensure_ascii=False)
    print(f"{len(files)} files in {len(domains)} domains -> {os.path.relpath(INDEX, HERE)}")
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
