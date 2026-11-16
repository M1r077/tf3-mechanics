---
title: Arbeiter und Arbeiterbonus
summary: Wie Einwohner einen Arbeitsplatz in einer Industrie bekommen, welche für den Bonus zählen und wie groß er ist.
domain: industries
official: gamemanual:simulation:industriescargos#booster
status: verified
updated: 2026-11-15
game: 40425
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
3. Sind 20 Ankünfte gespeichert, fallen die ältesten weg; die neuen Ankünfte eines Updates bleiben immer vollständig (`industry_workers.script.tl:4`, `KeepHistoryCount = 20`, `industry_workers.script.tl:54-70`).
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
| Buslinie entfernt; 2 Jahre kommt niemand | fällt auf 0 | endet | ×1 |

## Arbeiter zu einer Industrie bringen

```diagram workers_trip
```

- Ein Arbeiter wird gezählt, wenn er **an der Industrie selbst ankommt**, sein Fahrtziel (`targetOrAtEntity`) die Industrie ist und sein letzter Fortbewegungsmodus **Linien** ist (`industry_workers.script.tl:86-94`). An einer Haltestelle auszusteigen reicht nicht: die Person muss die Industrie erreichen.
- Jeder Einwohner hat einen Fortbewegungsmodus pro Ziel (Wohnung, Geschäft, Arbeitsplatz). Das Industriefenster listet die zugeteilten Arbeiter mit einem Symbol für diesen Modus: **Zu Fuss**, **Auto** oder **Linien** (`entity_window_util.tl:1400-1435`). Bei einer Industrie sollte es immer Linien sein, weil Zu Fuss und Auto dort nicht erlaubt sind (`industryutil.lua:451-457`).
- „Nicht zu Fuß“ heißt also: die ganze Fahrt darf kein Fußweg und keine Autofahrt sein. Es heißt nicht „gar nicht laufen“: eine Fahrt mit Linien beginnt und endet trotzdem zu Fuß zwischen Haltestellen und Gebäuden (siehe Engine-Hinweis unten).
- **Umstiege zählen.** Das Skript schaut nur auf den Modus der Fahrt, nicht auf die Zahl der benutzten Linien (`industry_workers.script.tl:91`). Ein Arbeiter aus einer Stadt vier Linien weiter zählt genauso wie einer von nebenan, braucht aber vielleicht viel länger.
- **Jede deiner Linien kann sie bringen**, auch eine Frachtlinie, solange ihre Fahrzeuge Passagiere mitnehmen und die Haltestelle Passagiere lädt. Das Skript prüft den Fahrzeugtyp nicht (`industry_workers.script.tl:86-118`). Spieler berichten von weniger Problemen mit getrennten Personenlinien.
- Manche Industrien (zum Beispiel Ölplattformen) haben eine eigene eingebaute Haltestelle für Passagiere und Fracht (`industryutil.lua:156-165`).
- Das Industriefenster zeigt für jeden zugeteilten Arbeiter, ob er **Derzeit hier** oder **Unterwegs** ist (`entity_window_util.tl:1371-1384`). Der Bereich Booster listet die gezählten Arbeiter mit ihrer **Zeit übrig** von den 2 Jahren (`entity_window_util.tl:1579-1630`, `industry_eow.script.tl:644-649`).
- Wird keine Ankunft gezählt (keine in den letzten 2 Jahren), zeigt die Arbeiterliste im Booster-Abschnitt: „Erschliesse diesen Standort mit dem öffentlichen Verkehr, um den Einwohnern zu ermöglichen, dort zu arbeiten.“ (`entity_window_util.tl:1650-1652`, `entity_window_util.tl:1608`, `entity_window_util.tl:1632`).

```engine
Welche Haltestelle eine Industrie bedient, wie weit ein Arbeiter von einer Haltestelle zum Eingang der Industrie läuft und die Einwohner welcher Städte den Arbeitsplatz nehmen, entscheidet die Engine (Einzugsgebiete, Wegfindung, Arbeitsplatzwahl). Die Skripte setzen keine Distanzgrenze für Arbeiter. Spieler berichten, dass ein Bahnhof, dessen Einzugsgebiet die Industrie für Fracht abdeckt, keine Arbeiter brachte, bis ein Bus zum Eingang der Industrie fuhr (Steam-Thread „Problem getting workers to site“).
```

```tip
**Den Arbeiter-Boost (und den Auftrag „Arbeiter transportieren“) schnell bekommen: mit einer einfachen Linie beginnen.**

1. Baue eine **neue Personenlinie** von einer Haltestelle an der Industrie zu **einer einzigen Stadt**.
2. Setze die Stadthaltestelle so, dass ihr Einzugsgebiet **keinen deiner anderen Personenbahnhöfe berührt**.
3. Ein Fahrzeug reicht für den Start.

Die Arbeitsplätze werden vergeben, wenn die Linie öffnet: In zwei Tests gingen **alle 20 Arbeitsplätze an diese eine Stadt**, und der Boost startete nach **346 s und 925 s** Spielzeit (einmal mit nur einem Fahrzeug). Als die Stadthaltestelle das Einzugsgebiet eines Netzbahnhofs berührte, gingen einige Arbeitsplätze an eine entfernte Stadt und die letzten Arbeiter brauchten viel länger (964 s). Gemessen mit [Worker Origins](https://mod.io/g/transportfever3/m/worker-origins) und dem [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard); wer einen Arbeitsplatz bekommt, entscheidet weiterhin die Engine.
```

## Subvention Transportiere Arbeiter

- Sie wird nur für eine Industrie mit Arbeitsplätzen angeboten, deren Arbeiterbonus noch nicht aktiv ist und die im letzten Jahr Fracht versendet hat (`deliver_workers.script.tl:121-131`, `industry_util.tl:541-558`). Jede Regel hat eine Ausgabetabelle (Booster-Regeln haben `output = { }`), und eine leere Lua-Tabelle gilt als wahr: Nur dieser Zweig wird erreicht (`industry_util.tl:544-551`).
- Sie ist erfüllt, wenn der Arbeiterbonus aktiv wird: dieselben 10 von 20 verschiedenen Ankünften mit deinen Linien (`deliver_workers.script.tl:152-156`). Sonst wird nichts gezählt; es gibt keine versteckte Regel.
- Der Fortschrittsbalken auf der Vertragskarte ist „gezählte Arbeiter ÷ Hälfte der Arbeitsplätze“ (`deliver_workers.script.tl:267-272`, `industry_util.tl:11-18`).
- Die Pfeile auf der Vertragskarte kommen von den **5 nächsten Städten**. Sie sind nur ein Hinweis: das Skript zeichnet sie nach Entfernung, nicht danach, wer den Arbeitsplatz hat (`deliver_workers.script.tl:297-317`).
- Siehe [Subventionen: Angebote, Fristen und Belohnungen](subsidies.html) für Geld und Frist.

## Warum kommen meine Arbeiter nicht an?

| Prüfung | Wo schauen | Warum |
|---|---|---|
| Hat jemand den Arbeitsplatz? | Arbeitsplatzanzeige („12/20“) | Ohne zugeteilte Arbeiter fährt niemand. Die Arbeitsplatzwahl liegt in der Engine. |
| Modus-Symbol der Arbeiter | Arbeiterliste: Zu Fuss / Auto / Linien | Nur Fahrten mit Linien können zählen (`industry_workers.script.tl:91`). |
| Bewegen sie sich? | **Unterwegs** / **Derzeit hier** | Lange „Unterwegs“: langsame oder überlastete Umstiege, oder kein Weg von der letzten Haltestelle. |
| Erreicht die letzte Haltestelle den Eingang der Industrie? | Einzugsgebiet der Haltestelle, Zufahrtsstraße | Von Spielern berichtet; Engine-Sache. Ein kurzer Bus zum Eingang half. |
| Lädt die Haltestelle Passagiere? | Linienhalt, Güterfilter | Passagiere müssen an beiden Enden der Fahrt ein- und ausgeladen werden. |
| 10 **verschiedene** Personen in 2 Jahren? | Bereich Booster, **Zeit übrig** | Dieselbe Person zählt einmal; ältere Ankünfte fallen heraus (`industry_workers.script.tl:56-70`). |
| Mehr als 40 Arbeitsplätze (Mods)? | Arbeitsplatzanzeige | Mit 20 gemerkten Ankünften nie die Hälfte erreichbar. |

## Gut zu wissen

- Die Grenze von 20 gemerkten Ankünften und die 50-%-Regel bedeuten, dass eine Industrie mit **mehr als 40 Arbeitsplätzen** (mit Mods möglich) nie durch Arbeiter geboostet werden könnte.
- Die Subvention **Transportiere Arbeiter** ist erfüllt, wenn dieser Bonus aktiv wird (`deliver_workers.script.tl:152-156`).
- Booster-Fracht (Dünger, Maschinen, Werkzeuge) ist ein **eigener** Bonus der Rohstoffindustrien und wird hier nicht behandelt.
- Der Mod [Herkunft der Arbeiter (Worker Origins)](https://mod.io/g/transportfever3/m/worker-origins) zeigt im Industriefenster, aus welchen Städten die zugeteilten und die Bonus-Arbeiter kommen, mit Pfeilen auf der Karte.

```check
official: „If a sufficient amount of workers show up frequently, the overall throughput of the production increases. When too few workers have recently been at the industry, the worker booster stops again.“ ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos#booster))
scripts: „Genug“ = die Hälfte der Arbeitsplätze (10 von 20); „kürzlich“ = die letzten 2 Spieljahre, die letzten 20 Ankünfte, eine pro Person, nur mit deinen Linien; Bonusfaktor ×1,5 bis ×2,5 je Industrie. Umstiege zählen; der Fahrtmodus muss Linien sein, der Fußweg von einer Haltestelle gehört zu so einer Fahrt.
result: refines
```
