"""Build the static site (docs/) from content/<lang>/*.md, data/index.json and data/domains.json.

    python build.py

Pages are Markdown with a small header:

    ---
    title: Workers and the workers boost
    summary: One sentence for the index card.
    domain: industries
    official: gamemanual:simulation:industriescargos#booster
    status: verified            (verified | draft | engine)
    updated: 2026-11-14
    ---

Inside a page:
  - `file.tl:12` or `file.tl:12-20` (a path ending in .lua / .tl, optional lines) becomes a source reference;
  - a fenced block ```diagram NAME``` inserts the SVG diagram NAME from diagrams.py (localised);
  - a fenced block ```check``` holds the verification box: lines "official: ...", "scripts: ...", "result: agrees|refines|differs".
"""
import html
import json
import os
import re
import shutil
import sys

import markdown

import diagrams

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
OUT = os.path.join(HERE, "docs")
INDEX = os.path.join(HERE, "data", "index.json")
DOMAINS = os.path.join(HERE, "data", "domains.json")
OFFICIAL = os.path.join(HERE, "data", "official_pages.json")
LANGS = ["en", "fr", "de"]
LANG_NAMES = {"en": "English", "fr": "Français", "de": "Deutsch"}
OFFICIAL_BASE = "https://wiki.transportfever3.com/doku.php?id="

UI = {
    "en": {
        "site": "TF3 Mechanics", "tagline": "How Transport Fever 3 really works, read from the game's own scripts.",
        "home": "Index", "sources": "Sources in the game files", "official": "Official wiki",
        "status": {"verified": "Verified", "draft": "To write", "engine": "Decided by the engine"},
        "check": "Checked against", "result": {"agrees": "agrees", "refines": "adds detail", "differs": "differs"},
        "official_says": "Official wiki", "scripts_show": "Game scripts",
        "domains": "Game systems", "pages": "Explained mechanics", "files": "files",
        "footer": "Fan project by Miro. Not affiliated with Urban Games. Texts and images: CC BY 4.0. "
                  "Game code © Urban Games: only short references are shown.",
        "engine_note": "Decided by the game engine (C++), not visible in the scripts.",
        "read_more": "Read", "no_page": "No page yet", "updated": "Updated",
        "src_note": "Paths are inside the game's base/content folder or its zip files.",
    },
    "fr": {
        "site": "Mécaniques TF3", "tagline": "Comment Transport Fever 3 fonctionne vraiment, lu dans les scripts du jeu.",
        "home": "Index", "sources": "Sources dans les fichiers du jeu", "official": "Wiki officiel",
        "status": {"verified": "Vérifié", "draft": "À écrire", "engine": "Décidé par le moteur"},
        "check": "Vérifié avec", "result": {"agrees": "concorde", "refines": "précise", "differs": "diffère"},
        "official_says": "Wiki officiel", "scripts_show": "Scripts du jeu",
        "domains": "Systèmes du jeu", "pages": "Mécaniques expliquées", "files": "fichiers",
        "footer": "Projet de fan par Miro. Non affilié à Urban Games. Textes et images : CC BY 4.0. "
                  "Code du jeu © Urban Games : seules de courtes références sont montrées.",
        "engine_note": "Décidé par le moteur du jeu (C++), non visible dans les scripts.",
        "read_more": "Lire", "no_page": "Pas encore de page", "updated": "Mis à jour",
        "src_note": "Les chemins sont dans le dossier base/content du jeu ou dans ses fichiers zip.",
    },
    "de": {
        "site": "TF3-Mechaniken", "tagline": "Wie Transport Fever 3 wirklich funktioniert, gelesen in den Skripten des Spiels.",
        "home": "Index", "sources": "Quellen in den Spieldateien", "official": "Offizielles Wiki",
        "status": {"verified": "Geprüft", "draft": "Zu schreiben", "engine": "Von der Engine entschieden"},
        "check": "Geprüft mit", "result": {"agrees": "stimmt überein", "refines": "ergänzt", "differs": "weicht ab"},
        "official_says": "Offizielles Wiki", "scripts_show": "Spielskripte",
        "domains": "Spielsysteme", "pages": "Erklärte Mechaniken", "files": "Dateien",
        "footer": "Fanprojekt von Miro. Nicht mit Urban Games verbunden. Texte und Bilder: CC BY 4.0. "
                  "Spielcode © Urban Games: es werden nur kurze Verweise gezeigt.",
        "engine_note": "Von der Spiel-Engine (C++) entschieden, in den Skripten nicht sichtbar.",
        "read_more": "Lesen", "no_page": "Noch keine Seite", "updated": "Aktualisiert",
        "src_note": "Die Pfade liegen im Ordner base/content des Spiels oder in seinen Zip-Dateien.",
    },
}

CSS = """
:root{--bg:#14181c;--panel:#1d2329;--line:#2e363e;--text:#e6e9ec;--dim:#9aa4ad;--gold:#e8b13a;--teal:#3cc2b4;--red:#e0675a}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 "Segoe UI",system-ui,-apple-system,sans-serif}
a{color:var(--gold)}a:hover{color:#ffd27a}
header{border-bottom:1px solid var(--line);background:#101317}
.wrap{max-width:980px;margin:0 auto;padding:0 20px}
.top{display:flex;align-items:center;gap:16px;min-height:60px}
.brand{font-weight:700;letter-spacing:.06em;color:var(--text);text-decoration:none;font-size:18px}
.brand span{color:var(--gold)}
.langs{margin-left:auto;display:flex;gap:6px}
.langs a{padding:3px 9px;border:1px solid var(--line);border-radius:4px;text-decoration:none;color:var(--dim);font-size:13px}
.langs a.on{color:#111;background:var(--gold);border-color:var(--gold)}
main{padding:28px 0 40px}
h1{font-size:30px;line-height:1.25;margin:0 0 6px}h2{margin-top:36px;border-bottom:1px solid var(--line);padding-bottom:4px}
h3{margin-top:26px;color:var(--gold)}
.lead{color:var(--dim);margin:0 0 22px;font-size:17px}
.meta{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 22px;font-size:13px}
.pill{padding:2px 9px;border-radius:20px;border:1px solid var(--line);color:var(--dim)}
.pill.verified{color:#111;background:var(--teal);border-color:var(--teal)}
.pill.engine{color:#111;background:#b9a0e6;border-color:#b9a0e6}
.pill.draft{color:var(--dim)}
code{background:#262d34;padding:1px 5px;border-radius:3px;font-size:.92em}
code.src{color:var(--teal);background:#18302d}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--panel)}
blockquote{margin:16px 0;padding:10px 16px;border-left:4px solid var(--gold);background:var(--panel)}
.engine{border-left-color:#b9a0e6}
.check{margin:26px 0;border:1px solid var(--line);border-radius:6px;background:var(--panel)}
.check h4{margin:0;padding:9px 14px;border-bottom:1px solid var(--line);font-size:14px;letter-spacing:.04em;text-transform:uppercase;color:var(--dim)}
.check dl{margin:0;padding:10px 14px;display:grid;grid-template-columns:150px 1fr;gap:6px 14px}
.check dt{color:var(--dim)}.check dd{margin:0}
.res{font-weight:700}.res.agrees{color:var(--teal)}.res.refines{color:var(--gold)}.res.differs{color:var(--red)}
figure{margin:22px 0;text-align:center}figure svg{max-width:100%;height:auto}
figcaption{color:var(--dim);font-size:14px;margin-top:6px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin:16px 0}
.card{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:14px 16px;display:flex;flex-direction:column}
.card h3{margin:0 0 4px;font-size:17px;color:var(--text)}
.card p{margin:4px 0;color:var(--dim);font-size:14px}
.card .q{color:var(--text);font-size:14px;margin:6px 0 0;padding-left:16px}
.card .foot{margin-top:auto;padding-top:10px;display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--dim)}
.card.page{border-color:var(--gold)}
footer{border-top:1px solid var(--line);color:var(--dim);font-size:13px;padding:18px 0 30px}
ul.src{font-size:14px;color:var(--dim)}
"""


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def parse_page(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta = {}
    if text.startswith("---"):
        head, text = text[3:].split("\n---", 1)
        for line in head.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta, text.lstrip("\n")


def official_link(ref, ui):
    pid, _, anchor = ref.partition("#")
    url = OFFICIAL_BASE + pid + (f"#{anchor}" if anchor else "")
    return url


def render_check(block, ui):
    rows = {}
    for line in block.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            rows[k.strip()] = v.strip()
    res = rows.get("result", "agrees")
    md = lambda s: markdown.markdown(s).removeprefix("<p>").removesuffix("</p>")
    return (f'<div class="check"><h4>{ui["check"]}</h4><dl>'
            f'<dt>{ui["official_says"]}</dt><dd>{md(rows.get("official", ""))}</dd>'
            f'<dt>{ui["scripts_show"]}</dt><dd>{md(rows.get("scripts", ""))}</dd>'
            f'<dt></dt><dd class="res {res}">{ui["result"].get(res, res)}</dd>'
            f'</dl></div>')


def render_body(text, lang, ui):
    """Markdown -> HTML with diagram / check / source blocks."""
    blocks = {}

    def stash(html_snippet):
        key = f"@@BLOCK{len(blocks)}@@"
        blocks[key] = html_snippet
        return f"\n\n{key}\n\n"

    def fence(m):
        kind, arg, body = m.group(1), (m.group(2) or "").strip(), m.group(3)
        if kind == "diagram":
            svg, caption = diagrams.render(arg, lang)
            cap = f"<figcaption>{html.escape(caption)}</figcaption>" if caption else ""
            return stash(f"<figure>{svg}{cap}</figure>")
        if kind == "check":
            return stash(render_check(body, ui))
        if kind == "engine":
            inner = markdown.markdown(body.strip(), extensions=["tables"])
            return stash(f'<blockquote class="engine"><strong>{ui["engine_note"]}</strong>{inner}</blockquote>')
        return m.group(0)

    text = re.sub(r"```(diagram|check|engine)[ \t]*([^\n]*)\n(.*?)```", fence, text, flags=re.S)
    out = markdown.markdown(text, extensions=["tables", "toc", "attr_list"])
    out = re.sub(r"<code>([\w./-]+\.(?:lua|tl)(?::\d+(?:-\d+)?)?)</code>", r'<code class="src">\1</code>', out)
    for key, snippet in blocks.items():
        out = out.replace(f"<p>{key}</p>", snippet).replace(key, snippet)
    return out


def page_shell(lang, title, body, rel_root, alt_links):
    ui = UI[lang]
    langs = "".join(
        f'<a href="{alt_links[l]}" class="{"on" if l == lang else ""}" hreflang="{l}">{l.upper()}</a>' for l in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · {ui["site"]}</title>
<link rel="stylesheet" href="{rel_root}style.css">
</head><body>
<header><div class="wrap top"><a class="brand" href="{rel_root}{lang}/index.html">TF3 <span>MECHANICS</span></a>
<nav class="langs">{langs}</nav></div></header>
<main><div class="wrap">{body}</div></main>
<footer><div class="wrap">{ui["footer"]} · <a href="https://wiki.transportfever3.com">{ui["official"]}</a></div></footer>
</body></html>
"""


def build():
    index = load_json(INDEX, {"domains": {}, "files": {}})
    domains = load_json(DOMAINS, [])
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    with open(os.path.join(OUT, "style.css"), "w", encoding="utf-8", newline="\n") as f:
        f.write(CSS.strip() + "\n")
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")

    # pages per language
    pages = {lang: {} for lang in LANGS}
    for lang in LANGS:
        d = os.path.join(CONTENT, lang)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".md"):
                meta, text = parse_page(os.path.join(d, fn))
                pages[lang][fn[:-3]] = (meta, text)

    for lang in LANGS:
        ui = UI[lang]
        os.makedirs(os.path.join(OUT, lang), exist_ok=True)
        for slug, (meta, text) in pages[lang].items():
            status = meta.get("status", "draft")
            pills = [f'<span class="pill {status}">{ui["status"].get(status, status)}</span>']
            if meta.get("official"):
                pills.append(f'<a class="pill" href="{official_link(meta["official"], ui)}">{ui["official"]} ↗</a>')
            if meta.get("updated"):
                pills.append(f'<span class="pill">{ui["updated"]} {meta["updated"]}</span>')
            body = (f'<p><a href="index.html">← {ui["home"]}</a></p><h1>{html.escape(meta.get("title", slug))}</h1>'
                    f'<p class="lead">{html.escape(meta.get("summary", ""))}</p>'
                    f'<div class="meta">{"".join(pills)}</div>{render_body(text, lang, ui)}'
                    f'<p class="src"><small>{ui["src_note"]}</small></p>')
            alt = {l: (f"../{l}/{slug}.html" if slug in pages[l] else f"../{l}/index.html") for l in LANGS}
            with open(os.path.join(OUT, lang, f"{slug}.html"), "w", encoding="utf-8", newline="\n") as f:
                f.write(page_shell(lang, meta.get("title", slug), body, "../", alt))

        # index
        page_cards = []
        for slug, (meta, _t) in pages[lang].items():
            status = meta.get("status", "draft")
            page_cards.append(
                f'<a class="card page" href="{slug}.html" style="text-decoration:none">'
                f'<h3>{html.escape(meta.get("title", slug))}</h3><p>{html.escape(meta.get("summary", ""))}</p>'
                f'<div class="foot"><span class="pill {status}">{ui["status"].get(status, status)}</span>'
                f'<span>{ui["read_more"]} →</span></div></a>')
        dom_cards = []
        for dom in domains:
            t = dom["text"].get(lang) or dom["text"]["en"]
            nfiles = sum(1 for sid in index["files"] if any(sid.startswith(p) for p in dom["prefixes"]))
            linked = [s for s, (m, _x) in pages[lang].items() if m.get("domain") == dom["id"]]
            qs = "".join(f"<li>{html.escape(q)}</li>" for q in t.get("questions", []))
            links = ", ".join(f'<a href="{s}.html">{html.escape(pages[lang][s][0].get("title", s))}</a>' for s in linked)
            off = "".join(f' <a href="{OFFICIAL_BASE}{o}">{ui["official"]} ↗</a>' for o in dom.get("official", [])[:1])
            dom_cards.append(
                f'<div class="card"><h3>{html.escape(t["name"])}</h3><p>{html.escape(t["what"])}</p>'
                f'<ul class="q">{qs}</ul>'
                f'<div class="foot"><span>{nfiles} {ui["files"]}{off}</span>'
                f'<span>{links or ui["no_page"]}</span></div></div>')
        body = (f'<h1>{ui["site"]}</h1><p class="lead">{ui["tagline"]}</p>'
                f'<h2>{ui["pages"]}</h2><div class="cards">{"".join(page_cards)}</div>'
                f'<h2>{ui["domains"]}</h2><div class="cards">{"".join(dom_cards)}</div>')
        alt = {l: f"../{l}/index.html" for l in LANGS}
        with open(os.path.join(OUT, lang, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page_shell(lang, ui["site"], body, "../", alt))

    # root: pick the browser language
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write("""<!DOCTYPE html><html><head><meta charset="utf-8"><title>TF3 Mechanics</title>
<meta http-equiv="refresh" content="0; url=en/index.html">
<script>var l=(navigator.language||"en").slice(0,2);if(["fr","de"].indexOf(l)>=0)location.replace(l+"/index.html");</script>
</head><body><a href="en/index.html">English</a> · <a href="fr/index.html">Français</a> · <a href="de/index.html">Deutsch</a></body></html>
""")
    n = sum(len(p) for p in pages.values())
    print(f"built {n} pages + {len(LANGS)} indexes -> {os.path.relpath(OUT, HERE)}")


if __name__ == "__main__":
    build()
    sys.exit(0)
