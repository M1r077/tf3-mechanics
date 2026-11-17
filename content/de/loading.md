---
title: Lade- und Entladegeschwindigkeit
summary: Was ein Fahrzeug an einem Halt schnell oder langsam laden lässt: das Fahrzeug, die Bahnsteigabschnitte und das Lager, das die Fracht gibt oder nimmt.
domain: stations
official: gamemanual:management:linesvehicles#loading_speed
status: verified
updated: 2026-11-15
game: 40425
fact: ×2 | spezialisierter Bahnsteigabschnitt
fact: ×0,25 | falscher Abschnitt oder Zug zu lang
fact: ×4 | bestenfalls: Bahnsteig und Lager spezialisiert
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
| ohne Abschnitt ihrer Klasse am Bahnsteig | **×0,25** (Konstante des Lade-Tooltips; den Faktor selbst wendet die Engine an) | `cargo_react_util.tl:60` |
| jenseits der Bahnsteiglänge (Zug zu lang) | **×0,25** (Konstante des Lade-Tooltips; den Faktor selbst wendet die Engine an) | `cargo_react_util.tl:61` |

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

## Wo die Fracht entladen wird

Jeder Halt einer Linie hat eine Liste **Ladung**, im Fenster „Güterfilter“ des Halts. Am Halt behält das Fahrzeug die Fracht dieser Liste an Bord; der Rest wird in jeden Bestand im Einzugsbereich entladen, der sie annimmt, auch in ein Lager (im Spiel gemessen).

- So leert sich ein Zug mitten auf seiner Linie in ein Lager. Im Spiel: An einem Halt neben einem Lager, mit nur Kunststoff in der Liste, gingen die Werkzeuge an Bord ins Lager, obwohl es fast voll war.
- Ein Personenbahnsteig hat keinen Güterumschlag: Die Fracht bleibt dort an Bord (im Spiel gemessen).
- Um die Fracht an Bord zu behalten, füge sie der Liste Ladung dieses Halts hinzu.

```tip
**Fracht verschwindet an einem Halt neben einem Lager? Nimm sie in die Liste Ladung dieses Halts auf.** Alles, was nicht in der Liste steht, wird in einen Bestand in Reichweite entladen, und das Lager zahlt nichts dafür.
```

| Option im „Güterfilter“ | Wirkung | Quelle |
|---|---|---|
| „Entladen aller Güter nach Ankunft erzwingen“ | Tooltip: „Güter auch bei vollen Beständen entladen“; die Güter, die nicht hineinpassen, werden vernichtet: Das Spiel nennt den Bahnhof als Ziel, und ein Bahnhof verbraucht nie Fracht (im Spiel gemessen). Bei einem neuen Halt aus. | `cargofilter_window.tl:757`, `line_util.tl:476` |
| „Bei Konfigurationsänderung Güter nach Ankunft zerstören“ | entlädt oder zerstört die Fracht an Bord, wenn an diesem Halt Fracht für eine andere Ladekonfiguration des Fahrzeugs wartet; was davon geschieht, entscheidet die Engine | `cargofilter_window.tl:767` |
| „Durch neuere Güter ersetzen, falls verfügbar“ | zerstört Fracht, die zu dem Halt zurückgekommen ist, an dem sie geladen wurde, wenn neuere Fracht derselben Art wartet | `cargofilter_window.tl:778` |

- Ist die erste Option aus, zeigt das Frachtsymbol „≤“ und der Tooltip „Entladen nur, wenn Lagerkapazität vorhanden“ (`cargofilter_window.tl:124`, `cargofilter_window.tl:158`).

## Mehrere Frachten auf einer Linie

- Die Liste **Ladung** eines Halts ist ein Ja/Nein pro Güterart, **ohne Reihenfolge**: Der Spieler kann nicht festlegen, welche Fracht zuerst geladen wird. Die Symbole werden einfach in der Güterreihenfolge des Spiels gezeichnet (`line_util.tl:471-475`, `line_util.tl:510`, `cargofilter_window.tl:533-535`).
- Ein Wagen oder Lkw, der mehrere Frachten aufnimmt, hat pro Abteil mehrere **Ladekonfigurationen**; die Kapazität des Abteils ist die größte davon, nicht ihre Summe (`model_metadata_util.lua:682-733`, `vehicle_metadata_util.lua:27-37`). Er transportiert also jeweils nur eine davon.
- Bei neuen Fahrzeugen ist die automatische Wahl der Konfiguration für jedes Abteil eingeschaltet (`vehicle_react_util.tl:339`), und das Spiel hat kein Fenster, um die Fracht eines Fahrzeugs von Hand zu wählen.
- Passagiere und Fracht können sich eine Linie teilen: Die Skripte lehnen Fracht an einem Halt nie ab, weil er auch Passagiere aufnimmt (`line_util.tl:1381-1386`). Fracht wird nur an einem Halt gestrichen, dessen Terminal keine Fracht laden oder entladen kann (`line_util.tl:554-559`).
- Bei mehreren Frachten verhalten sich **Vollladen einer Güterart** und **Vollladen jeder Güterart** unterschiedlich: siehe [Abfahrtseinstellungen: Vollladen, Füllstand und Haltezeiten](departure.html).
- Passt die Konfiguration nicht, zeigt die Linie **Einige Gütertyp-Konfigurationen dieser Linie stehen in Konflikt**, zum Beispiel "Ein konfigurierter Gütertyp der Linie kann von keinem Fahrzeug transportiert werden." (`line_warning.script.tl:10-36`).

```engine
In welcher Reihenfolge mehrere Frachten geladen werden, wie ein gemeinsamer Bestand auf wartende Fahrzeuge aufgeteilt wird und wie ein Fahrzeug seine Ladekonfiguration wählt, entscheidet die Engine.
```

## Die automatische Konfiguration

Solange niemand eine Änderung im Fenster „Güterfilter“ eines Halts gespeichert hat, was sie auf dieser Linie für immer abschaltet (`line_util.tl:495-498`, `cargofilter_window.tl:438`), füllt das Spiel die Listen Ladung selbst, jedes Mal wenn die Linie erstellt, ein Halt hinzugefügt oder entfernt, die Halte umsortiert oder ein Wegpunkt hinzugefügt wird (`manager_window.tl:6712`, `:6786`, `:6845`, `:6879`, `:6963`). Einen Halt an einen anderen Bahnhof oder Bahnsteig zu verschieben sowie einen Wegpunkt zu entfernen oder zu verschieben, startet sie nicht (`manager_window.tl:6851-6868`, `manager_window.tl:6968-6992`).

- Sie beginnt wieder mit leeren Listen, mit Passagieren an Personenbahnhöfen (`line_util.tl:542-588`).
- Sie sucht Erzeuger und Abnehmer nur unter Industrien und Stadtgebäuden: Lager zählen nicht (`cargo_util.tl:518-526`).
- Sie setzt eine Fracht auf die Liste Ladung eines Halts, wenn die Fracht weiter hinten gebraucht wird und am Halt nichts sie annimmt. Ein Lager zählt so, als nehme es alles an, was es lagert (`line_util.tl:676-693`): An einem Halt neben einem Lager, das die Fracht lagert, bleibt sie von der Liste, und der Zug entlädt sie dort.
- Sobald ein Filter von Hand geändert wurde, ist die Linie als angepasst markiert (`cargofilter_window.tl:438`), und die automatische Konfiguration fasst sie nie wieder an, auch nicht, wenn später Halte hinzukommen (`line_util.tl:496`).

```engine
Die Skripte schreiben nur die Listen Ladung; das Entladen selbst macht die Engine. Die Regel oben (was nicht auf der Liste steht, wird in jeden Bestand entladen, der es annimmt) wurde im Spiel mit [Platform Details](https://mod.io/g/transportfever3/m/platform-details) beobachtet, November 2026.
```

## Gut zu wissen

- Bahnhöfe innerhalb einer Industrie sind immer auf die Fracht spezialisiert, die die Industrie braucht (offizielles Wiki).
- Spezialisierte Lagermodule frieren außerdem die Lieferfrist der gelagerten Fracht ein (offizielles Wiki); ein Universallager nicht.
- [Platform Details](https://mod.io/g/transportfever3/m/platform-details) zeigt beide Faktoren jedes Fahrzeugs am Bahnsteig und wohin die entladene Fracht ging.

```check
official: „Loading speed is also influenced by the vehicle's specialization, the terminal's specialization and where applicable, a warehouse's specialization.“ Spezialisierte Lager „enable faster loading / unloading speeds“. ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles), [Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Spezialisierter Abschnitt ×2, universal ×1, kein passender Abschnitt ×0,25, jenseits des Bahnsteigs ×0,25, gemischt nach Anteil am Zug; spezialisiertes Lagermodul ×2, Universallager ×1.
result: refines
```
