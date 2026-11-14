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
    w, g = 158, 27
    for i, (big, title, sub, col) in enumerate(t["c"]):
        x = 6 + i * (w + g)
        optional = i >= 3
        s.card(x, 20, w, 170, stroke=col if not optional else LINE, dash="6 5" if optional else None)
        s.text(x + w / 2, 70, big, 25 if len(big) < 6 else 19, col, weight=800)
        s.text(x + w / 2, 108, title, 14, TEXT, weight=700)
        words, line, rows = sub.split(), "", []
        for wd in words:
            if len(line) + len(wd) + 1 > 21 and line:
                rows.append(line)
                line = wd
            else:
                line = (line + " " + wd).strip()
        rows.append(line)
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
    "en": {"cap": "Paid: the straight line from where the cargo was picked up to where it is delivered, plus 8 m per metre of climb. "
                  "The real route only costs (maintenance).",
           "a": "origin", "b": "destination", "paid": "paid: straight line (3D)", "real": "real route: not paid, costs maintenance",
           "climb": "climb h", "bonus": "+ 8 × h paid", "ex1": "5 km, 100 m higher", "ex2": "paid as 5.8 km (+16 %)",
           "down": "the other way round: no bonus, no malus"},
    "fr": {"cap": "Payé : la ligne droite entre l'endroit où le fret a été pris et celui où il est livré, plus 8 m par mètre de montée. "
                  "Le vrai trajet ne fait que coûter (entretien).",
           "a": "départ", "b": "destination", "paid": "payé : ligne droite (3D)", "real": "vrai trajet : pas payé, coûte l'entretien",
           "climb": "montée h", "bonus": "+ 8 × h payés", "ex1": "5 km, 100 m plus haut", "ex2": "payé comme 5,8 km (+16 %)",
           "down": "dans l'autre sens : ni bonus, ni malus"},
    "de": {"cap": "Bezahlt wird die Luftlinie vom Abholort bis zum Lieferort, plus 8 m pro Meter Steigung. "
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
        rel = f"×{sec / 900:.2f}".rstrip("0").rstrip(".")
        if lang != "en":
            rel = rel.replace(".", ",")
        s.text(x0 + wmax + 12, y + 18, rel, 14, TEXT, "start", 800)
        label = ", ".join(names.get(c, c) for c in cargos)
        s.text(x0 + wmax + 76, y + 18, label, 13.5, DIM if col != RED else TEXT, "start", 500)
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
        s.text(X0 - 12, py(r) + 4, str(r).replace(".", ",") if lang != "en" else str(r), 12, DIM, "end")
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
    s.text(460, 118, t["mul"], 14 if len(t["mul"]) < 17 else 12, GOLD, weight=800)
    s.text(460, 146, t["mul2"], 22, TEXT, weight=800)
    s.text(460, 168, t["mul3"], 11.5, DIM)
    s.chip(460 - (len(t["hq"]) * 12 * .62 + 22) / 2, 226, t["hq"], VIOLET, size=12, h=24)
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
    fmt = (lambda v: f"{v:.1f}") if lang == "en" else (lambda v: f"{v:.1f}".replace(".", ","))
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


REGISTRY = {
    "town_xp": town_xp,
    "growth_matrix": growth_matrix,
    "town_size": town_size,
    "income_formula": income_formula,
    "income_distance": income_distance,
    "delivery_times": delivery_times,
    "delivery_rating": delivery_rating,
    "workers_flow": workers_flow,
    "workers_window": workers_window,
    "loading_factors": loading_factors,
    "loading_sections": loading_sections,
}


def render(name, lang):
    if name not in REGISTRY:
        raise KeyError(f"unknown diagram {name!r}")
    return REGISTRY[name](lang)
