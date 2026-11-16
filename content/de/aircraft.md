---
title: Flugzeuge, Flughäfen und Hubschrauber
summary: Flugplatz oder Flughafen, welches Flugzeug wo landet, Terminals, die zweite Landebahn, Heliports, und die Liste aller Luftfahrzeuge mit Fracht, Kapazität und Geschwindigkeit.
domain: stations
official: gamemanual:infrastructure:stationsdepots
status: verified
updated: 2026-11-15
fact: 2 | Flugzeuggrößen: klein und groß
fact: 1950 | erster Flughafen und erste Hubschrauber
fact: 1980 | zweite Landebahn
fact: 5 | Luftfahrzeuge pro Hangar
---

Jedes Flugzeug ist **klein** oder **groß**. Ein **Flugplatz** nimmt nur kleine Flugzeuge an; ein **Flughafen** nimmt beide an, und Hubschrauber an seinem Hauptgebäude. Hubschrauber haben auch eigene Stationen.

```diagram air_access
```

## Flugplatz und Flughafen

- **Flugplatz**: „Flugplatz mit einer Landebahn für kleine Flugzeuge.“ Varianten von 1920, 1950 und 1980; 1, 2 oder 3 Terminals und ein optionales Depot (`airfield.tl:49`, `airfield.tl:76`, `airfield_era_a.metacon.tl:3`).
- **Flughafen**: „Flughafen mit bis zu zwei Landebahnen für Flugzeuge.“ Varianten von 1950 und 1980; 2, 3 oder 4 Terminals und eine Landungsrichtung (`airport.tl:24`, `airport.tl:80`, `airport1950.metacon.tl:3-4`).
- Flugplatz-Terminals nehmen nur kleine Flugzeuge an; Flughafen-Terminals nehmen beide Größen an (`af_terminal.module.lua:715`, `ap_terminal.module.lua:897`).
- Das Hauptgebäude des Flughafens hat Hubschrauberlandeplätze (`ap_main.module.lua:532`), und ab 1950 kann ein Flughafen ein Hubschrauber-Terminal bekommen (`ap_terminal_heli.module.lua:897`, `ap_terminal_heli.module.lua:971`).
- **Zweite Landebahn**: ein Flughafenmodul ab 1980 (`airport_2nd_runway.module.lua:5`). Manche Flughafenmodule brauchen sie und zeigen ohne sie „Zweite Landebahn benötigt“ (`airport.script.lua:261`).
- Alle Luftstationen nehmen Passagiere und alle Güter an (`airfield.tl:59`, `airport.tl:34`).

| Gebäude | Wartende Passagiere | Quelle |
|---|---|---|
| Flugplatz-Terminal | bis zu 250 | `af_terminal.module.lua:773` |
| Hauptgebäude des Flughafens | bis zu 400 | `ap_main.module.lua:667` |
| Flughafen-Terminal | bis zu 850 | `ap_terminal.module.lua:951` |
| Hubschrauber-Terminal des Flughafens | bis zu 450 | `ap_terminal_heli.module.lua:990` |

## Hangars und Hubschrauberstationen

- Ein **Hangar** an Flugplatz oder Flughafen fasst 5 Luftfahrzeuge und wartet Luftfahrzeuge in einem Radius von 550 m (`af_hangar.module.lua:273-278`, `ap_hangar.module.lua:456-461`).
- **Heliport** (ab 1950): kauft und wartet Hubschrauber, Depot für 5, Wartungsradius 800 m (`heliport.script.lua:301-306`).
- **Helipad** (ab 1950): ein kleiner Landeplatz für Passagiere und Güter, ohne Depot (`helipad.con.lua:29-33`).

## Kosten

Preis und Unterhalt der ersten Variante. Spätere Varianten kosten ×3 oder ×9 ([Kosten, Unterhalt und Darlehen](costs.html)); der erste Flugplatz nutzt bereits ×3 (`airfield.tl:8`).

| Gebäude | Preis | Unterhalt pro Jahr | Quelle |
|---|---|---|---|
| Flugplatz | 1.200.000 - 3.000.000 | 50.000 - 200.000 | `airfield.tl:55-56` |
| Flughafen | 1.800.000 - 4.500.000 | 300.000 - 750.000 | `airport.tl:30-31` |
| Flugplatzmodul (Hauptgebäude, Terminal, Hangar) | 600.000 | 100.000 | `af_main.module.lua:316-317`, `af_hangar.module.lua:326-327` |
| Flughafenmodul (Terminal, Hangar, zweite Landebahn) | 900.000 | 150.000 | `ap_main.module.lua:672-673`, `ap_hangar.module.lua:508-509`, `airport_2nd_runway.module.lua:27-28` |

- Der Unterhalt von Flughäfen und Flugplätzen folgt auch dem Kalenderjahr, ×1 im Jahr 1900 bis ×6 im Jahr 2020 ([Kosten, Unterhalt und Darlehen](costs.html)).
- Preis und Betriebskosten eines Luftfahrzeugs werden aus Geschwindigkeit und Kapazität berechnet, wie bei Schiffen und Straßenfahrzeugen ([Kosten, Unterhalt und Darlehen](costs.html)).

## Alle Flugzeuge

Geschwindigkeit in km/h, gerundet. „Alle Güter“ heißt jede Güterart. Die Kapazität ist die Summe, die der Fahrzeugkauf zeigt: alle Abteile zusammen, jedes mit seiner größten Ladekonfiguration (`vehicle_store_util.tl:70-95`).

| Flugzeug | Jahre | Größe | Fracht | Kapazität | Geschwindigkeit | Ladegeschwindigkeit |
|---|---|---|---|---|---|---|
| Junkers F 13 Herta | 1920-1950 | klein | Passagiere | 16 | 135 | - |
| Vickers J6860 Victoria | 1922-1960 | klein | alle Güter | 32 | 150 | 2,5 |
| Fokker F VII A | 1925-1960 | klein | Passagiere | 32 | 175 | 2 |
| Junkers JU-52 Tante Ju | 1933-1982 | klein | Passagiere, alle Güter | **48** (2 × 24) | 200 | 3 |
| Douglas DC-3 | 1935-1995 | klein | Passagiere | 56 | 300 | 2,5 |
| Curtiss C-46 Commando | 1942-1980 | klein | alle Güter | 80 | 280 | - |
| Douglas DC-4 | 1944-1998 | klein | Passagiere | 100 | 365 | 3 |
| Bristol Typ 170 Frachter | 1949-2005 | klein | Passagiere, alle Güter | **80** (2 × 40) | 350 | 1,5 |
| Lockheed L-1049 Super Connie | 1952-1986 | groß | Passagiere | 120 | 486 | 3 |
| Lockheed L-1049D/H Super Connie | 1959-2000 | groß | alle Güter | **120** (2 × 60) | 486 | 2,5 |
| De Havilland DH.106 Comet | 1960-2000 | groß | Passagiere | 160 | 724 | 3 |
| Canadair CL-44 Frachter | 1962-2005 | groß | alle Güter | **144** (3 × 48) | 645 | 2 |
| Convair CV 990 Coronado | 1962-2020 | groß | Passagiere | 200 | 917 | 2 |
| Lockheed L-100 Hercules | 1976-2000 | klein | alle Güter | **132** (3 × 44) | 400 | 3 |
| McDonnell Douglas DC-10-30 | 1978- | groß | Passagiere | 400 | 960 | 2,5 |
| McDonnell Douglas DC-10-30CF | 1978- | groß | alle Güter | **396** (3 × 132) | 960 | 4 |
| Airbus A310 300F Frachter | 1982- | groß | alle Güter | 160 | 850 | 3 |
| Short 330 Sherpa | 1984- | klein | Passagiere, alle Güter | **80** (2 × 40) | 455 | 2,5 |
| Airbus A320 | 1985- | groß | Passagiere | 180 | 753 | 3 |
| Br. Aerospace 146 | 1985- | klein | Passagiere | 112 | 753 | 3 |
| Br. Aerospace 146 Frachter | 1985- | klein | alle Güter | **96** (2 × 48) | 753 | 2 |
| Fokker 100 | 1988- | groß | Passagiere | 160 | 845 | 3,5 |
| Tupolev Tu-204 | 1995- | groß | Passagiere | 280 | 850 | 4 |
| Tupolev Tu-204C Frachter | 1995- | groß | alle Güter | **204** (3 × 68) | 850 | 2 |
| Boeing 737-700 | 1998- | groß | Passagiere | 200 | 974 | 2,5 |
| Boeing 737-700-C Frachter | 1998- | groß | alle Güter | **160** (2 × 80) | 974 | 3 |
| Bombardier DHC-8 | 2000- | klein | Passagiere | 120 | 648 | 3 |
| Bombardier DHC-8 Frachter | 2008- | klein | alle Güter | 120 | 648 | 2 |
| Sukhoi Superjet 100 | 2011- | klein | Passagiere | 160 | 870 | 3 |
| Airbus Canada A220 | 2013- | groß | Passagiere | 180 | 830 | 5 |

## Alle Hubschrauber

| Hubschrauber | Jahre | Fracht | Kapazität | Geschwindigkeit | Ladegeschwindigkeit |
|---|---|---|---|---|---|
| Bell 47 | 1950-1990 | Passagiere, alle Güter | 8 | 150 | 2 |
| Piasecki H-21 Workhorse | 1952-1985 | Passagiere, alle Güter | 80 (48 Güter) | 210 | 3 |
| Sikorsky S-64 Skycrane | 1962-2017 | alle Güter | 40 | 213 | 4 |
| Bell 206 Long Ranger | 1965-2025 | Passagiere | 32 | 241 | 2,5 |
| Boeing Vertol 234 Chinook | 1980- | Passagiere, alle Güter | 80 | 269 | 2 |
| AgustaWestland AW101 Merlin | 1990- | Passagiere | 60 | 278 | 3 |
| Mil Mi-26TC | 1993- | alle Güter | 120 | 295 | 4 |
| Eurocopter 120B Colibri | 1998- | Passagiere | 48 | 210 | 3 |
| Kaman K-MAX | 2005- | alle Güter | 60 | 190 | 3 |
| Airbus H225 Super Puma | 2013- | Passagiere | 48 | 288 | 3 |
| NextGen Senkrechtstarter | 2030- | Passagiere | 56 | 610 | 4 |

## Gut zu wissen

- **Kleine Flugzeuge bleiben bis zum Ende nützlich.** Die DHC-8, ihr Frachter und der Sukhoi Superjet 100 sind klein, also reicht ihnen ein Flugplatz.
- **Vor 1952 gibt es kein großes Flugzeug**, ein früher Flughafen bringt also noch keinen Zugang zu größeren Maschinen.
- Flugzeuge fliegen in gerader Linie, und die Bezahlung zählt nur die Luftlinie, ein Umweg kostet sie also nichts extra ([Gütereinnahmen und Lieferzeit](income.html)).
- Mindestlänge der Landebahn, Flugbahnen und Landung entscheidet die Spiel-Engine; die Skripte zeigen sie nicht.

```check
official: "It can be used by small airplanes." (Airfield) "It can be used by small and large airplanes." (Airport), build menu descriptions.
scripts: Gleich: Flugplatz-Terminals nehmen nur SMALL_AIRCRAFT an, Flughafen-Terminals AIRCRAFT und SMALL_AIRCRAFT, Hubschrauber am Hauptgebäude des Flughafens, Heliport und Helipad ab 1950, zweite Landebahn ab 1980, Hangars für 5; 15 kleine und 15 große Flugzeuge und 11 Hubschrauber im Basisspiel.
result: agrees
```
