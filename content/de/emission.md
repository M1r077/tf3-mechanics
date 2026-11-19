---
title: Verschmutzung und Lärm
summary: Was Lärm und Verschmutzung erzeugt, wann ein Gebäude mehr ausstößt, wie Städte das bewerten und was Industriebegrünung und Reinigungsanlage wirklich tun.
domain: emission
official: gamemanual:simulation:towns#town_authority_rating
status: verified
updated: 2026-11-16
game: 40444
fact: 65–80 dB | Lärm in der Stadt: volle Bewertung bei 65, null bei 80
fact: 60–74 | Verschmutzung in der Stadt, auf der logarithmischen Skala der Skripte (kein Schallpegel): volle Bewertung bei 60, null bei 74
fact: −80 % | Lärm und Verschmutzung einer begrünten Industrie
fact: 700 m | Reichweite der Reinigungsanlage
---

Fahrzeuge, Gleise, Straßen, Bahnhöfe, Depots, Lager und Industrien erzeugen alle **Lärm** und **Verschmutzung**. Zwei Stadtbewertungen, **Lärm** und **Verschmutzung**, vergleichen, was die Stadt erreicht, mit festen Grenzen. Eine schlechte senkt die Bewertung der **Stadtverwaltung** und damit das Wachstum (siehe [Städte](towns.html)).

## Wann ein Gebäude mehr ausstößt

Ein Spielskript setzt die Emission von vier Gebäudearten alle paar Updates, zwischen einem ruhigen und einem ausgelasteten Niveau (`emissions.script.tl:12-18`):

| Gebäude | Stößt mehr aus, wenn | Quelle |
|---|---|---|
| **Industrie** | sie produziert, und noch mehr mit jedem Boost (Fracht oder Arbeiter); sind alle Ausgangslager zugleich voll, wird ihr Niveau halbiert: produzierend → Ruhe, zweimal geboostet → produzierend | `emissions.script.tl:152-194` |
| **Bahnhof** | er stärker ausgelastet ist: wartende Personen und Fracht im Verhältnis zur Kapazität | `emissions.script.tl:211-222` |
| **Depot**, **Wartungsstation** | mehr Fahrzeuge seine Wartung nutzen | `emissions.script.tl:223-234` |
| **Lager** | seine Bestände voller sind | `emissions.script.tl:237-250` |

- Jede Industrie hat ihre eigenen vier Stufen: ruhend, produzierend, einmal geboostet, zweimal geboostet (`industryutil.lua:464-475`; der Standard 0 / 78 / 84 / 88 gilt nur für eine Industrie ohne eigene Werte). Die meisten stoßen auch ruhend etwas aus: Eine Kohlemine geht von 2 → 10 → 20 → 30 Verschmutzung, ihre Felder 2 → 30 → 60 → 90 (`coal_mine.con.lua:99-135`, siehe [Industrien](industries.html)).
- Eine Industrie, deren Ausgangslager alle voll sind, fällt auf die Hälfte ihres Niveaus (`emissions.script.tl:172-182`): Sie zu bedienen erhöht ihre Verschmutzung.
- Auch Fahrzeuge und Gleise stoßen aus; ein Fahrzeug in schlechtem Zustand stößt mit der Einstellung **Fahrzeugwartungseffekt** mehr aus (siehe [Kosten, Unterhalt und Kredite](costs.html)).

## Was das Baumenü zeigt

| Gebäude | Lärm | Verschmutzung | Quelle |
|---|---|---|---|
| Hafen | 180–280 | 180–280 | `harbor_modular.tl:86-87` |
| Flughafen | 8–56 | 80–560 | `airport.tl:28-29` |
| Bahnhof | 25 | 45–350 | `modular_station.con.lua:97-98` |
| Bahndepot | 50 | 100 | `rail_depot.con.lua:32-33` |
| Straßen- und Tramdepot | 40 | 80 | `road_depot.con.lua:30-31`, `tram_depot.con.lua:32-33` |
| U-Bahn-Station | 40 | 80 | `underground_station.con.lua:75-76` |
| Lkw- und Busbahnhof | 1–10 | 12–76 | `modular_terminal.con.lua:67-68`, `modular_terminal.con.lua:121-122` |
| Wartungsstationen | 20 | 40–50 | `road_maint_station.con.lua:30-31`, `rail_maint_station.con.lua:30-31` |
| Lager | 20 | 50 (universal) oder 100 (spezialisiert) | `warehouses/warehouse.tl:51`, `warehouses/warehouse.tl:73-74` |

Zwei Werte sind die Spanne, die das Menü zeigt, vom niedrigsten zum höchsten, wie die Preisspanne daneben (`construction_desc_react_util.tl:733-746`); ein Wert ist eine einzelne Zahl. Im Betrieb stößt jedes Gebäude mehr aus, je ausgelasteter es ist (Tabelle oben). Halte Häfen, Flughäfen und große Güterbahnhöfe von Häusern fern.

## Wie eine Stadt es bewertet

| Bewertung | Gemessen | Volle Bewertung | Null | Quelle |
|---|---|---|---|---|
| **Lärm** | Lärm an den Gebäuden der Stadt | 65 dB oder weniger | 80 dB | `town_util.tl:433-443`, `emission_config.tl:10-11` |
| **Verschmutzung** | mittlere Verschmutzung pro 16-m-Zelle der Stadtfläche (Fläche als mindestens 5 und höchstens 10 km² gezählt), umgerechnet auf die logarithmische Skala der Skripte („dB“) | 60 oder weniger | 74 | `town_util.tl:413-431`, `emission_config.tl:23-30` |

- Nur das **Wohngebäude**-Viertel leidet unter Lärm; Gewerbe- und Industriegebäude nicht (offizielles Wiki). Das Fenster eines Hauses zeigt den Lärm an seiner Position (`town_building.tl:165-183`).
- Verschmutzung wird über die ganze Fläche gemittelt: Eine Quelle weit vom Zentrum wiegt in einer großen Stadt weniger als in einer kleinen.
- Die Einstellungen **Lärmempfindlichkeit** und **Verschmutzungsempfindlichkeit** verschieben die Grenzen: doppelte Empfindlichkeit zählt als +3 dB (`town_util.tl:426-428`, `town_util.tl:439-441`). Verschmutzung nutzt dieselbe logarithmische Skala wie Lärm (10·log10): +3 „dB“ heißt doppelte Verschmutzung. Es ist kein Schallpegel.

| Stufe | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Quelle |
|---|---|---|---|---|---|---|---|---|
| Lärm | Aus (immer voll) | ×¼ | ×½ | ×1 | ×1,4 | ×1,8 | ×3,5 | `difficulty_util.tl:48` |
| Verschmutzung | Aus (immer voll) | ×¼ | ×½ | ×1 | ×1,7 | ×3 | ×5 | `difficulty_util.tl:49` |

Die Voreinstellungen Leicht, Mittel, Schwer und Sehr schwer nutzen die Stufen 3, 4, 5 und 6 (`difficulty_util.tl:114-115`, `difficulty_util.tl:142-143`, `difficulty_util.tl:169-170`, `difficulty_util.tl:196-197`).

## Industriebegrünung

| | | Quelle |
|---|---|---|
| Wirkung | Lärm und Verschmutzung der Industrie ×0,2 (−80 %), dauerhaft | `emission_config.tl:32`, `emissions.script.tl:184-192` |
| Nutzungen | je eine bei Unternehmensrang 3, 6, 9, 12 und 15 | `industry_greenify_tool.script.tl:99-104` |
| Grenze | einmal pro Industrie; ein zweiter Versuch verbraucht keine Genehmigung | `company.script.tl:489-494` |

- Die Wirkung hängt an dieser Version der Industrie: Wird die Industrie neu gebaut, geht sie verloren (`emissions.script.tl:187-190`).
- Beste Nutzung: die meistbeschäftigte Industrie direkt neben einer Stadt, denn eine geboostete Industrie stößt am meisten aus.

## Die Reinigungsanlage

Ein Unternehmensvorteil, der die Verschmutzung in der Umgebung entfernt.

| | | Quelle |
|---|---|---|
| Preis | 100.000.000 | `pollution_cleanup_facility.script.lua:560` |
| Unterhalt pro Jahr | 10.000.000 | `pollution_cleanup_facility.script.lua:561` |
| Verfügbar | 15 bei Unternehmensrang 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Bedarf | **Maschinen**: 8 pro Zyklus, zwei Zyklen pro Jahr; 20 Arbeiter | `pollution_cleanup_facility.con.lua:43-60` |
| Reichweite | 700 m | `pollution_cleanup_facility.con.lua:72-99` |

| Zustand | Verschmutzung | Lärm | Quelle |
|---|---|---|---|
| ruhend (keine Maschinen) | −50 | 20 | `pollution_cleanup_facility.con.lua:74-79` |
| in Betrieb | −10.000 | 80 | `pollution_cleanup_facility.con.lua:80-85` |
| einmal geboostet | −20.000 | 160 | `pollution_cleanup_facility.con.lua:86-91` |
| zweimal geboostet | −40.000 | 200 | `pollution_cleanup_facility.con.lua:92-97` |

Die letzte Stufe braucht eine Booster-Regel, die die Reinigungsanlage nicht hat: Mit Arbeitern erreicht sie −20.000 (`pollution_cleanup_facility.con.lua:51-58`, `emissions.script.tl:158-166`).

- Ohne Maschinen tut sie fast nichts: Sie muss wie eine Industrie beliefert werden.
- Sie ist laut: Baue sie außerhalb des Wohnviertels, höchstens 700 m vom verschmutzten Gebiet entfernt.
- Ihr Arbeiter-Boostfaktor ist ×2 (`pollution_cleanup_facility.script.lua:549`). Siehe [Arbeiter](workers.html).

## Gut zu wissen

- Öffne das Stadtfenster oder die Lärm- und Verschmutzungsebenen, um die Bewertung und die Brennpunkte zu sehen.
- Sind alle Ausgangslager einer Industrie voll, wird ihr Emissionsniveau halbiert, aber du verlierst ihre Fracht: Besser die Stadt verlegen als die Industrie aushungern.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) und [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) helfen, die am stärksten ausgelasteten Bahnhöfe zu finden.

```engine
Die Engine berechnet die Lärm- und Verschmutzungskarten, wie sich die Werte ausbreiten, die Emissionen von Fahrzeugen und Gleisen und wann eine Industrie neu gebaut wird. Das Skript setzt nur das Niveau jedes Gebäudes und die Grenzen der Städte.
```

```check
official: "Noise reflects noise levels in residential areas." "Pollution reflects pollution levels across the town area." Das Wohnviertel "is sensitive to noise"; das Gewerbeviertel "is robust against the influence of noise". ([Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Lärmbewertung 65 → 80 dB, Verschmutzung 60 → 74 dB gemittelt über 5–10 km²; Empfindlichkeit addiert 10·log10 dB; Industrien, Bahnhöfe, Depots und Lager stoßen bei Auslastung mehr aus; sind alle Ausgangslager voll, wird das Emissionsniveau einer Industrie halbiert; Begrünung −80 % einmal pro Industrie; die Reinigungsanlage entfernt bis zu 20.000 Verschmutzung (40.000 ist definiert, braucht aber eine Booster-Regel) im Umkreis von 700 m und braucht Maschinen.
result: refines
```
