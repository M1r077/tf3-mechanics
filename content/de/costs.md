---
title: Kosten, Unterhalt und Darlehen
summary: Was die Kosteneinstellungen ändern, welche Kosten mit dem Kalenderjahr steigen, wie Fahrzeugpreise berechnet werden und was ein Darlehen wirklich kostet.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
game: 40444
fact: ×6 | Jahresfaktor auf den Unterhalt von Lagern, Häfen und Flughäfen bis 2020
fact: 6 Jahre | Betriebskosten: der Preis eines Fahrzeugs
fact: einmal | wird der Zinssatz eines Darlehens auf den Betrag angewandt, nicht jedes Jahr
fact: 4 | Darlehen gleichzeitig
---

Die Einstellung **Inflation** erhöht keine Kosten: Sie senkt nur deine Einnahmen, wenn der Firmenrang steigt (siehe [Fracht-Einnahmen](income.html)). Die Kosten steigen stattdessen mit dem **Kalenderjahr**, und vier Regler skalieren sie von Anfang an.

```diagram cost_years
```

## Die Kosteneinstellungen

| Einstellung | Werte | Vorgaben Easy · Normal · Hard · Very Hard | Quelle |
|---|---|---|---|
| **Fahrzeugkosten**, **Fahrzeugwartung** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:39`, `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Infrastrukturkosten**, **Unterhalt der Infrastruktur** | 50 % · 75 % · 100 % · 125 % · 150 % | 50 % · 100 % · 125 % · 150 % | `difficulty_util.tl:98-101`, `difficulty_util.tl:125-128`, `difficulty_util.tl:153-156`, `difficulty_util.tl:180-183` |
| **Fahrzeugwartungseffekt** | Keine ×0 · Niedrig ×0,5 · Mittel ×1 · Hoch ×1,5 · Sehr hoch ×2 | Niedrig · Mittel · Hoch · Sehr hoch | `difficulty_util.tl:42`, `difficulty_util.tl:103`, `difficulty_util.tl:185` |
| **Inflation** | nur Einnahmen, siehe [Fracht-Einnahmen](income.html) | Niedrig · Normal · Hoch · Sehr hoch | `difficulty_util.tl:50`, `mod.script.tl:695-698` |

- **Infrastrukturkosten** skaliert den Preis von Straßen, Gleisen, Brücken, Tunneln, Bahnübergängen, Gebäuden und Modulen sowie Geländearbeiten (`post_run_util.tl:23-52`, `post_run_util.tl:83-120`, `construction.script.tl:31-35`, `mod.script.tl:224-227`). Sie skaliert auch die Abrisskosten von Gebäuden (`construction.script.tl:39-44`). **Unterhalt der Infrastruktur** skaliert beim Laden den Unterhalt von Straßen, Gleisen, Brücken, Tunneln, Bahnübergängen und Modulen (`post_run_util.tl:43-45`, `post_run_util.tl:105-112`). Bei Gebäuden wenden die Skripte ihn nur im Gebäudefenster an (`entity_window_util.tl:186`); was abgebucht wird, entscheidet die Engine.
- **Fahrzeugkosten** und **Fahrzeugwartung** skalieren Kaufpreis und Betriebskosten jedes Fahrzeugs (`post_run_util.tl:54-81`).
- **Fahrzeugwartungseffekt** legt fest, wie stark ein Fahrzeug in schlechtem Zustand Geschwindigkeit, Leistung und Komfort verliert und Lärm, Verschmutzung und Betriebskosten gewinnt (`mod.script.tl:242-246`).

## Was mit dem Kalenderjahr steigt

- **Gebäudeunterhalt**: ×1 im Jahr 1900, ×1,5 1920, ×2,2 1940, ×3,2 1960, ×4 1980, ×5 2000, ×6 2020 (`mod.script.tl:92-100`). Das Gebäudefenster und das Baumenü wenden ihn auf jedes Gebäude an, das dem Jahr folgen soll, und das Baumenü markiert jede Meta-Konstruktion (im Basisspiel: Lager, Flugfelder, Flughäfen und Häfen) (`entity_window_util.tl:186-193`, `construction_react_util.tl:1152`, `warehouse.tl:7`, `harbor_modular.tl:24`).
- **Module** eines solchen Gebäudes kosten den Preis des Baujahrs des Gebäudes, ihr Unterhalt den des aktuellen Jahres (`construction.tl:3741-3748`, `construction.tl:4413-4416`).
- **Epochenvarianten**: Depots, Wartungsstationen, Lager, Bahnhöfe, Häfen und Flughäfen haben eine Variante pro Epoche, und jede spätere Variante kostet **×3** (Epoche B) oder **×9** (Epoche C) der ersten (`rail_depot.con.lua:7`, `warehouse.tl:48`, `modular_station.con.lua:71`, `harbor_modular.tl:76`, `airport.tl:8`).
- **Geld aus Subventionen**: ×1 im Jahr 1900 bis ×4 ab 2000 (`finances_util.tl:87-90`). **Darlehensbeträge**: ×0,4 im Jahr 1900 bis ×2,4 im Jahr 2020 (`loan_util.tl:7-10`).
- **Einnahmen** haben gar keinen Jahresfaktor (`cargo_income.script.lua:10-13`).

```engine
Der tatsächlich abgebuchte Unterhalt, und ob Straßen, Gleise und Fahrzeuge ebenfalls der Jahrestabelle folgen, entscheidet die Engine (getCostMultiplierForYear; die Grundkonfiguration setzt nur chargeMaintenanceInterval = 60, `mod.script.tl:105`). Die Skripte berechnen nur die Werte, die in den Fenstern und im Baumenü angezeigt werden, mit der Tabelle oben. Kein Skript setzt das Kennzeichen „dem Jahr folgen" der anderen Gebäude.
```

## Gleise, Straßen und Gebäude

Straßen- und Gleisdateien geben Preis und jährlichen Unterhalt pro Meter an; das Baumenü zeigt sie pro Kilometer (`construction_react_util.tl:2466`, `construction_react_util.tl:2480-2488`). Bei den meisten Typen beträgt der Unterhalt **ein Sechstel** des Baupreises:

| Typ | Verfügbar ab | Bau pro km | Unterhalt pro km und Jahr | Quelle |
|---|---|---|---|---|
| Einfaches Gleis | Start | 60.000 | 10.000 | `simple.street_template.lua:9`, `simple.street_template.lua:33` |
| Standardgleis | 1930 | 180.000 | 30.000 | `standard.street_template.lua:11`, `standard.street_template.lua:35` |
| Hochgeschwindigkeitsgleis | 1980 | 540.000 | 90.000 | `high_speed.street_template.lua:11`, `high_speed.street_template.lua:35` |
| Kleine alte Landstraße | Start – 1940 | 60.000 | 10.000 | `country_old_small.street_template.lua:4-5`, `country_old_small.street_template.lua:8`, `country_old_small.street_template.lua:58` |
| Große neue Stadtstraße | 1940 | 540.000 | 90.000 | `town_new_large.street_template.lua:11`, `town_new_large.street_template.lua:91` |

- Eine Oberleitung kostet zusätzlich **30 %** des Gleispreises; eine Busspur 10 %, ein Straßenbahngleis 20 %, ein elektrisches Straßenbahngleis 40 % des Straßenpreises (`mod.script.tl:24-28`).
- Gelände anheben kostet 4,5 pro m³, absenken 5,25 pro m³, beides × Infrastrukturkosten; ein Feld entfernen 200.000 (`mod.script.tl:20-22`, `mod.script.tl:33`, `mod.script.tl:226-227`).
- Ein Gebäude ohne eigenen Unterhalt zahlt **ein Sechstel seines Preises** pro Jahr, berechnet aus dem Preis vor der Einstellung Infrastrukturkosten (`construction.script.tl:25-27`).
- Die Grundkonfiguration setzt einen Rückerstattungsfaktor beim Abriss von 0,75 und eine Frist von 60 (`mod.script.tl:30-31`): Was du gerade gebaut hast, bringt beim Abriss den Großteil des Geldes zurück. Die Engine wendet das an.

Jährlicher Unterhalt laut Dateien, für die erste Variante (vor 1940) und die späteren; Lager bekommen zusätzlich den Jahresfaktor oben:

| Gebäude | Erste Variante | ×3 (ab 1940) | ×9 (ab 1980) | Quelle |
|---|---|---|---|---|
| Zugdepot, Schiffsdepot | 100.000 | 300.000 | 900.000 | `rail_depot.con.lua:34`, `water_depot.con.lua:32` |
| Straßendepot | 30.000 | 90.000 | 270.000 | `road_depot.con.lua:32` |
| Straßenbahndepot | 20.000 | 60.000 | 180.000 | `tram_depot.con.lua:34` |
| Wartungsstation Zug oder Schiff | 40.000 | 120.000 | 360.000 | `rail_maint_station.con.lua:32`, `water_maint_station.con.lua:32` |
| Wartungsstation Straße | 10.000 | 30.000 | 90.000 | `road_maint_station.con.lua:32` |
| Universallager | 25.000 | 75.000 | 225.000 | `warehouse.tl:48-52`, `warehouse.tl:75` |
| Speziallager | 50.000 | 150.000 | 450.000 | `warehouse.tl:51`, `warehouse.tl:75` |

Jedes dieser Gebäude kostet **6 ×** seinen Unterhalt im Bau (`rail_depot.con.lua:35`, `warehouse.tl:76`): 2,7 M für ein Speziallager der letzten Epoche, vor dem Jahresfaktor.

- Das erste **Flugfeld** (bis 1950) nutzt schon das ×3 der zweiten Epoche: Seine Prüfung liest das Endjahr der Variante statt des Startjahres (`airfield.tl:8`, `airfield_era_a.metacon.tl:3`).

## Fahrzeuge

Kein Fahrzeug des Grundspiels hat einen festen Preis: Das Spiel berechnet ihn aus Geschwindigkeit und Kapazität, wenn es das Modell lädt (`model_metadata_util.lua:488-552`):

1. **Betriebskosten pro Jahr** = etwa 675 × Durchschnittsgeschwindigkeit (m/s) × Kapazität / 4 (`model_metadata_util.lua:499-518`). Die 675 kommen aus der durchschnittlichen Einnahme pro km, verringert, um Leerfahrten, den Kauf und die sinkenden Ticketpreise zu berücksichtigen (`model_metadata_util.lua:500-508`).
2. Die **Durchschnittsgeschwindigkeit** liegt unter der Höchstgeschwindigkeit (v in km/h): Straßenfahrzeuge und Trams v^0,78 + 4, Züge v^0,86 + 10, Flugzeuge −0,0000203 × v² + 0,17 × v + 28,36 (v höchstens 4.000), Schiffe 65 % der Höchstgeschwindigkeit (`model_metadata_util.lua:448-474`).
3. **Züge**: Ein Wagen zählt die Hälfte seiner Kapazität; eine Lok zählt zusätzlich Leistung ÷ Höchstgeschwindigkeit (km/h) × 12,5 als Kapazität, ebenfalls halbiert (`model_metadata_util.lua:511-512`, `model_metadata_util.lua:526-540`). Eine starke, langsame Lok ist teuer.
4. **Preis** = **6 ×** die jährlichen Betriebskosten (`model_metadata_util.lua:548-549`).

Beispiel bei 100 %: Ein Bus mit 35 km/h für 48 Passagiere kostet etwa 45.000 pro Jahr im Betrieb und etwa 270.000 im Kauf.

- Der Zustand eines Fahrzeugs hat fünf Stufen (100–80 %, dann alle 20 %) (`vehicle_store_util.tl:231-234`); bei **20 %** warnt das Spiel, bis er wieder über 30 % liegt (`notifications.script.tl:310-318`).

```engine
Wie schnell der Zustand eines Fahrzeugs sinkt, wie stark die Betriebskosten dadurch steigen und ob sich Fahrzeugpreise mit dem Jahr ändern, sind Werte der Engine (getMaintenanceRunningCostPenalty und die anderen Abzüge); die Skripte skalieren sie nur mit dem Fahrzeugwartungseffekt.
```

## Darlehen

```diagram loan_interest
```

| Art | Betrag um 1960 (×0,4 im Jahr 1900, ×2,4 im Jahr 2020) | Laufzeit | Zinssatz | Quelle |
|---|---|---|---|---|
| Klein | 5–10 M | 1–5 Jahre | 3–5 % | `loan_util.tl:12-22` |
| Mittel | 15–25 M | 3–8 Jahre | 5–8 % | `loan_util.tl:24-34` |
| Groß | 30–50 M | 5–12 Jahre | 8–10 % | `loan_util.tl:36-46` |
| Sehr groß | 40–60 M | 10–24 Jahre | 10–12 % | `loan_util.tl:48-58` |

- Die Karte nennt ihn **Jährlicher Zinsfuss**, aber der Satz wird **einmal** auf den Betrag angewandt: Die Zinsen insgesamt sind Betrag × Satz, unabhängig von der Laufzeit. Sie werden in gleichen Teilen jeden Monat mit der Tilgung bezahlt (`loan_util.tl:102-111`, `loan_util.tl:126-136`, `loan.script.tl:83-99`). Ein langes Darlehen ist deshalb pro Jahr billiger als ein kurzes mit demselben Satz.
- **Zurückzahlen** zahlt nur den Rest der Tilgung: Die restlichen Zinsen entfallen (`loan.script.tl:171-190`). Der Knopf braucht diesen Betrag in bar (`finances_loan_gui.tl:284-286`).
- Die Zinssätze hängen **nicht** vom Schwierigkeitsgrad ab: Jede Art hat ihre eigene feste Spanne (`loan_util.tl:12-58`).
- Höchstens **4 Darlehen** gleichzeitig (`loan_util.tl:4`, `loan.script.tl:134`). Ein Angebot wird nach einem halben Jahr ersetzt; der Platz eines genommenen Darlehens bleibt 4 bis 8 Monate leer (`loan.script.tl:61-76`, `loan.script.tl:150`).
- Zu Spielbeginn bekommt jeder der vier Plätze die Werte einer zufälligen Art, das erste „kleine" Angebot kann also ein großes Darlehen sein; sobald ein Angebot erneuert wird, bietet jeder Platz seine eigene Art (`loan_util.tl:60-74`, `loan.script.tl:63-75`).

```tip scripts
**Nimm den längsten Kredit und zahle früh zurück.** Die Zinsen insgesamt sind bei jeder Laufzeit gleich, die Monatsraten kleiner, und Zurückzahlen streicht die restlichen Zinsen.
```

## Gut zu wissen

- Nimm das **längste** Darlehen, das du bekommst: Die Zinsen sind insgesamt gleich, auf mehr Monate verteilt, und du kannst vorzeitig zurückzahlen, ohne den Rest zu zahlen.
- Gebäude mit Epochenvarianten kosten in späteren Epochen ×3 und ×9, und ihr Unterhalt steigt weiter mit dem Jahr: Ein Speziallager der letzten Epoche ist ein großer Fixkostenblock.
- Ein schnelles Fahrzeug mit großer Kapazität kostet mehr im Betrieb, transportiert aber auch mehr: Preis und Betriebskosten folgen Geschwindigkeit × Kapazität, wie die Einnahmen, die es erzielen kann.

```check
official: "It is recommended to pay back the loan as soon as possible because there is a monthly interest rate. How high this rate is depends on the level of difficulty." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Der Zinssatz eines Darlehens hängt nur von seiner Art ab (3–12 %), nicht vom Schwierigkeitsgrad, und er wird einmal auf den Betrag angewandt, verteilt auf die Monate der Laufzeit; vorzeitiges Zurückzahlen streicht die restlichen Zinsen. Inflation ändert nur die Einnahmen; der Gebäudeunterhalt folgt dem Jahr (×1 bis ×6); Fahrzeugpreis = 6 × jährliche Betriebskosten, beide aus Geschwindigkeit und Kapazität.
result: differs
```
