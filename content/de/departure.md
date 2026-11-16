---
title: Abfahrtseinstellungen: Vollladen, Füllstand und Haltezeiten
summary: Wann ein Fahrzeug einen Halt verlässt: die drei Abfahrtsmodi, der Füllstand jeder Fracht und die minimale, maximale und zusätzliche Haltezeit.
domain: stations
official: gamemanual:management:linesvehicles
status: verified
updated: 2026-11-15
fact: 600 s | Standard-Max. Haltezeit eines neuen Halts
fact: 30 s / 60 s | Standard-Max. zusätzlicher Aufenthalt, Straße / Schiene
fact: 0–100 % | Füllstand, pro Fracht, der Fahrzeugkapazität
---

Jeder Halt einer Linie hat eigene Abfahrtseinstellungen, im Fenster „Güterfilter“ des Halts (klick den Halt im Linienfenster an). Sie bestimmen, **wie viel** das Fahrzeug dort lädt und **wie lange** es warten darf.

## Die Einstellungen

| Einstellung | Werte | Neuer Halt | Quelle |
|---|---|---|---|
| „Lade wenn vorhanden“, „Vollladen einer Güterart“, „Vollladen jeder Güterart“ | einer von drei | Lade wenn vorhanden (gemessen) | `cargofilter_window.tl:798-821` |
| „Min. Haltezeit“ | 0–600 s, Schritt 10 | 0 s (gemessen) | `cargofilter_window.tl:841-845` |
| „Max. Haltezeit“ | 0–600 s oder „---“ (keine Grenze, Schieberegler am Ende) | **600 s** (gemessen) | `cargofilter_window.tl:855-863` |
| „Max. zusätzlicher Aufenthalt“ | 0–600 s, Schritt 10 | 60 s; 30 s an einem Straßen- oder Straßenbahnbahnhof ohne Schiene | `cargofilter_window.tl:827-831`, `line_util.tl:478-490` |
| „Füllstand“, pro geladener Fracht | 0–100 %, Schritt 1 | 100 % | `cargofilter_window.tl:698-704`, `line_util.tl:472` |

- Ein Klick auf eine Zeit öffnet ein Zahlenfeld: Dort lassen sich Werte über 600 s eingeben (`cargofilter_window.tl:204-208`).
- Die drei Zeiten halten ihre Reihenfolge: Wird das Minimum oder der zusätzliche Aufenthalt über das Maximum gehoben, steigt das Maximum mit (`cargofilter_window.tl:834-835`, `cargofilter_window.tl:848-849`, `cargofilter_window.tl:865-869`).
- Eine Änderung an einer davon markiert die Linie als angepasst: Die automatische Konfiguration fasst ihre Listen Ladung nicht mehr an (`cargofilter_window.tl:438`, siehe [Lade- und Entladegeschwindigkeit](loading.html)). Die automatische Konfiguration selbst ändert nie den Modus oder die Zeiten (`line_util.tl:495-513`).

## Füllstand: eine Obergrenze pro Fracht

Der Füllstand ist das Höchste, was das Fahrzeug von dieser Fracht an diesem Halt nimmt, als Anteil der Fahrzeugkapazität, auf die nächste Einheit gerundet (im Spiel gemessen).

| Fahrzeug | Füllstand | Fährt ab mit |
|---|---|---|
| LKW, 15 Plätze, Holz | 50 % | **8** (7,5 aufgerundet) |
| LKW, 22 Plätze, Stoff | 70 % | jedes Mal **15** (15,4) |
| Zug, 18 Plätze, Glas | 48 % | höchstens **9** (8,64) |
| Straßenbahn, 28 Plätze, Treibstoff | 66 % | höchstens **18** (18,48) |

- Fracht, die schon an Bord ist, zählt mit: Eine Straßenbahn, die mit 14 Treibstoff ankam, fuhr mit 18 ab, nicht mit 14 + 18.
- Über der Grenze wird ihretwegen nichts geladen **und nichts entladen**: Ein LKW, der mit 22 Dünger ankam (Grenze 11), fuhr mit 22 ab.
- **0 %** heißt: diese Fracht hier nicht laden.
- In einem Vollladen-Modus gilt die Grenze als voll: Holz-LKW mit 50 % Füllstand warteten etwa 270 s und fuhren mit 8 von 15 ab, nicht mit 15.
- Es gibt keinen Entlade-Prozentwert. Das Entladen bestimmen die Liste Ladung und „Entladen aller Güter nach Ankunft erzwingen“ ([Lade- und Entladegeschwindigkeit](loading.html)).

## Vollladen und die Haltezeiten

- **Lade wenn vorhanden**: Das Fahrzeug nimmt, was da ist, und fährt ab.
- **Vollladen jeder Güterart**: Das Fahrzeug wartet, bis es voll ist. Holz-LKW warteten 460–566 s und fuhren mit 15 von 15 ab.
- **Vollladen einer Güterart**: Das Fahrzeug fährt ab, wenn eine Fracht voll ist. Ein Zug für Holz und Bretter fuhr nach 369–380 s mit 143 und 144 Holz ab; zwei andere Abfahrten nach etwa 30 s mit 57 und 118 Holz sind nicht erklärt.
- **Max. Haltezeit** beendet das Warten, auch wenn nichts geladen wurde. Ein Gemüsezug mit Vollladen jeder Güterart und 120 s Maximum war entweder in etwa 25 s voll (64 von 64) oder fuhr nach 116–120 s mit 26 oder **0** ab. Mit den standardmäßigen 600 s fuhr er nach 596–600 s mit 26 von 64 ab.
- **Min. Haltezeit** ist der ganze Halt, Laden inklusive, keine zusätzliche Zeit danach: Mit 60 s hielten Glaszüge jedes Mal 55–61 s, egal was sie luden.
- **Max. zusätzlicher Aufenthalt**: „Maximum wait time after loading to improve vehicle distribution“ (`cargofilter_window.tl:828`). Das Fahrzeugfenster zeigt „Sicheren Abstand garantieren“, während es wartet (`entity_window_util.tl:2279-2286`).
- **Mehrere Fahrzeuge an einem Halt laden gleichzeitig**, egal wann jedes ankam (im Spiel gesehen). Zwei Holz-LKW, die etwa 90 s nacheinander ankamen, fuhren in derselben Sekunde ab, jeder mit 8. Wie die Fracht zwischen ihnen aufgeteilt wird, wurde nicht gemessen.

```engine
Die Skripte speichern nur die Einstellungen; wann ein Fahrzeug abfährt, entscheidet die Engine.
```

Die Regeln oben wurden mit der Datenbank von [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) gemessen (Aufnahmen alle 2 s, Haltezeiten also ±2 s), November 2026.

## Gut zu wissen

- Langes Warten mit Vollladen an einem Halt, an dem wenig Fracht ankommt, blockiert den Bahnsteig: Andere Fahrzeuge der Linie stauen sich dahinter.
- Eine kurze Max. Haltezeit mit Vollladen kann Fahrzeuge leer losschicken, wenn sie zurückkommen, bevor neue Fracht da ist.
- Einmal hielt ein Zug mit Vollladen jeder Güterart 783–992 s bei 600 s Maximum. Die Ursache wurde nicht gefunden.

```check
official: „Full load (any): The vehicle will stop and wait until one cargo type is fully loaded. Full load (all): The vehicle will stop and wait until it is fully loaded.“ „In the vanilla game "all" and "any" only applies to trains and ships […] Any other vehicle type will wait for full load in both cases.“ Jede Fracht wird geladen „to what percentage of a vehicle's total capacity“. ([Lines and Vehicles](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:linesvehicles#departure_configuration))
scripts: Drei Abfahrtsmodi, Min. / Max. Haltezeit 0–600 s (oder keine Grenze), Max. zusätzlicher Aufenthalt 0–600 s (60 s, 30 s Straße), Füllstand 0–100 % pro Fracht; gemessen: Der Füllstand begrenzt die Fracht an Bord, auf die nächste Einheit gerundet, und gilt beim Vollladen als voll; die Max. Haltezeit beendet ein Vollladen, auch leer; die Min. Haltezeit schließt das Laden ein; Fahrzeuge an einem Halt laden gemeinsam.
result: refines
```
