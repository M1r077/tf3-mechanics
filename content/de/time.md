---
title: Spielzeit und Kalender
summary: Spielgeschwindigkeit und Kalendergeschwindigkeit sind zwei verschiedene Dinge. Wie lange ein Tag und ein Jahr dauern, was ein langsamerer oder pausierter Kalender ändert und was nicht.
domain: time
official: gamemanual:simulation:overview#simulation_speed
status: verified
updated: 2026-11-16
fact: 4 s | ein Kalendertag bei Kalendergeschwindigkeit ×1, Spielgeschwindigkeit 1x
fact: ≈ 24 min | ein Kalenderjahr bei denselben Geschwindigkeiten
fact: 0 ×0,25 ×0,5 ×1 ×2 ×4 | Stufen der Kalendergeschwindigkeit
fact: 0 1x 2x 4x | Stufen der Spielgeschwindigkeit
---

Das Spiel hat **zwei Uhren**. Die **Spielgeschwindigkeit** (Pause, 1x, 2x, 4x) lässt alles schneller laufen: Fahrzeuge, Produktion, Städte. Die **Kalendergeschwindigkeit** legt nur fest, wie schnell das Datum vorrückt. Fast jede Regel des Spiels zählt in Spielzeit, nicht in Kalendertagen.

## Die zwei Einstellungen

| Einstellung | Stufen | Was sie ändert | Quelle |
|---|---|---|---|
| **Spielgeschwindigkeit** | Pause, 1x, 2x, 4x | wie schnell die ganze Simulation läuft | `game_bar_widgets.tl:199-203` |
| **Kalendergeschwindigkeit** | Pausiert, ×0,25, ×0,5, ×1, ×2, ×4 | wie viele Spielsekunden ein Tag dauert | `game_bar_widgets.tl:321-335`, `game_bar_widgets.tl:351` |

- Bei Kalendergeschwindigkeit ×1 dauert ein Tag **4 Sekunden** Spielzeit (offizielles Wiki), ein Monat also etwa 2 Minuten und ein Jahr etwa **24 Minuten** bei 1x. Gemessen mit [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard): 4,0 s pro Tag bei ×1, 1 s bei ×4, 8 s bei ×0,5, 16 s bei ×0,25.
- ×4 lässt das Datum viermal so schnell laufen; **Pausiert** hält das Datum an, die Simulation läuft weiter.
- 2x und 4x sind ein Maximum: Das Spiel senkt sie, wenn der Computer nicht mitkommt (`game.tl:636-642`). Gemessen: 2x ergab 1,9x, 4x ergab im Schnitt 3,6x.
- Die **Tageszeit** und das Wetter sind eine dritte, optische Uhr: Standardmäßig ändern sie sich von selbst, egal wie der Kalender steht (`game_time_config.res.lua:5`, `weather_config.res.lua:5`).

## Was der Spielzeit folgt, egal wie der Kalender steht

Diese Dinge zählen in Spielzeit, ein langsamerer oder pausierter Kalender bremst sie also nicht:

- **Produktion**: Die Produktionszeit einer Industrie ist ein fester Anteil eines Standardjahres (`industry_react_util.tl:51`). Das Industriefenster zeigt sie in Tagen des aktuellen Kalenders (`industry_react_util.tl:23`): Bei ×0,25 zeigt dieselbe Rate ein Viertel der Tage.
- **Darlehensraten**: eine pro Standardmonat Spielzeit, auch bei pausiertem Kalender (`loan.script.tl:83-88`).
- **Fristen von Subventionen** und der Einnahmebonus ×2 (`subvention_util.tl:290-292`).
- **Erholung des Stadtansehens** (`towns.script.tl:121-130`), **Arbeiterboni** (`industry_productivity_util.tl:3`) und **Schließung von Industrien** nach Jahren ohne Anbindung (`industries.script.tl:119-128`).
- **Lieferbewertungen** der Städte, über das letzte halbe Jahr (`town_util.tl:840`).

Läuft der Kalender, zeigt das Spiel diese Dauern in Jahren, Monaten und Tagen der aktuellen Kalendergeschwindigkeit (`util.tl:40-49`).

## Was dem Kalenderdatum folgt

- **Neue Fahrzeuge, Bahnhöfe und Gebäude** erscheinen nach Jahr (offizielles Wiki: "Different calendar speeds only affect the availability of vehicles and infrastructure").
- **Kosten, die mit dem Jahr steigen**: Gebäudeunterhalt, Epochenvarianten, Subventionsgeld und Darlehensbeträge folgen dem Datum. Siehe [Kosten, Unterhalt und Darlehen](costs.html).

## Bei pausiertem Kalender

1. Das Datum und damit das Jahr bleiben fest: keine neuen Fahrzeuge, und die jahresabhängigen Kosten bleiben, wo sie sind.
2. Dauern werden in **Minuten und Sekunden** statt in Tagen angezeigt (`util.tl:41-43`, `industry_react_util.tl:16-21`).
3. Ein Darlehen zeigt seine Rate **pro Minute** statt pro Jahr (`finances_loan_gui.tl:223-231`), und die Karte für ein eigenes Darlehen kann nicht genommen werden (`finances_loan_gui.tl:393`).
4. Produktion, Raten, Fristen und Ansehen behalten ihr Tempo in Spielzeit.

## Gut zu wissen

- Du willst mehr Zeit, um ein Netz auszubauen, bevor neue Fahrzeuge kommen? Senke die Kalendergeschwindigkeit: Deine Einnahmen pro Spielminute ändern sich nicht.
- Die "pro Jahr" angezeigte Produktion hängt von der Kalendergeschwindigkeit ab; vergleiche Industrien bei derselben Geschwindigkeit.
- [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) zeigt auch bei pausiertem Kalender lesbare Finanzdiagramme.

```engine
Die Länge von Standardtag, -monat und -jahr (getDefaultDayDuration und die anderen) kommt aus der Engine. Das Stadtskript zählt einen Monat als 30 × 4 Sekunden (`towns.script.tl:121`), was zum gemessenen Tag von 4 Sekunden passt; einige andere Konstanten gehen noch von einem Tag mit 2 Sekunden aus (`cargotype.script.lua:3`, `mod.script.tl:172`).
```

```check
official: "By default a day in the game lasts 4 seconds." "Different calendar speeds only affect the availability of vehicles and infrastructure. The amount of produced and consumed cargo as well as the maintenance of vehicles is automatically adapted to stay consistent." ([Simulation Overview](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:overview))
scripts: Kalendergeschwindigkeit ×0,25 bis ×4 oder pausiert, relativ zum Standardtag; Produktion, Darlehen, Subventionen, Ansehen und Arbeiter-Timer laufen in Spielzeit; ein pausierter Kalender zeigt Dauern in Minuten und Raten pro Minute und sperrt neue Darlehen; gemessen: 4 s pro Tag bei ×1.
result: refines
```
