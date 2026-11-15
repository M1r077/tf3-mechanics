---
title: Arbeiter und Arbeiterbonus
summary: Wie Einwohner einen Arbeitsplatz in einer Industrie bekommen, welche für den Bonus zählen und wie groß er ist.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-14
fact: 10 / 20 | Arbeiter für den Bonus nötig
fact: 2 Jahre | so lange zählt eine Ankunft
fact: ×1,5–2,5 | Bonusfaktor, pro Industrie fest
---

Jede Industrie bietet Arbeitsplätze. Wenn genug Arbeiter **mit deinen Personenlinien ankommen**, produziert die Industrie mehr. Das Industriefenster zeigt zwei verschiedene Zahlen, und sie zu verwechseln ist die häufigste Ursache für Missverständnisse.

```diagram workers_flow
```

## Wer in einer Industrie arbeiten kann

- Jede Industrie des Grundspiels hat **20 Arbeitsplätze** (`industrialCapacity = 20`).
- Die Arbeitsplätze sind so eingestellt, dass Einwohner **nicht zu Fuß oder mit dem Auto** hinkommen: nur deine Linien bringen sie hin (`industryutil.lua:451-457`, `disallowedMoveModes = {"WALK", "DRIVE"}`).
- Jeder Einwohner hat eine Wohnung, ein Geschäft und einen Arbeitsplatz. Das Spiel wählt den Arbeitsplatz unter den Orten, die der Einwohner erreichen kann; eine Industrie hat ein Zielgewicht von 2,0 (`industryutil.lua:455`).

```engine
Wie ein Einwohner einen Arbeitsplatz unter allen erreichbaren Orten wählt (Reisezeit, Kosten, Gewicht 2,0), berechnet die Engine. Die Skripte liefern nur die Eingaben.
```

## Zugeteilte Arbeiter

Die Einwohner, deren Arbeitsplatz diese Industrie ist. Das ist die Arbeitsplatzanzeige im Industriefenster und die Spalte **Arbeitsplätze** der Industriestatistik („12/20“) (`entity_window_util.tl:1238`, `statistic_industries.tl:305`). Zugeteilt zu sein reicht **nicht** für den Bonus: die Fahrt muss wirklich stattfinden.

## Für den Bonus gezählte Arbeiter

Ein kleines Spielskript beobachtet jede Ankunft (`industry_workers.script.tl`):

1. Kommt ein Einwohner an einer Industrie an und war seine **letzte Fahrt mit deinen Linien**, wird die Ankunft mit der Spielzeit notiert (`industry_workers.script.tl:86-118`).
2. Nur Ankünfte der **letzten 2 Spieljahre** bleiben (`industry_productivity_util.tl:3`: `2 * getDefaultYearDuration()`).
3. Höchstens die **letzten 20** Ankünfte bleiben (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`).
4. Kommt dieselbe Person erneut an, ersetzt die neue Ankunft die alte: jeder Einwohner zählt **nur einmal** (`industry_workers.script.tl:56-70`).

```diagram workers_window
```

## Wann der Bonus beginnt und endet

- Die Industrie ist geboostet, wenn die gezählten Arbeiter **die Hälfte der Arbeitsplätze** erreichen: `gezählt ≥ Arbeitsplätze × 0,5` (`industry_productivity_util.tl:35-48`, `RequiredWorkersFractionForBoost = 0.5`). Bei 20 Arbeitsplätzen: **10 Arbeiter**.
- Der Bereich Booster im Industriefenster zeigt genau das: „gezählt / benötigt“, aufgerundet (`industry_react_util.tl:627`).
- Die Prüfung läuft bei jeder neuen Ankunft erneut und wenn die älteste älter als 2 Jahre wird (`industry_workers.script.tl:40-43`). Der Bonus **endet also von selbst** etwa 2 Jahre, nachdem keine Arbeiter mehr kommen.

## Wie groß der Bonus ist

- Die Produktion wird mit dem **Bonusfaktor** der Industrie multipliziert, im Fenster als „+X %“ angezeigt (`industry_react_util.tl:716`).
- Der Faktor wird einmal aus dem Zufallswert der Industrie gezogen: **zwischen ×1,5 und ×2,5**, und er ändert sich für diese Industrie nie (`industry_productivity_util.tl:58-72`). Eine Industrie ohne Zufallswert nutzt ×2.
- Zwei gleiche Minen können also verschiedene Boni haben: schau auf das „+X %“, bevor du wählst, welche du bedienst.

## Beispiel

Ein Kohlebergwerk mit 20 Arbeitsplätzen und „+84 %“.

| Lage | Gezählt | Geboostet? | Produktion |
|---|---|---|---|
| Neue Buslinie: 14 Einwohner zugeteilt, noch keiner angekommen | 0 | nein | ×1 |
| 12 verschiedene Einwohner kamen dieses Jahr mit dem Bus | 12 | ja (≥ 10) | ×1,84 |
| Linie entfernt; 2 Jahre kommt niemand | fällt auf 0 | endet | ×1 |

## Gut zu wissen

- Die Grenze von 20 gemerkten Ankünften und die 50-%-Regel bedeuten, dass eine Industrie mit **mehr als 40 Arbeitsplätzen** (mit Mods möglich) nie durch Arbeiter geboostet werden könnte.
- Die Subvention „Transportiere Arbeiter“ ist erfüllt, wenn dieser Bonus aktiv wird (offizielles Wiki, Subventionen).
- Booster-Fracht (Dünger, Maschinen, Werkzeuge) ist ein **eigener** Bonus der Rohstoffindustrien und wird hier nicht behandelt.
- Der Mod [Herkunft der Arbeiter (Worker Origins)](https://mod.io/g/transportfever3/m/worker-origins) zeigt im Industriefenster, aus welchen Städten die zugeteilten und die Bonus-Arbeiter kommen, mit Pfeilen auf der Karte.

```check
official: „If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again.“ ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: „Genug“ = die Hälfte der Arbeitsplätze (10 von 20); „kürzlich“ = die letzten 2 Spieljahre, die letzten 20 Ankünfte, eine pro Person, nur mit deinen Linien; Bonusfaktor ×1,5 bis ×2,5 je Industrie.
result: refines
```
