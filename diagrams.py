"""SVG diagrams of the wiki, one function per diagram, texts per language.

render(name, lang) -> (svg markup, caption).
Every diagram gets its own id prefix, so several diagrams can sit on one page.
"""
import html
import unicodedata

import icons
import langs

GOLD, TEAL, RED, DIM, TEXT, PANEL, LINE, VIOLET, BLUE = (
    "#f2b84b", "#38d1bf", "#f0705f", "#8f9bab", "#eef1f5", "#161c24", "#2a3340", "#b49cf0", "#5aa9ff")
DEEP = "#0f141b"
FONT = ("Inter,Segoe UI Variable,Segoe UI,system-ui,Microsoft YaHei,Microsoft JhengHei,Yu Gothic,Malgun Gothic,"
        "PingFang SC,Hiragino Sans,Noto Sans CJK SC,sans-serif")


def width(s):
    """Display width in Latin characters: CJK and full-width characters count double."""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def split_at(s, n):
    """Cut s before display width n: at the last space, or anywhere for CJK text without spaces."""
    w, cut = 0, len(s)
    for i, c in enumerate(s):
        w += width(c)
        if w > n:
            cut = i
            break
    if cut == len(s):
        return s, ""
    sp = s.rfind(" ", 0, cut + 1)
    if sp > 0:
        return s[:sp], s[sp:].strip()
    return s[:cut], s[cut:]


def wrap_rows(s, n):
    rows = []
    while s:
        a, s = split_at(s, n)
        rows.append(a)
    return rows or [""]


class Svg:
    def __init__(self, name, w, h):
        self.id, self.w, self.h, self.parts = name, w, h, []
        i = name
        self.defs = (
            f'<linearGradient id="{i}-gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7cf72"/><stop offset="1" stop-color="#e09a2a"/></linearGradient>'
            f'<linearGradient id="{i}-teal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5ee6d3"/><stop offset="1" stop-color="#1fa596"/></linearGradient>'
            f'<linearGradient id="{i}-card" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2430"/><stop offset="1" stop-color="#131921"/></linearGradient>'
            f'<linearGradient id="{i}-tealsoft" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#38d1bf" stop-opacity=".05"/><stop offset="1" stop-color="#38d1bf" stop-opacity=".28"/></linearGradient>'
            f'<filter id="{i}-sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity=".45"/></filter>'
            f'<filter id="{i}-glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
            f'<marker id="{i}-ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker>')

    def ref(self, what):
        return f"url(#{self.id}-{what})"

    def add(self, s):
        self.parts.append(s)

    def card(self, x, y, w, h, stroke=LINE, r=16, dash=None, fill=None, shadow=True):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        f = fill or self.ref("card")
        sh = f' filter="{self.ref("sh")}"' if shadow else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}" stroke="{stroke}" stroke-width="1.5"{d}{sh}/>')

    def rect(self, x, y, w, h, fill, r=6, stroke="none", sw=1.5, opacity=1):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

    def text(self, x, y, s, size=15, color=TEXT, anchor="middle", weight=400, spacing=0):
        ls = f' letter-spacing="{spacing}"' if spacing else ""
        self.add(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}"{ls} '
                 f'font-family="{FONT}">{html.escape(s)}</text>')

    def lines(self, x, y, rows, size=14, color=DIM, anchor="middle", gap=1.4, weight=400):
        for i, s in enumerate(rows):
            self.text(x, y + i * size * gap, s, size, color, anchor, weight)

    def icon_badge(self, cx, cy, name, color, r=30, fill=None):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill or color}" fill-opacity="{1 if fill else .14}" '
                 f'stroke="{color}" stroke-opacity=".55" stroke-width="1.5"/>')
        size = r * 1.05
        self.add(icons.place(name, cx - size / 2, cy - size / 2, size, color if not fill else DEEP, 2))

    def chip(self, x, y, label, color, w=None, h=26, size=14, dark=True):
        w = w or (width(label) * size * 0.62 + 22)
        self.rect(x, y, w, h, color, r=h / 2)
        self.text(x + w / 2, y + h * 0.69, label, size, DEEP if dark else TEXT, weight=700)
        return w

    def flow(self, x1, y1, x2, y2, color=GOLD, width=3, animate=True):
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-opacity=".25" stroke-width="{width + 5}" stroke-linecap="round"/>')
        anim = ('<animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.2s" repeatCount="indefinite"/>'
                if animate else "")
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-dasharray="8 4" '
                 f'stroke-linecap="round" marker-end="{self.ref("ah")}">{anim}</line>')

    def wrapped(self, x, y, s, width_chars, size=13, color=TEXT, anchor="start", weight=400):
        """Text on one or two lines, split at the last space before width_chars; y is the middle."""
        a, b = split_at(s, width_chars)
        if not b:
            self.text(x, y + size * .35, s, size, color, anchor, weight)
            return
        self.text(x, y - size * .35, a, size, color, anchor, weight)
        self.text(x, y + size * 1.05, b, size, color, anchor, weight)

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" role="img">'
                f'<defs>{self.defs}</defs>{"".join(self.parts)}</svg>')


# ---------------------------------------------------------------- workers: assignment vs boost
T_WORKERS = {
    "en": {
        "cap": "Two different counts: the residents the game assigns to the industry, and the arrivals that count for the boost.",
        "home": "Home", "home2": "in a town", "lines": "Your passenger lines", "lines2": "the only way there",
        "no": "no walking, no car",
        "ind": "Industry", "ind2": "20 workplaces",
        "a": "Assigned", "a2": "residents whose job is this industry",
        "b": "Counted for the boost", "b2": "arrivals by your lines, last 2 years, latest 20",
        "ex": "e.g.", "need": "10 needed = 50 %",
        "rule": "Boosted", "eff": "production ×1.5 to ×2.5, fixed per industry",
        "nob": "assigned alone: no boost",
    },
    "fr": {
        "cap": "Deux comptes différents : les habitants que le jeu attribue à l'industrie, et les arrivées qui comptent pour le bonus.",
        "home": "Logement", "home2": "dans une ville", "lines": "Tes lignes de passagers", "lines2": "le seul moyen d'y aller",
        "no": "ni à pied, ni en voiture",
        "ind": "Industrie", "ind2": "20 emplois",
        "a": "Attribués", "a2": "habitants dont l'emploi est cette industrie",
        "b": "Comptés pour le bonus", "b2": "arrivées par tes lignes, 2 dernières années, 20 max",
        "ex": "ex.", "need": "10 requis = 50 %",
        "rule": "Boostée", "eff": "production ×1,5 à ×2,5, fixe pour chaque industrie",
        "nob": "attribués seuls : pas de bonus",
    },
    "de": {
        "cap": "Zwei verschiedene Zählungen: die Einwohner, die das Spiel der Industrie zuteilt, und die Ankünfte, die für den Bonus zählen.",
        "home": "Wohnung", "home2": "in einer Stadt", "lines": "Deine Personenlinien", "lines2": "der einzige Weg dorthin",
        "no": "nicht zu Fuß, nicht mit dem Auto",
        "ind": "Industrie", "ind2": "20 Arbeitsplätze",
        "a": "Zugeteilt", "a2": "Einwohner, deren Arbeit diese Industrie ist",
        "b": "Für den Bonus gezählt", "b2": "Ankünfte mit deinen Linien, 2 Jahre, max. 20",
        "ex": "z. B.", "need": "10 nötig = 50 %",
        "rule": "Geboostet", "eff": "Produktion ×1,5 bis ×2,5, pro Industrie fest",
        "nob": "nur zugeteilt: kein Bonus",
    },
}


def _gauge(s, x, y, w, value, total, color, threshold=None, label=""):
    """Bar of `total` segments, `value` of them filled."""
    seg = w / total
    for i in range(total):
        on = i < value
        s.rect(x + i * seg + 1.5, y, seg - 3, 18, color if on else "#232c38", r=3, opacity=1 if on else 1)
    if threshold:
        tx = x + threshold * seg
        s.add(f'<line x1="{tx}" y1="{y - 8}" x2="{tx}" y2="{y + 26}" stroke="{TEXT}" stroke-width="2" stroke-dasharray="3 3"/>')
        s.text(tx, y + 44, label, 13, TEXT, weight=600)


def workers_flow(lang):
    t = T_WORKERS[lang]
    s = Svg("wf", 900, 470)
    # route
    s.flow(150, 90, 352, 90, GOLD)
    s.flow(548, 90, 750, 90, GOLD)
    for cx, ic, col, name, sub in ((90, "home", BLUE, t["home"], t["home2"]),
                                   (810, "industries", TEXT, t["ind"], t["ind2"])):
        s.icon_badge(cx, 76, ic, col, 38)
        s.text(cx, 140, name, 18, TEXT, weight=700)
        s.text(cx, 161, sub, 13, DIM)
    s.card(352, 34, 196, 112, stroke=GOLD)
    s.icon_badge(450, 72, "bus", GOLD, 24, fill=s.ref("gold"))
    s.text(450, 116, t["lines"], 15, GOLD, weight=700)
    s.text(450, 135, t["lines2"], 12, DIM)
    # forbidden ways
    s.add(f'<path d="M110 176 Q450 232 790 176" fill="none" stroke="{RED}" stroke-opacity=".55" stroke-width="2" stroke-dasharray="4 5"/>')
    s.add(icons.place("walk_no", 438, 194, 24, RED))
    s.text(450, 238, t["no"], 13, RED, weight=600)
    # counters
    for x, title, sub, val, col, dash, thr in ((40, t["a"], t["a2"], 14, DIM, "6 5", None),
                                                 (470, t["b"], t["b2"], 12, TEAL, None, 10)):
        s.card(x, 262, 390, 128, stroke=col if col == TEAL else LINE, dash=dash)
        s.text(x + 24, 294, title, 17, TEAL if col == TEAL else TEXT, "start", 700)
        s.text(x + 24, 314, sub, 12.5, DIM, "start")
        s.text(x + 366, 294, f'{t["ex"]} {val}/20', 15, col if col == TEAL else TEXT, "end", 700)
        _gauge(s, x + 24, 330, 342, val, 20, s.ref("teal") if col == TEAL else "#5b6676", thr, t["need"] if thr else "")
    s.text(235, 380, t["nob"], 12.5, DIM, weight=600)
    # result
    s.add(f'<line x1="665" y1="390" x2="665" y2="410" stroke="{TEAL}" stroke-width="2"/>')
    s.rect(240, 410, 620, 46, s.ref("teal"), r=23)
    s.add(icons.place("bolt", 262, 421, 24, DEEP))
    s.text(296, 440, t["rule"], 17, DEEP, "start", 800)
    s.text(300 + width(t["rule"]) * 10.5, 440, t["eff"], 14.5, DEEP, "start", 500)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- workers: 2-year window, 20 kept
T_WINDOW = {
    "en": {"cap": "Each arrival by your lines is remembered for 2 game years; at most the latest 20 are kept.",
           "now": "now", "ago": "2 years ago", "kept": "counted: arrivals of the last 2 years (20 max)", "old": "too old: dropped",
           "same": "same person again: only the latest arrival counts"},
    "fr": {"cap": "Chaque arrivée par tes lignes est retenue 2 années de jeu ; au plus les 20 dernières sont gardées.",
           "now": "maintenant", "ago": "il y a 2 ans", "kept": "comptées : arrivées des 2 dernières années (20 max)", "old": "trop anciennes : retirées",
           "same": "même personne à nouveau : seule la dernière arrivée compte"},
    "de": {"cap": "Jede Ankunft mit deinen Linien wird 2 Spieljahre gemerkt; höchstens die letzten 20 bleiben.",
           "now": "jetzt", "ago": "vor 2 Jahren", "kept": "gezählt: Ankünfte der letzten 2 Jahre (max. 20)", "old": "zu alt: entfernt",
           "same": "dieselbe Person erneut: nur die letzte Ankunft zählt"},
}


def workers_window(lang):
    t = T_WINDOW[lang]
    s = Svg("ww", 900, 250)
    x0, x1 = 170, 840
    s.rect(x0, 66, x1 - x0, 72, s.ref("tealsoft"), r=14, stroke=TEAL, sw=1.5)
    s.text((x0 + x1) / 2, 52, t["kept"], 14, TEAL, weight=700)
    s.add(f'<line x1="30" y1="102" x2="878" y2="102" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>')
    for x in range(40, 880, 40):
        s.add(f'<line x1="{x}" y1="97" x2="{x}" y2="107" stroke="{LINE}" stroke-width="2"/>')
    for x in (60, 110):
        s.add(f'<circle cx="{x}" cy="102" r="11" fill="{PANEL}" stroke="{DIM}" stroke-width="1.5"/>')
        s.add(icons.place("cross", x - 6, 96, 12, DIM, 2.5))
    s.text(85, 52, t["old"], 13, DIM, weight=600)
    xs = [205, 250, 320, 365, 440, 500, 560, 625, 680, 745, 800]
    for i, x in enumerate(xs):
        col = GOLD if i in (2, 9) else TEAL
        s.add(f'<circle cx="{x}" cy="102" r="12" fill="{col}" filter="{s.ref("glow")}"/>')
        s.add(f'<circle cx="{x}" cy="98" r="3.2" fill="{DEEP}"/><path d="M{x - 5.5} 108a5.5 5 0 0 1 11 0z" fill="{DEEP}"/>')
    # the same person twice: the older arrival is replaced
    s.add(f'<circle cx="{xs[2]}" cy="102" r="12" fill="{PANEL}" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 3"/>')
    s.add(f'<path d="M{xs[2]} 120 Q{(xs[2] + xs[9]) / 2} 190 {xs[9] - 4} 122" fill="none" stroke="{GOLD}" stroke-width="2" '
          f'marker-end="{s.ref("ah")}"/>')
    s.text((xs[2] + xs[9]) / 2, 182, t["same"], 13.5, GOLD, weight=600)
    s.text(x0, 232, t["ago"], 14, TEXT, weight=600)
    s.text(x1, 232, t["now"], 14, TEXT, weight=600)
    s.add(f'<line x1="{x0}" y1="140" x2="{x0}" y2="214" stroke="{DIM}" stroke-dasharray="3 4"/>')
    s.add(f'<line x1="{x1}" y1="140" x2="{x1}" y2="214" stroke="{DIM}" stroke-dasharray="3 4"/>')
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- loading: factors
T_LOAD = {
    "en": {"cap": "Loading speed = vehicle's base speed × platform factor × stock factor.",
           "veh": "Vehicle", "veh2": ["base load speed", "shown in the vehicle store"],
           "plat": "Platform", "stock": "Stock",
           "p": [("×2", "wagons on a section of their class", TEAL), ("×1", "universal section", DIM),
                 ("×0.25", "no section of their class", RED), ("×0.25", "part beyond the platform", RED)],
           "k": [("×2", "specialised warehouse module", TEAL), ("×1", "universal warehouse", DIM),
                 ("×1", "industry", DIM)],
           "res": "loading speed"},
    "fr": {"cap": "Vitesse de chargement = vitesse de base du véhicule × facteur du quai × facteur du stock.",
           "veh": "Véhicule", "veh2": ["vitesse de base", "affichée à l'achat"],
           "plat": "Quai", "stock": "Stock",
           "p": [("×2", "wagons sur une section de leur classe", TEAL), ("×1", "section universelle", DIM),
                 ("×0,25", "aucune section de leur classe", RED), ("×0,25", "partie au-delà du quai", RED)],
           "k": [("×2", "module d'entrepôt spécialisé", TEAL), ("×1", "entrepôt universel", DIM),
                 ("×1", "industrie", DIM)],
           "res": "vitesse de chargement"},
    "de": {"cap": "Ladegeschwindigkeit = Grundgeschwindigkeit des Fahrzeugs × Bahnsteigfaktor × Lagerfaktor.",
           "veh": "Fahrzeug", "veh2": ["Grund-Ladegeschwindigkeit", "im Fahrzeugkauf"],
           "plat": "Bahnsteig", "stock": "Lager",
           "p": [("×2", "Wagen auf Abschnitt ihrer Klasse", TEAL), ("×1", "Universalabschnitt", DIM),
                 ("×0,25", "kein Abschnitt ihrer Klasse", RED), ("×0,25", "Teil hinter dem Bahnsteig", RED)],
           "k": [("×2", "spezialisiertes Lagermodul", TEAL), ("×1", "Universallager", DIM),
                 ("×1", "Industrie", DIM)],
           "res": "Ladegeschwindigkeit"},
}


def loading_factors(lang):
    t = T_LOAD[lang]
    s = Svg("lf", 900, 330)
    # vehicle
    s.card(20, 40, 190, 250)
    s.icon_badge(115, 104, "train", BLUE, 36)
    s.text(115, 170, t["veh"], 19, TEXT, weight=700)
    s.lines(115, 194, t["veh2"], 12.5)
    s.chip(77, 236, "2.0x", BLUE)
    # platform
    s.text(236, 175, "×", 34, GOLD, weight=300)
    s.card(262, 20, 330, 290, stroke=GOLD)
    s.add(icons.place("stations", 286, 40, 26, GOLD))
    s.text(322, 61, t["plat"], 19, GOLD, "start", 700)
    for i, (v, lab, col) in enumerate(t["p"]):
        y = 92 + i * 52
        s.chip(286, y, v, col, w=70, h=30, size=15)
        s.wrapped(368, y + 15, lab, 27, 13)
    # stock
    s.text(618, 175, "×", 34, GOLD, weight=300)
    s.card(644, 40, 236, 250, stroke=TEAL)
    s.add(icons.place("warehouses", 668, 60, 26, TEAL))
    s.text(704, 81, t["stock"], 19, TEAL, "start", 700)
    for i, (v, lab, col) in enumerate(t["k"]):
        y = 112 + i * 52
        s.chip(668, y, v, col, w=62, h=30, size=15)
        s.wrapped(740, y + 15, lab, 18, 12.5)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- loading: sections of a platform
T_SECT = {
    "en": {"cap": "The game adds up the module lengths of each cargo class; where a module or a wagon stands does not count.",
           "mods": "Platform modules (40 m each), in any order", "sum": "added up per class",
           "bulk": "Bulk", "uni": "Universal",
           "train": "Train of 8 bulk wagons, 160 m: the factor is mixed by share of the train",
           "s1": "120 m on bulk: ×2", "s2": "40 m: ×1", "res": "≈ ×1.75",
           "no": "With no bulk section at all, these bulk wagons would get ×0.25."},
    "fr": {"cap": "Le jeu additionne les longueurs des modules de chaque classe de fret ; l'endroit où se trouvent un module ou un wagon ne compte pas.",
           "mods": "Modules du quai (40 m chacun), dans n'importe quel ordre", "sum": "additionnés par classe",
           "bulk": "Vrac", "uni": "Universel",
           "train": "Train de 8 wagons vrac, 160 m : le facteur est mélangé selon la part du train",
           "s1": "120 m sur vrac : ×2", "s2": "40 m : ×1", "res": "≈ ×1,75",
           "no": "Sans aucune section vrac sur le quai, ces wagons vrac auraient ×0,25."},
    "de": {"cap": "Das Spiel addiert die Modullängen jeder Frachtklasse; wo ein Modul oder ein Wagen steht, zählt nicht.",
           "mods": "Bahnsteigmodule (je 40 m), in beliebiger Reihenfolge", "sum": "pro Klasse addiert",
           "bulk": "Schüttgut", "uni": "Universal",
           "train": "Zug aus 8 Schüttgutwagen, 160 m: der Faktor wird nach Anteil des Zuges gemischt",
           "s1": "120 m auf Schüttgut: ×2", "s2": "40 m: ×1", "res": "≈ ×1,75",
           "no": "Ganz ohne Schüttgut-Abschnitt bekämen diese Schüttgutwagen ×0,25."},
}


def loading_sections(lang):
    t = T_SECT[lang]
    s = Svg("ls", 900, 360)
    s.text(40, 32, t["mods"], 14, DIM, "start", 600)
    order = ["bulk", "uni", "bulk", "bulk"]
    for i, k in enumerate(order):
        x = 40 + i * 92
        b = k == "bulk"
        s.rect(x, 46, 84, 44, s.ref("gold") if b else "#3a4554", r=8)
        s.text(x + 42, 74, t[k], 13, DEEP if b else TEXT, weight=700)
    s.flow(420, 68, 492, 68, DIM, 2.5, animate=False)
    s.text(512, 32, t["sum"], 14, DIM, "start", 600)
    s.rect(512, 46, 230, 44, s.ref("gold"), r=8)
    s.text(627, 74, f'{t["bulk"]} 120 m', 15, DEEP, weight=800)
    s.rect(746, 46, 130, 44, "#3a4554", r=8)
    s.text(811, 74, f'{t["uni"]} 40 m', 13.5, TEXT, weight=700)
    # train
    s.card(20, 118, 860, 220, stroke=LINE)
    s.text(44, 152, t["train"], 14.5, TEXT, "start", 700)
    for i in range(8):
        x = 44 + i * 100
        s.rect(x, 172, 92, 40, "#25303d", r=7, stroke=GOLD, sw=1.5)
        s.rect(x + 8, 180, 76, 18, s.ref("gold"), r=4, opacity=.85)
        for wx in (x + 18, x + 74):
            s.add(f'<circle cx="{wx}" cy="216" r="5" fill="{DIM}"/>')
    # share bar
    s.rect(44, 238, 592, 34, s.ref("teal"), r=8)
    s.text(340, 261, t["s1"], 14.5, DEEP, weight=800)
    s.rect(640, 238, 196, 34, "#3a4554", r=8)
    s.text(738, 261, t["s2"], 14, TEXT, weight=700)
    s.text(856, 261, "=", 18, DIM, weight=300)
    s.chip(760, 286, t["res"], TEAL, w=96, h=28, size=15)
    s.add(icons.place("info", 44, 293, 18, RED))
    s.text(70, 307, t["no"], 13.5, RED, "start", 600)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- income: the formula
T_INC = {
    "en": {"cap": "What one delivered cargo unit pays. Passengers use the same formula with a vehicle factor (see below).",
           "c": [("3.8", "income factor", "the same for every cargo", GOLD),
                 ("50–150 %", "Cargo Income", "game setting, 100 % in all presets", BLUE),
                 ("km", "distance", "straight line + 8 × climb", TEAL),
                 ("×1 → ×0.75", "company rank", "Inflation setting (Normal)", VIOLET),
                 ("×2", "subsidy lines", "after a completed contract", GOLD)],
           "res": "= income of the delivery", "not": "not in the formula: travel time, vehicle speed, real route length, late or on time"},
    "fr": {"cap": "Ce que rapporte une unité de fret livrée. Les passagers suivent la même formule avec un facteur du véhicule (voir plus bas).",
           "c": [("3,8", "facteur de revenu", "le même pour tous les frets", GOLD),
                 ("50–150 %", "Revenu fret", "réglage de partie, 100 % dans tous les préréglages", BLUE),
                 ("km", "distance", "ligne droite + 8 × la montée", TEAL),
                 ("×1 → ×0,75", "rang d'entreprise", "réglage Inflation (Normale)", VIOLET),
                 ("×2", "lignes du contrat", "après un contrat rempli", GOLD)],
           "res": "= revenu de la livraison", "not": "absents de la formule : durée du trajet, vitesse, longueur réelle du trajet, retard ou non"},
    "de": {"cap": "Was eine gelieferte Frachteinheit einbringt. Passagiere nutzen dieselbe Formel mit einem Fahrzeugfaktor (siehe unten).",
           "c": [("3,8", "Einnahmefaktor", "für jede Fracht gleich", GOLD),
                 ("50–150 %", "Gütereinnahmen", "Spieleinstellung, 100 % in allen Vorgaben", BLUE),
                 ("km", "Entfernung", "Luftlinie + 8 × Steigung", TEAL),
                 ("×1 → ×0,75", "Unternehmensrang", "Einstellung Inflation (Normal)", VIOLET),
                 ("×2", "Linien der Subvention", "nach erfüllter Subvention", GOLD)],
           "res": "= Einnahme der Lieferung", "not": "nicht in der Formel: Fahrzeit, Geschwindigkeit, echte Streckenlänge, verspätet oder pünktlich"},
}


def income_formula(lang):
    t = T_INC[lang]
    s = Svg("if", 900, 300)
    w, g = 158, 25  # 5 cards + 4 gaps = 890, inside the 900 viewBox
    for i, (big, title, sub, col) in enumerate(t["c"]):
        x = 5 + i * (w + g)
        optional = i >= 3
        s.card(x, 20, w, 170, stroke=col if not optional else LINE, dash="6 5" if optional else None)
        s.text(x + w / 2, 70, big, 25 if width(big) < 6 else 19, col, weight=800)
        s.text(x + w / 2, 108, title, 14, TEXT, weight=700)
        rows = wrap_rows(sub, 21)
        s.lines(x + w / 2, 132, rows, 12)
        if i < 4:
            s.text(x + w + g / 2, 112, "×", 26, GOLD, weight=300)
    s.rect(180, 210, 540, 40, s.ref("teal"), r=20)
    s.text(450, 236, t["res"], 16, DEEP, weight=800)
    s.add(icons.place("cross", 120, 268, 14, RED, 2.5))
    s.text(142, 280, t["not"], 13, RED, "start", 600)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- income: distance
T_DIST = {
    "en": {"cap": "Paid: the straight line from the source of the cargo to where it is delivered, plus 8 m per metre of climb. "
                  "The real route only costs (maintenance).",
           "a": "origin", "b": "destination", "paid": "paid: straight line (3D)", "real": "real route: not paid, costs maintenance",
           "climb": "climb h", "bonus": "+ 8 × h paid", "ex1": "5 km, 100 m higher", "ex2": "paid as 5.8 km (+16 %)",
           "down": "the other way round: no bonus, no malus"},
    "fr": {"cap": "Payé : la ligne droite entre la source du fret et l'endroit où il est livré, plus 8 m par mètre de montée. "
                  "Le vrai trajet ne fait que coûter (entretien).",
           "a": "départ", "b": "destination", "paid": "payé : ligne droite (3D)", "real": "vrai trajet : pas payé, coûte l'entretien",
           "climb": "montée h", "bonus": "+ 8 × h payés", "ex1": "5 km, 100 m plus haut", "ex2": "payé comme 5,8 km (+16 %)",
           "down": "dans l'autre sens : ni bonus, ni malus"},
    "de": {"cap": "Bezahlt wird die Luftlinie von der Quelle der Fracht bis zum Lieferort, plus 8 m pro Meter Steigung. "
                  "Die echte Strecke kostet nur (Unterhalt).",
           "a": "Start", "b": "Ziel", "paid": "bezahlt: Luftlinie (3D)", "real": "echte Strecke: nicht bezahlt, kostet Unterhalt",
           "climb": "Steigung h", "bonus": "+ 8 × h bezahlt", "ex1": "5 km, 100 m höher", "ex2": "bezahlt wie 5,8 km (+16 %)",
           "down": "in der Gegenrichtung: kein Bonus, kein Malus"},
}


def income_distance(lang):
    t = T_DIST[lang]
    s = Svg("id", 900, 330)
    # terrain
    s.add(f'<path d="M0 290 C140 286 200 280 300 262 S520 200 640 176 S800 160 900 158 L900 330 L0 330 Z" fill="#17202a"/>')
    s.add(f'<path d="M0 290 C140 286 200 280 300 262 S520 200 640 176 S800 160 900 158" fill="none" stroke="{LINE}" stroke-width="2"/>')
    ax, ay, bx, by = 90, 270, 760, 150
    # real route
    s.add(f'<path d="M{ax} {ay} C180 200 260 320 350 250 S470 120 560 210 S700 120 {bx} {by}" fill="none" stroke="{GOLD}" '
          f'stroke-width="3" stroke-dasharray="7 6" opacity=".8"/>')
    s.text(420, 300, t["real"], 13, GOLD, weight=600)
    # straight line
    s.add(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>')
    s.add(f'<text font-size="14" font-weight="700" fill="{TEAL}" font-family="{FONT}" text-anchor="middle" '
          f'transform="translate(410 196) rotate(-10.2)">{html.escape(t["paid"])}</text>')
    # climb
    s.add(f'<line x1="{bx + 40}" y1="{ay}" x2="{bx + 40}" y2="{by}" stroke="{VIOLET}" stroke-width="2.5" marker-end="{s.ref("ah")}"/>')
    s.add(f'<line x1="{ax}" y1="{ay}" x2="{bx + 50}" y2="{ay}" stroke="{DIM}" stroke-dasharray="3 4"/>')
    s.text(bx + 52, 214, t["climb"], 13, VIOLET, "start", 700)
    s.text(bx + 52, 232, t["bonus"], 13, VIOLET, "start", 600)
    for x, y, lab, col, ic in ((ax, ay, t["a"], BLUE, "industries"), (bx, by, t["b"], TEAL, "towns")):
        s.icon_badge(x, y, ic, col, 22, fill=s.ref("teal") if col == TEAL else None)
        s.text(x, y + (40 if col == BLUE else -32), lab, 14, TEXT, weight=700)
    s.card(24, 18, 300, 92, stroke=TEAL)
    s.text(44, 50, t["ex1"], 15, TEXT, "start", 700)
    s.text(44, 76, t["ex2"], 15, TEAL, "start", 800)
    s.text(44, 98, t["down"], 12, DIM, "start")
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- income: cargo that changes line (measured in game)
T_SPLIT = {
    "en": {"cap": "One payment, at the consumer, for the straight line from the source. Each line gets the share of its leg's "
                  "straight-line length. Measured in game.",
           "src": "source", "wh": "warehouse", "dst": "consumer",
           "leg1": "leg 1: ship, 2 km", "leg2": "leg 2: train, 6 km",
           "paid": "paid once, at delivery: 3.8 × straight line source → consumer",
           "whnote": "unloaded here: nothing paid yet",
           "l1": "ship line 25 %", "l2": "train line 75 %",
           "hold": "the delivering vehicle holds the money a moment, then every line of the chain is credited"},
    "fr": {"cap": "Un seul paiement, chez le client, pour la ligne droite depuis la source. Chaque ligne reçoit la part de la "
                  "longueur en ligne droite de son étape. Mesuré en jeu.",
           "src": "source", "wh": "entrepôt", "dst": "client",
           "leg1": "étape 1 : bateau, 2 km", "leg2": "étape 2 : train, 6 km",
           "paid": "payé une fois, à la livraison : 3,8 × ligne droite source → client",
           "whnote": "déchargé ici : rien de payé encore",
           "l1": "ligne bateau 25 %", "l2": "ligne train 75 %",
           "hold": "le véhicule qui livre garde l'argent un instant, puis chaque ligne de la chaîne est créditée"},
    "de": {"cap": "Eine Zahlung, beim Abnehmer, für die Luftlinie ab der Quelle. Jede Linie erhält den Anteil der Luftlinie "
                  "ihres Abschnitts. Im Spiel gemessen.",
           "src": "Quelle", "wh": "Lagerhaus", "dst": "Abnehmer",
           "leg1": "Abschnitt 1: Schiff, 2 km", "leg2": "Abschnitt 2: Zug, 6 km",
           "paid": "einmal bezahlt, bei Lieferung: 3,8 × Luftlinie Quelle → Abnehmer",
           "whnote": "hier entladen: noch nichts bezahlt",
           "l1": "Schiffslinie 25 %", "l2": "Zuglinie 75 %",
           "hold": "das liefernde Fahrzeug hält das Geld kurz, dann wird jede Linie der Kette gutgeschrieben"},
}


def income_split(lang):
    t = T_SPLIT[lang]
    s = Svg("sp", 900, 340)
    sx, sy, wx, wy, dx, dy = 90, 132, 300, 192, 810, 132
    # what is paid: one arc from the source to the consumer, above their labels
    s.add(f'<path d="M{sx} 80 Q450 8 {dx} 80" fill="none" stroke="{GOLD}" stroke-width="3" '
          f'stroke-dasharray="7 6" marker-end="{s.ref("ah")}"/>')
    s.text(450, 30, t["paid"], 14, GOLD, weight=700)
    # the two legs
    s.flow(sx + 24, sy + 7, wx - 26, wy - 7, BLUE, 3)
    s.flow(wx + 26, wy - 7, dx - 26, dy + 7, TEAL, 3)
    s.text(150, 192, t["leg1"], 12.5, BLUE, weight=700)
    s.text((wx + dx) / 2, 146, t["leg2"], 12.5, TEAL, weight=700)
    for x, y, lab, col, ic in ((sx, sy, t["src"], BLUE, "industries"), (wx, wy, t["wh"], DIM, "warehouses"),
                               (dx, dy, t["dst"], TEAL, "industries")):
        s.icon_badge(x, y, ic, col, 22, fill=s.ref("teal") if col == TEAL else None)
        s.text(x, y - 32, lab, 14, TEXT, weight=700)
    s.lines(wx, wy + 42, wrap_rows(t["whnote"], 44), 12, DIM)
    # the split, to scale
    bx, bw, by = 90, 720, 262
    w1 = bw * 2 / 8
    s.rect(bx, by, w1 - 2, 30, BLUE, r=8)
    s.rect(bx + w1 + 2, by, bw - w1 - 2, 30, TEAL, r=8)
    s.text(bx + w1 / 2, by + 20, t["l1"], 13 if width(t["l1"]) <= 22 else 11.5, DEEP, weight=800)
    s.text(bx + w1 + (bw - w1) / 2, by + 20, t["l2"], 13, DEEP, weight=800)
    s.lines(450, 318, wrap_rows(t["hold"], 110), 12.5, DIM)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- delivery: time limits per cargo
CARGO_TIMES = [  # timeToDeliverInSeconds in the base-game .cargo.lua files
    (900, ["Meat"]), (1125, ["Beverages", "Fish", "Vegetables"]), (1286, ["Grain"]),
    (1500, ["Clothes", "Fabric", "Fertilizer", "Plastic", "Tires", "Wool"]),
    (1800, ["Books", "Chemicals", "Furniture", "Paper", "Rubber", "Tinned Food"]),
    (2250, ["Cement", "Dyes", "Fuel", "Glass", "Machines", "Sawdust", "Tools", "Vehicles"]),
    (3000, ["Bricks", "Clay", "Coal", "Crude Oil", "Logs", "Planks", "Sheet Metal"]),
    (4500, ["Iron Ore", "Sand", "Steel", "Stone"]),
]
CARGO_NAMES = {
    "fr": {"Meat": "Viande", "Beverages": "Boissons", "Fish": "Poisson", "Vegetables": "Légumes", "Grain": "Céréales",
           "Clothes": "Vêtements", "Fabric": "Tissu", "Fertilizer": "Engrais", "Plastic": "Plastique", "Tires": "Pneus",
           "Wool": "Laine", "Books": "Livres", "Chemicals": "Produits chimiques", "Furniture": "Meubles", "Paper": "Papier",
           "Rubber": "Caoutchouc", "Tinned Food": "Tinned Food", "Cement": "Ciment", "Dyes": "Colorants", "Fuel": "Carburant",
           "Glass": "Verre", "Machines": "Machines", "Sawdust": "Sciure", "Tools": "Outils", "Vehicles": "Véhicules",
           "Bricks": "Briques", "Clay": "Argile", "Coal": "Charbon", "Crude Oil": "Pétrole brut", "Logs": "Bois",
           "Planks": "Planches", "Sheet Metal": "Tôle", "Iron Ore": "Minerai de fer", "Sand": "Sable", "Steel": "Acier",
           "Stone": "Pierre"},
    "de": {"Meat": "Fleisch", "Beverages": "Getränke", "Fish": "Fisch", "Vegetables": "Gemüse", "Grain": "Getreide",
           "Clothes": "Kleidung", "Fabric": "Stoff", "Fertilizer": "Dünger", "Plastic": "Kunststoff", "Tires": "Reifen",
           "Wool": "Wolle", "Books": "Bücher", "Chemicals": "Chemikalien", "Furniture": "Möbel", "Paper": "Papier",
           "Rubber": "Gummi", "Tinned Food": "Tinned Food", "Cement": "Zement", "Dyes": "Farbstoffe", "Fuel": "Treibstoff",
           "Glass": "Glas", "Machines": "Maschinen", "Sawdust": "Sägespäne", "Tools": "Werkzeuge", "Vehicles": "Fahrzeuge",
           "Bricks": "Ziegel", "Clay": "Lehm", "Coal": "Kohle", "Crude Oil": "Rohöl", "Logs": "Holz", "Planks": "Bretter",
           "Sheet Metal": "Blech", "Iron Ore": "Eisenerz", "Sand": "Sand", "Steel": "Stahl", "Stone": "Stein"},
}
T_TIMES = {
    "en": {"cap": "Time allowed before a delivery counts as delayed, relative to meat (the shortest). "
                  "The game adjusts the actual time: Finances › Delivery Time shows it for your map.",
           "short": "fresh food: hurry", "long": "raw materials: plenty of time"},
    "fr": {"cap": "Délai accordé avant qu'une livraison soit retardée, comparé à la viande (le plus court). "
                  "Le jeu ajuste le délai réel : Finances › Délai de livraison l'affiche pour ta carte.",
           "short": "produits frais : vite", "long": "matières premières : large"},
    "de": {"cap": "Erlaubte Zeit, bevor eine Lieferung als verzögert gilt, im Vergleich zu Fleisch (die kürzeste). "
                  "Das Spiel passt die tatsächliche Zeit an: Finanzen › Lieferzeit zeigt sie für deine Karte.",
           "short": "Frischware: schnell", "long": "Rohstoffe: viel Zeit"},
}


def delivery_times(lang):
    t = T_TIMES[lang]
    names = CARGO_NAMES.get(lang, {})
    rows = len(CARGO_TIMES)
    s = Svg("dt", 900, 60 + rows * 42)
    x0, wmax = 24, 300
    s.text(x0, 26, t["short"], 13, RED, "start", 700)
    s.text(x0 + wmax + 70, 26, t["long"], 13, TEAL, "end", 700)
    for i, (sec, cargos) in enumerate(CARGO_TIMES):
        y = 44 + i * 42
        w = wmax * sec / 4500
        k = (sec - 900) / 3600
        col = RED if k < .15 else GOLD if k < .45 else TEAL
        s.rect(x0, y, wmax, 26, "#1b232d", r=8)
        s.rect(x0, y, w, 26, col, r=8, opacity=.9)
        rel = "×" + f"{sec / 900:.2f}".rstrip("0").rstrip(".").replace(".", langs.BY_CODE[lang]["dec"])
        s.text(x0 + wmax + 12, y + 18, rel, 14, TEXT, "start", 800)
        label = ", ".join(names.get(c, c) for c in cargos)
        # 500 px after the bar: about 72 Latin characters at 13.5 px; longer lists go on two smaller lines
        if width(label) <= 72:
            s.text(x0 + wmax + 76, y + 18, label, 13.5, DIM if col != RED else TEXT, "start", 500)
        else:
            sep = "、" if langs.is_cjk(lang) and lang != "ko" else ", "  # Korean lists use commas
            half = (len(cargos) + 1) // 2
            for k, part in enumerate((cargos[:half], cargos[half:])):
                txt = sep.join(names.get(c, c) for c in part) + ("," if k == 0 and sep == ", " else "")
                s.text(x0 + wmax + 76, y + 9 + k * 15, txt, 12, DIM if col != RED else TEXT, "start", 500)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- delivery: town rating
T_RATE = {
    "en": {"cap": "The Delivery rating of a town from the share of deliveries on time over the last half year, "
                  "for three settings of Delivery Sensitivity.",
           "x": "deliveries on time (last half year)", "y": "Delivery rating",
           "lines": [("Low", 0.75, BLUE), ("Normal", 1.0, GOLD), ("Very High", 2.0, RED)],
           "pt": "90 % on time → 0.86"},
    "fr": {"cap": "La note Livraison d'une ville selon la part de livraisons à l'heure sur le dernier semestre, "
                  "pour trois réglages de Sensibilité aux livraisons.",
           "x": "livraisons à l'heure (dernier semestre)", "y": "note Livraison",
           "lines": [("Faible", 0.75, BLUE), ("Normale", 1.0, GOLD), ("Très élevée", 2.0, RED)],
           "pt": "90 % à l'heure → 0,86"},
    "de": {"cap": "Die Lieferungs-Bewertung einer Stadt aus dem Anteil pünktlicher Lieferungen im letzten Halbjahr, "
                  "für drei Stufen der Lieferungsempfindlichkeit.",
           "x": "pünktliche Lieferungen (letztes Halbjahr)", "y": "Lieferungs-Bewertung",
           "lines": [("Niedrig", 0.75, BLUE), ("Normal", 1.0, GOLD), ("Sehr hoch", 2.0, RED)],
           "pt": "90 % pünktlich → 0,86"},
}


def delivery_rating(lang):
    import math
    t = T_RATE[lang]
    s = Svg("dr", 900, 330)
    X0, Y0, W, H = 90, 270, 560, 220
    px = lambda f: X0 + f * W
    py = lambda r: Y0 - r * H
    s.rect(X0, Y0 - H, W, H, "#121921", r=10, stroke=LINE)
    for f in (0, .25, .5, .75, 1):
        s.add(f'<line x1="{px(f)}" y1="{Y0 - H}" x2="{px(f)}" y2="{Y0}" stroke="{LINE}" stroke-dasharray="2 5"/>')
        s.text(px(f), Y0 + 20, f"{int(f * 100)} %", 12, DIM)
    for r in (0, .5, 1):
        s.add(f'<line x1="{X0}" y1="{py(r)}" x2="{X0 + W}" y2="{py(r)}" stroke="{LINE}" stroke-dasharray="2 5"/>')
        s.text(X0 - 12, py(r) + 4, langs.num(r, lang), 12, DIM, "end")
    s.text(X0 + W / 2, Y0 + 46, t["x"], 13, TEXT, weight=600)
    s.add(f'<text font-size="13" font-weight="600" fill="{TEXT}" font-family="{FONT}" text-anchor="middle" '
          f'transform="translate({X0 - 52} {Y0 - H / 2}) rotate(-90)">{html.escape(t["y"])}</text>')
    for i, (lab, sens, col) in enumerate(t["lines"]):
        lo = 1 - math.exp(-0.35667 * sens)
        c = min(max(sens, 0), 1)
        hi = -1.2 * c * c + 2.2 * c
        pts = [(px(0), py(0)), (px(lo), py(0)), (px(min(hi, 1)), py(1)), (px(1), py(1))]
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        s.add(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{3.5 if sens == 1 else 2.5}" stroke-linejoin="round"/>')
        ly = 70 + i * 40
        s.rect(690, ly - 14, 26, 6, col, r=3)
        s.text(728, ly - 6, lab, 14, TEXT, "start", 700)
        s.text(728, ly + 12, f"0 → {int(round(lo * 100))} %, 1 ← {int(round(min(hi, 1) * 100))} %", 12, DIM, "start")
    fx, fy = px(.9), py((0.9 - 0.3) / 0.7)
    s.add(f'<circle cx="{fx}" cy="{fy}" r="7" fill="{GOLD}" stroke="{DEEP}" stroke-width="2"/>')
    s.chip(fx - 200, fy - 14, t["pt"], GOLD, h=26, size=13)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- towns: where XP comes from
T_TXP = {
    "en": {"cap": "Raw XP from your passengers and cargo, multiplied by the town's growth rate, fills the level bar; "
                  "each level makes the town bigger.",
           "src": [("person", "Passengers", "5 · 10 · 20 XP", "from the same town · a neighbour town · farther", GOLD),
                   ("truck", "Cargo unit", "10 · 20 · 40 XP", "by cargo tier 0 · 1 · 2", TEAL),
                   ("subsidies", "Subsidy reward", "% of the level", "some contracts, also × growth rate", VIOLET)],
           "mul": "× growth rate", "mul2": "0–100 %", "mul3": "Authority × Supplies", "hq": "+5 % per HQ part",
           "lv": "Town level", "lv2": "level 2 after 1,000 XP,", "lv3": "each next level × 1.5",
           "sz": "Town size", "sz2": "grows with the levels gained", "sz3": "since the start of the game",
           "not": "no XP: time passing, trips to industries, trips without your lines"},
    "fr": {"cap": "L'XP brute de tes passagers et de ton fret, multipliée par le taux de croissance de la ville, remplit la barre de niveau ; "
                  "chaque niveau agrandit la ville.",
           "src": [("person", "Passagers", "5 · 10 · 20 XP", "même ville · ville voisine · plus loin", GOLD),
                   ("truck", "Unité de fret", "10 · 20 · 40 XP", "selon le niveau du fret 0 · 1 · 2", TEAL),
                   ("subsidies", "Récompense de contrat", "% du niveau", "certains contrats, aussi × le taux", VIOLET)],
           "mul": "× taux de croissance", "mul2": "0–100 %", "mul3": "Autorité × Apports", "hq": "+5 % par partie du siège",
           "lv": "Niveau de la ville", "lv2": "niveau 2 après 1 000 XP,", "lv3": "chaque niveau suivant × 1,5",
           "sz": "Taille de la ville", "sz2": "grandit avec les niveaux gagnés", "sz3": "depuis le début de la partie",
           "not": "pas d'XP : le temps qui passe, les trajets vers les industries, les trajets sans tes lignes"},
    "de": {"cap": "Roh-XP aus deinen Passagieren und deiner Fracht, multipliziert mit der Wachstumsrate der Stadt, füllt den Stufenbalken; "
                  "jede Stufe macht die Stadt größer.",
           "src": [("person", "Passagiere", "5 · 10 · 20 XP", "gleiche Stadt · Nachbarstadt · weiter weg", GOLD),
                   ("truck", "Frachteinheit", "10 · 20 · 40 XP", "nach Frachtstufe 0 · 1 · 2", TEAL),
                   ("subsidies", "Subventionsbelohnung", "% der Stufe", "manche Aufträge, auch × Rate", VIOLET)],
           "mul": "× Wachstumsrate", "mul2": "0–100 %", "mul3": "Verwaltung × Versorgung", "hq": "+5 % pro HQ-Teil",
           "lv": "Stadtstufe", "lv2": "Stufe 2 nach 1.000 XP,", "lv3": "jede weitere Stufe × 1,5",
           "sz": "Stadtgröße", "sz2": "wächst mit den gewonnenen Stufen", "sz3": "seit Spielbeginn",
           "not": "keine XP: verstrichene Zeit, Fahrten zu Industrien, Fahrten ohne deine Linien"},
}


def town_xp(lang):
    t = T_TXP[lang]
    s = Svg("tx", 900, 350)
    for i, (ic, title, big, sub, col) in enumerate(t["src"]):
        y = 16 + i * 92
        s.card(16, y, 300, 78, stroke=col)
        s.icon_badge(54, y + 39, ic, col, 22)
        s.text(88, y + 26, title, 14, TEXT, "start", 700)
        s.text(88, y + 48, big, 15, col, "start", 800)
        s.text(88, y + 66, sub, 11.5, DIM, "start")
        s.flow(322, y + 39, 382, 140, col, 2.5)
    s.add(f'<circle cx="460" cy="140" r="74" fill="{s.ref("card")}" stroke="{GOLD}" stroke-width="2" filter="{s.ref("sh")}"/>')
    s.text(460, 118, t["mul"], 14 if width(t["mul"]) < 17 else 12, GOLD, weight=800)
    s.text(460, 146, t["mul2"], 22, TEXT, weight=800)
    s.text(460, 168, t["mul3"], 11.5, DIM)
    s.chip(460 - (width(t["hq"]) * 12 * .62 + 22) / 2, 226, t["hq"], VIOLET, size=12, h=24)
    s.flow(538, 140, 590, 140, GOLD, 3)
    s.card(598, 30, 286, 96, stroke=TEAL)
    s.text(618, 60, t["lv"], 15, TEAL, "start", 800)
    s.text(618, 84, t["lv2"], 12.5, TEXT, "start")
    s.text(618, 104, t["lv3"], 12.5, TEXT, "start")
    s.add(f'<line x1="741" y1="128" x2="741" y2="152" stroke="{TEAL}" stroke-width="2" marker-end="{s.ref("ah")}"/>')
    s.card(598, 156, 286, 96, stroke=LINE)
    s.text(618, 186, t["sz"], 15, TEXT, "start", 800)
    s.text(618, 210, t["sz2"], 12.5, DIM, "start")
    s.text(618, 230, t["sz3"], 12.5, DIM, "start")
    s.add(icons.place("cross", 30, 310, 14, RED, 2.5))
    s.text(52, 322, t["not"], 13, RED, "start", 600)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- towns: growth rate matrix
GROWTH_XP = [0, .2, .4, .6, .8, 1.0]


def _growth_index(auth, sup):
    """Growth level 0..5 from authority level 0..5 and supplies level (None = no deliveries); town_util.tl:607-633."""
    w = [1.4 ** i for i in range(6)]
    tot, acc, thr = sum(w), 0, []
    for x in w:
        acc += x / tot
        thr.append(acc)
    g = auth / 5 * (0 if sup is None else (sup + 1) / 6)
    for i, th in enumerate(thr):
        if g < th:
            return i
    return 5


T_GM = {
    "en": {"cap": "Growth rate (× on all XP) from the two ratings of the town window. Headquarters bonus on top.",
           "lv": ["Very Poor", "Poor", "Mediocre", "Good", "Very Good", "Excellent"], "none": "no deliveries",
           "sup": "Supplies", "auth": "Town Authority (lowest of 6 ratings)",
           "g": ["Stagnant", "Growing Very Slowly", "Growing Slowly", "Growing", "Growing Fast", "Growing Lightning Fast"]},
    "fr": {"cap": "Taux de croissance (× sur toute l'XP) selon les deux notes de la fenêtre de la ville. Bonus du siège social en plus.",
           "lv": ["Très insuffisant", "Insuffisant", "Médiocre", "Bon", "Très bon", "Excellent"], "none": "aucune livraison",
           "sup": "Apports", "auth": "Autorité municipale (la plus basse des 6 notes)",
           "g": ["Stagnante", "Croissance très lente", "Croissance lente", "En croissance", "Croissance rapide", "Croissance fulgurante"]},
    "de": {"cap": "Wachstumsrate (× auf alle XP) aus den zwei Wertungen des Stadtfensters. Hauptquartier-Bonus obendrauf.",
           "lv": ["Sehr schlecht", "Schlecht", "Mittelmässig", "Gut", "Sehr gut", "Ausgezeichnet"], "none": "keine Lieferungen",
           "sup": "Versorgung", "auth": "Stadtverwaltung (niedrigste der 6 Wertungen)",
           "g": ["Stagnierend", "Sehr Langsames Wachstum", "Langsames Wachstum", "Wachsend", "Schnell Wachsend", "Unfassbar schnell wachsend"]},
}
GM_COL = ["#5a2a2a", "#7a3f2c", "#8a6a2a", "#4f7a4a", "#2f8f80", "#38d1bf"]


def growth_matrix(lang):
    t = T_GM[lang]
    s = Svg("gm", 900, 470)
    X0, Y0, CW, RH = 250, 104, 88, 44
    cols = [None] + list(range(6))
    s.text(X0 + CW * 3.5, 24, t["sup"], 15, GOLD, weight=800)
    for j, c in enumerate(cols):
        lab = t["none"] if c is None else t["lv"][c]
        s.wrapped(X0 + j * CW + CW / 2, 66, lab, 14, 11.5, DIM if c is None else TEXT, "middle", 600)
    s.add(f'<text font-size="12.5" font-weight="800" fill="{TEAL}" font-family="{FONT}" text-anchor="middle" '
          f'transform="translate(30 {Y0 + RH * 3}) rotate(-90)">{html.escape(t["auth"])}</text>')
    for r in range(6):
        a = 5 - r
        y = Y0 + r * RH
        s.text(X0 - 14, y + RH / 2 + 5, t["lv"][a], 12.5, TEXT, "end", 600)
        for j, c in enumerate(cols):
            gi = _growth_index(a, c)
            x = X0 + j * CW
            s.rect(x + 2, y + 2, CW - 4, RH - 4, GM_COL[gi], r=6)
            s.text(x + CW / 2, y + RH / 2 + 5, f"{int(GROWTH_XP[gi] * 100)} %", 14, DEEP if gi >= 4 else TEXT, weight=800)
    ly = Y0 + 6 * RH + 30
    for k in range(6):
        x = 40 + (k % 3) * 285
        y = ly + (k // 3) * 32
        s.rect(x, y - 13, 18, 18, GM_COL[k], r=4)
        s.text(x + 28, y + 1, f"{int(GROWTH_XP[k] * 100)} %  {t['g'][k]}", 12.5, TEXT, "start", 500)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- towns: size per levels gained
T_TS = {
    "en": {"cap": "Target size of a town (all its districts together) compared with its size at the start, "
                  "by levels gained since then.",
           "x": "levels gained since the start", "y": "size × start", "rows": "levels gained → size"},
    "fr": {"cap": "Taille visée d'une ville (tous ses quartiers ensemble) comparée à sa taille au départ, "
                  "selon les niveaux gagnés depuis.",
           "x": "niveaux gagnés depuis le départ", "y": "taille × départ", "rows": "niveaux gagnés → taille"},
    "de": {"cap": "Zielgröße einer Stadt (alle Viertel zusammen) im Vergleich zu ihrer Größe am Anfang, "
                  "nach den seitdem gewonnenen Stufen.",
           "x": "gewonnene Stufen seit dem Start", "y": "Größe × Start", "rows": "gewonnene Stufen → Größe"},
}


def _size_factor(levels_gained):
    l = levels_gained + 1  # town_cargo_util.tl:107
    return 0.00930472 * l ** 3 - 0.08061382 * l ** 2 + 0.63330472 * l + 0.438


def town_size(lang):
    t = T_TS[lang]
    s = Svg("ts", 900, 320)
    X0, Y0, W, H = 80, 256, 540, 210
    px = lambda g: X0 + g / 17 * W
    py = lambda f: Y0 - (f - 1) / 39 * H
    fmt = lambda v: langs.num(v, lang, 1)
    s.rect(X0, Y0 - H, W, H, "#121921", r=10, stroke=LINE)
    for f in (1, 10, 20, 30, 40):
        s.add(f'<line x1="{X0}" y1="{py(f)}" x2="{X0 + W}" y2="{py(f)}" stroke="{LINE}" stroke-dasharray="2 5"/>')
        s.text(X0 - 10, py(f) + 4, f"×{f}", 12, DIM, "end")
    for g in (0, 4, 8, 12, 17):
        s.text(px(g), Y0 + 20, str(g), 12, DIM)
    s.text(X0 + W / 2, Y0 + 46, t["x"], 13, TEXT, weight=600)
    s.add(f'<text font-size="13" font-weight="600" fill="{TEXT}" font-family="{FONT}" text-anchor="middle" '
          f'transform="translate({X0 - 52} {Y0 - H / 2}) rotate(-90)">{html.escape(t["y"])}</text>')
    pts = [(px(g / 4), py(_size_factor(g / 4))) for g in range(0, 69)]
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    s.add(f'<path d="{d}" fill="none" stroke="{TEAL}" stroke-width="3.5" stroke-linejoin="round"/>')
    s.card(660, 40, 224, 216, stroke=TEAL)
    s.text(680, 70, t["rows"], 13, TEAL, "start", 800)
    for i, g in enumerate((1, 4, 8, 12, 17)):
        f = _size_factor(g)
        s.add(f'<circle cx="{px(g)}" cy="{py(f)}" r="5" fill="{GOLD}" stroke="{DEEP}" stroke-width="2"/>')
        y = 104 + i * 32
        s.text(690, y, f"+{g}", 15, TEXT, "start", 700)
        s.text(860, y, f"×{fmt(f)}", 15, GOLD, "end", 800)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- subsidies: life of a contract
T_SUBL = {
    "en": {"cap": "What happens to an offer and to an accepted contract. Money is scaled by the calendar year (×1 in 1900, ×4 from 2000).",
           "offer": "Offer", "offer2": "about 6 months to accept",
           "acc": "Accepted", "acc2": "upfront payment (or reputation)", "acc3": "deadline starts",
           "ok": "Fulfilled", "ok2": "reward: town experience, cash", "ok3": "or ×2 income for 5 years",
           "ko": "Deadline missed", "ko2": "upfront paid back", "ko3": "+ fine or reputation loss",
           "dec": "Declined: no penalty", "dec2": "next offer twice as fast",
           "miss": "Not accepted in time: no penalty", "max": "at most 5 accepted at once"},
    "fr": {"cap": "Ce que devient une offre et un contrat accepté. L'argent suit l'année du calendrier (×1 en 1900, ×4 dès 2000).",
           "offer": "Offre", "offer2": "environ 6 mois pour accepter",
           "acc": "Accepté", "acc2": "paiement d'avance (ou réputation)", "acc3": "le délai commence",
           "ok": "Rempli", "ok2": "récompense : expérience, argent", "ok3": "ou revenus ×2 pendant 5 ans",
           "ko": "Délai dépassé", "ko2": "avance remboursée", "ko3": "+ amende ou perte de réputation",
           "dec": "Refusé : aucune pénalité", "dec2": "offre suivante deux fois plus vite",
           "miss": "Pas accepté à temps : aucune pénalité", "max": "au plus 5 acceptés en même temps"},
    "de": {"cap": "Was aus einem Angebot und einem angenommenen Vertrag wird. Geld folgt dem Kalenderjahr (×1 im Jahr 1900, ×4 ab 2000).",
           "offer": "Angebot", "offer2": "etwa 6 Monate zum Annehmen",
           "acc": "Angenommen", "acc2": "Vorauszahlung (oder Ruf)", "acc3": "die Frist beginnt",
           "ok": "Erfüllt", "ok2": "Belohnung: Erfahrung, Geld", "ok3": "oder ×2 Einnahmen für 5 Jahre",
           "ko": "Frist verpasst", "ko2": "Vorauszahlung zurück", "ko3": "+ Strafe oder Rufverlust",
           "dec": "Abgelehnt: keine Strafe", "dec2": "nächstes Angebot doppelt so schnell",
           "miss": "Nicht rechtzeitig angenommen: keine Strafe", "max": "höchstens 5 gleichzeitig angenommen"},
}


def subsidy_life(lang):
    t = T_SUBL[lang]
    s = Svg("sl", 900, 330)
    # offer
    s.card(16, 96, 200, 116, stroke=GOLD)
    s.icon_badge(56, 136, "subsidies", GOLD, 22)
    s.text(88, 132, t["offer"], 17, GOLD, "start", 800)
    s.lines(116, 176, wrap_rows(t["offer2"], 24), 12.5, DIM)
    # accepted
    s.flow(222, 154, 300, 154, GOLD, 3)
    s.card(306, 96, 250, 116, stroke=TEAL)
    s.icon_badge(346, 136, "check", TEAL, 22)
    s.text(378, 132, t["acc"], 17, TEAL, "start", 800)
    s.text(431, 170, t["acc2"], 12.5, TEXT)
    s.text(431, 190, t["acc3"], 12.5, DIM)
    # fulfilled / missed
    s.flow(562, 130, 628, 70, TEAL, 3)
    s.flow(562, 178, 628, 236, RED, 3)
    s.card(634, 16, 250, 104, stroke=TEAL)
    s.text(654, 46, t["ok"], 16, TEAL, "start", 800)
    s.text(654, 72, t["ok2"], 12.5, TEXT, "start")
    s.text(654, 92, t["ok3"], 12.5, GOLD, "start", 700)
    s.card(634, 190, 250, 104, stroke=RED)
    s.text(654, 220, t["ko"], 16, RED, "start", 800)
    s.text(654, 246, t["ko2"], 12.5, TEXT, "start")
    s.text(654, 266, t["ko3"], 12.5, RED, "start", 700)
    # no-penalty exits of an offer
    s.add(f'<path d="M116 92 L116 40" stroke="{DIM}" stroke-width="2" stroke-dasharray="4 4" marker-end="{s.ref("ah")}"/>')
    s.text(128, 30, t["dec"], 13, TEXT, "start", 700)
    s.text(128, 48, t["dec2"], 12, DIM, "start")
    s.add(f'<path d="M116 216 L116 262" stroke="{DIM}" stroke-width="2" stroke-dasharray="4 4" marker-end="{s.ref("ah")}"/>')
    s.text(128, 284, t["miss"], 13, TEXT, "start", 700)
    s.chip(431 - (width(t["max"]) * 12 * .62 + 22) / 2, 226, t["max"], VIOLET, size=12, h=24)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- subsidies: the four types
T_SUBT = {
    "en": {"cap": "The four contract types of a free game, what completes them and what they can give. Amounts at Subsidies Risk Fair.",
           "types": [("industries", "Supply Industry", "an industry that never produced", "deliver 50–100 of its inputs", "×2 income", GOLD),
                     ("towns", "Supply Town", "a cargo the town lacks", "deliver 30–100 of it", "experience or cash, ×2", TEAL),
                     ("person", "Connect Towns", "two towns, one line", "one passenger, no transfer", "experience in both, ×2", BLUE),
                     ("person", "Transport Workers", "an industry with workers", "reach its workers boost", "cash", VIOLET)],
           "need": "to complete", "get": "on fulfillment"},
    "fr": {"cap": "Les quatre types de contrats d'une partie libre, ce qui les remplit et ce qu'ils peuvent donner. Quantités au risque Équitable.",
           "types": [("industries", "Approvisionner l'industrie", "une industrie qui n'a jamais produit", "livrer 50 à 100 de ses intrants", "revenus ×2", GOLD),
                     ("towns", "Approvisionner la ville", "un fret qui manque à la ville", "en livrer 30 à 100", "expérience ou argent, ×2", TEAL),
                     ("person", "Relier des villes", "deux villes, une ligne", "un passager, sans correspondance", "expérience aux deux, ×2", BLUE),
                     ("person", "Transporter des travailleurs", "une industrie avec emplois", "atteindre son bonus", "argent", VIOLET)],
           "need": "pour remplir", "get": "à la réalisation"},
    "de": {"cap": "Die vier Vertragsarten eines freien Spiels, was sie erfüllt und was sie bringen können. Mengen bei Subventionsrisiko Fair.",
           "types": [("industries", "Industrie beliefern", "eine Industrie, die nie produziert hat", "50–100 ihrer Rohstoffe liefern", "×2 Einnahmen", GOLD),
                     ("towns", "Stadt versorgen", "eine Fracht, die der Stadt fehlt", "30–100 davon liefern", "Erfahrung oder Geld, ×2", TEAL),
                     ("person", "Städte verbinden", "zwei Städte, eine Linie", "ein Passagier, ohne Umstieg", "Erfahrung in beiden, ×2", BLUE),
                     ("person", "Transportiere Arbeiter", "eine Industrie mit Arbeitsplätzen", "ihren Arbeiterbonus erreichen", "Geld", VIOLET)],
           "need": "zum Erfüllen", "get": "bei Erfüllung"},
}


def subsidy_types(lang):
    t = T_SUBT[lang]
    s = Svg("st", 900, 300)
    w, g = 206, 18  # 4 cards + 3 gaps = 878, inside the 900 viewBox
    for i, (ic, title, target, need, get, col) in enumerate(t["types"]):
        x = 11 + i * (w + g)
        s.card(x, 14, w, 272, stroke=col)
        s.icon_badge(x + w / 2, 52, ic, col, 24)
        rows = wrap_rows(title, 22)
        s.lines(x + w / 2, 100, rows, 15, col, weight=800, gap=1.25)
        y = 100 + len(rows) * 19
        s.lines(x + w / 2, y + 4, wrap_rows(target, 28), 12, DIM)
        s.text(x + w / 2, 182, t["need"], 11, DIM, weight=700, spacing=.5)
        s.lines(x + w / 2, 202, wrap_rows(need, 26), 13, TEXT, weight=600)
        s.text(x + w / 2, 244, t["get"], 11, DIM, weight=700, spacing=.5)
        s.text(x + w / 2, 266, get, 13 if width(get) < 26 else 11.5, GOLD, weight=700)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- costs: what follows the calendar year
T_CYEAR = {
    "en": {"cap": "Factors set by the calendar year in the scripts. Income has none; the Inflation setting only lowers income with "
                  "the company rank.",
           "x": "calendar year", "up": "upkeep of warehouses, harbours, airports", "sub": "subsidy cash",
           "loan": "loan amounts", "inc": "cargo and passenger income"},
    "fr": {"cap": "Facteurs fixés par l'année du calendrier dans les scripts. Les revenus n'en ont aucun ; le réglage Inflation ne fait "
                  "que baisser les revenus avec le rang de l'entreprise.",
           "x": "année du calendrier", "up": "entretien des entrepôts, ports, aéroports", "sub": "argent des contrats",
           "loan": "montant des emprunts", "inc": "revenus du fret et des passagers"},
    "de": {"cap": "Faktoren, die in den Skripten vom Kalenderjahr abhängen. Einnahmen haben keinen; die Einstellung Inflation senkt "
                  "nur die Einnahmen mit dem Firmenrang.",
           "x": "Kalenderjahr", "up": "Unterhalt von Lagern, Häfen, Flughäfen", "sub": "Geld aus Subventionen",
           "loan": "Darlehensbeträge", "inc": "Einnahmen aus Fracht und Passagieren"},
}


def cost_years(lang):
    t = T_CYEAR[lang]
    s = Svg("cy", 900, 330)
    X0, Y0, W, H = 70, 280, 560, 240
    px = lambda y: X0 + (y - 1900) / 120 * W
    py = lambda f: Y0 - f / 6 * H
    s.rect(X0, Y0 - H, W, H, "#121921", r=10, stroke=LINE)
    for y in range(1900, 2021, 20):
        s.add(f'<line x1="{px(y)}" y1="{Y0 - H}" x2="{px(y)}" y2="{Y0}" stroke="{LINE}" stroke-dasharray="2 5"/>')
        s.text(px(y), Y0 + 20, str(y), 12, DIM)
    for f in range(0, 7):
        s.add(f'<line x1="{X0}" y1="{py(f)}" x2="{X0 + W}" y2="{py(f)}" stroke="{LINE}" stroke-dasharray="2 5"/>')
        s.text(X0 - 10, py(f) + 4, f"×{f}", 12, DIM, "end")
    s.text(X0 + W / 2, Y0 + 42, t["x"], 13, TEXT, weight=600)
    import math
    fx = lambda f: "×" + (str(int(f)) if f == int(f) else langs.num(f, lang))
    up = [(1900, 1), (1920, 1.5), (1940, 2.2), (1960, 3.2), (1980, 4), (2000, 5), (2020, 6)]
    lo, hi = math.log2(0.4), math.log2(2.4)  # loan_util.tl:7-10
    loan = [(y, 2 ** (lo + (y - 1900) / 120 * (hi - lo))) for y in range(1900, 2021, 10)]
    series = [
        (t["up"], GOLD, up, True, "×1 → ×6"),
        (t["sub"], VIOLET, [(1900, 1), (2000, 4), (2020, 4)], False, "×1 → ×4"),
        (t["loan"], BLUE, loan, False, f"{fx(0.4)} → {fx(2.4)}"),
        (t["inc"], TEAL, [(1900, 1), (2020, 1)], False, "×1"),
    ]
    for i, (lab, col, pts, dots, rng) in enumerate(series):
        d = "M" + " L".join(f"{px(x):.1f} {py(f):.1f}" for x, f in pts)
        dash = "" if dots else ' stroke-dasharray="7 5"'
        s.add(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{3.5 if dots else 2.5}" stroke-linejoin="round"{dash}/>')
        if dots:
            for x, f in pts:
                s.add(f'<circle cx="{px(x):.1f}" cy="{py(f):.1f}" r="5" fill="{col}" stroke="{DEEP}" stroke-width="2"/>')
                s.text(px(x) - (10 if x == 2020 else 0), py(f) - 12, fx(f), 11.5, col, weight=700)
        ly = 64 + i * 56
        s.rect(660, ly - 10, 26, 6, col, r=3)
        rows = wrap_rows(lab, 26)
        s.lines(698, ly - 3, rows, 13, TEXT, "start", gap=1.3, weight=600)
        s.text(698, ly - 3 + len(rows) * 17, rng, 12, col, "start", 700)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- costs: a loan's interest
T_LOAN = {
    "en": {"cap": "Example: 40 M at 8 %. The interest is 8 % of the amount once, whatever the term, paid month by month with the "
                  "principal. Repaying early drops the interest still to come.",
           "short": "5 years", "long": "12 years", "inside": "40 M + 3.2 M interest",
           "py1": "3.2 M ÷ 5 = 0.64 M interest per year", "py2": "3.2 M ÷ 12 = 0.27 M interest per year",
           "rep": "Repay after 3 years: 30 M left to pay", "drop": "remaining interest (2.4 M): dropped",
           "same": "same total interest"},
    "fr": {"cap": "Exemple : 40 M à 8 %. L'intérêt vaut une seule fois 8 % du montant, quelle que soit la durée, payé mois par mois "
                  "avec le capital. Rembourser plus tôt supprime les intérêts restants.",
           "short": "5 ans", "long": "12 ans", "inside": "40 M + 3,2 M d'intérêts",
           "py1": "3,2 M ÷ 5 = 0,64 M d'intérêts par an", "py2": "3,2 M ÷ 12 = 0,27 M d'intérêts par an",
           "rep": "Rembourser après 3 ans : 30 M restent à payer", "drop": "intérêts restants (2,4 M) : supprimés",
           "same": "même total d'intérêts"},
    "de": {"cap": "Beispiel: 40 M zu 8 %. Die Zinsen sind einmal 8 % des Betrags, unabhängig von der Laufzeit, Monat für Monat mit "
                  "der Tilgung bezahlt. Vorzeitiges Zurückzahlen streicht die noch ausstehenden Zinsen.",
           "short": "5 Jahre", "long": "12 Jahre", "inside": "40 M + 3,2 M Zinsen",
           "py1": "3,2 M ÷ 5 = 0,64 M Zinsen pro Jahr", "py2": "3,2 M ÷ 12 = 0,27 M Zinsen pro Jahr",
           "rep": "Nach 3 Jahren zurückzahlen: 30 M noch offen", "drop": "restliche Zinsen (2,4 M): gestrichen",
           "same": "gleiche Zinsen insgesamt"},
}


def loan_interest(lang):
    t = T_LOAN[lang]
    s = Svg("li", 900, 300)
    X0, PER = 130, 52  # px per year
    rows = ((t["short"], 5, t["py1"]), (t["long"], 12, t["py2"]))
    for i, (lab, years, note) in enumerate(rows):
        y = 44 + i * 114
        s.text(X0 - 16, y + 24, lab, 15, TEXT, "end", 800)
        s.text(X0, y - 10, t["inside"], 13, TEXT, "start", 700)
        w = years * PER
        s.rect(X0, y, w, 38, s.ref("teal"), r=9)
        s.rect(X0, y, w, 7, GOLD, r=3)
        for k in range(1, years):
            s.add(f'<line x1="{X0 + k * PER}" y1="{y + 8}" x2="{X0 + k * PER}" y2="{y + 38}" stroke="{DEEP}" stroke-opacity=".35"/>')
        s.text(X0, y + 60, note, 13, GOLD, "start", 700)
    # repay early on the long loan
    rx, ry = X0 + 3 * PER, 158
    s.add(f'<rect x="{rx}" y="{ry}" width="{9 * PER}" height="38" rx="9" fill="{DEEP}" fill-opacity=".6" '
          f'stroke="{RED}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    s.add(f'<line x1="{rx}" y1="{ry}" x2="{rx}" y2="{ry + 38}" stroke="{RED}" stroke-width="3"/>')
    s.text(rx + 14, ry + 25, t["drop"], 12.5, RED, "start", 700)
    s.text(rx + 14, 286, t["rep"], 13, TEXT, "start", 700)
    s.add(f'<line x1="{rx}" y1="{ry + 40}" x2="{rx}" y2="{281}" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 3"/>')
    s.chip(X0 + 5 * PER + 20, 51, t["same"], GOLD, size=12, h=24)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- reputation: a penalty and its recovery
T_REP = {
    "en": {"cap": "Example: terrain work costs 40 %. Reputation comes back by itself at about 67 % a year (the window says 33 %); "
                  "a Marketing Campaign makes it about 200 % a year while it runs. Six levels, as for every rating.",
           "x": "years", "hit": "terrain work −40 %", "camp": "Marketing Campaign", "slow": "≈ 67 % a year",
           "fast": "≈ 200 % a year", "noc": "without campaign"},
    "fr": {"cap": "Exemple : des travaux de terrain coûtent 40 %. La réputation revient seule à environ 67 % par an (la fenêtre dit 33 %) ; une campagne "
                  "marketing la fait revenir à environ 200 % par an tant qu'elle dure. Six niveaux, comme pour chaque note.",
           "x": "années", "hit": "travaux de terrain −40 %", "camp": "Campagne marketing", "slow": "≈ 67 % par an",
           "fast": "≈ 200 % par an", "noc": "sans campagne"},
    "de": {"cap": "Beispiel: Geländearbeiten kosten 40 %. Der Ruf kommt von selbst mit etwa 67 % pro Jahr zurück (das Fenster zeigt 33 %); "
                  "eine Marketingkampagne macht daraus etwa 200 % pro Jahr, solange sie läuft. Sechs Stufen wie bei jeder Wertung.",
           "x": "Jahre", "hit": "Geländearbeiten −40 %", "camp": "Marketingkampagne", "slow": "≈ 67 % pro Jahr",
           "fast": "≈ 200 % pro Jahr", "noc": "ohne Kampagne"},
}


def rep_recovery(lang):
    t = T_REP[lang]
    lv = T_GM[lang]["lv"]
    s = Svg("rr", 900, 330)
    X0, Y0, W, H = 70, 270, 600, 240
    px = lambda yr: X0 + yr * W  # one year wide: recovery is fast
    py = lambda v: Y0 - v * H
    s.rect(X0, Y0 - H, W, H, "#121921", r=10, stroke=LINE)
    for i in range(6):  # six levels: floor(value * 6), town_util.tl:983-985
        y0, y1 = py((i + 1) / 6), py(i / 6)
        s.rect(X0 + 1, y0, W - 2, y1 - y0, GM_COL[i], r=0, opacity=.22)
        s.text(X0 + W + 12, (y0 + y1) / 2 + 4, lv[i], 12, TEXT if i >= 3 else DIM, "start", 600)
    for yr in (0, .25, .5, .75, 1):
        s.add(f'<line x1="{px(yr)}" y1="{Y0 - H}" x2="{px(yr)}" y2="{Y0}" stroke="{LINE}" stroke-dasharray="2 5"/>')
        s.text(px(yr), Y0 + 20, langs.num(yr, lang) if yr != int(yr) else str(int(yr)), 12, DIM)
    for v in (0, .5, 1):
        s.text(X0 - 10, py(v) + 4, f"{int(v * 100)} %", 12, DIM, "end")
    s.text(X0 + W / 2, Y0 + 44, t["x"], 13, TEXT, weight=600)
    # campaign window: from 0.3, lasts one year (runs past the right edge)
    s.rect(px(.3), Y0 - H + 1, px(1) - px(.3), H - 2, VIOLET, r=0, opacity=.10)
    s.chip(px(.3) + 8, Y0 - 30, t["camp"], VIOLET, size=12, h=22)
    # hit at 0.1; campaign from 0.3: +2 per year (measured) -> full at 0.43
    R4 = .6 + .2 * 2 / 3
    d = (f"M{px(0):.1f} {py(1):.1f} L{px(.1):.1f} {py(1):.1f} L{px(.1):.1f} {py(.6):.1f} L{px(.3):.1f} {py(R4):.1f} "
         f"L{px(.3 + (1 - R4) / 2):.1f} {py(1):.1f} L{px(1):.1f} {py(1):.1f}")
    # without campaign (dashed): +2/3 per year (measured) -> full at 0.7
    s.add(f'<path d="M{px(.3):.1f} {py(R4):.1f} L{px(.7):.1f} {py(1):.1f}" fill="none" stroke="{DIM}" '
          f'stroke-width="2" stroke-dasharray="6 5"/>')
    s.text(px(.7) + 6, py(1) + 18, t["noc"], 11.5, DIM, "start", 600)
    s.add(f'<path d="{d}" fill="none" stroke="{GOLD}" stroke-width="3.5" stroke-linejoin="round"/>')
    s.add(f'<circle cx="{px(.1):.1f}" cy="{py(.6):.1f}" r="5" fill="{RED}" stroke="{DEEP}" stroke-width="2"/>')
    s.text(px(.1) + 10, py(.6) + 22, t["hit"], 12.5, RED, "start", 700)
    s.text(px(.28), py(.8), t["slow"], 12, GOLD, "end", 700)
    s.text(px(.44) + 8, py(.9), t["fast"], 12, VIOLET, "start", 700)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- industries: closure of an unused industry
T_ICLOSE = {
    "en": {"cap": "An unused industry: 5 years without loading or consumption make it a candidate; each year it may then be marked "
                  "(1.1 % at Rarely, 8.8 % at Very Often); the countdown lasts 2 years. One load or consumption resets everything.",
           "x": "years", "last": "last load or consumption", "cand": "candidate", "roll": "marked by chance each year",
           "count": "countdown 730 days", "gone": "removed", "save": "one load or consumption: saved"},
    "fr": {"cap": "Une industrie inutilisée : 5 ans sans chargement ni consommation en font une candidate ; chaque année elle peut alors "
                  "être marquée (1,1 % à Rarement, 8,8 % à Très souvent) ; le compte à rebours dure 2 ans. Un seul chargement ou une "
                  "consommation remet tout à zéro.",
           "x": "années", "last": "dernier chargement ou consommation", "cand": "candidate", "roll": "marquée au hasard chaque année",
           "count": "compte à rebours 730 jours", "gone": "supprimée", "save": "un chargement ou une consommation : sauvée"},
    "de": {"cap": "Eine ungenutzte Industrie: 5 Jahre ohne Verladen oder Verbrauch machen sie zum Kandidaten; danach kann sie jedes Jahr "
                  "markiert werden (1,1 % bei Selten, 8,8 % bei Sehr oft); der Countdown dauert 2 Jahre. Ein einziges Verladen oder "
                  "ein Verbrauch setzt alles zurück.",
           "x": "Jahre", "last": "letztes Verladen oder Verbrauch", "cand": "Kandidat", "roll": "jedes Jahr zufällig markiert",
           "count": "Countdown 730 Tage", "gone": "entfernt", "save": "einmal verladen oder verbraucht: gerettet"},
}


def ind_closure(lang):
    t = T_ICLOSE[lang]
    s = Svg("ic", 900, 300)
    X0, PER, Y = 40, 80, 150  # px per year
    px = lambda yr: X0 + yr * PER
    # phases: unused 0-5, waiting for the draw 5-7.5, countdown 7.5-9.5
    s.rect(px(0), Y - 22, px(5) - px(0), 44, "#1c2430", r=10, stroke=LINE)
    s.rect(px(5), Y - 22, px(7.5) - px(5), 44, GOLD, r=0, opacity=.18)
    s.rect(px(7.5), Y - 22, px(9.5) - px(7.5), 44, RED, r=0, opacity=.28)
    for yr in range(0, 11):
        s.add(f'<line x1="{px(yr)}" y1="{Y + 24}" x2="{px(yr)}" y2="{Y + 32}" stroke="{DIM}"/>')
        s.text(px(yr), Y + 50, str(yr), 12, DIM)
    s.text(px(5), Y + 74, t["x"], 13, TEXT, weight=600)
    s.add(f'<circle cx="{px(0)}" cy="{Y}" r="7" fill="{TEAL}" stroke="{DEEP}" stroke-width="2"/>')
    s.text(px(0) - 6, Y - 40, t["last"], 13, TEAL, "start", 700)
    s.add(f'<line x1="{px(5)}" y1="{Y - 34}" x2="{px(5)}" y2="{Y + 24}" stroke="{GOLD}" stroke-width="2.5"/>')
    s.chip(px(5) - 8, Y - 70, t["cand"], GOLD, size=12, h=24)
    s.text(px(6.25), Y + 5, "?", 18, GOLD, weight=800)
    s.lines(px(6.25), Y - 86, wrap_rows(t["roll"], 20), 12, GOLD, gap=1.3, weight=600)
    s.add(f'<line x1="{px(7.5)}" y1="{Y - 34}" x2="{px(7.5)}" y2="{Y + 24}" stroke="{RED}" stroke-width="2.5"/>')
    s.text(px(8.5), Y + 5, t["count"], 12, TEXT, weight=700)
    s.icon_badge(px(10), Y, "industries", RED, 20)
    s.text(px(10), Y - 34, t["gone"], 13, RED, weight=800)
    # saved: dashed return arrow from the countdown back to the start
    s.add(f'<path d="M{px(8.5)} {Y + 90} C {px(8.5)} {Y + 130}, {px(0)} {Y + 130}, {px(0)} {Y + 14}" fill="none" stroke="{TEAL}" '
          f'stroke-width="2" stroke-dasharray="5 4" marker-end="{s.ref("ah")}"/>')
    s.text(px(4.2), Y + 136, t["save"], 13, TEAL, weight=700)
    return s.svg(), t["cap"]


def _load_translations():
    """Diagram texts and cargo names of the languages kept in i18n/<code>.json."""
    for code in langs.translated():
        t = langs.texts(code)
        for name, table in t.get("diagrams", {}).items():
            globals()[name][code] = table
        if "cargo" in t:
            CARGO_NAMES[code] = t["cargo"]


_load_translations()

REGISTRY = {
    "town_xp": town_xp,
    "growth_matrix": growth_matrix,
    "town_size": town_size,
    "income_formula": income_formula,
    "income_distance": income_distance,
    "income_split": income_split,
    "delivery_times": delivery_times,
    "delivery_rating": delivery_rating,
    "workers_flow": workers_flow,
    "workers_window": workers_window,
    "loading_factors": loading_factors,
    "loading_sections": loading_sections,
    "subsidy_life": subsidy_life,
    "subsidy_types": subsidy_types,
    "cost_years": cost_years,
    "loan_interest": loan_interest,
    "rep_recovery": rep_recovery,
    "ind_closure": ind_closure,
}


def render(name, lang):
    if name not in REGISTRY:
        raise KeyError(f"unknown diagram {name!r}")
    return REGISTRY[name](lang)
