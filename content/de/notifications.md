---
title: Benachrichtigungen und Warnungen
summary: Wann jede Warnung erscheint und wann sie verschwindet: festsitzende Fahrzeuge, nicht verwendbare oder überfüllte Stationen, Linien- und Haltestellenprobleme, Stadtwertungen, Fahrzeugzustand, schliessende Industrien und welche Warnungen standardmässig im Protokoll ausgeblendet sind.
domain: notifications
official: gamemanual:ui:userinterface
status: verified
updated: 2026-11-17
game: 40425
fact: 5 min | Spielzeit Stillstand, bevor ein Fahrzeug als festsitzend gemeldet wird
fact: 20 % | Zustand, der die Warnung auslöst, bis das Fahrzeug wieder über 30 % liegt
fact: 11 | Benachrichtigungstypen, die in einem neuen Spiel aus sind
fact: 75 Tage | zwischen zwei Prüfungen auf Stationen ohne Strassenanbindung
---

Die meisten Warnungen sind **dauerhaft**: ein Spielskript prüft die Lage immer wieder, die Warnung bleibt, solange das Problem besteht, und endet von selbst, wenn es gelöst ist. Die Prüfungen sind abwechselnd auf 4 Updates verteilt, daher kann eine Warnung einen Moment brauchen, bis sie erscheint oder verschwindet (`notifications.script.tl:13`, `notifications.script.tl:49`).

## Wann jede Warnung erscheint

| Warnung | Erscheint, wenn | Verschwindet, wenn | Quelle |
|---|---|---|---|
| **Fahrzeug steckt fest** | eines deiner Fahrzeuge ist unterwegs, nicht von dir angehalten, und hat seit **5 Minuten** Spielzeit Geschwindigkeit 0 | es fährt wieder | `notifications.script.tl:557-580` |
| **Station funktionslos** | kein Terminal der Station lädt oder entlädt Passagiere und **nichts** liegt in ihrem Einzugsgebiet (kein Lager, keine Industrie, kein Stadtgebäude), während eine deiner Linien dort hält | etwas kommt ins Einzugsgebiet | `notifications.script.tl:602-617`, `notifications.script.tl:630-647`, `station_useless.script.tl:39` |
| **Station überfüllt** | die Station hat mehr wartende Passagiere oder Güter, als sie fassen kann (Überlauf), während eine deiner Linien dort hält; Passagiere gehen weg | der Überlauf endet | `notifications.script.tl:599`, `notifications.script.tl:649-661`, `overcrowding.script.tl:23` |
| **Fahrzeugzustand** | ein Fahrzeug von dir hat **20 %** Zustand oder weniger | es liegt wieder über **30 %** | `notifications.script.tl:310-318` |
| **Stadtbewertung sehr schlecht** | eine der Wertungen der Stadt fällt auf Sehr schlecht (unter 1/6) | die Wertung ist wieder Mittelmässig oder besser | `notifications.script.tl:230-238`, `town_util.tl:763-769`, `town_util.tl:983-985` |
| **Stadtbewertung sinkt** | eine Wertung ist Schlecht oder Mittelmässig (unter 50 %), ohne in der Warnung Sehr schlecht zu sein | die Wertung ist Gut oder besser | `notifications.script.tl:240-248` |
| **Industrieschliessung** | eine Industrie startet ihren Schliessungs-Countdown | sie schliesst, oder sie wird rechtzeitig wieder genutzt | `notifications.script.tl:439-451`, `industry_close.script.tl:53-59` |
| **Keine Strassenanbindung** | eine Station ist nicht mit einer Strasse verbunden; geprüft alle **75 Tage** | die nächste Prüfung findet eine Strasse | `notifications.script.tl:16`, `notifications.script.tl:423-436` |
| **Güter-Entladeproblem** | Güter eines Fahrzeugs werden auf seiner Linie nie entladen | sie werden entladen | `notifications.script.tl:277-290`, `cargo_rtc_warning.script.tl:28-37` |

- Ein Fahrzeug **im Depot** gilt nie als festsitzend: diese Prüfung ist im Skript abgeschaltet (`notifications.script.tl:563-564`). Ein von dir angehaltenes Fahrzeug zählt auch nie.
- Die Prüfung Station funktionslos schaut nur auf das Einzugsgebiet. Eine Station, an deren Terminal schon Passagiere ein- oder aussteigen, wird nie gemeldet (`notifications.script.tl:606-610`).
- Wie man eine Stadtwertung hebt: [Stadtwachstum](towns.html) und [Ruf](reputation.html). Wie der Schliessungs-Countdown funktioniert und wie man ihn stoppt: [Industrien](industries.html). Was der Zustand mit einem Fahrzeug macht: [Kosten, Unterhalt und Kredite](costs.html).

```engine
Ob eine Station überläuft, ob ein Fahrzeug eine Strecke hat, ob eine Linie ihre Stationen erreichen kann und wie lange die Fahrt zwischen zwei Städten dauern darf, ermittelt die Engine (calculateStationGroupCargo, getVehicleProblems, getLineProblems, getTownProblems). Die Skripte machen aus ihren Antworten nur Warnungen.
```

```tip scripts
Fahrzeug steckt fest, Fahrzeugproblem, Fahrzeugzustand, Station überfüllt und Station nicht verwendbar sind im Protokoll eines neuen Spiels aus. Schalte sie in den Benachrichtigungseinstellungen ein: genau diese Warnungen melden dir einen Stau, eine fehlende Strecke oder eine abgenutzte Flotte.
```

## Linien-, Haltestellen- und Fahrzeugprobleme

Diese kommen direkt aus den Prüfungen der Engine an deinen Linien und Fahrzeugen; das Skript gibt jeder einen Titel.

| Warnung | Fälle | Quelle |
|---|---|---|
| **Linienproblem** | zu wenige Stationen; eine Station zweimal hintereinander; Stationen, die nicht zueinander passen; Stationen konnten nicht verbunden werden; alternative Terminals konnten nicht verbunden werden | `line_warning.script.tl:46-128` |
| **Linie ist falsch konfiguriert** | eine Güterart, die nirgends geladen oder nirgends entladen werden kann; kein Fahrzeug kann eine zum Laden eingestellte Güterart transportieren; Fahrzeuge, die keine der konfigurierten Güter transportieren, oder reine Güterfahrzeuge auf einer Passagierlinie; gar keine Güter konfiguriert | `line_warning.script.tl:15-36`, `line_warning.script.tl:133` |
| **Stationsproblem** | ein Halt, den die aktuellen Fahrzeuge nicht nutzen können; ein Passagierhalt, der von Güterfahrzeugen genutzt wird (einem oder allen); ein Güterhalt, der von Passagierfahrzeugen genutzt wird; eine konfigurierte Güterart, die an diesem Halt nicht geladen oder entladen werden kann | `line_station_warning.script.tl:6-87` |
| **Fahrzeugproblem** | keine elektrifizierte Strecke; keine Strecke für grosse Flugzeuge; keine Strecke für grosse Schiffe; gar keine Strecke; zwei Züge, die sich gegenseitig blockieren | `vehicle_warning.script.tl:6-58` |
| **Stadt nicht angebunden** | die Strasse zwischen zwei Städten ist unterbrochen; die Fahrt zwischen zwei Städten dauert zu lange | `town_warning.script.tl:7-19` |

- „Keine Strecke für grosse Flugzeuge“ und „Keine Strecke für grosse Schiffe“ bedeuten, dass das Fahrzeug zu gross für eine Landebahn, einen Anleger oder eine Wasserstrasse seiner Linie ist: siehe [Flugzeuge](aircraft.html) und [Schiffe](ships.html).

## Protokoll, Pop-ups und Einstellungen

- Jeder Warnungstyp lässt sich in den Benachrichtigungseinstellungen abschalten („Benachrichtigungsprotokollierung konfigurieren“). Ein abgeschalteter Typ bekommt kein Pop-up und wird nicht im Protokoll behalten (`notification_util.tl:145-146`, `notification_log.tl:480`).
- In einem **neuen Spiel** sind 11 Typen von Anfang an aus: **Fahrzeug steckt fest**, **Fahrzeugproblem**, **Fahrzeugzustand**, **Station überfüllt**, **Station nicht verwendbar**, **Station nicht verbunden**, **Stadt nicht angebunden**, **Güter nicht entladen** sowie die Fortschrittsmeldungen Prospektion, Marketingkampagne und Industriebegrünung des Unternehmens (`stuck_vehicle.res.lua:7`, `vehicle_warning.res.lua:8`, `noroadconnection.res.lua:8`, `vehiclecondition.res.lua:8`, `overcrowding.res.lua:8`, `station_useless.res.lua:7`, `town_warning.res.lua:8`, `cargo_rtc_warning.res.lua:8`, `notification_util.tl:32-39`).
- Einmalige Meldungen (neues Fahrzeug, neuer Bau, Rangaufstieg, Subventionen) blenden ihr Pop-up nach **60 Sekunden** Spielzeit aus; sie bleiben im Verlauf (`notification_util.tl:10`, `notifications.script.tl:85-94`).
- Eine Benachrichtigung endet auch, wenn alles, worauf sie zeigt, entfernt oder neu gebaut wurde (`notifications.script.tl:95-107`).
- In einer Mission starten die Benachrichtigungen pausiert, bis die Mission sie einschaltet (`notifications.script.tl:700-704`).

## Gut zu wissen

- Eine Festsitz-Warnung nach 5 Minuten sagt nicht, warum. Schau dir das Fahrzeug an: ein rotes Signal, ein Einbahnsignal in falscher Richtung oder eine Warnung Fahrzeugproblem für dasselbe Fahrzeug.
- „Station funktionslos“ heisst nur „noch nichts im Einzugsgebiet“. Rücke die Station näher an Häuser, eine Industrie oder ein Lager, oder vergrössere sie.
- Eine überfüllte Station verliert Passagiere: füge Fahrzeuge hinzu oder verkürze das Intervall (siehe [Abfahrt und Warten](departure.html)).

```check
official: Die Seite User Interface des offiziellen Wikis beschreibt den Benachrichtigungsknopf, das Protokoll und seine Filter, ohne die Bedingungen der einzelnen Warnungen. ([User Interface](https://wiki.transportfever3.com/doku.php?id=gamemanual:ui:userinterface))
scripts: Die Bedingungen oben: festsitzend nach 5 Minuten bei Geschwindigkeit 0 unterwegs, Fahrzeugzustand bei 20 % bis 30 %, Stadtwertung Sehr schlecht unter 1/6, Strassenanbindung alle 75 Tage geprüft, 11 Typen standardmässig aus.
result: adds
```
