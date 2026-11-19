---
title: Warum verliere ich Geld?
summary: Was einbringt, was kostet, und eine Prüfung in sechs Schritten, um die Linien zu finden, die Geld verlieren, und warum, mit Links zu den Seiten, die jeden Punkt erklären.
domain: finance
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-15
game: 40444
fact: 1 | Zahlung pro Einheit, beim Verbraucher, für die Luftlinie
fact: 0 | bezahlt in einem Lager oder beim Umstieg
fact: 100 % | bezahlt, auch bei Verspätung
fact: ×6 | angezeigter Jahresfaktor auf den Unterhalt von Lagern, Flugfeldern, Flughäfen und Häfen bis 2020
---

Eine Lieferung bezahlt **eine einzige Luftlinie**, vom Ort, an dem die Fracht hergestellt wurde, bis zum Ort, an dem sie gebraucht wird, und nur wenn sie dort ankommt. Alles, was du baust und kaufst, kostet jedes Jahr Geld, ein Teil davon mit dem Kalenderjahr immer mehr. Eine Linie verliert Geld, wenn ihr Anteil an den Zahlungen kleiner ist als die Kosten, die sie verursacht.

```diagram money_flow
```

## Was einbringt

- **Die Luftlinie** von der Quelle zum Verbraucher, plus 8 × die Steigung. Die Länge deiner Strecke zählt nicht (`cargo_income.script.lua:3-7`, `cargo_income.script.lua:5`).
- **Jede Fracht zahlt gleich viel** pro Kilometer: Der Einnahmefaktor ist für alle 3,8 (`cargotype.script.lua:7-13`).
- **Einmal, beim Verbraucher.** Entladen in ein Lager oder an einem Umsteigebahnhof bringt nichts. Die Zahlung wird dann nach der Luftlinienlänge jeder Etappe auf die Linien der Kette verteilt (im Spiel gemessen).
- **Verspätete Fracht wird voll bezahlt**: Die Fahrzeit wird nicht verwendet (`cargotype.script.lua:7-13`). Verspätung senkt stattdessen die **Lieferungs**-Bewertung der Stadt.
- **Der Unternehmensrang** senkt alle Einnahmen mit der Einstellung **Inflation**: auf Rang 15 ×0,75 bei Normal (`company_progression_util.tl:25-40`).
- Eine **erfüllte Subvention** verdoppelt für 5 Jahre die Einnahmen der Lieferungen, die sie abdeckt: an ihre Industrie, an ihre Stadt oder Passagiere zwischen ihren beiden Städten, nur auf ihren Linien (`subvention_util.tl:286`). Siehe [Subventionen: Angebote, Fristen und Belohnungen](subsidies.html).

Details: [Gütereinnahmen und Lieferzeit](income.html).

## Was kostet

- **Fahrzeuge**: Die Betriebskosten folgen Durchschnittstempo × Kapazität, und der Preis entspricht 6 Jahren Betriebskosten (`model_metadata_util.lua:499-518`, `model_metadata_util.lua:548-549`).
- **Gleise und Straßen**: etwa ein Sechstel des Baupreises pro km und Jahr; Hochgeschwindigkeitsgleis kostet 9-mal so viel wie einfaches Gleis (`simple.street_template.lua:33`, `high_speed.street_template.lua:35`).
- **Depots, Bahnhöfe, Lager, Häfen, Flughäfen**: Varianten späterer Epochen kosten ×3 und ×9 (`rail_depot.con.lua:7`, `warehouse.tl:48`), und für Lager, Flugfelder, Flughäfen und Häfen zeigt das Gebäudefenster einen Unterhalt, der dem Jahr folgt, ×1 im Jahr 1900 bis ×6 im Jahr 2020 (`mod.script.tl:92-100`, `entity_window_util.tl:188-192`). Was abgebucht wird, entscheidet die Engine.
- **Darlehen**: Der Zinssatz wird einmal auf den Betrag berechnet und über die Laufzeit verteilt (`loan_util.tl:102-111`).
- **Inflation erhöht keine Kosten**. Sie senkt nur die Einnahmen.

Details: [Kosten, Unterhalt und Darlehen](costs.html).

## Sechs Prüfungen, der Reihe nach

```diagram money_check
```

1. **Welche Linien verlieren Geld?** Schau dir die Bilanz jeder Linie an, nicht die Summe der Firma. Die Mod [Second Screen Dashboard](https://mod.io/g/transportfever3/m/second-screen-dashboard) zeigt die Bilanz jeder Linie über die letzten 12 Monate und ihren Durchschnitt über mehrere Jahre.
2. **Fährt die Fracht weit?** Nur die Luftlinie von der Quelle zum Verbraucher zählt. Ein kurzer Zubringer zu einem Lager bekommt nur den Anteil seiner eigenen kurzen Etappe ([Gütereinnahmen und Lieferzeit](income.html)).
3. **Fährt sie voll?** Ein Fahrzeug kostet voll oder leer gleich viel. Achte auf leere Rückfahrten, den **Füllstand** und **Vollladen** an jedem Halt ([Abfahrtseinstellungen: Vollladen, Füllstand und Haltezeiten](departure.html)).
4. **Wird sie dort entladen, wo es zahlt?** Was nicht in der Liste Ladung eines Halts steht, wird in jeden Bestand in der Nähe entladen, auch in ein Lager, und ein Lager zahlt nichts ([Lade- und Entladegeschwindigkeit](loading.html), [Lager](warehouses.html)). Fracht, die nicht in volle Bestände der Stadt passt, bleibt an Bord ([Stadtwachstum: XP, Wertungen und Größe](towns.html)).
5. **Zu viel Fahrzeug?** Tempo und Kapazität kosten Geld, aber Tempo bringt nichts ein: Es hilft nur, wenn es mehr Fahrten pro Jahr ergibt. In der Stadt kann ein alter, langsamer Bus mehr Gewinn bringen als ein neuer, schneller ([Kosten, Unterhalt und Darlehen](costs.html)).
6. **Fixkosten.** Depots, zusätzliche Lagermodule, schnelle Gleise und Gebäude einer späteren Epoche kosten jedes Jahr, ob benutzt oder nicht ([Kosten, Unterhalt und Darlehen](costs.html)).

## Gut zu wissen

- **Wähle Frachten nach Menge und Entfernung**, nicht nach Preis: Jede Fracht zahlt pro km gleich viel.
- Eine **lange Hauptlinie**, die von kurzen Linien beliefert wird, verdient den Großteil des Geldes; die Zubringer zeigen kleine Bilanzen, aber es zählt die ganze Kette.
- **Mehr zu transportieren**: Eine geboostete Industrie produziert mehr ([Arbeiter und Arbeiterbonus](workers.html), [Industrien](industries.html)), und eine größere Stadt verlangt mehr Fracht.
- Eine Linie schneller zu machen erhöht die Zahlung pro Einheit nicht. Es hilft nur, wenn dieselben Fahrzeuge mehr Fahrten machen.

```check
official: "The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." "While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks))
scripts: Gleich: Luftlinie plus 8 × Steigung, derselbe Faktor für jede Fracht, Fahrzeit nicht verwendet; im Spiel gemessen: einmal beim Verbraucher bezahlt und nach Etappenlänge verteilt; Kosten folgen Tempo × Kapazität bei Fahrzeugen, 1/6 des Preises bei Gleisen, Epochenvarianten ×3 / ×9 und Jahresfaktor ×1 bis ×6 bei Gebäuden; Inflation senkt nur die Einnahmen.
result: refines
```
