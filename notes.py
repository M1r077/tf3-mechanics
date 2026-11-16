"""Official release notes (wiki.transportfever3.com, page "releasenotes") -> data/builds.json, and the task list.

The wiki describes the stable game. Preview builds come to stable later, so their notes are the to-do list:
each note gets a triage (what it means for our pages) before it reaches stable.

    python notes.py            refresh data/builds.json from the official page, then print the tasks
    python notes.py --tasks    print the tasks only (no download)

data/builds.json (written by hand where marked, the rest by this script):
  "stable":  newest stable build on the official page;
  "builds":  {build: {"branch": "stable" | "preview", "date": "YYYY-MM-DD", "store": "Steam" ...}};
  "notes":   one entry per note text; the same text under a later build (a preview note repeated when it
             reaches stable) keeps its triage:
             {"text", "tag", "builds": [...], "triage": {"status", "pages", "dashboard", "why"}}  (triage: by hand)
             status: "new" (not looked at), "todo" (pages to check or update), "watch" (to measure in game),
             "done" (pages updated, see "pages"), "none" (nothing for the wiki).
  "builds"[b]["findings"]: (by hand) [{"page", "what"}]: changes read in the scripts of a build with
             scan.py --diff, which the release notes do not name; applied when the build reaches stable.
"""
import html
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BUILDS = os.path.join(HERE, "data", "builds.json")
URL = "https://wiki.transportfever3.com/doku.php?id=releasenotes&do=export_xhtml"
UA = {"User-Agent": "tf3-mechanics-wiki/1.0 (fan project; reads public pages)"}
MONTHS = {m: i for i, m in enumerate(("January February March April May June July August September October "
                                      "November December").split(), 1)}
RX_VERSION = re.compile(r"Version\s+(\d{5,})\s*([^(]*?)\s*\((\w+)\s+(\d{1,2}),\s*(\d{4})\)")


def load():
    if os.path.exists(BUILDS):
        with open(BUILDS, encoding="utf-8") as f:
            return json.load(f)
    return {"stable": None, "builds": {}, "notes": []}


def save(data):
    with open(BUILDS, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def text_of(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def parse(xhtml):
    """[(branch, build, store, date, [(tag, text)])] in page order (newest first in each section)."""
    out = []
    sections = re.split(r'<h2[^>]*id="(preview|stable)"[^>]*>', xhtml)
    for branch, body in zip(sections[1::2], sections[2::2]):
        body = body.split("<h2", 1)[0]
        parts = re.split(r"<p>\s*(Version[^<]*?)\s*</p>", body)
        for head, items in zip(parts[1::2], parts[2::2]):
            m = RX_VERSION.search(text_of(head))
            if not m:
                print(f"  ! version line not understood: {text_of(head)!r}")
                continue
            build, store, month, day, year = m.groups()
            date = f"{year}-{MONTHS.get(month, 0):02d}-{int(day):02d}"
            notes = []
            for li in re.findall(r'<div class="li">(.*?)</div>', items, re.S):
                tag = re.search(r'<span class="wrap_btn[^"]*">(.*?)</span>', li)
                t = text_of(re.sub(r'<span class="wrap_btn[^"]*">.*?</span>', "", li))
                notes.append(((text_of(tag.group(1)) if tag else ""), t))
            out.append((branch, int(build), store.strip(), date, notes))
    return out


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def refresh(data):
    with urllib.request.urlopen(urllib.request.Request(URL, headers=UA), timeout=30) as r:
        versions = parse(r.read().decode("utf-8", "replace"))
    if not versions:
        raise SystemExit("no version found on the release notes page (layout changed?)")
    by_text = {norm(n["text"]): n for n in data["notes"]}
    added = 0
    for branch, build, store, date, notes in versions:
        b = data["builds"].setdefault(str(build), {})
        if b.get("branch") == "preview" and branch == "stable":
            print(f"  build {build} moved from preview to stable")
        b.update({"branch": branch, "date": date, "store": store})
        for tag, t in notes:
            n = by_text.get(norm(t))
            if n is None:
                n = {"text": t, "tag": tag, "builds": [], "triage": {"status": "new"}}
                data["notes"].append(n)
                by_text[norm(t)] = n
                added += 1
            if build not in n["builds"]:
                n["builds"] = sorted(n["builds"] + [build])
    stable = [b for br, b, *_ in versions if br == "stable"]
    data["stable"] = max(stable) if stable else data.get("stable")
    data["builds"] = dict(sorted(data["builds"].items(), key=lambda kv: int(kv[0]), reverse=True))
    print(f"{len(versions)} versions, {len(data['notes'])} notes ({added} new), stable {data['stable']}")


def first_stable(data, note):
    """The first stable build that carries the note, or None while it is preview only."""
    st = [b for b in note["builds"] if data["builds"].get(str(b), {}).get("branch") == "stable"]
    return min(st) if st else None


def tasks(data, verified):
    """Prints what is left to do. verified: {page: build} from the pages' "game:" field."""
    stable = data.get("stable")
    print(f"\nStable build {stable}; pages verified on: "
          + ", ".join(f"{b} ({len(p)} pages)" for b, p in sorted(group(verified).items())))
    old = sorted(p for p, b in verified.items() if stable and b < stable)
    if old:
        print(f"  ! pages verified on an older build than the stable {stable}: {', '.join(old)}"
              f"  -> python scan.py --diff {min(verified.values())} {stable}")
    groups = {"new": [], "todo": [], "watch": []}
    for n in data["notes"]:
        st = n["triage"].get("status", "new")
        if st in groups:
            groups[st].append(n)
    labels = {"new": "not triaged yet", "todo": "pages to check or update", "watch": "to measure in game"}
    for st, lst in groups.items():
        if not lst:
            continue
        print(f"\n{labels[st]} ({len(lst)}):")
        for n in sorted(lst, key=lambda n: (first_stable(data, n) or 10**9, min(n["builds"]))):
            fs = first_stable(data, n)
            when = f"stable {fs}" if fs else f"preview {min(n['builds'])}"
            tri = n["triage"]
            extra = ""
            if tri.get("pages"):
                extra += f"  pages: {', '.join(tri['pages'])}"
            if tri.get("dashboard"):
                extra += "  [dashboard]"
            print(f"  [{when}] {('(' + n['tag'] + ') ') if n['tag'] else ''}{n['text']}{extra}")
            if tri.get("why"):
                print(f"      {tri['why']}")
    for build, b in data["builds"].items():
        if b.get("findings"):
            print(f"\nfound in the scripts of {b['branch']} {build} (scan.py --diff), for the pages:")
            for f in b["findings"]:
                print(f"  - {f['page']}: {f['what']}")
    ready = [n for n in groups["todo"] + groups["watch"] if first_stable(data, n)]
    if ready:
        print(f"\n  ! {len(ready)} triaged note(s) are now in a stable build: update the pages, then set status \"done\"")


def group(verified):
    g = {}
    for p, b in verified.items():
        g.setdefault(b, []).append(p)
    return g


def verified_pages():
    out = {}
    d = os.path.join(HERE, "content", "en")
    for f in sorted(os.listdir(d)):
        if f.endswith(".md"):
            m = re.search(r"(?m)^game:\s*(\d+)", open(os.path.join(d, f), encoding="utf-8").read().split("\n---", 1)[0])
            if m:
                out[f[:-3]] = int(m.group(1))
    return out


def main():
    data = load()
    if "--tasks" not in sys.argv:
        refresh(data)
        save(data)
    tasks(data, verified_pages())
    return 0


if __name__ == "__main__":
    sys.exit(main())
