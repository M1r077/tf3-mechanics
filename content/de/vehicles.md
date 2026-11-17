---
title: Fahrzeuge: Zustand, Alter und Ladegeschwindigkeit
summary: Was die Fahrzeugwerte bedeuten, wie Zustand und Alter funktionieren, was Depots und Wartungsstationen tun, woher Preis und Betriebskosten kommen und wann man ein Fahrzeug ersetzen sollte.
domain: vehicles
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-16
game: 40425
fact: 5 | Zustandsstufen, von Sehr schlecht bis Sehr gut, je 20 %
fact: 20 % | Zustand, der die Warnung Fahrzeugzustand auslöst
fact: 6 × | die jährlichen Grund-Betriebskosten: der Preis eines Fahrzeugs
fact: 4 bis 16 | Fahrzeuge im Wartungspool eines Depots oder einer Wartungsstation
---

Jedes Fahrzeug hat feste Werte (Geschwindigkeit, Kapazität, Ladegeschwindigkeit, Preis, Betriebskosten, Lebensdauer) und zwei Werte, die sich ändern: seinen **Zustand** und sein **Alter**. Der Zustand sinkt im Betrieb und wird durch Wartung wiederhergestellt. Das Alter wächst nur.

## Die Werte im Fahrzeugkatalog

- Der Katalog zeigt jeden Wert als Balken. Der Balken nutzt eine feste Skala je Verkehrsträger, die sich mit dem Jahr ändert (zum Beispiel Ladegeschwindigkeit von Schiffen: 10 bis 45 ab 2003). Er vergleicht das Fahrzeug nicht mit anderen Fahrzeugen (`vehicle_util.tl:210-245`, `vehicle_util.tl:259-268`).
- Bei einem Zug zeigt der Katalog die **höchste** Ladegeschwindigkeit aller seiner Teile (`vehicle_store_util.tl:333`).
- Ein Fahrzeug, dessen Datei keine Ladegeschwindigkeit, keinen Lärm, keine Verschmutzung oder keinen Komfort festlegt, erhält einen aus seinen anderen Werten berechneten Wert (Jahr, Geschwindigkeit, Leistung, Gewicht, Größe) (`model_metadata_util.lua:395-417`, `vehicle_metadata_util.lua:233-256`). Die berechnete Ladegeschwindigkeit wird auf 0,5 gerundet und ist nie kleiner als 1 (`vehicle_metadata_util.lua:267-269`).

## Welches Fahrzeug lädt am schnellsten?

Die Ladegeschwindigkeit des Fahrzeugs ist nur der erste Faktor; Bahnsteig und Bestand multiplizieren sie (siehe [Lade- und Entladegeschwindigkeit](loading.html)).

| Verkehrsträger | Ladegeschwindigkeit, die als voller Balken angezeigt wird (letzte Epoche) | Source |
|---|---|---|
| Schiffe | 10 bis 45 (ab 2003) | `vehicle_util.tl:219-223` |
| Straßenfahrzeuge, Straßenbahnen | 0,5 bis 10 (ab 1995) | `vehicle_util.tl:232-243` |
| Züge | 0,1 bis 10 (ab 1981) | `vehicle_util.tl:226-229` |
| Flugzeuge | 1 bis 4 (ab 1978) | `vehicle_util.tl:212-216` |

- Schiffe haben mit Abstand die höchsten Ladegeschwindigkeiten, Flugzeuge die niedrigste Skala.
- Vergleiche Fahrzeuge eines Verkehrsträgers im Katalog über die Spalte Ladegeschwindigkeit; neuere Modelle liegen meist höher auf dem Balken.
- Jede Frachtart hat einen Ladefaktor von 0,0625, Passagiere 1 (`coal.cargo.lua:29`, `passengers.cargo.lua:23`).

```engine
Wie Ladegeschwindigkeit des Fahrzeugs, Ladefaktor der Fracht sowie Bahnsteig- und Bestandsfaktoren zur tatsächlichen Ladezeit kombiniert werden, berechnet die Engine. Die Skripte liefern nur die Eingaben.
```

## Zustand

| Zustand | Stufe | Source |
|---|---|---|
| über 80 % | **Sehr gut** | `vehicle_util.tl:159-172` |
| 60–80 % | **Gut** | `vehicle_util.tl:159-172` |
| 40–60 % | **Mittelmässig** | `vehicle_util.tl:159-172` |
| 20–40 % | **Schlecht** | `vehicle_util.tl:159-172` |
| bis 20 % | **Sehr schlecht** | `vehicle_util.tl:159-172` |

- Der Zustand eines Zuges ist der **Durchschnitt** aller seiner Wagen und Lokomotiven (`vehicle_util.tl:285-295`).
- Ein abgenutztes Fahrzeug verliert Höchstgeschwindigkeit, Leistung und Komfort und gewinnt Lärm, Verschmutzung und Betriebskosten (`vehicle_store_util.tl:236-258`). Wie viel und ab welchem Zustand, sind Werte der Engine. Das Fahrzeugfenster listet diese Abzüge unter **Zustand**.
- Wie stark diese Abzüge sind, legt **Fahrzeugwartungseffekt** fest (Keine, Niedrig, Mittel, Hoch, Sehr hoch); bei Keine hat der Zustand keine Wirkung (`difficulty_util.tl:42`, `mod.script.tl:241-245`, `vehicle_store_util.tl:166-168`, `vehicle_store_util.tl:216-228`). Details: [Kosten, Unterhalt und Darlehen](costs.html).
- Bei **20 %** oder weniger erhältst du die Warnung **Fahrzeugzustand**. Sie bleibt, bis das Fahrzeug wieder über **30 %** liegt (`notifications.script.tl:310-318`).
- Ein geklontes Fahrzeug ist ein Neukauf: Zustand 100 %, neues Kaufdatum (`manager_window.tl:8502-8506`).

```engine
Wie schnell der Zustand sinkt, wie viel ein Besuch in einer Wartungsstation wiederherstellt und wie groß jeder Abzug ist (getMaintenanceTopSpeedPenalty und die anderen), sind Engine-Werte. Jedes Fahrzeugmodell kann außerdem pro Stufe einen eigenen Abzug der Höchstgeschwindigkeit festlegen (`vehicle_store_util.tl:250-253`).
```

## Depots und Wartungsstationen

Fahrzeuge werden von einem nahen Depot oder einer nahen Wartungsstation gewartet. Jedes davon bedient eine begrenzte Zahl von Fahrzeugen: seinen **Wartungspool**.

| Gebäude | Wartungspool | Radius | Abgestellte Fahrzeuge | Source |
|---|---|---|---|---|
| Zugdepot | 6 | 800 m | 5 | `rail_depot.script.lua:341-349` |
| Zug-Wartungsstation | 12 | 800 m | – | `rail_maint_station.script.lua:151-157` |
| Straßendepot, Straßenbahndepot | 12 | 400 m | 10 / 8 | `road_depot.script.lua:189-198`, `tram_depot.script.lua:217-226` |
| Straßen-Wartungsstation | 16 | 600 m | – | `road_maint_station.script.lua:234-240` |
| Schiffsdepot | 8 | 1000 m | 5 | `water_depot.script.lua:370-379` |
| Schiffs-Wartungsstation | 12 | 1400 m | – | `water_maint_station.script.lua:256-262` |
| Hangar eines Flugfelds oder Flughafens | 16 | 550 m | 5 | `af_hangar.module.lua:272-280`, `ap_hangar.module.lua:455-463` |
| Heliport | 4 | 800 m | 5 | `heliport.script.lua:300-309` |

- Das Gebäudefenster zeigt „belegt / Pool“ (zum Beispiel 14 / 12) und die Liste der bedienten Fahrzeuge mit ihrem Zustand (`entity_window_util.tl:2010-2039`, `maintenance_station_eow.script.tl:188-215`).
- Ein vollerer Pool macht das Gebäude lauter und schmutziger: Die Emissionen steigen mit dem belegten Anteil des Pools (`emissions.script.tl:223-234`).
- Eine Zug-Wartungsstation bedient doppelt so viele Züge wie ein Zugdepot: 12 gegen 6.
- Wartungsstationen können keine Fahrzeuge kaufen oder abstellen, haben aber oft einen größeren Radius als das Depot: 600 m gegen 400 m auf der Straße, 1400 m gegen 1000 m bei Schiffen. Straßenbahnen werden vom Straßenbahndepot und von der Straßen-Wartungsstation gewartet; das Straßendepot wartet keine Straßenbahnen (`tram_depot.script.lua:209`, `tram_depot.script.lua:226`).
- Das offizielle Wiki empfiehlt Wegpunkte, um Fahrzeuge an einem Wartungsgebäude vorbeizuschicken.

```engine
Welcher Station ein Fahrzeug zugeordnet wird, was passiert, wenn mehr Fahrzeuge eine Station nutzen als ihr Pool, und welcher Einzugsradius gilt, entscheidet die Engine.
```

## Preis und Betriebskosten

- Fahrzeuge des Grundspiels haben keinen festen Preis: Die Betriebskosten ergeben sich aus Geschwindigkeit und Kapazität, und der Preis beträgt das **6-Fache** der jährlichen Grund-Betriebskosten, vor den Einstellungen Fahrzeugkosten und Fahrzeugwartung (`model_metadata_util.lua:548-549`). Genau 6 Jahre Betriebskosten sind es nur, wenn beide Einstellungen gleich sind. Vollständige Formel: [Kosten, Unterhalt und Darlehen](costs.html).
- **Fahrzeugkosten** skaliert die Preise von 50 % bis 150 % (`post_run_util.tl:54-81`), und **Fahrzeugwartung** skaliert die Betriebskosten genauso. Im Spiel gemessen an den 921 Fahrzeugen eines Spielstands, geladen mit 75 %, 100 % und 125 %: Die Betriebskosten folgen dem Regler (Median ×0,75 und ×1,25; Fahrzeuge, deren Zustand sich zwischen den Ladevorgängen änderte, weichen etwas ab).
- Ein Fahrzeug in schlechtem Zustand zahlt zusätzlich zum Grundwert höhere Betriebskosten (`vehicle_store_util.tl:256-259`).

## Alter und Lebensdauer

- Jedes Modell hat eine **Lebensdauer** (`vehicle_util.tl:31-34`). Die Spalte **Alter** im Linienfenster zeigt das Alter; ihr Tooltip zeigt die verbleibende Zeit oder **Lebensdauer erreicht** (`line_eow.script.tl:133-147`). Der Anteil der Lebensdauer in diesem Tooltip steht auf **0 %**, bis die Lebensdauer erreicht ist: Das Skript rundet den Bruch vor der Anzeige ab (`line_eow.script.tl:139`), während derselbe Anteil an anderer Stelle vollständig berechnet wird (`vehicle_util.tl:311`). Nimm stattdessen die verbleibende Zeit.
- Bei einem Zug zählt der **älteste** Teil (`vehicle_util.tl:36-52`). Ein einziger alter Wagen lässt den ganzen Zug alt erscheinen.

```engine
Was das Erreichen der Lebensdauer ändert (zum Beispiel schnellerer Zustandsverlust oder niedrigerer Verkaufswert), steht nicht in den Skripten. Die Skripte zeigen nur Alter und Lebensdauer an.
```

## Wann sollte ich alte Fahrzeuge ersetzen?

1. **Der Zustand bleibt niedrig**, obwohl eine Wartungsstation in der Nähe ist: Das Fahrzeug verliert Geschwindigkeit und zahlt höhere Betriebskosten. Prüfe zuerst den Pool der Station: Er ist vielleicht voll.
2. **Lebensdauer erreicht** im Tooltip von Alter: Das Modell hat seine geplante Lebensdauer überschritten.
3. **Es gibt ein besseres Modell**: Schnellere oder größere Fahrzeuge kosten mehr im Betrieb, transportieren aber mehr (der Preis folgt Geschwindigkeit × Kapazität).
4. Nutze **Fahrzeuge ersetzen** im Linienmanager. Es öffnet den Katalog mit einem Vergleich zum aktuellen Fahrzeug (`vehicle_store_window.tl:4893-4928`, `vehicle_store_window.tl:2611`).

```tip scripts
**Fahrzeuge bleiben neben einem Depot in schlechtem Zustand? Öffne sein Fenster und prüfe „belegt / Pool“.** Ein Zugdepot bedient 6 Züge, eine Zug-Wartungsstation 12. Was die Engine mit Fahrzeugen über dem Pool macht, steht nicht in den Skripten; ein zweites Gebäude ist die sichere Lösung.
```

## Gut zu wissen

- Baue genug Wartungskapazität: Ein Zugdepot bedient nur 6 Züge.
- Mit **Fahrzeugwartungseffekt** auf Keine spielt der Zustand keine Rolle.
- **Ins Depot schicken** schickt ein Fahrzeug zum nächsten erreichbaren Depot, nicht zu dem, in dem es gekauft wurde (offizielles Wiki).
- [Vehicle Comparison](https://mod.io/g/transportfever3/m/vehicle-comparison) hilft, Modelle vor dem Ersetzen zu vergleichen.

```check
official: „This section shows how well the vehicle is maintained and how the maintenance state affects the vehicle properties.“ „Loading speed modifies a vehicle's base loading speed which can be seen in the vehicle window or in the vehicle store.“ ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles))
scripts: Fünf Zustandsstufen zu je 20 %; Abzüge bei Geschwindigkeit, Leistung, Komfort, Emissionen und Betriebskosten unter 80 %, skaliert durch Fahrzeugwartungseffekt; Warnung bei 20 %, aufgehoben über 30 %. Wartungspool 4 bis 16 Fahrzeuge pro Gebäude. Preis = 6 Jahre Betriebskosten. Alter eines Zuges = sein ältester Teil. Fehlende Ladegeschwindigkeiten werden aus den anderen Werten berechnet, auf 0,5 gerundet, mindestens 1.
result: refines
```
