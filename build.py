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
    fact: 10 / 20 | workers needed for the boost      (0 to 4 lines: big value | label)
    ---

Inside a page:
  - `file.tl:12` or `file.tl:12-20` (a path ending in .lua / .tl, optional lines) becomes a source reference;
  - a fenced block ```diagram NAME``` inserts the SVG diagram NAME from diagrams.py (localised);
  - a fenced block ```engine``` marks what the engine decides;
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
import langs as L
from icons import P as ICONS, icon

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
OUT = os.environ.get("WIKI_OUT") or os.path.join(HERE, "docs")  # WIKI_OUT: build elsewhere (previews)
INDEX = os.path.join(HERE, "data", "index.json")
DOMAINS = os.path.join(HERE, "data", "domains.json")
LANGS = L.present()
SOURCE_LANGS = ("en", "fr", "de")  # written directly; the others are translated from English
REPO = "https://github.com/M1r077/tf3-mechanics"
OFFICIAL_BASE = "https://wiki.transportfever3.com/doku.php?id="

UI = {
    "en": {
        "site": "TF3 Mechanics", "tagline": "How Transport Fever 3 really works, read from the game's own scripts.",
        "hero_kicker": "Fan wiki · game scripts · official wiki",
        "home": "Index", "official": "Official wiki",
        "status": {"verified": "Verified in the scripts", "draft": "To write", "engine": "Decided by the engine"},
        "check": "Official wiki vs game scripts", "result": {"agrees": "Agrees", "refines": "Adds detail", "differs": "Differs"},
        "official_says": "Official wiki says", "scripts_show": "Game scripts show",
        "domains": "Game systems", "domains_sub": "Every system of the game, with the questions players ask and the number of script files behind it.",
        "pages": "Explained mechanics", "pages_sub": "Each page is checked line by line in the game files and compared with the official wiki.",
        "files": "script files",
        "footer": "Fan project by Miro. Not affiliated with Urban Games.",
        "lic": "Texts and images: CC BY 4.0 · Game code © Urban Games: only short references are shown.",
        "engine_note": "Decided by the game engine",
        "engine_sub": "C++, not visible in the scripts",
        "read_more": "Read", "no_page": "No page yet", "updated": "Updated",
        "src_note": "Paths are inside the game's base/content folder or its zip files.",
        "toc": "On this page", "more": "Other mechanics", "filter": "Filter the game systems…",
        "st_pages": "explained mechanics", "st_dom": "game systems", "st_files": "script files read", "st_lang": "languages",
        "sources": "source references", "in": "in",
        "translated": "Translated from English; corrections welcome", "lang_label": "Language",
    },
    "fr": {
        "site": "Mécaniques TF3", "tagline": "Comment Transport Fever 3 fonctionne vraiment, lu dans les scripts du jeu.",
        "hero_kicker": "Wiki de fan · scripts du jeu · wiki officiel",
        "home": "Index", "official": "Wiki officiel",
        "status": {"verified": "Vérifié dans les scripts", "draft": "À écrire", "engine": "Décidé par le moteur"},
        "check": "Wiki officiel et scripts du jeu", "result": {"agrees": "Concorde", "refines": "Précise", "differs": "Diffère"},
        "official_says": "Le wiki officiel dit", "scripts_show": "Les scripts du jeu montrent",
        "domains": "Systèmes du jeu", "domains_sub": "Chaque système du jeu, avec les questions des joueurs et le nombre de fichiers de scripts derrière.",
        "pages": "Mécaniques expliquées", "pages_sub": "Chaque page est vérifiée ligne par ligne dans les fichiers du jeu et comparée au wiki officiel.",
        "files": "fichiers de scripts",
        "footer": "Projet de fan par Miro. Non affilié à Urban Games.",
        "lic": "Textes et images : CC BY 4.0 · Code du jeu © Urban Games : seules de courtes références sont montrées.",
        "engine_note": "Décidé par le moteur du jeu",
        "engine_sub": "C++, non visible dans les scripts",
        "read_more": "Lire", "no_page": "Pas encore de page", "updated": "Mis à jour",
        "src_note": "Les chemins sont dans le dossier base/content du jeu ou dans ses fichiers zip.",
        "toc": "Sur cette page", "more": "Autres mécaniques", "filter": "Filtrer les systèmes du jeu…",
        "st_pages": "mécaniques expliquées", "st_dom": "systèmes du jeu", "st_files": "fichiers de scripts lus", "st_lang": "langues",
        "sources": "références aux sources", "in": "dans",
        "translated": "Traduit de l'anglais ; corrections bienvenues", "lang_label": "Langue",
    },
    "de": {
        "site": "TF3-Mechaniken", "tagline": "Wie Transport Fever 3 wirklich funktioniert, gelesen in den Skripten des Spiels.",
        "hero_kicker": "Fan-Wiki · Spielskripte · offizielles Wiki",
        "home": "Index", "official": "Offizielles Wiki",
        "status": {"verified": "In den Skripten geprüft", "draft": "Zu schreiben", "engine": "Von der Engine entschieden"},
        "check": "Offizielles Wiki und Spielskripte", "result": {"agrees": "Stimmt überein", "refines": "Ergänzt", "differs": "Weicht ab"},
        "official_says": "Das offizielle Wiki sagt", "scripts_show": "Die Spielskripte zeigen",
        "domains": "Spielsysteme", "domains_sub": "Jedes System des Spiels, mit den Fragen der Spieler und der Zahl der Skriptdateien dahinter.",
        "pages": "Erklärte Mechaniken", "pages_sub": "Jede Seite wird Zeile für Zeile in den Spieldateien geprüft und mit dem offiziellen Wiki verglichen.",
        "files": "Skriptdateien",
        "footer": "Fanprojekt von Miro. Nicht mit Urban Games verbunden.",
        "lic": "Texte und Bilder: CC BY 4.0 · Spielcode © Urban Games: es werden nur kurze Verweise gezeigt.",
        "engine_note": "Von der Spiel-Engine entschieden",
        "engine_sub": "C++, in den Skripten nicht sichtbar",
        "read_more": "Lesen", "no_page": "Noch keine Seite", "updated": "Aktualisiert",
        "src_note": "Die Pfade liegen im Ordner base/content des Spiels oder in seinen Zip-Dateien.",
        "toc": "Auf dieser Seite", "more": "Weitere Mechaniken", "filter": "Spielsysteme filtern…",
        "st_pages": "erklärte Mechaniken", "st_dom": "Spielsysteme", "st_files": "gelesene Skriptdateien", "st_lang": "Sprachen",
        "sources": "Quellverweise", "in": "in",
        "translated": "Aus dem Englischen übersetzt; Korrekturen willkommen", "lang_label": "Sprache",
    },
}

for _code in L.translated():
    UI[_code] = L.texts(_code)["ui"]


def load_domains():
    """data/domains.json, plus the domain texts of the translated languages."""
    domains = load_json(DOMAINS, [])
    for code in L.translated():
        tr = L.texts(code).get("domains", {})
        for d in domains:
            if d["id"] in tr:
                d["text"][code] = tr[d["id"]]
    return domains


LOGO = ('<svg class="logo" viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#f7cf72"/><stop offset="1" stop-color="#e09a2a"/></linearGradient></defs>'
        '<rect width="32" height="32" rx="9" fill="url(#lg)"/>'
        '<circle cx="16" cy="16" r="6.5" fill="none" stroke="#0f141b" stroke-width="2.6"/>'
        '<path d="M16 4.5v4M16 23.5v4M4.5 16h4M23.5 16h4M7.9 7.9l2.8 2.8M21.3 21.3l2.8 2.8M7.9 24.1l2.8-2.8M21.3 10.7l2.8-2.8" '
        'stroke="#0f141b" stroke-width="2.6" stroke-linecap="round"/></svg>')

CSS = r"""
:root{
  --bg:#0b0f14;--bg2:#10151c;--panel:#141a22;--panel2:#19212b;--line:#232c38;--line2:#2f3a48;
  --text:#eef1f5;--soft:#c3cad4;--dim:#8f9bab;
  --gold:#f2b84b;--gold2:#e09a2a;--teal:#38d1bf;--red:#f0705f;--violet:#b49cf0;--blue:#5aa9ff;
  --r:16px;--shadow:0 10px 30px -12px rgba(0,0,0,.6);
  --font:Inter,"Segoe UI Variable Text","Segoe UI",system-ui,-apple-system,sans-serif;
  --mono:"Cascadia Code","JetBrains Mono",Consolas,ui-monospace,monospace;
}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;background:var(--bg);color:var(--soft);font:16.5px/1.7 var(--font);-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:radial-gradient(900px 500px at 85% -10%,rgba(242,184,75,.10),transparent 60%),
             radial-gradient(800px 500px at -10% 10%,rgba(56,209,191,.08),transparent 60%)}
a{color:var(--gold);text-decoration:none}a:hover{color:#ffd58a}
.ic{flex:none;vertical-align:-.2em}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
::selection{background:rgba(242,184,75,.35);color:#fff}

/* header */
header.bar{position:sticky;top:0;z-index:20;background:rgba(11,15,20,.72);backdrop-filter:blur(14px) saturate(1.4);
  -webkit-backdrop-filter:blur(14px) saturate(1.4);border-bottom:1px solid rgba(255,255,255,.06)}
.top{display:flex;align-items:center;gap:22px;height:64px}
.brand{display:flex;align-items:center;gap:11px;color:var(--text);font-weight:800;letter-spacing:.02em;font-size:17px}
.brand:hover{color:var(--text)}.brand .logo{width:32px;height:32px}
.brand b{color:var(--gold);font-weight:800}
.nav{display:flex;gap:4px;margin-left:12px}
.nav a{color:var(--dim);font-size:14.5px;font-weight:600;padding:7px 12px;border-radius:9px;display:flex;align-items:center;gap:7px}
.nav a:hover,.nav a.on{color:var(--text);background:rgba(255,255,255,.05)}
.langs{margin-left:auto;position:relative}
.langs summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:8px;padding:7px 12px;border-radius:11px;
  background:var(--panel);border:1px solid var(--line);color:var(--text);font-size:13.5px;font-weight:700;user-select:none}
.langs summary::-webkit-details-marker{display:none}
.langs summary:hover,.langs[open] summary{border-color:var(--gold)}
.langs summary .chev{transition:transform .2s;color:var(--dim)}.langs[open] summary .chev{transform:rotate(180deg)}
.langs .menu{position:absolute;right:0;top:calc(100% + 8px);min-width:210px;padding:6px;border-radius:14px;background:var(--panel2);
  border:1px solid var(--line2);box-shadow:0 18px 40px -12px rgba(0,0,0,.7);display:grid;gap:2px;z-index:30}
.langs .menu a{display:flex;justify-content:space-between;gap:14px;padding:7px 12px;border-radius:9px;color:var(--soft);font-size:14px;font-weight:600}
.langs .menu a small{color:var(--dim);font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.langs .menu a:hover{background:rgba(255,255,255,.06);color:var(--text)}
.langs .menu a.on{color:#0f141b;background:linear-gradient(135deg,#f7cf72,#e09a2a)}.langs .menu a.on small{color:#0f141b}
:lang(ja),:lang(ja) *{--font:Inter,"Segoe UI","Yu Gothic UI","Yu Gothic","Hiragino Sans","Noto Sans CJK JP","Noto Sans JP",sans-serif}
:lang(ko),:lang(ko) *{--font:Inter,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo","Noto Sans CJK KR","Noto Sans KR",sans-serif}
:lang(zh-Hans),:lang(zh-Hans) *{--font:Inter,"Segoe UI","Microsoft YaHei","PingFang SC","Noto Sans CJK SC","Noto Sans SC",sans-serif}
:lang(zh-Hant),:lang(zh-Hant) *{--font:Inter,"Segoe UI","Microsoft JhengHei","PingFang TC","Noto Sans CJK TC","Noto Sans TC",sans-serif}
:lang(ja) svg text,:lang(ko) svg text,:lang(zh-Hans) svg text,:lang(zh-Hant) svg text{font-family:var(--font)}
:lang(ja) h1,:lang(ko) h1,:lang(zh-Hans) h1,:lang(zh-Hant) h1{letter-spacing:0;line-height:1.25}
:lang(ja) body,:lang(ko) body,:lang(zh-Hans) body,:lang(zh-Hant) body{line-height:1.85}
footer .tr{color:var(--dim)}footer .tr a{color:var(--soft)}

/* hero */
.hero{position:relative;padding:58px 0 40px;overflow:hidden;border-bottom:1px solid var(--line)}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;opacity:.5;
  background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);
  background-size:44px 44px;mask-image:radial-gradient(ellipse at 50% 0,#000 30%,transparent 75%);
  -webkit-mask-image:radial-gradient(ellipse at 50% 0,#000 30%,transparent 75%)}
.crumb{display:flex;align-items:center;gap:9px;font-size:14px;font-weight:600;color:var(--dim);margin-bottom:18px}
.crumb a{color:var(--dim);display:flex;align-items:center;gap:7px}.crumb a:hover{color:var(--text)}
.crumb .dom{display:inline-flex;align-items:center;gap:7px;color:var(--gold);background:rgba(242,184,75,.1);
  border:1px solid rgba(242,184,75,.25);padding:3px 11px 3px 9px;border-radius:30px}
.kicker{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);margin-bottom:14px}
h1{color:var(--text);font-size:clamp(34px,4.6vw,54px);line-height:1.08;letter-spacing:-.025em;margin:0 0 16px;font-weight:800;max-width:900px}
h1 .grad{background:linear-gradient(100deg,#ffe2a4,#f2b84b 45%,#38d1bf);-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:clamp(17px,1.6vw,20px);color:var(--soft);max-width:760px;margin:0 0 24px;line-height:1.6}
.meta{display:flex;gap:10px;flex-wrap:wrap;font-size:13.5px}
.pill{display:inline-flex;align-items:center;gap:7px;padding:5px 13px;border-radius:30px;border:1px solid var(--line2);color:var(--soft);
  background:rgba(255,255,255,.03);font-weight:600}
a.pill:hover{border-color:var(--gold);color:var(--text)}
.pill.verified{color:#0b1512;background:linear-gradient(135deg,#5ee6d3,#1fa596);border-color:transparent}
.pill.engine{color:#130f1c;background:var(--violet);border-color:transparent}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:34px}
.fact{position:relative;padding:18px 20px;border-radius:var(--r);background:linear-gradient(180deg,var(--panel2),var(--panel));
  border:1px solid var(--line);box-shadow:var(--shadow);overflow:hidden}
.fact::after{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:linear-gradient(var(--gold),var(--teal))}
.fact b{display:block;color:var(--text);font-size:30px;font-weight:800;letter-spacing:-.02em;line-height:1.15}
.fact span{color:var(--dim);font-size:14px}

/* article layout */
.layout{display:grid;grid-template-columns:minmax(0,1fr) 250px;gap:56px;padding:44px 0 20px}
article{min-width:0;max-width:780px}
article>p:first-child{font-size:18px;color:var(--text)}
article h2{color:var(--text);font-size:27px;letter-spacing:-.015em;line-height:1.25;margin:56px 0 16px;display:flex;align-items:center;gap:14px}
article h2 .n{flex:none;display:grid;place-items:center;width:34px;height:34px;border-radius:10px;font-size:15px;font-weight:800;
  color:#0f141b;background:linear-gradient(135deg,#f7cf72,#e09a2a);box-shadow:0 6px 18px -6px rgba(242,184,75,.6)}
article h3{color:var(--gold);font-size:19px;margin:32px 0 10px}
article strong{color:var(--text);font-weight:700}
article ul,article ol{padding-left:0;list-style:none;margin:16px 0}
article li{position:relative;padding-left:30px;margin:10px 0}
article ul>li::before{content:"";position:absolute;left:8px;top:.72em;width:8px;height:8px;border-radius:3px;background:var(--teal);
  box-shadow:0 0 0 4px rgba(56,209,191,.12)}
article ol{counter-reset:o}
article ol>li{counter-increment:o}
article ol>li::before{content:counter(o);position:absolute;left:0;top:.18em;width:22px;height:22px;border-radius:7px;display:grid;place-items:center;
  font-size:12.5px;font-weight:800;color:var(--teal);background:rgba(56,209,191,.12);border:1px solid rgba(56,209,191,.35)}
code{font-family:var(--mono);background:#1b232d;border:1px solid var(--line);padding:1px 6px;border-radius:6px;font-size:.84em;color:#e6dcc6}
code.src{color:var(--teal);background:rgba(56,209,191,.08);border-color:rgba(56,209,191,.22);white-space:nowrap}
code.src::before{content:"</>";font-size:.85em;opacity:.6;margin-right:5px}

/* tables */
.tbl{margin:22px 0;border:1px solid var(--line);border-radius:var(--r);overflow:auto;background:var(--panel);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:15px}
th{background:var(--panel2);color:var(--dim);font-size:12.5px;text-transform:uppercase;letter-spacing:.08em;font-weight:700;text-align:left;padding:12px 16px}
td{padding:12px 16px;border-top:1px solid var(--line);vertical-align:top}
tr:hover td{background:rgba(255,255,255,.02)}
td strong{color:var(--gold)}

/* figures */
figure{margin:30px 0;padding:22px;border-radius:20px;border:1px solid var(--line);
  background:radial-gradient(600px 240px at 50% 0,rgba(255,255,255,.035),transparent),var(--bg2);box-shadow:var(--shadow)}
figure>svg{display:block;width:100%;height:auto}
figcaption{display:flex;gap:9px;align-items:flex-start;color:var(--dim);font-size:14px;margin-top:16px;padding-top:14px;border-top:1px solid var(--line)}
figcaption .ic{color:var(--gold);margin-top:2px}

/* callouts */
.callout{display:flex;gap:16px;margin:26px 0;padding:18px 20px;border-radius:var(--r);border:1px solid rgba(180,156,240,.3);
  background:linear-gradient(135deg,rgba(180,156,240,.12),rgba(180,156,240,.03))}
.callout .badge{flex:none;width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:#130f1c;background:var(--violet)}
.callout h4{margin:0;color:var(--text);font-size:15.5px}.callout h4 small{color:var(--violet);font-weight:600;margin-left:8px}
.callout p{margin:5px 0 0;font-size:15px}

.check{margin:46px 0 16px;border-radius:20px;border:1px solid var(--line);background:var(--panel);overflow:hidden;box-shadow:var(--shadow)}
.check .head{display:flex;align-items:center;gap:12px;padding:15px 20px;border-bottom:1px solid var(--line);background:var(--panel2)}
.check .head h4{margin:0;color:var(--text);font-size:15px;display:flex;align-items:center;gap:9px}
.check .res{margin-left:auto;padding:4px 13px;border-radius:30px;font-size:13px;font-weight:800;display:flex;align-items:center;gap:6px}
.res.agrees{color:#0b1512;background:var(--teal)}.res.refines{color:#1a1205;background:var(--gold)}.res.differs{color:#1c0b08;background:var(--red)}
.check .cols{display:grid;grid-template-columns:1fr 1fr}
.check .col{padding:18px 20px;font-size:15px}.check .col+.col{border-left:1px solid var(--line)}
.check .lab{display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px}
.check .off .lab{color:var(--blue)}.check .scr .lab{color:var(--teal)}
.check .off p{font-style:italic}

.srcnote{display:flex;gap:8px;align-items:center;font-size:13px;color:var(--dim);margin-top:30px}

/* toc */
aside.toc{position:sticky;top:96px;align-self:start;font-size:14px}
.toc h5{margin:0 0 12px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);display:flex;gap:8px;align-items:center}
.toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--line)}
.toc li a{display:block;padding:6px 0 6px 16px;margin-left:-1px;border-left:2px solid transparent;color:var(--dim);line-height:1.4}
.toc li a:hover{color:var(--text)}
.toc li a.on{color:var(--gold);border-left-color:var(--gold)}
.toc .box{margin-top:26px;padding:16px;border-radius:14px;background:var(--panel);border:1px solid var(--line)}
.toc .box b{display:block;color:var(--text);font-size:26px;font-weight:800;line-height:1.1}
.toc .box a{display:flex;align-items:center;gap:7px;margin-top:12px;font-weight:600}

/* index */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:38px}
.section{padding:56px 0 8px}
.section-h{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-bottom:24px}
.section-h h2{color:var(--text);font-size:30px;letter-spacing:-.02em;margin:0 0 6px}
.section-h p{margin:0;color:var(--dim);max-width:640px}
.feat{display:grid;grid-template-columns:repeat(auto-fit,minmax(440px,1fr));gap:22px}
.fcard{display:flex;flex-direction:column;border-radius:22px;border:1px solid var(--line);background:var(--panel);overflow:hidden;color:var(--soft);
  box-shadow:var(--shadow);transition:transform .25s,border-color .25s,box-shadow .25s}
.fcard:hover{transform:translateY(-4px);border-color:rgba(242,184,75,.55);color:var(--soft);box-shadow:0 24px 50px -20px rgba(242,184,75,.25)}
.fcard .thumb{padding:20px 22px 12px;background:radial-gradient(500px 200px at 50% 0,rgba(242,184,75,.08),transparent),var(--bg2);border-bottom:1px solid var(--line)}
.fcard .thumb svg{display:block;width:100%;height:auto}
.fcard .body{padding:20px 24px 22px;display:flex;flex-direction:column;flex:1}
.fcard .tag{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;font-weight:700;color:var(--gold);letter-spacing:.06em;text-transform:uppercase}
.fcard h3{margin:8px 0 6px;color:var(--text);font-size:22px;letter-spacing:-.01em;line-height:1.25}
.fcard p{margin:0 0 16px;font-size:15px}
.fcard .mini{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:18px}
.fcard .mini span{font-size:13px;padding:4px 11px;border-radius:9px;background:var(--panel2);border:1px solid var(--line)}
.fcard .mini b{color:var(--text)}
.fcard .go{margin-top:auto;display:flex;align-items:center;justify-content:space-between;font-size:14px;font-weight:700}
.fcard .go .r{display:flex;align-items:center;gap:7px;color:var(--gold)}
.search{display:flex;align-items:center;gap:10px;padding:0 14px;height:44px;width:320px;max-width:100%;border-radius:12px;
  background:var(--panel);border:1px solid var(--line2);color:var(--dim)}
.search:focus-within{border-color:var(--gold)}
.search input{flex:1;background:none;border:0;outline:0;color:var(--text);font:inherit;font-size:15px}
.dgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}
.dcard{position:relative;display:flex;flex-direction:column;padding:20px;border-radius:18px;border:1px solid var(--line);
  background:linear-gradient(180deg,var(--panel2),var(--panel));transition:border-color .2s,transform .2s}
.dcard:hover{border-color:var(--line2);transform:translateY(-2px)}
.dcard.has{border-color:rgba(242,184,75,.4)}
.dcard .t{display:flex;align-items:center;gap:13px;margin-bottom:10px}
.dcard .di{flex:none;width:42px;height:42px;border-radius:12px;display:grid;place-items:center;color:var(--gold);
  background:rgba(242,184,75,.1);border:1px solid rgba(242,184,75,.22)}
.dcard.has .di{color:#0f141b;background:linear-gradient(135deg,#f7cf72,#e09a2a);border:0}
.dcard h3{margin:0;color:var(--text);font-size:17px;line-height:1.3}
.dcard .what{margin:0 0 12px;font-size:14px;color:var(--dim);line-height:1.55}
.dcard ul{list-style:none;margin:0 0 14px;padding:0}
.dcard li{position:relative;font-size:14px;color:var(--soft);padding:5px 0 5px 22px;line-height:1.45}
.dcard li::before{content:"?";position:absolute;left:0;top:6px;width:15px;height:15px;border-radius:5px;font-size:10px;font-weight:800;
  display:grid;place-items:center;color:var(--teal);background:rgba(56,209,191,.12)}
.dcard .foot{margin-top:auto;padding-top:12px;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:9px;font-size:13px;color:var(--dim)}
.meter{height:5px;border-radius:5px;background:#202935;overflow:hidden}.meter i{display:block;height:100%;border-radius:5px;background:linear-gradient(90deg,var(--teal),var(--gold))}
.dcard .row{display:flex;justify-content:space-between;align-items:center;gap:10px}
.dcard .row a{display:inline-flex;align-items:center;gap:5px;font-weight:600}
.dcard .pages a{display:inline-flex;align-items:center;gap:6px;font-weight:700}
.empty{display:none;color:var(--dim);padding:30px 0}

/* more + footer */
.more{padding:30px 0 10px}
.more h2{color:var(--text);font-size:22px;margin:0 0 16px}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.mcard{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:16px;border:1px solid var(--line);background:var(--panel);color:var(--soft)}
.mcard:hover{border-color:rgba(242,184,75,.5);color:var(--soft)}
.mcard .di{flex:none;width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:#0f141b;background:linear-gradient(135deg,#f7cf72,#e09a2a)}
.mcard b{display:block;color:var(--text);font-size:15.5px}.mcard small{color:var(--dim);font-size:13px}
.mcard .ic.end{margin-left:auto;color:var(--gold)}
footer{margin-top:70px;border-top:1px solid var(--line);background:rgba(0,0,0,.25)}
footer .wrap{display:flex;gap:24px;align-items:center;flex-wrap:wrap;padding-top:28px;padding-bottom:36px;font-size:13.5px;color:var(--dim)}
footer .brand{font-size:15px}footer .brand .logo{width:26px;height:26px}
footer .txt{display:flex;flex-direction:column;gap:3px}
footer .links{margin-left:auto;display:flex;gap:16px}
footer .links a{display:flex;align-items:center;gap:6px;color:var(--soft);font-weight:600}

/* motion */
@media (prefers-reduced-motion:no-preference){
  .rise{animation:rise .6s cubic-bezier(.2,.7,.2,1) both}
  .d1{animation-delay:.06s}.d2{animation-delay:.12s}.d3{animation-delay:.18s}.d4{animation-delay:.24s}
  @keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
}
@media (max-width:1020px){.layout{grid-template-columns:1fr}aside.toc{display:none}.stats{grid-template-columns:repeat(2,1fr)}}
@media (max-width:640px){
  .langs summary span{display:none}
  .wrap{padding:0 18px}.nav{display:none}.feat{grid-template-columns:1fr}.check .cols{grid-template-columns:1fr}
  .check .col+.col{border-left:0;border-top:1px solid var(--line)}figure{padding:12px}.hero{padding-top:38px}
}
"""

JS = r"""
(function(){
  var links=[].slice.call(document.querySelectorAll('.toc a[href^="#"]'));
  if(links.length&&'IntersectionObserver' in window){
    var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
      links.forEach(function(a){a.classList.remove('on')});var a=map[e.target.id];if(a)a.classList.add('on');}})},
      {rootMargin:'-90px 0px -65% 0px'});
    Object.keys(map).forEach(function(id){var h=document.getElementById(id);if(h)io.observe(h)});
  }
  var q=document.getElementById('q');
  if(q){q.addEventListener('input',function(){
    var v=q.value.normalize('NFKC').trim().toLowerCase(),n=0;
    [].forEach.call(document.querySelectorAll('.dcard'),function(c){
      var ok=!v||c.textContent.normalize('NFKC').toLowerCase().indexOf(v)>=0;c.style.display=ok?'':'none';if(ok)n++;});
    document.querySelector('.empty').style.display=n?'none':'block';});}
})();
"""


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def parse_page(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta = {"facts": []}
    if text.startswith("---"):
        head, text = text[3:].split("\n---", 1)
        for line in head.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                k, v = k.strip(), v.strip()
                if k == "fact":
                    value, _, label = v.partition("|")
                    meta["facts"].append((value.strip(), label.strip()))
                else:
                    meta[k] = v
    return meta, text.lstrip("\n")


def official_link(ref):
    pid, _, anchor = ref.partition("#")
    return OFFICIAL_BASE + pid + (f"#{anchor}" if anchor else "")


def md_inline(s):
    return markdown.markdown(s).removeprefix("<p>").removesuffix("</p>")


def render_check(block, ui):
    rows = {}
    for line in block.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            rows[k.strip()] = v.strip()
    res = rows.get("result", "agrees")
    res_icon = {"agrees": "check", "refines": "info", "differs": "cross"}.get(res, "info")
    return (f'<section class="check"><div class="head"><h4>{icon("scale", 18)}{ui["check"]}</h4>'
            f'<span class="res {res}">{icon(res_icon, 14, stroke=3)}{ui["result"].get(res, res)}</span></div>'
            f'<div class="cols"><div class="col off"><div class="lab">{icon("book", 16)}{ui["official_says"]}</div>'
            f'<p>{md_inline(rows.get("official", ""))}</p></div>'
            f'<div class="col scr"><div class="lab">{icon("code", 16)}{ui["scripts_show"]}</div>'
            f'<p>{md_inline(rows.get("scripts", ""))}</p></div></div></section>')


def render_body(text, lang, ui):
    """Markdown -> HTML with diagram / check / engine blocks; returns (html, toc entries)."""
    blocks = {}

    def stash(snippet):
        key = f"@@BLOCK{len(blocks)}@@"
        blocks[key] = snippet
        return f"\n\n{key}\n\n"

    def fence(m):
        kind, arg, body = m.group(1), (m.group(2) or "").strip(), m.group(3)
        if kind == "diagram":
            svg, caption = diagrams.render(arg, lang)
            cap = f"<figcaption>{icon('info', 16)}<span>{html.escape(caption)}</span></figcaption>" if caption else ""
            return stash(f"<figure>{svg}{cap}</figure>")
        if kind == "check":
            return stash(render_check(body, ui))
        if kind == "engine":
            inner = markdown.markdown(body.strip(), extensions=["tables"])
            return stash(f'<aside class="callout"><div class="badge">{icon("cpu", 22)}</div><div>'
                         f'<h4>{ui["engine_note"]}<small>{ui["engine_sub"]}</small></h4>{inner}</div></aside>')
        return m.group(0)

    text = re.sub(r"```(diagram|check|engine)[ \t]*([^\n]*)\n(.*?)```", fence, text, flags=re.S)
    # en/fr/de keep their ASCII anchors; other scripts need Unicode anchors (ASCII ones would all be "_1", "_2"...)
    from markdown.extensions.toc import TocExtension, slugify, slugify_unicode
    toc_ext = TocExtension(slugify=slugify if lang in SOURCE_LANGS else slugify_unicode)
    out = markdown.markdown(text, extensions=["tables", toc_ext, "attr_list"])
    out = re.sub(r"<code>([\w./-]+\.(?:lua|tl)(?::\d+(?:-\d+)?)?)</code>", r'<code class="src">\1</code>', out)
    out = out.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    toc = []

    def h2(m):
        hid, title = m.group(1), m.group(2)
        plain = re.sub(r"^\d+\.\s*", "", re.sub("<[^>]+>", "", title))
        toc.append((hid, plain))
        return f'<h2 id="{hid}"><span class="n">{len(toc)}</span><span>{html.escape(plain)}</span></h2>'

    out = re.sub(r'<h2 id="([^"]+)">(.*?)</h2>', h2, out)
    for key, snippet in blocks.items():
        out = out.replace(f"<p>{key}</p>", snippet).replace(key, snippet)
    return out, toc


def page_shell(lang, title, body, alt_links, nav_on="", page_title=None):
    ui = UI[lang]
    hl = {l: L.BY_CODE[l]["html"] for l in LANGS}
    langs = "".join(
        f'<a href="{alt_links[l]}" class="{"on" if l == lang else ""}" hreflang="{hl[l]}" lang="{hl[l]}">'
        f'{L.BY_CODE[l]["name"]}<small>{l}</small></a>' for l in LANGS)
    alternates = "".join(f'<link rel="alternate" hreflang="{hl[l]}" href="{alt_links[l]}">' for l in LANGS)
    tr_note = ("" if lang in SOURCE_LANGS else
               f'<span class="tr">{ui["translated"]} (<a href="{REPO}/issues">GitHub</a>)</span>')
    t = f"{html.escape(page_title)} · {ui['site']}" if page_title else ui["site"]
    return f"""<!DOCTYPE html>
<html lang="{hl[lang]}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#0b0f14">
<title>{t}</title>
<meta name="description" content="{html.escape(ui['tagline'])}">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../style.css">
{alternates}
</head><body>
<header class="bar"><div class="wrap top">
<a class="brand" href="index.html">{LOGO}<span>TF3 <b>MECHANICS</b></span></a>
<nav class="nav"><a href="index.html" class="{"on" if nav_on == "home" else ""}">{icon("list", 17)}{ui["home"]}</a>
<a href="https://wiki.transportfever3.com">{icon("book", 17)}{ui["official"]}{icon("external", 13)}</a></nav>
<details class="langs"><summary aria-label="{ui["lang_label"]}">{icon("globe", 16)}<span>{L.BY_CODE[lang]["name"]}</span>{icon("chev", 14, "chev")}</summary><nav class="menu" aria-label="{ui["lang_label"]}">{langs}</nav></details></div></header>
{body}
<footer><div class="wrap"><a class="brand" href="index.html">{LOGO}<span>TF3 <b>MECHANICS</b></span></a>
<div class="txt"><span>{ui["footer"]}</span><span>{ui["lic"]}</span>{tr_note}</div>
<div class="links"><a href="https://wiki.transportfever3.com">{icon("book", 15)}{ui["official"]}</a></div></div></footer>
<script>{JS.strip()}</script>
</body></html>
"""


def root_redirect():
    """Picks the visitor's language: zh-TW/HK/MO/Hant -> traditional, other zh -> simplified, pt -> pt-br."""
    have = json.dumps(LANGS)
    links = " · ".join(f'<a href="{l}/index.html" lang="{L.BY_CODE[l]["html"]}">{L.BY_CODE[l]["name"]}</a>' for l in LANGS)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>TF3 Mechanics</title>
<meta http-equiv="refresh" content="1; url=en/index.html">
<script>(function(){{var have={have};
var ls=(navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||"en"]);
for(var i=0;i<ls.length;i++){{var t=ls[i].toLowerCase(),c=t.split("-")[0];
if(c==="zh")c=/-(tw|hk|mo|hant)/.test(t)?"zh-tw":"zh-cn";else if(c==="pt")c="pt-br";
if(have.indexOf(c)>=0){{location.replace(c+"/index.html");return;}}}}
location.replace("en/index.html");}})();</script>
</head><body style="background:#0b0f14;color:#c3cad4;font-family:system-ui,sans-serif">{links}</body></html>
"""


def domain_of(domains, did):
    return next((d for d in domains if d["id"] == did), None)


def count_refs(text):
    return len(set(re.findall(r"`([\w./-]+\.(?:lua|tl))(?::\d+(?:-\d+)?)?`", text)))


def first_diagram(text, lang):
    m = re.search(r"```diagram\s+(\w+)", text)
    return diagrams.render(m.group(1), lang)[0] if m else ""


def build():
    index = load_json(INDEX, {"domains": {}, "files": {}})
    domains = load_domains()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    with open(os.path.join(OUT, "style.css"), "w", encoding="utf-8", newline="\n") as f:
        f.write(CSS.strip() + "\n")
    with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LOGO.replace('class="logo" ', 'xmlns="http://www.w3.org/2000/svg" '))
    with open(os.path.join(OUT, ".nojekyll"), "w") as f:
        f.write("")

    pages = {lang: {} for lang in LANGS}
    for lang in LANGS:
        d = os.path.join(CONTENT, lang)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".md"):
                pages[lang][fn[:-3]] = parse_page(os.path.join(d, fn))

    files = index["files"]
    dom_files = {d["id"]: sum(1 for sid in files if any(sid.startswith(p) for p in d["prefixes"])) for d in domains}
    max_files = max(dom_files.values() or [1]) or 1

    for lang in LANGS:
        ui = UI[lang]
        os.makedirs(os.path.join(OUT, lang), exist_ok=True)

        def dname(did):
            dom = domain_of(domains, did)
            return (dom["text"].get(lang) or dom["text"]["en"])["name"] if dom else did

        # ---------------------------------------------------------------- pages
        for slug, (meta, text) in pages[lang].items():
            status = meta.get("status", "draft")
            did = meta.get("domain", "")
            pills = [f'<span class="pill {status}">{icon("check", 14, stroke=3)}{ui["status"].get(status, status)}</span>']
            if meta.get("official"):
                pills.append(f'<a class="pill" href="{official_link(meta["official"])}">{icon("book", 14)}{ui["official"]}'
                             f'{icon("external", 12)}</a>')
            if meta.get("updated"):
                pills.append(f'<span class="pill">{icon("clock", 14)}{ui["updated"]} {meta["updated"]}</span>')
            facts = "".join(f'<div class="fact rise d{i + 1}"><b>{html.escape(v)}</b><span>{html.escape(lab)}</span></div>'
                            for i, (v, lab) in enumerate(meta["facts"]))
            article, toc = render_body(text, lang, ui)
            dom_icon = icon(did, 15) if did in ICONS else ""
            hero = (f'<section class="hero"><div class="wrap">'
                    f'<div class="crumb rise"><a href="index.html">{icon("back", 15)}{ui["home"]}</a><span>/</span>'
                    f'<span class="dom">{dom_icon}{html.escape(dname(did))}</span></div>'
                    f'<h1 class="rise d1">{html.escape(meta.get("title", slug))}</h1>'
                    f'<p class="lead rise d2">{html.escape(meta.get("summary", ""))}</p>'
                    f'<div class="meta rise d3">{"".join(pills)}</div>'
                    f'{f"<div class=facts>{facts}</div>" if facts else ""}</div></section>')
            toc_html = "".join(f'<li><a href="#{hid}">{html.escape(t)}</a></li>' for hid, t in toc)
            side = (f'<aside class="toc"><h5>{icon("list", 14)}{ui["toc"]}</h5><ol>{toc_html}</ol>'
                    f'<div class="box"><b>{count_refs(text)}</b><span>{ui["sources"]}</span>'
                    + (f'<a href="{official_link(meta["official"])}">{icon("book", 15)}{ui["official"]}{icon("external", 12)}</a>'
                       if meta.get("official") else "") + '</div></aside>')
            others = "".join(
                f'<a class="mcard" href="{s}.html"><span class="di">{icon(m.get("domain", "list"), 20)}</span>'
                f'<span><b>{html.escape(m.get("title", s))}</b><small>{html.escape(dname(m.get("domain", "")))}</small></span>'
                f'{icon("arrow", 18, "end")}</a>'
                for s, (m, _t) in pages[lang].items() if s != slug)
            more = f'<section class="wrap more"><h2>{ui["more"]}</h2><div class="mgrid">{others}</div></section>' if others else ""
            body = (f'{hero}<div class="wrap layout"><article>{article}'
                    f'<p class="srcnote">{icon("code", 15)}{ui["src_note"]}</p></article>{side}</div>{more}')
            alt = {l: (f"../{l}/{slug}.html" if slug in pages[l] else f"../{l}/index.html") for l in LANGS}
            with open(os.path.join(OUT, lang, f"{slug}.html"), "w", encoding="utf-8", newline="\n") as f:
                f.write(page_shell(lang, meta.get("title", slug), body, alt, page_title=meta.get("title", slug)))

        # ---------------------------------------------------------------- index
        feat = []
        for slug, (meta, text) in pages[lang].items():
            did = meta.get("domain", "")
            mini = "".join(f"<span><b>{html.escape(v)}</b> {html.escape(lab)}</span>" for v, lab in meta["facts"][:2])
            feat.append(
                f'<a class="fcard rise" href="{slug}.html"><div class="thumb">{first_diagram(text, lang)}</div>'
                f'<div class="body"><span class="tag">{icon(did, 15) if did else ""}{html.escape(dname(did))}</span>'
                f'<h3>{html.escape(meta.get("title", slug))}</h3><p>{html.escape(meta.get("summary", ""))}</p>'
                f'<div class="mini">{mini}</div>'
                f'<div class="go"><span class="pill verified">{icon("check", 13, stroke=3)}'
                f'{ui["status"].get(meta.get("status", "draft"))}</span>'
                f'<span class="r">{ui["read_more"]}{icon("arrow", 17)}</span></div></div></a>')
        dom_cards = []
        for dom in domains:
            t = dom["text"].get(lang) or dom["text"]["en"]
            n = dom_files[dom["id"]]
            linked = [s for s, (m, _x) in pages[lang].items() if m.get("domain") == dom["id"]]
            qs = "".join(f"<li>{html.escape(q)}</li>" for q in t.get("questions", []))
            pl = "".join(f'<a href="{s}.html">{icon("arrow", 14)}{html.escape(pages[lang][s][0].get("title", s))}</a>'
                         for s in linked)
            off = "".join(f'<a href="{OFFICIAL_BASE}{o}">{ui["official"]}{icon("external", 11)}</a>'
                          for o in dom.get("official", [])[:1])
            dom_cards.append(
                f'<div class="dcard{" has" if linked else ""}"><div class="t"><span class="di">{icon(dom["id"], 21)}</span>'
                f'<h3>{html.escape(t["name"])}</h3></div><p class="what">{html.escape(t["what"])}</p><ul>{qs}</ul>'
                f'<div class="foot"><div class="pages">{pl or ui["no_page"]}</div>'
                f'<div class="meter"><i style="width:{max(4, round(100 * n / max_files))}%"></i></div>'
                f'<div class="row"><span>{n} {ui["files"]}</span>{off}</div></div></div>')
        n_pages = len(pages[lang])
        stats = "".join(f'<div class="fact rise d{i + 1}"><b>{v}</b><span>{lab}</span></div>' for i, (v, lab) in enumerate(
            [(n_pages, ui["st_pages"]), (len(domains), ui["st_dom"]), (f"{len(files):,}".replace(",", "\u202f"), ui["st_files"]),
             (len(LANGS), ui["st_lang"])]))
        site = ui["site"]
        words = site.split(" ", 1) if " " in site else site.split("-", 1)
        sep = " " if " " in site else "-"
        title_html = (f'{html.escape(words[0])}{sep}<span class="grad">{html.escape(words[1])}</span>'
                      if len(words) == 2 else html.escape(site))
        body = (f'<section class="hero"><div class="wrap"><div class="kicker rise">{icon("bolt", 15)}{ui["hero_kicker"]}</div>'
                f'<h1 class="rise d1">{title_html}</h1><p class="lead rise d2">{ui["tagline"]}</p>'
                f'<div class="stats">{stats}</div></div></section>'
                f'<section class="wrap section"><div class="section-h"><div><h2>{ui["pages"]}</h2><p>{ui["pages_sub"]}</p></div></div>'
                f'<div class="feat">{"".join(feat)}</div></section>'
                f'<section class="wrap section"><div class="section-h"><div><h2>{ui["domains"]}</h2><p>{ui["domains_sub"]}</p></div>'
                f'<label class="search">{icon("search", 18)}<input id="q" type="search" placeholder="{ui["filter"]}"></label></div>'
                f'<div class="dgrid">{"".join(dom_cards)}</div><p class="empty">–</p></section>')
        alt = {l: f"../{l}/index.html" for l in LANGS}
        with open(os.path.join(OUT, lang, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page_shell(lang, site, body, alt, nav_on="home"))

    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(root_redirect())
    n = sum(len(p) for p in pages.values())
    print(f"built {n} pages + {len(LANGS)} indexes -> {OUT}")


if __name__ == "__main__":
    build()
    sys.exit(0)
