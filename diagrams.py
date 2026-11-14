"""SVG diagrams of the wiki, one function per diagram, texts per language.

render(name, lang) -> (svg markup, caption).
Every diagram gets its own id prefix, so several diagrams can sit on one page.
"""
import html

import icons

GOLD, TEAL, RED, DIM, TEXT, PANEL, LINE, VIOLET, BLUE = (
    "#f2b84b", "#38d1bf", "#f0705f", "#8f9bab", "#eef1f5", "#161c24", "#2a3340", "#b49cf0", "#5aa9ff")
DEEP = "#0f141b"
FONT = "Inter,Segoe UI Variable,Segoe UI,system-ui,sans-serif"


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
        w = w or (len(label) * size * 0.62 + 22)
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
        if len(s) <= width_chars:
            self.text(x, y + size * .35, s, size, color, anchor, weight)
            return
        cut = s.rfind(" ", 0, width_chars)
        cut = cut if cut > 0 else width_chars
        self.text(x, y - size * .35, s[:cut], size, color, anchor, weight)
        self.text(x, y + size * 1.05, s[cut:].strip(), size, color, anchor, weight)

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
    s.text(300 + len(t["rule"]) * 10.5, 440, t["eff"], 14.5, DEEP, "start", 500)
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


REGISTRY = {
    "workers_flow": workers_flow,
    "workers_window": workers_window,
    "loading_factors": loading_factors,
    "loading_sections": loading_sections,
}


def render(name, lang):
    if name not in REGISTRY:
        raise KeyError(f"unknown diagram {name!r}")
    return REGISTRY[name](lang)
