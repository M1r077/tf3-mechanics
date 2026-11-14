"""SVG diagrams of the wiki, one function per diagram, texts per language.

render(name, lang) -> (svg markup, caption).
Kept simple on purpose (rectangles, arrows, text) so the same description can later be rasterised for images.
"""
import html

GOLD, TEAL, RED, DIM, TEXT, PANEL, LINE, VIOLET = (
    "#e8b13a", "#3cc2b4", "#e0675a", "#9aa4ad", "#e6e9ec", "#1d2329", "#2e363e", "#b9a0e6")


class Svg:
    def __init__(self, w, h):
        self.w, self.h, self.parts = w, h, []
        self.parts.append(
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs>')

    def box(self, x, y, w, h, fill=PANEL, stroke=LINE, r=8, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"{d}/>')

    def text(self, x, y, s, size=16, color=TEXT, anchor="middle", weight="normal"):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" '
                          f'font-weight="{weight}" font-family="Segoe UI,system-ui,sans-serif">{html.escape(s)}</text>')

    def lines(self, x, y, rows, size=15, color=TEXT, anchor="middle", gap=1.35, weight="normal"):
        for i, s in enumerate(rows):
            self.text(x, y + i * size * gap, s, size, color, anchor, weight)

    def arrow(self, x1, y1, x2, y2, color=GOLD, width=3, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"{d} marker-end="url(#ah)"/>')

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" '
                f'role="img">{"".join(self.parts)}</svg>')


# ---------------------------------------------------------------- workers: assignment vs boost
T_WORKERS = {
    "en": {
        "cap": "Two different counts: the residents the game assigns to the industry, and the arrivals that count for the boost.",
        "home": "Home", "home2": ["in a town"], "lines": "Your passenger lines", "lines2": ["walking and car", "not allowed"],
        "ind": "Industry", "ind2": ["20 workplaces"],
        "a": "Assigned", "a2": ["residents whose job", "is this industry", "(workplaces bar)"],
        "b": "Counted for the boost", "b2": ["arrivals by your lines", "in the last 2 game years,", "the latest 20 kept"],
        "rule": "Boost when counted ≥ 50 % of the workplaces (10 of 20)",
        "eff": "Production × 1.5 to 2.5 (fixed per industry)",
    },
    "fr": {
        "cap": "Deux comptes différents : les habitants que le jeu attribue à l'industrie, et les arrivées qui comptent pour le bonus.",
        "home": "Logement", "home2": ["dans une ville"], "lines": "Tes lignes de passagers", "lines2": ["à pied et en voiture", "interdit"],
        "ind": "Industrie", "ind2": ["20 emplois"],
        "a": "Attribués", "a2": ["habitants dont l'emploi", "est cette industrie", "(jauge des emplois)"],
        "b": "Comptés pour le bonus", "b2": ["arrivées par tes lignes", "sur les 2 dernières années,", "les 20 dernières gardées"],
        "rule": "Bonus quand les comptés ≥ 50 % des emplois (10 sur 20)",
        "eff": "Production × 1,5 à 2,5 (fixe pour chaque industrie)",
    },
    "de": {
        "cap": "Zwei verschiedene Zählungen: die Einwohner, die das Spiel der Industrie zuteilt, und die Ankünfte, die für den Bonus zählen.",
        "home": "Wohnung", "home2": ["in einer Stadt"], "lines": "Deine Personenlinien", "lines2": ["zu Fuß und mit dem Auto", "nicht erlaubt"],
        "ind": "Industrie", "ind2": ["20 Arbeitsplätze"],
        "a": "Zugeteilt", "a2": ["Einwohner, deren Arbeit", "diese Industrie ist", "(Arbeitsplatzanzeige)"],
        "b": "Für den Bonus gezählt", "b2": ["Ankünfte mit deinen Linien", "in den letzten 2 Spieljahren,", "die letzten 20 behalten"],
        "rule": "Bonus, wenn Gezählte ≥ 50 % der Arbeitsplätze (10 von 20)",
        "eff": "Produktion × 1,5 bis 2,5 (pro Industrie fest)",
    },
}


def workers_flow(lang):
    t = T_WORKERS[lang]
    s = Svg(900, 430)
    s.box(20, 40, 170, 110)
    s.text(105, 85, t["home"], 20, weight="bold")
    s.lines(105, 112, t["home2"], 14, DIM)
    s.box(330, 40, 240, 110, stroke=GOLD)
    s.text(450, 85, t["lines"], 18, GOLD, weight="bold")
    s.lines(450, 112, t["lines2"], 14, DIM)
    s.box(710, 40, 170, 110)
    s.text(795, 85, t["ind"], 20, weight="bold")
    s.lines(795, 112, t["ind2"], 14, DIM)
    s.arrow(190, 95, 326, 95)
    s.arrow(570, 95, 706, 95)
    # two counters
    s.box(150, 200, 280, 130, stroke=DIM, dash="6 5")
    s.text(290, 232, t["a"], 18, TEXT, weight="bold")
    s.lines(290, 260, t["a2"], 14, DIM)
    s.box(470, 200, 280, 130, stroke=TEAL)
    s.text(610, 232, t["b"], 18, TEAL, weight="bold")
    s.lines(610, 260, t["b2"], 14, DIM)
    s.arrow(795, 150, 700, 196, DIM, 2, "5 4")
    s.arrow(795, 150, 380, 196, DIM, 2, "5 4")
    s.box(150, 352, 600, 62, fill="#18302d", stroke=TEAL)
    s.text(450, 378, t["rule"], 16, TEXT, weight="bold")
    s.text(450, 401, t["eff"], 14, DIM)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- workers: 2-year window, 20 kept
T_WINDOW = {
    "en": {"cap": "Each arrival by your lines is remembered for 2 game years; at most the latest 20 are kept.",
           "now": "now", "ago": "2 years ago", "kept": "counted", "old": "too old: dropped",
           "same": "same person again: only the latest arrival is kept"},
    "fr": {"cap": "Chaque arrivée par tes lignes est retenue 2 années de jeu ; au plus les 20 dernières sont gardées.",
           "now": "maintenant", "ago": "il y a 2 ans", "kept": "comptée", "old": "trop ancienne : retirée",
           "same": "même personne à nouveau : seule la dernière arrivée est gardée"},
    "de": {"cap": "Jede Ankunft mit deinen Linien wird 2 Spieljahre gemerkt; höchstens die letzten 20 bleiben.",
           "now": "jetzt", "ago": "vor 2 Jahren", "kept": "gezählt", "old": "zu alt: entfernt",
           "same": "dieselbe Person erneut: nur die letzte Ankunft bleibt"},
}


def workers_window(lang):
    t = T_WINDOW[lang]
    s = Svg(900, 220)
    s.box(120, 60, 700, 70, fill="#18302d", stroke=TEAL)
    s.parts.append(f'<line x1="40" y1="95" x2="870" y2="95" stroke="{DIM}" stroke-width="2"/>')
    s.text(820, 160, t["now"], 15, TEXT)
    s.text(120, 160, t["ago"], 15, TEXT)
    for i, x in enumerate([170, 230, 300, 340, 420, 470, 540, 610, 650, 720, 780]):
        s.parts.append(f'<circle cx="{x}" cy="95" r="9" fill="{TEAL}"/>')
    for x in (55, 85):
        s.parts.append(f'<circle cx="{x}" cy="95" r="9" fill="{LINE}" stroke="{DIM}"/>')
    s.text(470, 50, t["kept"], 15, TEAL, weight="bold")
    s.text(70, 50, t["old"], 13, DIM)
    s.text(450, 200, t["same"], 14, DIM)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- loading: factors
T_LOAD = {
    "en": {"cap": "Loading speed = vehicle's base speed × platform factor × stock factor.",
           "veh": "Vehicle", "veh2": ["base load speed", "(vehicle store)"],
           "plat": "Platform factor", "plat2": ["x2 wagons on a section", "of their class", "x1 universal section",
                                                 "x0.25 no matching section", "x0.25 part longer", "than the platform"],
           "stock": "Stock factor", "stock2": ["x2 specialised", "warehouse module", "x1 universal warehouse,", "industry, town"],
           "x": "×"},
    "fr": {"cap": "Vitesse de chargement = vitesse de base du véhicule × facteur du quai × facteur du stock.",
           "veh": "Véhicule", "veh2": ["vitesse de base", "(magasin de véhicules)"],
           "plat": "Facteur du quai", "plat2": ["x2 wagons sur une section", "de leur classe", "x1 section universelle",
                                                "x0,25 aucune section adaptée", "x0,25 partie plus longue", "que le quai"],
           "stock": "Facteur du stock", "stock2": ["x2 module d'entrepôt", "spécialisé", "x1 entrepôt universel,", "industrie, ville"],
           "x": "×"},
    "de": {"cap": "Ladegeschwindigkeit = Grundgeschwindigkeit des Fahrzeugs × Bahnsteigfaktor × Lagerfaktor.",
           "veh": "Fahrzeug", "veh2": ["Grund-Ladegeschw.", "(Fahrzeugkauf)"],
           "plat": "Bahnsteigfaktor", "plat2": ["x2 Wagen auf Abschnitt", "ihrer Klasse", "x1 Universalabschnitt",
                                                "x0,25 kein passender Abschnitt", "x0,25 Teil länger", "als der Bahnsteig"],
           "stock": "Lagerfaktor", "stock2": ["x2 spezialisiertes", "Lagermodul", "x1 Universallager,", "Industrie, Stadt"],
           "x": "×"},
}


def loading_factors(lang):
    t = T_LOAD[lang]
    s = Svg(900, 300)
    s.box(20, 50, 220, 200)
    s.text(130, 92, t["veh"], 20, weight="bold")
    s.lines(130, 122, t["veh2"], 14, DIM)
    s.text(270, 160, t["x"], 34, GOLD, weight="bold")
    s.box(300, 30, 300, 240, stroke=GOLD)
    s.text(450, 66, t["plat"], 20, GOLD, weight="bold")
    s.lines(450, 98, t["plat2"], 14, TEXT)
    s.text(630, 160, t["x"], 34, GOLD, weight="bold")
    s.box(660, 50, 220, 200, stroke=TEAL)
    s.text(770, 92, t["stock"], 20, TEAL, weight="bold")
    s.lines(770, 124, t["stock2"], 14, TEXT)
    return s.svg(), t["cap"]


# ---------------------------------------------------------------- loading: sections of a platform
T_SECT = {
    "en": {"cap": "A platform is a list of sections, one per cargo class, with the module lengths of each class added up. "
                  "Where a wagon stands does not count.",
           "plat": "Platform 160 m", "s1": "Bulk 120 m", "s2": "Universal 40 m",
           "w1": "bulk wagons on 120 m: x2", "w2": "the other wagons: x1 (universal)",
           "w3": "no bulk section at all: x0.25"},
    "fr": {"cap": "Un quai est une liste de sections, une par classe de fret, avec les longueurs des modules de chaque classe "
                  "additionnées. L'endroit où s'arrête un wagon ne compte pas.",
           "plat": "Quai 160 m", "s1": "Vrac 120 m", "s2": "Universel 40 m",
           "w1": "wagons vrac sur 120 m : x2", "w2": "les autres wagons : x1 (universel)",
           "w3": "aucune section vrac : x0,25"},
    "de": {"cap": "Ein Bahnsteig ist eine Liste von Abschnitten, einer pro Frachtklasse, mit den addierten Modullängen jeder Klasse. "
                  "Wo ein Wagen steht, zählt nicht.",
           "plat": "Bahnsteig 160 m", "s1": "Schüttgut 120 m", "s2": "Universal 40 m",
           "w1": "Schüttgutwagen auf 120 m: x2", "w2": "die übrigen Wagen: x1 (universal)",
           "w3": "kein Schüttgut-Abschnitt: x0,25"},
}


def loading_sections(lang):
    t = T_SECT[lang]
    s = Svg(900, 250)
    s.text(450, 30, t["plat"], 16, DIM)
    s.box(60, 45, 585, 50, fill="#3a3220", stroke=GOLD, r=4)
    s.text(352, 77, t["s1"], 16, GOLD, weight="bold")
    s.box(645, 45, 195, 50, fill=PANEL, stroke=DIM, r=4)
    s.text(742, 77, t["s2"], 16, TEXT)
    for i in range(8):
        x = 70 + i * 96
        s.box(x, 115, 86, 34, fill="#18302d" if i < 6 else LINE, stroke=TEAL if i < 6 else DIM, r=4)
    s.text(352, 180, t["w1"], 15, TEAL, weight="bold")
    s.text(742, 180, t["w2"], 15, TEXT)
    s.text(450, 225, t["w3"], 15, RED)
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
