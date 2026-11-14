"""Checks before publishing:

1. every page exists in every language of content/, with the same diagrams and the same source references;
   every language has its interface texts (build.UI) and every diagram has its texts;
2. every `file.lua:12-20` reference names a real game file, and its lines exist;
3. no long copy of game code (fenced code blocks of more than 3 lines are refused);
4. every relative link of the built site points to an existing file;
5. every mod named in a page (data/mods.json) is a link to its own mod.io page.

    python check.py      (exit code 1 on any problem)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
DOCS = os.environ.get("WIKI_OUT") or os.path.join(HERE, "docs")
import langs as L

LANGS = L.present()
RX_REF = re.compile(r"`([\w./-]+\.(?:lua|tl))(?::(\d+)(?:-(\d+))?)?`")
RX_DIAG = re.compile(r"```diagram\s+(\w+)")
RX_FENCE = re.compile(r"```(\w*)[^\n]*\n(.*?)```", re.S)


def main():
    problems = []
    with open(os.path.join(HERE, "data", "index.json"), encoding="utf-8") as f:
        files = json.load(f)["files"]
    by_name = {}
    for sid, info in files.items():
        by_name.setdefault(sid.split("!", 1)[-1].split("/")[-1], []).append((sid, info["lines"]))
        by_name.setdefault(sid.split("!", 1)[-1], []).append((sid, info["lines"]))

    pages = {l: sorted(f[:-3] for f in os.listdir(os.path.join(CONTENT, l)) if f.endswith(".md")) for l in LANGS}
    for l in LANGS[1:]:
        if pages[l] != pages["en"]:
            problems.append(f"pages differ: en={pages['en']} {l}={pages[l]}")

    for slug in pages["en"]:
        texts = {}
        for l in LANGS:
            p = os.path.join(CONTENT, l, slug + ".md")
            if os.path.exists(p):
                texts[l] = open(p, encoding="utf-8").read()
        ref_sets = {l: sorted(set(m.group(0) for m in RX_REF.finditer(t))) for l, t in texts.items()}
        diag_sets = {l: RX_DIAG.findall(t) for l, t in texts.items()}
        for l in texts:
            if ref_sets[l] != ref_sets["en"]:
                extra = set(ref_sets[l]) ^ set(ref_sets["en"])
                problems.append(f"{l}/{slug}: source references differ from en: {sorted(extra)}")
            if diag_sets[l] != diag_sets["en"]:
                problems.append(f"{l}/{slug}: diagrams differ from en")
            # same shape as English: headings, facts, links, fenced blocks
            for what, rx in (("headings", r"(?m)^## "), ("facts", r"(?m)^fact:"), ("fenced blocks", r"(?m)^```\w"),
                             ("table rows", r"(?m)^\|")):
                a, b = len(re.findall(rx, texts["en"])), len(re.findall(rx, texts[l]))
                if a != b:
                    problems.append(f"{l}/{slug}: {b} {what}, en has {a}")
            links = lambda t: sorted(set(re.findall(r"\]\(([^)\s]+)\)", t)))  # same targets; a language may link one twice
            if links(texts[l]) != links(texts["en"]):
                problems.append(f"{l}/{slug}: links differ from en: {sorted(set(links(texts[l])) ^ set(links(texts['en'])))}")
            for m in RX_FENCE.finditer(texts[l]):
                kind, body = m.group(1), m.group(2)
                if kind not in ("diagram", "check", "engine") and body.count("\n") > 3:
                    problems.append(f"{l}/{slug}: code block of {body.count(chr(10))} lines (no long copies of game code)")
        for m in RX_REF.finditer(texts["en"]):
            name, a, b = m.group(1), m.group(2), m.group(3)
            cands = by_name.get(name, [])
            if not cands:
                problems.append(f"{slug}: unknown source file {name}")
                continue
            if a:
                last = int(b or a)
                if not any(last <= n for _sid, n in cands):
                    problems.append(f"{slug}: {name} has no line {last}")

    problems += check_mod_links(pages["en"])
    problems += check_texts()

    for root, _d, fs in os.walk(DOCS):
        for f in fs:
            if f.endswith(".html"):
                t = open(os.path.join(root, f), encoding="utf-8").read()
                for href in re.findall(r'href="([^"#]+)"', t):
                    if href.startswith(("http://", "https://", "mailto:")):
                        continue
                    target = os.path.normpath(os.path.join(root, href))
                    if not os.path.exists(target):
                        problems.append(f"broken link in {os.path.relpath(os.path.join(root, f), DOCS)}: {href}")

    for p in problems:
        print("  !", p)
    print(f"{len(problems)} problem(s); pages: {', '.join(pages['en'])}")
    return 1 if problems else 0


MODIO = "https://mod.io/g/transportfever3/m/"


def check_texts():
    """Interface strings and diagram texts must exist for every language, with the same keys as English."""
    import build
    import diagrams
    found = []
    for l in LANGS:
        if l not in build.UI:
            found.append(f"{l}: no interface texts in build.UI")
        elif set(build.UI[l]) != set(build.UI["en"]):
            found.append(f"{l}: interface keys differ from en: {sorted(set(build.UI[l]) ^ set(build.UI['en']))}")
    for name, table in vars(diagrams).items():
        if name.startswith("T_") and isinstance(table, dict):
            for l in LANGS:
                if l not in table:
                    found.append(f"{l}: diagram texts {name} missing")
                elif set(table[l]) != set(table["en"]):
                    found.append(f"{l}: diagram texts {name} keys differ from en")
    for d in build.load_domains():
        for l in LANGS:
            t = d["text"].get(l)
            if not t:
                found.append(f"{l}: domain texts of {d['id']} missing")
            elif set(t) != set(d["text"]["en"]) or len(t.get("questions", [])) != len(d["text"]["en"].get("questions", [])):
                found.append(f"{l}: domain texts of {d['id']} differ in shape from en")
    for l in LANGS:
        if l != "en" and set(diagrams.CARGO_NAMES.get(l, {})) != set(diagrams.CARGO_NAMES["fr"]):
            found.append(f"{l}: cargo names missing in diagrams.CARGO_NAMES")
    for l in LANGS:
        for name in diagrams.REGISTRY:
            try:
                diagrams.render(name, l)
            except Exception as e:  # noqa: BLE001
                found.append(f"{l}: diagram {name} fails: {e!r}")
    return found


def check_mod_links(slugs):
    """A mod name outside a link, or a link to the wrong mod.io page, is a problem."""
    with open(os.path.join(HERE, "data", "mods.json"), encoding="utf-8") as f:
        mods = json.load(f)["mods"]
    found = []
    rx_link = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    for l in LANGS:
        for slug in slugs:
            p = os.path.join(CONTENT, l, slug + ".md")
            if not os.path.exists(p):
                continue
            text = open(p, encoding="utf-8").read()
            spans = [(m.start(), m.end(), m.group(1), m.group(2)) for m in rx_link.finditer(text)]
            for mid, info in mods.items():
                # longest names first, so "Swiss Names - Romandie" is not taken for "Swiss Names"
                for name in sorted(info["names"], key=len, reverse=True):
                    for m in re.finditer(r"(?<![\w-])" + re.escape(name) + r"(?![\w-]| -)", text):
                        inside = [s for s in spans if s[0] < m.start() < s[1]]
                        if not inside:
                            found.append(f"{l}/{slug}: mod '{name}' named without its mod.io link ({MODIO}{mid})")
                        elif inside[0][3].rstrip("/").split("#")[0] != MODIO + mid:
                            found.append(f"{l}/{slug}: '{name}' links to {inside[0][3]}, expected {MODIO}{mid}")
    return found


if __name__ == "__main__":
    sys.exit(main())
