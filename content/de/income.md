---
title: Gütereinnahmen und Lieferzeit
summary: Was eine Lieferung einbringt (Luftlinie, Steigung, Unternehmensrang, Subventionen) und was eine Verspätung wirklich kostet.
domain: economy
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-14
fact: 3,8 | derselbe Einnahmefaktor für jede Fracht
fact: +8 × Steigung | Höhenmeter, die zur Entfernung addiert werden
fact: 100 % | bezahlt, auch wenn die Lieferung verspätet ist
---

Eine Lieferung bezahlt die **Luftlinie**, sonst nichts von der Fahrt. Die Geschwindigkeit zählt aus einem anderen Grund: Jede Fracht hat eine **Lieferzeit**, und verspätete Lieferungen senken die **Lieferungs**-Bewertung der Stadt, nicht deine Einnahmen.

```diagram income_formula
```

## Die Einnahmeformel

Die ganze Formel steht in einem kurzen Spielskript (`cargo_income.script.lua:10-13`):

1. **Einnahmefaktor** der Fracht. Alle Frachten des Grundspiels nutzen dieselbe Funktion und dieselben Preise (`initialPrice = 4`, `finalPrice = 3.2`), das ergibt **3,8 für alle 36 Frachten** (`cargotype.script.lua:7-13`, `coal.cargo.lua:21-22`). Kohle bringt über dieselbe Entfernung genau so viel wie Güter.
2. Einstellung **Gütereinnahmen**: 50 %, 75 %, 100 %, 125 % oder 150 % (`difficulty_util.tl:38`, `mod.script.tl:211`). Alle vier Schwierigkeitsvorgaben nutzen 100 % (`difficulty_util.tl:97`).
3. **Entfernung**, siehe unten.

Die Funktion erhält die Fahrzeit, **nutzt sie aber nicht** (`cargotype.script.lua:7-13`): Eine langsame oder verspätete Lieferung bringt gleich viel.

## Entfernung: Luftlinie plus Steigung

```diagram income_distance
```

- Die Entfernung ist die **Luftlinie in 3D** zwischen den beiden Punkten, nicht die Länge deiner Strecke (`cargo_income.script.lua:3-7`).
- Ist der Höhenunterschied positiv, werden **8 × diese Höhe** addiert (`cargo_income.script.lua:5`): 100 m Steigung bringen so viel wie 800 m mehr. In der Gegenrichtung wird nichts abgezogen.
- Eine kurvige Linie verdient also so viel wie eine gerade, aber du zahlst Unterhalt für jeden gebauten Meter Gleis oder Straße.

```engine
Die Engine wählt die zwei Punkte und gibt sie an das Skript. Im Spiel gemessen (siehe unten): Es sind die **Quelle** der Fracht (die Industrie oder das Stadtgebäude, das sie erzeugt hat) und der **Abnehmer**, der sie erhält, wie das offizielle Wiki sagt („between the source and the final destination").
```

## Fracht, die die Linie wechselt

Wenn eine Einheit über mehrere Linien reist, zum Beispiel Schiff → Lagerhaus → Zug, bezahlt das Spiel sie trotzdem **nur einmal**:

```diagram income_split
```

1. Das Entladen in einem Lagerhaus oder einem Umsteigebahnhof bringt **nichts**. Von etwa 17.000 gemessenen Zahlungen gingen nur 43 an ein Lager, das kein Abnehmer war.
2. Wenn das letzte Fahrzeug beim Abnehmer liefert, wird die Einheit mit der Formel oben bezahlt, für die Luftlinie **von der Quelle zum Abnehmer**. Die Abschnitte und die echte Strecke zählen nicht: Ein Umweg über ein Lagerhaus bringt nichts mehr.
3. Dieses Geld wird zwischen den Linien der Kette geteilt, **im Verhältnis der Luftlinie jedes Abschnitts**: von einem Abholpunkt zum nächsten und vom letzten Abholpunkt zum Abnehmer. Der Steigungsbonus zählt bei dieser Aufteilung nicht.
4. Das liefernde Fahrzeug hält zuerst den ganzen Betrag, mit einem Anteil pro Abschnitt. Er wird einige Sekunden Spielzeit später gebucht (Median etwa 6 s): Jede Linie und jedes Fahrzeug erhält seinen Anteil. Der Kontostand einer Linie bewegt sich also kurz nach der Lieferung, nicht am Lagerhaus.

Eine kurze Zubringerlinie zu einem Lagerhaus verdient also wenig, obwohl sie das ganze Sammeln erledigt; der lange Abschnitt verdient am meisten. Jede Linie zeigt trotzdem ihren echten Anteil in ihrem eigenen Kontostand.

```engine
Die Skripte berechnen nur den Gesamtbetrag (`economy/cargo_income.script.lua`); die Aufteilung macht die Engine, sie ist in den Skripten nicht sichtbar. Die Regeln oben wurden mit einem Test-Mod gemessen, der nur liest: etwa 1.700 Zahlungen von Einheiten mit 2 oder 3 Abschnitten und die Kontobewegungen jeder beteiligten Linie und jedes Fahrzeugs. In 769 sauberen Fällen (eine Einheit, eine Zahlung) passte die Aufteilung jedes Mal auf 1 % genau zu den Abschnittslängen; eine Aufteilung mit Steigungsbonus passte nur in 59 % der Fälle, eine gleiche Aufteilung in keinem.
```

## Was den Betrag noch ändert

| Was | Wirkung | Quelle |
|---|---|---|
| **Unternehmensrang** mit der Einstellung Inflation | Rang 1: ×1, dann gleichmäßig sinkend bis Rang 15: ×0,9 (Niedrig), **×0,75 (Normal)**, ×0,6 (Hoch), ×0,5 (Sehr hoch); Aus: immer ×1 | `company_progression_util.tl:25-40`, `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| **Erfüllte Subvention** | ×2 auf den Linien, die für die Subvention geliefert haben | `deliver_cargo.script.tl:463-469`, `deliver_cargo_town.script.tl:554-565` |
| **Verspätete Lieferung** | keine Wirkung auf die Einnahme | `cargotype.script.lua:7-13` |

- Der Rangmultiplikator gilt für **alle** Fracht- und Passagierzahlungen (`company_growth.script.tl:159-170`). Die Schwierigkeitsvorgaben nutzen Inflation Niedrig (Easy), Normal (Normal), Hoch (Hard), Sehr hoch (Very Hard) (`difficulty_util.tl:108`).
- Das ×2 der Subventionen gilt nur für die Linien, die während der Subvention geliefert haben, und nur für begrenzte Zeit (offizielles Wiki, Subsidies).

## Passagiere

Passagiere nutzen dieselbe Entfernung und einen festen Einnahmefaktor von etwa 3,61 (`cargotype.script.lua:50-53`), multipliziert mit **0,5 + dem Ticketpreisfaktor des Fahrzeugs** (`cargo_income.script.lua:14-17`). Legt ein Fahrzeugmodell keinen Komfortfaktor fest, setzt das Spiel den Preisfaktor auf 0,3 für Busse und Trams, 0,9 für Flugzeuge, 0,1 für Schiffe und 0,5 für Züge (`base_mod.lua:46-61`); bei den übrigen Modellen ist es ein Wert der Engine, in den Skripten nicht sichtbar. Eine Passagier-Subvention verdoppelt ebenfalls die Einnahmen auf ihrer Linie (`deliver_passengers.script.tl:284-298`).

## Lieferzeiten

Jede Fracht hat ihre eigene Lieferzeit (`meat.cargo.lua:30`, `coal.cargo.lua:30`). Frischware hat die kürzeste, schwere Rohstoffe fünfmal mehr:

```diagram delivery_times
```

- **Finanzen › Lieferzeit** zeigt die Zeit jeder Fracht auf deiner Karte; die Ebene Güterzufriedenheit färbt die Strecken von grün bis rot.
- Eine Lieferung gilt als **verzögert**, wenn sie nach ihrer Lieferzeit ankommt (`towns.script.tl:425`).
- Spezialisierte Lagermodule **frieren** die Lieferzeit der gelagerten Fracht ein (offizielles Wiki, Warehouses).

```engine
Die Engine macht aus der Grundzeit die in Finanzen gezeigte Lieferzeit (die Skripte lesen sie mit getAdjustedDeliveryTime) und entscheidet, wann eine Einheit verspätet ist. Nur die relativen Werte oben stammen aus den Frachtdateien.
```

## Was eine Verspätung kostet: die Lieferungs-Bewertung

Verspätete Fracht wird voll bezahlt, aber jede Stadt führt eine **Lieferungs**-Bewertung (`town_util.tl:505-519`):

1. Das Spiel zählt die Lieferungen an die Stadt im **letzten Halbjahr** und wie viele verspätet waren (mindestens 10 werden angenommen, damit die ersten Lieferungen sie nicht kippen).
2. Pünktlicher Anteil → Bewertung: unter einer unteren Grenze ist sie 0, über einer oberen 1, dazwischen linear. Mit der Standard-Empfindlichkeit (**Normal**): **30 % pünktlich → 0, 100 % → 1**, also ergeben 90 % pünktlich 0,86.
3. Die Einstellung **Lieferungsempfindlichkeit** verschiebt die Grenzen (`difficulty_util.tl:47`). Aus: immer 1. Vorgaben: Easy Niedrig, Normal Normal, Hard Hoch, Very Hard Sehr hoch (`difficulty_util.tl:113`).

```diagram delivery_rating
```

Lieferung ist eine der sechs Wertungen, deren niedrigste die Wachstumsrate der Stadt bestimmt: eine einzige Wertung Sehr schlecht stoppt die Stadt (siehe [Stadtwachstum](towns.html)).

## Beispiel

Dieselbe Kohlelieferung, 5 km Luftlinie.

| Situation | Bezahlt |
|---|---|
| flach, egal wie lang die Strecke | **100 %** |
| 10 km Luftlinie | **200 %** |
| Ziel 100 m höher | **116 %** |
| verspätet geliefert | **100 %** (Lieferungs-Bewertung sinkt) |
| Unternehmensrang 15, Inflation Normal | **75 %** |
| Linie einer erfüllten Subvention | **200 %** |

## Gut zu wissen

- Da jede Fracht pro Kilometer gleich viel bringt, **wähle Frachten nach Menge, Entfernung und Lieferzeit**, nicht nach Preis.
- Lieferzeiten zählen vor allem bei Fleisch, Fisch, Gemüse und Getränken: kurze Linien oder Lager, die die Zeit einfrieren.
- Jede an ein Stadtgebäude gelieferte Einheit gibt dieser Stadt auch Erfahrung (`town_growth.script.tl:642`, `town_growth_config.res.lua:5`).

```check
official: „The farther people and cargo travel, the higher the revenue … distances are measured 'as the crow flies'." „While delayed cargo still provides the full income, the on time delivery rating drops, hindering town growth." ([Tips & Tricks](https://wiki.transportfever3.com/doku.php?id=gamemanual:gettingstarted:tipstricks), [Towns](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:towns))
scripts: Derselbe Faktor 3,8 für alle Frachten; Entfernung in 3D plus 8 × Steigung; der Unternehmensrang senkt die Einnahmen bis ×0,75 bei Rang 15 (Inflation Normal); ×2 nach einer Subvention; die Zeit wird für die Einnahme nicht genutzt; im Spiel gemessen: Eine Einheit, die die Linie wechselt, wird einmal beim Abnehmer bezahlt und nach Abschnittslänge zwischen den Linien geteilt; Lieferungs-Bewertung aus dem pünktlichen Anteil des letzten Halbjahrs (Normal: 30 % → 0, 100 % → 1).
result: refines
```
