---
title: Lager
summary: Universal- oder spezialisierte Module, was jedes Lager fasst, eine Frachtart festlegen, Ladegeschwindigkeit, Kosten und Verschmutzung, und was ein Lager nicht tut.
domain: warehouses
official: gamemanual:infrastructure:warehouses
status: verified
updated: 2026-11-16
fact: 500 | Einheiten Fracht pro Modul, egal welcher Art
fact: ×2 | Ladegeschwindigkeit an einem spezialisierten Modul, ×1 an einem Universalmodul
fact: 150.000 / 300.000 | Preis eines Universal- / spezialisierten Moduls
fact: 0 | Einnahmen für Fracht, die in einem Lager entladen wird
---

Ein Lager ist ein Eingang und eine Reihe von **Modulen**. Es lagert Fracht zwischen zwei Linien: Eine Linie entlädt sie, eine andere lädt sie wieder. Bahnhöfe erreichen es über ihren Einzugsbereich; Städte und Industrien nehmen nie etwas daraus (offizielles Wiki).

## Universal- oder spezialisierte Module

| Modul | Bestand | Fasst | Ladefaktor | Quelle |
|---|---|---|---|---|
| **Mehrzwecklager** | alle Universalmodule teilen sich **einen** Bestand | jede Fracht, gemischt | ×1 | `warehouse.script.lua:272-295`, `modules.script.lua:49` |
| **Flüssiggutlager**, **Schüttgutlager**, **Sperrgutlager**, **Stückgutlager** | **ein Bestand pro Modul** | jeweils eine Frachtart, aus seiner Klasse | ×2 | `warehouse.script.lua:296-314`, `modules.script.lua:120`, `modules.script.lua:165`, `modules.script.lua:247`, `modules.script.lua:296` |

- Jedes Modul fügt **500** Einheiten hinzu (`modules.script.lua:49`, `modules.script.lua:120`). Fünf Universalmodule ergeben einen Bestand von 2.500; fünf Flüssiggutmodule ergeben fünf Bestände von 500.
- Passagiere werden nie gelagert (`warehouse.script.lua:279`, `warehouse.script.lua:304`).
- Ein spezialisiertes Modul nimmt jeweils nur eine Frachtart: Für Rohöl und Kraftstoff brauchst du zwei Flüssiggutmodule (offizielles Wiki).
- Das ×2 eines spezialisierten Moduls multipliziert sich mit dem Bahnsteigfaktor: Ein Schüttgut-Bahnsteig und ein Schüttgutmodul ergeben ×4. Details: [Lade- und Entladegeschwindigkeit](loading.html).

## Universal oder spezialisiert?

1. **Viele Frachtarten, kleine Mengen**: universal. Ein gemeinsamer Bestand, halber Preis und halbe Verschmutzung.
2. **Eine Fracht in großen Mengen** (Kohle, Rohöl, Baumstämme): spezialisiert. Fahrzeuge entladen und laden dort doppelt so schnell, aber du brauchst ein Modul pro Frachtart.
3. **Lebensmittel und andere Fracht mit kurzer Lieferzeit**: spezialisiert; laut offiziellem Wiki frieren diese Module die Lieferfrist ein (siehe unten).
4. Beide Arten lassen sich in einem Lager mischen: Die Universalmodule bilden weiter einen Bestand, jedes spezialisierte Modul seinen eigenen.

## Beschleunigt ein Lager das Entladen?

- **Spezialisiertes Modul**: ja, ×2 für die Fracht, die es nimmt. Der Lade-Tooltip des Fahrzeugs zeigt „Spezialisiertes Lager: +100 %“ (`cargo_react_util.tl:51-54`).
- **Universalmodul**: nein. Sein Bestand wird mit ×1 angelegt; das vom Modul verlangte ×2 wird ignoriert (`warehouse.script.lua:284`, `warehouse.script.lua:288-289`).
- Geht ein Teil der Fracht in ein Lager und ein Teil in eine Industrie, bedient das Fahrzeug sie abwechselnd, also ändert sich die Geschwindigkeit während eines Halts (im Spiel gemessen, siehe [Lade- und Entladegeschwindigkeit](loading.html)).

## Der Bereich Bestände

- Eine Zeile pro Bestand: die Fracht, die er nimmt, die Menge, und beim Darüberfahren die **Durchschnittliche verbleibende Lieferzeit** (`entity_window_util.tl:408-410`).
- **Eine Frachtart festlegen**: Klicke an einem spezialisierten Modul auf ein Frachtsymbol. Das Spiel baut das Lager neu, mit diesem Modul für diese Fracht reserviert (`entity_window_util.tl:339-367`, `warehouse.script.lua:308`). Entfernen oder Ersetzen des Moduls hebt die Festlegung auf (`warehouse.script.lua:403-405`).
- **Alle Güter entsorgen**: leert diese Zeile auf einmal (`entity_window_util.tl:423-434`). Die Fracht ist verloren.
- Beide Knöpfe fehlen nur an einem Lager, das einem anderen Spieler gehört; deine Lager und Lager ohne Besitzer haben sie (`warehouse_eow.script.tl:127-137`, `gui/entity_window/warehouse/warehouse.tl:38`, `entity_util.tl:83-86`).
- Das Diagramm **Statistiken** zeigt **Eingehend** (entladen) und **Ausgehend** (geladen) pro Jahr (`warehouse_eow.script.tl:159-160`).

## Kosten und Verschmutzung

| | Universalmodul | Spezialisiertes Modul | Quelle |
|---|---|---|---|
| Preis | 150.000 | 300.000 | `wh_universal.module.lua:18`, `wh_liquid.module.lua:22` |
| Unterhalt pro Jahr | 25.000 | 50.000 | `wh_universal.module.lua:19`, `wh_liquid.module.lua:23` |
| Lärm | 20 | 20 | `wh_universal.module.lua:33`, `wh_liquid.module.lua:37` |
| Verschmutzung | 25 | 50 | `wh_universal.module.lua:34`, `wh_liquid.module.lua:38` |

- Das Lager fügt eigene Verschmutzung hinzu: **25**, oder **50**, sobald ein spezialisiertes Modul gebaut ist (`warehouse.script.lua:327`, `warehouse.script.lua:338-345`).
- Das Baumenü hat einen Eintrag pro Klasse und Epoche (ab 1900, 1940 und 1980) (`warehouses/warehouse.tl:3-5`); spätere Epochen zeigen ×3 und ×9, und der Lagerunterhalt steigt außerdem mit dem Jahr. Details: [Kosten, Unterhalt und Darlehen](costs.html).
- Schüttgut-, Sperrgut- und Stückgutmodule kosten so viel wie Flüssiggutmodule (`wh_bulk.module.lua:22-23`, `wh_flatbed.module.lua:22-23`, `wh_goods.module.lua:18-19`).

```engine
Die Skripte geben zwei Emissionsstufen an, die zweite doppelt so hoch wie die erste (`warehouse.script.lua:342-343`); das Lager geht von der ersten zur zweiten über, je voller seine Lager sind, volle Lager = doppelt (`emissions.script.tl:237-249`). Den tatsächlich berechneten Preis der Module bestimmt die Engine.
```

## Was ein Lager nicht tut

- **Es bringt nichts ein.** Entladen in ein Lager bringt keine Einnahmen; die Einheit wird einmal bezahlt, wenn sie ihren Abnehmer erreicht, für die Luftlinie ab ihrer Quelle (im Spiel gemessen, siehe [Gütereinnahmen und Lieferzeit](income.html)).
- **Es beliefert keine Städte oder Industrien** in seiner Nähe: Sie nehmen Fracht nur von Fahrzeugen (offizielles Wiki).
- **Es ist kein Ziel für die automatische Linienkonfiguration**, die nur Erzeuger und Abnehmer sucht; aber ein Halt neben einem Lager, das eine Fracht lagert, lässt diese Fracht von der Liste Ladung, sodass Züge sie dort entladen (siehe [Lade- und Entladegeschwindigkeit](loading.html)).
- **Es braucht keine Straße.** Der Eingang rastet an einer Straße ein, aber Fracht bewegt sich nur über die Einzugsbereiche von Bahnhöfen (`warehouse.script.lua:386-389`, offizielles Wiki). Das Lagerfenster zeigt seinen Einzugsbereich (`gui/entity_window/warehouse/warehouse.tl:88-96`).

```engine
Wohin entladene Fracht geht und ob die Lieferfrist einer gelagerten Einheit stoppt, entscheidet die Engine. Kein Skript friert die Frist ein: Laut offiziellem Wiki tun spezialisierte Module das, ein Universalmodul nicht.
```

## Gut zu wissen

- Prüfe die Liste Ladung jedes Halts in der Nähe eines Lagers: Was nicht darauf steht, wird ins Lager entladen, auch mitten auf der Linie.
- Ein voller Bestand nimmt keine weitere Fracht an, außer der Halt nutzt „Entladen aller Güter nach Ankunft erzwingen“, was alles zerstört, was nicht hineinpasst (siehe [Lade- und Entladegeschwindigkeit](loading.html)).
- Um ein spezialisiertes Modul für eine Fracht zu behalten, lege seine Frachtart im Bereich Bestände fest.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) listet pro Bahnhof die erreichbaren Lager mit ihren Beständen; [Platform Details](https://mod.io/g/transportfever3/m/platform-details) zeigt, wohin die entladene Fracht ging.

```check
official: „Universal warehouses are a cost-efficient generic solution, because it allows you to store a mix of all cargo types.“ Spezialisierte Lager „freeze the cargo item's delivery timer“ und „enable faster loading / unloading speeds“. „In specialized warehouses, only one cargo type can be stored at a time for a given module.“ ([Warehouses](https://wiki.transportfever3.com/doku.php?id=gamemanual:infrastructure:warehouses))
scripts: Universalmodule bilden einen gemeinsamen Bestand mit Ladefaktor ×1, jedes spezialisierte Modul einen eigenen Bestand von 500 mit ×2 und einer Frachtart. Ein spezialisiertes Modul kostet doppelt so viel (300.000, Unterhalt 50.000) und verschmutzt doppelt so stark (50). Das Einfrieren der Frist steht nicht in den Skripten.
result: refines
```
