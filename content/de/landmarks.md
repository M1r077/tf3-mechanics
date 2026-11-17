---
title: Wahrzeichen, Feiern und Spassfunktionen
summary: Was jedes Wahrzeichen an Fracht kostet, wann es freigeschaltet wird und was es den Fahrzeugen seiner Stadt bringt, wie die Einstellung Benötigte Ressourcen für Wahrzeichen es skaliert und was Feiern, Feuerwerke, Luftschiffe und UFOs wirklich tun.
domain: landmarks
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 9 + 3 | Wahrzeichen: 9 im Basisspiel (Ränge 2 bis 15), 3 weitere mit den DLC-Paketen (Rang 1)
fact: +20 % / +25 % / -20 % / -25 % | Höchstgeschwindigkeit, Verschmutzung oder Komfort für die Fahrzeuge seiner Stadt
fact: ×0 bis ×4 | benötigte Fracht, mit der Einstellung Benötigte Ressourcen für Wahrzeichen
fact: 2-4 Jahre | zwischen zwei UFOs
---

Ein Wahrzeichen wird wie eine Baustelle gebaut: Du schaltest es mit einem Unternehmensrang frei, platzierst es und **lieferst Fracht** dorthin. Wenn die Baustelle ihre ganze Fracht hat, ist das Wahrzeichen fertig und gibt den Fahrzeugen **seiner Stadt** einen Bonus. Das Hauptquartier ist ein eigenes Gebäude mit eigenen Regeln (siehe [Unternehmensrang, Vorteile und Hauptquartier](company.html)).

## Die Wahrzeichen

Fracht bei **Benötigte Ressourcen für Wahrzeichen** ×1 (Normal).

| Wahrzeichen | Rang | Zu liefernde Fracht | Bonus für die Fahrzeuge seiner Stadt | Quelle |
|---|---|---|---|---|
| **Amphitheater** | 2 | 800 Stein | Strassenfahrzeuge: Lärm **-25 %** | `arena.con.lua:10`, `arena.con.lua:20-26`, `arena.con.lua:39` |
| **Grosser Leuchtturm** | 5 | 1.200 Stein, 200 Treibstoff | Schiffe: Höchstgeschwindigkeit **+20 %** | `lighthouse.con.lua:10`, `lighthouse.con.lua:14`, `lighthouse.con.lua:29`, `lighthouse.con.lua:48` |
| **Burg des weissen Reihers** | 7 | 1.200 Stein, 400 Bretter | Züge: Verschmutzung **-20 %** | `white_heron_castle.con.lua:10`, `white_heron_castle.con.lua:14`, `white_heron_castle.con.lua:28`, `white_heron_castle.con.lua:47` |
| **Schifffahrtsmuseum** | 9 | 600 Holz, 600 Bretter, 200 Stoff | Schiffe: Komfort **+25 %** | `ship_museum.con.lua:10-18`, `ship_museum.con.lua:36`, `ship_museum.con.lua:55` |
| **Schloss Neuschwanstein** | 10 | 1.000 Stein, 600 Bretter, 200 Farbstoffe | Strassenfahrzeuge: Komfort **+25 %** | `neuschwanstein.con.lua:10-18`, `neuschwanstein.con.lua:36`, `neuschwanstein.con.lua:55` |
| **Freiheitsstatue** | 11 | 800 Stein, 400 Stahl, 400 Blech | Schiffe: Verschmutzung **-20 %** | `statue_of_liberty.con.lua:10-18`, `statue_of_liberty.con.lua:38`, `statue_of_liberty.con.lua:57` |
| **Sommerpalast** | 13 | 600 Stein, 300 Bretter, 300 Farbstoffe, 300 Möbel | Flugzeuge: Verschmutzung **-20 %** | `summer_palace.con.lua:10-22`, `summer_palace.con.lua:44`, `summer_palace.con.lua:63` |
| **Opernhaus** | 14 | 800 Stein, 400 Glas, 400 Blech, 400 Stoff | Züge: Komfort **+25 %** | `opera_house.con.lua:10-22`, `opera_house.con.lua:44`, `opera_house.con.lua:63` |
| **Parlament** | 15 | 800 Stein, 400 Bretter, 400 Glas, 400 Möbel | Strassenfahrzeuge, Züge, Schiffe und Flugzeuge: Höchstgeschwindigkeit **+20 %** | `westminster.con.lua:10-22`, `westminster.con.lua:45`, `westminster.con.lua:79` |

**DLC-Wahrzeichen.** Zwei DLC-Pakete fügen drei weitere hinzu, freigeschaltet ab Rang 1. Ihre Dateien liegen in den DLC-Ordnern des Spiels (Deluxe Upgrade Pack und Pre-order Pack), ausserhalb der Basisdateien, die dieses Wiki indexiert, deshalb haben sie hier keine Quellenlinks.

| Wahrzeichen | DLC | Rang | Zu liefernde Fracht | Bonus für die Fahrzeuge seiner Stadt |
|---|---|---|---|---|
| **Eiffelturm** | Deluxe Upgrade Pack | 1 | 400 Stahl | Strassenfahrzeuge: Höchstgeschwindigkeit **+25 %** |
| **Taj Mahal** | Deluxe Upgrade Pack | 1 | 800 Stein | Flugzeuge: Lärm **-25 %** |
| **Cheops Pyramide** | Pre-order Pack | 1 | 800 Stein | Züge: Höchstgeschwindigkeit **+25 %** |

- Jedes Wahrzeichen wird einmal freigeschaltet, durch seinen Rang; wie der Rang steigt, steht in [Unternehmensrang, Vorteile und Hauptquartier](company.html).
- Laut ihren Dateien kosten Wahrzeichen nichts beim Bau und nichts pro Jahr: nur die Fracht (`arena.con.lua:59-64`).
- Die Baustelle lagert jeweils die Hälfte jeder Fracht, sie braucht also mindestens zwei Lieferungen von jeder (`arena.con.lua:13-18`).

## Ein Wahrzeichen bauen

- Die Baustelle hat **4 Stufen**. Sie steigt, während Fracht ankommt: Stufe 2 bei einem Drittel der gesamten Fracht, Stufe 3 bei zwei Dritteln, fertig bei 100 %. Jede Fracht zählt nur bis zu ihrer eigenen Menge, zusätzlicher Stein ersetzt also keine fehlenden Bretter (`landmarks.script.tl:34-46`).
- Der Bonus wirkt erst, wenn das Wahrzeichen **fertig** ist (`landmark_util_serialized.tl:393-395`). Dann erscheint die Meldung „Bau abgeschlossen“ (`landmarks.script.tl:49-61`).
- Die Einstellung **Benötigte Ressourcen für Wahrzeichen** multipliziert die gesamte Fracht: Keine ×0, Niedrig ×0,5, Normal ×1, Hoch ×2 oder Sehr hoch ×4. Die Vorgaben sind Easy ×0,5, Normal ×1, Hard ×2, Very Hard ×4. Bei ×0 ist ein Wahrzeichen fertig, sobald es platziert ist (`difficulty_util.tl:40`, `difficulty_util.tl:107`, `difficulty_util.tl:135`, `difficulty_util.tl:162`, `difficulty_util.tl:189`, `landmarks.script.tl:38`, `landmarks.script.tl:46`).

## Wer den Bonus bekommt

- Der Bonus geht an die Stadt, die **dem Wahrzeichen am nächsten** liegt, und an die Fahrzeuge der genannten Verkehrsart, deren nächste Stadt diese Stadt ist (`landmark_util.tl:6-47`, `landmarks.script.tl:208-236`).
- Fährt ein Fahrzeug in das Gebiet einer anderen Stadt, übernimmt es deren Boni und verliert die alten (`landmarks.script.tl:279-299`).
- Boni mehrerer Wahrzeichen in derselben Stadt **addieren sich**: zweimal +20 % Höchstgeschwindigkeit ergeben +40 % (`landmark_util.tl:46`, `vehicle_modifier.script.tl:3-16`).

```engine
Welche Stadt die „nächste Stadt“ eines Wahrzeichens oder eines fahrenden Fahrzeugs ist, entscheidet die Engine (getConstructionClosestTown, closestTown). Wie die Engine +25 % Komfort oder +20 % Höchstgeschwindigkeit in Fahrten und Einnahmen umsetzt, ist ebenfalls Sache der Engine.
```

```tip scripts
Setze das Parlament in die Stadt, in der die meisten deiner Fahrzeuge fahren: +20 % Höchstgeschwindigkeit für jede Verkehrsart. Weitere +20 % gibt der Grosse Leuchtturm für Schiffe in derselben Stadt. Der Erfolg Zentralisiert verlangt 10 fertige Wahrzeichen mit derselben nächsten Stadt; das Hauptquartier zählt nicht, da es keine Fracht zum Liefern hat. Das Basisspiel enthält 9 Wahrzeichen und die DLC-Pakete fügen 3 hinzu (gezählt); ob Zentralisiert ohne DLC erreichbar ist, ist unbekannt (siehe [Erfolge](achievements.html)).
```

## Feiern

Eine Feier ist das kleine Fest, das über einer Stadt angezeigt wird, wenn etwas zum ersten Mal passiert. Sie erhöht auch den **Ruf** der Stadt, aber nur, wenn der Ruf nicht schon voll ist.

| Ereignis | Ruf | Quelle |
|---|---|---|
| erster Passagier steigt in der Stadt in eine deiner Linien ein | +50 % | `celebrations.script.tl:228-252` |
| erste Fracht an die Stadt geliefert | +50 % | `celebrations.script.tl:187-198` |
| die Stadt steigt eine Stufe auf | +50 % | `celebrations.script.tl:260-272` |
| erste Fracht an eine Industrie geliefert | +20 % für die ihr nächste Stadt | `celebrations.script.tl:202-219` |

- Eine Stadt, die aufsteigt, bekommt auch ein **Feuerwerk**, ausser es ist ausgeschaltet (`town_growth.script.tl:108-112`).
- Wie der Ruf funktioniert: [Ruf](reputation.html).

## Spassfunktionen

- Ein **Luftschiff** fliegt über eine Stadt, wenn du dort eine Marketingkampagne startest (`fun_elements.script.tl:112-117`).
- Ein **UFO** erscheint alle **2 bis 4 Jahre** Spielzeit, zufällig gewählt, wenn keines auf der Karte ist (`fun_elements.script.tl:10`, `fun_elements.script.tl:79-91`). Klicke es an für den Erfolg Begegnung der dritten Art.
- Keines davon verändert die Wirtschaft.

## Gut zu wissen

- Wähle die Stadt vor dem Bau: Der Bonus folgt nicht deinen Linien, nur den Fahrzeugen nahe dieser Stadt.
- Auf Very Hard braucht ein Wahrzeichen die vierfache Fracht: Das Parlament verlangt dann 3.200 Stein und 1.600 von jeder anderen Fracht.

```check
official: The official wiki's User Interface page shows the landmarks in the build menu and the town window, without their cargo or bonuses.
scripts: Neun Basis-Wahrzeichen, eines pro Rang von 2 bis 15, plus drei DLC-Wahrzeichen auf Rang 1, jedes aus gelieferter Fracht in 4 Stufen gebaut, skaliert durch Benötigte Ressourcen für Wahrzeichen ×0 bis ×4. Fertig gibt jedes einen Bonus (+20 % oder +25 % Höchstgeschwindigkeit, -20 % Verschmutzung, -25 % Lärm oder +25 % Komfort) an die Fahrzeuge einer Verkehrsart in seiner nächsten Stadt; Boni addieren sich. Feiern geben 50 % oder 20 % Ruf; alle 2 bis 4 Jahre kommt ein UFO.
result: adds
```
