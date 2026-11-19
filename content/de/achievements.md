---
title: Erfolge
summary: Was das Spielskript für jeden Erfolg des freien Spiels prüft und wann, welche nur Fahrzeuge, Fracht und Tiere des Grundspiels zählen und welche Prüfungen der Engine überlassen sind.
domain: achievements
official: gamemanual:gamemodes:achievements
status: verified
updated: 2026-11-17
game: 40444
fact: 17 | Erfolge, die das Spielskript selbst freischaltet
fact: 500 m | Höhe des ersten Wagens eines Zuges an einem Halt für Zwischenstopp am Gipfel
fact: < 1 % | Ruf der Stadt für Ich war es nicht
fact: 10 | Wahrzeichen, die dieselbe nächste Stadt haben müssen, für Zentralisiert
---

Das offizielle Wiki listet 41 Erfolge. Das Spielskript (`achievements.script.tl`) schaltet **17** davon selbst frei und speist **9 spielübergreifende Zähler**; die anderen (Kampagne, Wetter, Stadtgrösse, Lagerhaus, Zinsen, Booster, Autos, 1900-2000, Dampf in den 2000ern) werden anderswo geprüft, von der Engine oder der Plattform. Jede Prüfung fragt zuerst die Engine, ob der Erfolg noch freigeschaltet werden kann; ob Mods oder Einstellungen ihn sperren, wird dort entschieden (`achievements.script.tl:632`, `achievements.script.tl:510`).

## Vom Skript geprüfte Erfolge

| Erfolg | Was das Skript prüft | Quelle |
|---|---|---|
| **Paket angekommen** | eine Frachteinheit erreicht ihr Ziel | `achievements.script.tl:221-225`, `achievements.script.tl:632-636` |
| **Im Auftrag von** | eine Subvention abgeschlossen | `achievements.script.tl:241-244`, `achievements.script.tl:638-642` |
| **Subventionsserie** | 10 Subventionen abgeschlossen ohne eine gescheiterte dazwischen; eine gescheiterte Subvention setzt den Zähler auf 0 zurück | `achievements.script.tl:243-249`, `achievements.script.tl:644-648` |
| **Hausmeister** | die Lieferbewertung einer Stadt wechselt zu **Ausgezeichnet** | `achievements.script.tl:270-276`, `towns.script.tl:27-30`, `achievements.script.tl:650-654` |
| **Stadtentwicklung** | eine Stadt steigt eine Stufe auf | `achievements.script.tl:253-255`, `town_growth.script.tl:92` |
| **Gestiegene Nachfrage** | eine Stadt bekommt eine Nachfrage nach einem neuen Frachttyp | `achievements.script.tl:257-259`, `achievements.script.tl:668-672` |
| **Ich war es nicht** | der Ruf einer Stadt **sinkt** unter **1 %** | `achievements.script.tl:261-267`, `towns.script.tl:33-36` |
| **Beförderung** | das Unternehmen steigt einen Rang auf | `achievements.script.tl:280-282`, `achievements.script.tl:680-684` |
| **Karriereleiter** | das Unternehmen erreicht den höchsten Rang | `achievements.script.tl:284-290`, `achievements.script.tl:686-690` |
| **Landschaftsgärtner** | du setzt Bäume, und nur Bäume, in einem Bau (nichts entfernt, nicht durch Aufforstung) | `achievements.script.tl:346-377` |
| **Perfektionist** | dieselbe Station wird abgerissen, neu gebaut, abgerissen und neu gebaut, in dieser Reihenfolge, ohne dass dazwischen eine andere Station gebaut oder entfernt wird | `achievements.script.tl:304-341`, `achievements.script.tl:694-710` |
| **Zentralisiert** | genau 10 fertige Wahrzeichen haben dieselbe nächste Stadt | `achievements.script.tl:382-395`, `achievements.script.tl:713-721` |
| **Zwischenstopp am Gipfel** | einer deiner Züge kommt an einem Halt an, mit seinem ersten Wagen höher als **500 m** | `achievements.script.tl:407-417`, `achievements.script.tl:723-727` |
| **Offshore** | einer deiner Hubschrauber kommt an einem Halt einer Ölplattform an | `achievements.script.tl:420-450`, `achievements.script.tl:729-733` |
| **Museumsflotte** | jedes Schiffsmodell des Grundspiels fährt gleichzeitig auf einer deiner Schiffslinien | `achievements.script.tl:735-776` |
| **Begegnung der dritten Art** | du klickst auf ein UFO | `achievements.script.tl:793-806` |
| **Zeitnehmer** | du änderst die Tageszeit von Hand | `achievements.script.tl:839-844` |

- **Perfektionist** zählt nur einen Bau, der eine ganze Station hinzufügt oder entfernt: ein Gleis oder ein Modul zu einer Station hinzuzufügen zählt nicht (`achievements.script.tl:301-302`).
- **Zentralisiert** zählt jedes Wahrzeichen, wenn es fertig ist, für die Stadt, die ihm in diesem Moment am nächsten ist (`achievements.script.tl:386`).
- **Museumsflotte** wird nur geprüft, wenn ein Schiffsmodell, das noch nie gehalten hat, an einem Halt ankommt; es schaut auf die Fahrzeuge deiner Schiffslinien, nicht auf Schiffe im Depot (`achievements.script.tl:736`, `achievements.script.tl:750-766`).
- **Ich war es nicht** braucht den Ruf, keine andere Bewertung: siehe [Ruf der Städte](reputation.html).

```tip scripts
Zwischenstopp am Gipfel prüft die Höhe des ersten Wagens, wenn der Zug hält, nicht die Höhe des Bahnhofsgebäudes. Baue den Bahnhof auf einem Berg über 500 m und lass einen Zug dorthin fahren.
```

## Spielübergreifende Zähler

Diese laufen von Spiel zu Spiel weiter (die Plattform speichert sie). Das Skript sendet nur, was sich seit der letzten Prüfung geändert hat.

| Zähler | Erfolg | Was zählt | Quelle |
|---|---|---|---|
| Streckenlänge | **Rund um die Welt** | der Zuwachs der Gesamtlänge im Logbuch (in km); beim Abreissen wird nichts abgezogen | `achievements.script.tl:511-523` |
| Bevölkerung | **Weltbevölkerung** | der Zuwachs der Bevölkerung der Karte, ab der Bevölkerung beim Laden des Spiels | `achievements.script.tl:512`, `achievements.script.tl:525-533` |
| Passagiere | **Passagierpionier** | Passagiere, die eine Fahrt auf einer deiner Linien beendet haben | `achievements.script.tl:236-238`, `achievements.script.tl:535-541` |
| Fracht | **Frachtpionier** | gelieferte Frachteinheiten | `achievements.script.tl:543-549` |
| Klimazonen | **Tycoon der Tycoons** | die Klimazone der Karte, wenn das Unternehmen dort den höchsten Rang erreicht | `achievements.script.tl:551-567` |
| Einnahmen | **Böses Geld** | deine aufsummierten Einnahmen, in Milliarden | `achievements.script.tl:202-204`, `achievements.script.tl:569-590` |
| Frachttypen | **Vertriebsmeister** | jeder Frachttyp des Grundspiels einmal geliefert | `achievements.script.tl:20-22`, `achievements.script.tl:230-232`, `achievements.script.tl:592-607` |
| Fahrzeuge | **Geniesser** | jedes Fahrzeugmodell des Grundspiels, das einmal an einem Halt ankommt | `achievements.script.tl:16-18`, `achievements.script.tl:469-481`, `achievements.script.tl:609-625` |
| Tiere | **Tierfreund** | jedes Tier des Grundspiels, auf das du einmal klickst | `achievements.script.tl:24-26`, `achievements.script.tl:809-834` |

- Fahrzeuge, Fracht und Tiere aus Mods zählen nie für diese Zähler: nur Dateien des Grundspiels (`::/vehicle`, `::/cargos`, `::/animal`) werden genommen (`achievements.script.tl:16-26`).
- Für Geniesser muss ein Fahrzeug **an einem Halt** einer Linie **ankommen**; es zu kaufen reicht nicht.

```engine
Ob ein Erfolg noch freigeschaltet werden kann (isAchievementUnlockable), ob die Zähler abgeschaltet sind (areStatsDisabled), die Ziele jedes Zählers und die 24 Erfolge, die nicht im Skript stehen, werden von der Engine und der Plattform behandelt. Das offizielle Wiki sagt, dass Erfolge mit nicht kosmetischen Mods oder mit Spieleinstellungen abseits der Standardwerte im Allgemeinen nicht verfügbar sind.
```

## Gut zu wissen

- Jeder „erstes Mal“-Erfolg wird gegen die vorherige Prüfung geprüft: er braucht ein **neues** Ereignis in einem Spiel, in dem der Erfolg noch offen ist; eine alte Subvention oder ein alter Rang aus einem Spielstand zählt nicht noch einmal (`achievements.script.tl:633`, `achievements.script.tl:779`).
- Dein Rang, Subventionen und der Ruf werden in [Unternehmensrang, Vorteile und Hauptquartier](company.html), [Subventionen](subsidies.html) und [Ruf der Städte](reputation.html) erklärt.

```check
official: "There are 41 achievements that can be earned by completing a certain task or reaching a specific goal." "Achievements are generally unavailable if non-cosmetic mods are used or the gameplay settings are deviating from standard values." ([Achievements](https://wiki.transportfever3.com/doku.php?id=gamemanual:gamemodes:achievements))
scripts: 17 Erfolge und 9 Zähler stehen im Skript. Es präzisiert die offiziellen Texte: Hausmeister bedeutet, dass die Lieferbewertung Ausgezeichnet erreicht, Ich war es nicht einen Ruf unter 1 %, Zwischenstopp am Gipfel den ersten Wagen über 500 m, Perfektionist Abreissen-Neubauen-Abreissen-Neubauen derselben Station und Museumsflotte alle Schiffsmodelle des Grundspiels gleichzeitig auf Linien. Nur Fahrzeuge, Fracht und Tiere des Grundspiels zählen für die Zähler.
result: refines
```
