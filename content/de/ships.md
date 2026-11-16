---
title: Schiffe und Häfen
summary: Kleine und große Schiffe, welcher Hafen welche aufnimmt, Terminals und Kosten der Häfen, und die Liste aller Schiffe mit Fracht, Kapazität und Geschwindigkeit.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
game: 40425
fact: 2 | Schiffsgrößen: klein und groß
fact: 1, 2, 4 | Terminals pro Hafen
fact: 27 | Schiffe im Basisspiel
fact: ×9 | Preis und Unterhalt der Hafenvariante von 1990
---

Jedes Schiff ist **klein** oder **groß**. Ein großes Schiff kann nur an einem **großen Hafen** anlegen; ein kleines Schiff legt an beiden an. Das sagt auch der Leitfaden im Spiel: „Besonders zu beachten ist, dass grosse Schiffe nur an grossen Häfen anlegen können.“

```diagram ship_access
```

## Kleine und große Häfen

- Zwei Häfen im Baumenü: **Kleiner Passagier-/Güterhafen** und **Grosser Passagier-/Güterhafen**. Beide nehmen Passagiere und alle Güter an (`harbor_modular.tl:92`, `harbor_modular.tl:122`).
- Der kleine Hafen besteht aus kleinen Anlegestellen, die nur kleine Schiffe annehmen (`small_pier.module.lua:7`). Der große Hafen nutzt mittlere Anlegestellen, die beide Größen annehmen (`medium_pier.module.lua:6`, `harbor_modular.script.lua:35-39`).
- **Terminals**: 1, 2 oder 4, beim Bau gewählt (`harbor_modular.tl:16`, `harbor_modular.script.lua:33`).
- Ein Anlegestellen-Terminal fasst 100 wartende Passagiere an einer kleinen und 50 an einer mittleren Anlegestelle (`modules.script.lua:872`, `modules.script.lua:1004`).
- Beim Platzieren eines Hafens blendet das Skript nur die Ebene für schiffbares Wasser ein (`harbor_modular.tl:26-30`). Wo ein Hafen stehen darf, entscheidet die Engine.
- Jedes Schiff legt seine Größe in seiner Fahrzeugdatei fest; das Spiel macht daraus den Modus kleines oder großes Schiff (`model_metadata_util.lua:1411-1412`).

## Kosten

Es gibt eine Hafenvariante pro Epoche: 1900, 1950 und 1990 (`harbor_modular.tl:71-73`). Preis und Unterhalt werden für eine Variante ab 1940 mit 3 und für eine ab 1980 mit 9 multipliziert (`harbor_modular.tl:76`):

| Hafen | Preis (erste Variante) | Unterhalt pro Jahr (erste Variante) | Quelle |
|---|---|---|---|
| Kleiner Hafen | 144.000 - 444.000 | 24.000 - 74.000 | `harbor_modular.tl:88-89` |
| Großer Hafen | 228.000 - 678.000 | 38.000 - 113.000 | `harbor_modular.tl:118-119` |

- Die beiden Werte sind die kleinste und die größte Anordnung.
- Der Unterhalt von Häfen folgt auch dem Kalenderjahr, ×1 im Jahr 1900 bis ×6 im Jahr 2020, wie bei Lagern und Flughäfen ([Kosten, Unterhalt und Darlehen](costs.html)).
- Häfen sind laut und schmutzig: 180 bis 280 für beide ([Verschmutzung und Lärm](emission.html)).
- Preis und Betriebskosten eines Schiffs werden aus Geschwindigkeit und Kapazität berechnet, wie bei Straßenfahrzeugen und Flugzeugen ([Kosten, Unterhalt und Darlehen](costs.html)).

## Alle Schiffe

Geschwindigkeit in km/h, gerundet. „Fracht“ listet die Frachtklassen der Fahrzeugdatei; „alle Güter“ heißt jede Güterart. Die Kapazität ist die Summe, die der Fahrzeugkauf zeigt: alle Abteile zusammen, jedes mit seiner größten Ladekonfiguration (`vehicle_store_util.tl:70-95`).

| Schiff | Jahre | Größe | Fracht | Kapazität | Geschwindigkeit | Ladegeschwindigkeit |
|---|---|---|---|---|---|---|
| Dunara Castle | 1875-1930 | groß | Passagiere, alle Güter | **160** (2 × 80) | 20 | 20 |
| Kanadischer Kutter | 1884-1948 | klein | alle Güter | 40 | 35 | 10 |
| Waimarie | 1889-1940 | klein | Passagiere | 80 | 30 | 15 |
| Sydfart | 1900-1930 | klein | Flüssiggut, Sperrgut, Stückgut, Schüttgut | 80 | 30 | 20 |
| PS Trillium | 1910-1955 | groß | Passagiere | 200 | 35 | 15 |
| Schaufelraddampfer | 1915-1960 | klein | Passagiere, alle Güter | **120** (2 × 60) | 40 | 10 |
| Terra Nova | 1925-1975 | groß | Schüttgut, Sperrgut, Stückgut | **200** (2 × 100) | 45 | 30 |
| Votrans Tankerschubboot | 1935-1990 | klein | Flüssiggut | 120 | 33 | 20 |
| Votrans Güterschubboot | 1935-1990 | klein | Schüttgut, Sperrgut, Stückgut | 120 | 33 | 20 |
| MS Stadt Kiel | 1943-1990 | klein | Passagiere | 80 | 30 | 20 |
| Borealis | 1948-1994 | klein | alle Güter | 60 | 38 | 20 |
| Wopper | 1950-2005 | klein | Flüssiggut, Sperrgut, Stückgut, Schüttgut | 160 | 30 | 25 |
| Meridian-Fähre | 1956-2011 | klein | Passagiere | 240 | 30 | 15 |
| Cap Arkona | 1965-2010 | groß | Passagiere | 200 | 40 | 20 |
| Tora Küstenschiff | 1970-2020 | groß | Flüssiggut, Sperrgut, Stückgut, Schüttgut | 320 | 40 | 25 |
| AP1-88 Hovercraft | 1980- | klein | Passagiere | 240 | 90 | 15 |
| Herkules XI Schubboot | 1990- | groß | Sperrgut, Stückgut, Schüttgut | **240** (2 × 120) | 32 | 20 |
| Baltica | 1994- | klein | alle Güter | 80 | 40 | 20 |
| HADAG Typ 2000 | 1995- | klein | Passagiere | 100 | 35 | 25 |
| Damen Tanker 800 | 1996- | klein | Flüssiggut | **320** (2 × 160) | 28 | 30 |
| Damen Schnellfähre | 2003- | groß | Passagiere | 220 | 75 | 20 |
| Luise Deymann | 2013- | groß | Flüssiggut | **480** (2 × 240) | 30 | 35 |
| MS Diamant | 2013- | groß | Passagiere | 280 | 45 | 35 |
| Virgo Schubboot | 2015- | groß | Sperrgut, Stückgut, Schüttgut | **320** (2 × 160) | 40 | 15 |
| GHL Oita Hovercraft | 2023- | klein | Passagiere | 320 | 100 | 20 |
| Yara Birkeland | 2030- | groß | Sperrgut, Stückgut, Schüttgut | 480 | 42 | 10 |
| Solar Shuttle | 2035- | klein | Passagiere | 80 | 30 | 30 |

## Gut zu wissen

- **Prüfe die Größe, bevor du einen kleinen Hafen baust.** Mehrere der größten Frachtschiffe (Tora, Virgo, Yara Birkeland) sind groß und legen dort nicht an.
- **„Keine Strecke für grosse Schiffe“** ist eine eigene Warnung für große Schiffe: Das Spiel hat keinen Wasserweg gefunden, den ein großes Schiff nutzen kann. Welches Wasser für welche Größe offen ist, entscheidet die Spiel-Engine, nicht die Skripte, die nur die Warnung anzeigen (`vehicle_warning.script.tl:28-36`).
- **Schiffswegpunkte** müssen auf Wasser gesetzt werden („Schiffswegpunkte müssen auf dem Wasser liegen.“).
- Schiffsdepot und Schiffswartungsstation sind getrennte Gebäude; die Wartung wirkt in einem Radius um sie herum ([Fahrzeuge: Zustand, Alter und Ladegeschwindigkeit](vehicles.html)).

```check
official: "Passenger and cargo ships are available in two sizes: small and large. Large ships can only dock at large harbors, so make sure the harbor matches the size of the ships assigned to the line." (in-game guide "Water Infrastructure")
scripts: Gleich: kleine Anlegestellen nehmen nur SMALL_SHIP an, mittlere SHIP und SMALL_SHIP; beide Häfen nehmen Passagiere und alle Güter an; 1, 2 oder 4 Terminals; drei Epochenvarianten zu ×1 / ×3 / ×9; 16 kleine und 11 große Schiffe im Basisspiel.
result: refines
```
