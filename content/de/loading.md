---
title: Lade- und Entladegeschwindigkeit
summary: Was ein Fahrzeug an einem Halt schnell oder langsam laden lässt: das Fahrzeug, die Bahnsteigabschnitte und das Lager, das die Fracht gibt oder nimmt.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-14
---

Die Zeit, die ein Fahrzeug zum Laden oder Entladen braucht, ist seine eigene Ladegeschwindigkeit mal zwei Faktoren: einer für den **Bahnsteig**, einer für das **Lager** auf der anderen Seite (Lager, Industrie, Stadt).

```diagram loading_factors
```

## 1. Das Fahrzeug

Jedes Fahrzeug hat eine Grund-Ladegeschwindigkeit, angezeigt im Fahrzeugkauf und im Fahrzeugfenster („2.0x“). Alles Folgende multipliziert sie.

## 2. Der Bahnsteigfaktor

Für das Spiel ist ein Bahnsteig keine Reihe von Modulen, sondern eine **Liste von Abschnitten, einer pro Frachtklasse**, mit den addierten Längen aller Module dieser Klasse.

```diagram loading_sections
```

| Wagen… | Faktor | Quelle |
|---|---|---|
| auf einem Abschnitt ihrer Klasse (Schüttgutwagen, Schüttgut-Abschnitt) | **×2** | `modular_station.script.lua:1042` |
| auf einem Universalabschnitt | ×1 | `modular_station.script.lua:1042` |
| ohne Abschnitt ihrer Klasse am Bahnsteig | **×0,25** | `cargo_react_util.tl:60` |
| jenseits der Bahnsteiglänge (Zug zu lang) | **×0,25** | `cargo_react_util.tl:61` |

- Der Faktor ist eine **Mischung nach Anteil am Zug**: passen 3/4 der Wagen und 1/4 nicht, ist der Faktor ¾ × 2 + ¼ × 0,25 ≈ ×1,56 (`cargo_react_util.tl:63-70`, dieselbe Aufteilung, die das Spiel als „Teilweise spezialisiertes Terminal“ zeigt).
- **Wo** die Wagen am Bahnsteig stehen, zählt nicht, nur die addierten Längen (im Spiel gemessen).
- Straße: spezialisierte LKW-Terminals geben ×2 (`modular_terminal.script.lua:2956`); die kleinen Straßenhaltestellen sind immer ×1 (`small_stops.script.lua:19`).
- Personenbahnsteige sind ×1.

## 3. Der Lagerfaktor

Beim Entladen geht jede Einheit an einen Empfänger: ein Lagermodul, eine Industrie oder ein Stadtgebäude. Das Lager des Empfängers hat seinen eigenen Faktor.

| Empfänger | Faktor | Quelle |
|---|---|---|
| **spezialisiertes** Lagermodul (Flüssig, Schüttgut, Flachwagen, Stückgut) | **×2** | `modules.script.lua:120`, `warehouse.script.lua:297-314` |
| **Universal**lager | ×1 | `warehouse.script.lua:272-285` |
| Industrie | ×1 | im Spiel gemessen |

- Jedes Lagermodul verlangt ×2, aber Universalmodule fügen nur Kapazität zu **einem gemeinsamen Universallager** hinzu, das mit ×1 angelegt wird. Nur spezialisierte Module haben ein eigenes Lager mit ×2.
- Der Tooltip des Spiels nennt diesen Faktor „Spezialisiertes Lager: +100 %“ (`cargo_react_util.tl:51-54`).
- Während eines Entladevorgangs bedient das Spiel die Empfänger **abwechselnd**: die Geschwindigkeit ändert sich beim Entladen, wenn ein Teil der Fracht in ein Lager und ein Teil in eine Industrie geht (im Spiel gemessen).

```engine
Welcher Empfänger jede Einheit bekommt und die endgültige Multiplikation geschehen in der Engine. Die Faktoren oben sind die Eingaben der Skripte; das Ergebnis wurde mit den Werten geprüft, die die Engine bereitstellt (Platform-Details-Sonde, Oktober 2026).
```

## Was das Spiel zeigt

- Die Ladeanzeige wird über ×1,5 als **beschleunigt** und unter ×0,75 als **verlangsamt** dargestellt (`cargo_react_util.tl:119-122`).
- Fahr mit der Maus darüber: der Tooltip listet „Spezialisiertes Terminal“, „Spezialisierungen stimmen nicht überein“, „Terminal zu kurz“ und „Spezialisiertes Lager“, jeweils mit Prozentwert (`cargo_react_util.tl:76-99`).

## Beispiel

Ein Zug mit 8 Schüttgutwagen, 160 m lang, entlädt Kohle.

| Bahnhof | Bahnsteig | Empfänger | Faktor |
|---|---|---|---|
| Universalbahnsteig 160 m | ×1 | Stahlwerk | **×1** |
| Schüttgut-Bahnsteig 160 m | ×2 | Stahlwerk | **×2** |
| Schüttgut-Bahnsteig 160 m | ×2 | spezialisiertes Schüttgutlager | **×4** |
| Schüttgut-Bahnsteig 160 m | ×2 | Universallager | **×2** |
| Universalbahnsteig 120 m (Zug 40 m zu lang) | ¾ × 1 + ¼ × 0,25 ≈ ×0,81 | Stahlwerk | **×0,81** |

## Gut zu wissen

- Bahnhöfe innerhalb einer Industrie sind immer auf die Fracht spezialisiert, die die Industrie braucht (offizielles Wiki).
- Spezialisierte Lagermodule frieren außerdem die Lieferfrist der gelagerten Fracht ein (offizielles Wiki); ein Universallager nicht.
- Platform Details zeigt beide Faktoren jedes Fahrzeugs am Bahnsteig und wohin die entladene Fracht ging.

```check
official: „Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization.“ Spezialisierte Lager „enable faster loading / unloading speeds“. ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Spezialisierter Abschnitt ×2, universal ×1, kein passender Abschnitt ×0,25, jenseits des Bahnsteigs ×0,25, gemischt nach Anteil am Zug; spezialisiertes Lagermodul ×2, Universallager ×1.
result: refines
```
