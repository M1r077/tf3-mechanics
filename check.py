"""Checks before publishing:

1. every page exists in en, fr and de, with the same diagrams and the same source references;
2. every `file.lua:12-20` reference names a real game file, and its lines exist;
3. no long copy of game code (fenced code blocks of more than 3 lines are refused);
4. every relative link of the built site points to an existing file.

    python check.py      (exit code 1 on any problem)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
DOCS = os.path.join(HERE, "docs")
LANGS = ["en", "fr", "de"]
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


if __name__ == "__main__":
    sys.exit(main())
