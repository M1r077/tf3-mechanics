---
title: Subventionen: Angebote, Fristen und Belohnungen
summary: Die vier Vertragsarten, was sie wirklich erfüllt, was du bekommst und was du riskierst, und wie oft neue Angebote kommen.
domain: subsidies
official: gamemanual:management:subsidies
status: verified
updated: 2026-11-15
game: 40444
change: 40444 | Städte verbinden: Die Linie, die das ×2 bekommt, wird bei Erfüllung des Vertrags festgelegt; ein Passagier zählt erst nach Annahme des Angebots; jede direkte Linie mit einem Passagierfahrzeug blockiert das Angebot.
fact: 4 | Vertragsarten im freien Spiel
fact: 5 | angenommene Verträge höchstens gleichzeitig
fact: ×2 | Einnahmen für 5 Jahre auf den Linien, die geliefert haben
fact: 0 | Strafe für das Ablehnen eines Angebots
---

Eine Subvention ist ein Vertrag: Eine Industrie oder eine Stadt bietet eine Aufgabe an, beim Annehmen bekommst du etwas, mehr, wenn du sie rechtzeitig erfüllst, und du zahlst die Vorauszahlung plus eine Strafe zurück, wenn du die Frist verpasst. Ein Angebot abzulehnen oder verfallen zu lassen, kostet nichts.

```diagram subsidy_life
```

## Die vier Vertragsarten

```diagram subsidy_types
```

| Vertrag | Ziel | Was ihn erfüllt | Quelle |
|---|---|---|---|
| **Industrie beliefern** | eine Industrie, die noch nie etwas produziert hat und eine Fracht braucht, die schon irgendwo auf der Karte produziert wird (`deliver_cargo.script.tl:163`) | die verlangte Zahl an Lieferungen zu ihr, **mit irgendeinem ihrer Rohstoffe** | `deliver_cargo.script.tl:60-67`, `deliver_cargo.script.tl:236-240`, `deliver_cargo.script.tl:463-472` |
| **Stadt versorgen** | eine Fracht, die die Stadt verlangt und gar nicht bekommt | die verlangte Zahl an Einheiten **dieser Fracht**, geliefert an Gebäude der Stadt | `deliver_cargo_town.script.tl:559-574` |
| **Städte verbinden** | zwei Städte | **ein** Passagier, der eine Fahrt zwischen den beiden Städten auf einer Linie beginnt, die in beiden hält | `deliver_passengers.script.tl:252-274`, `subvention_util.tl:561-592` |
| **Transportiere Arbeiter** | eine Industrie, die schon Fracht versendet oder empfängt, noch nicht geboostet | ihr Arbeiterbonus wird aktiv (die Hälfte ihrer Arbeitsplätze) | `deliver_workers.script.tl:121-131`, `deliver_workers.script.tl:152-156` |

- Jedes neue Angebot wählt eine der Arten, die gerade erscheinen können, mit gleichen Chancen (`subventions.script.tl:147-169`).
- **Industrie beliefern** und **Stadt versorgen** zählen Lieferungen, nicht Fahrten: Jede bezahlte Einheit, die am Ziel ankommt, zählt 1. Umladen ist erlaubt (`deliver_cargo.script.tl:463-472`).
- **Städte verbinden** verlangt keine Passagierzahl: Der erste Passagier, der zwischen den beiden Städten in deine Linie steigt, erfüllt ihn. „Ohne Umstieg" heißt, dass diese Fahrt auf einer einzigen Linie läuft, die beide Städte bedient. Es kommt kein Angebot, wenn schon eine Linie in beiden Städten Passagiere lädt und ein Fahrzeug hat, das sie befördern kann (`deliver_passengers.script.tl:76-85`).
- Nahe Städte sind viel wahrscheinlicher: Das Gewicht eines Paares ist (Entfernungsgewicht)^7 × 100 plus der **Durchschnitt** der Werte der beiden Städte, jeder mindestens 1, die die Engine an der Position der Stadt aus ihrem Raster der Spieler-Infrastruktur liest (`deliver_passengers.script.tl:159`, `deliver_passengers.script.tl:183`, `deliver_passengers.script.tl:188`). Das Entfernungsgewicht ist 1 bei 1 km und fällt gleichmäßig auf 0,01 bei 20 km (`deliver_passengers.script.tl:157-159`, `deliver_passengers.script.tl:175-191`). Der Entfernungsteil ist also etwa 19 bei 5 km, etwa 1 bei 10 km und fast null ab etwa 15 km; dort bleiben nur die Werte der Städte.
- **Stadt versorgen** bevorzugt Frachten, die schon irgendwo auf der Karte produziert werden: 16-mal wahrscheinlicher als die anderen (`deliver_cargo_town.script.tl:283-286`).
- Die zu liefernde Menge hängt von der Einstellung **Subventionsrisiko** ab:

| Subventionsrisiko | Industrie beliefern | Stadt versorgen (höchstens der Bedarf der Stadt) | Quelle |
|---|---|---|---|
| Keines | 10–50 | 10–30 | `deliver_cargo.script.tl:106-120`, `deliver_cargo_town.script.tl:171-194` |
| Fair | 50–100 | 30–100 | |
| Riskant | 75–150 | 35–125 | |
| Sehr riskant | 150–300 | 45–150 | |

## Was ist eine umsteigefreie Verbindung?

Die Karte **Städte verbinden** verlangt: „Richte eine umsteigefreie Verbindung von {fromTownName} nach {toTownName} ein und transportiere Passagiere zwischen den beiden Städten.“ (`deliver_passengers.script.tl:14`).

- **Eine Linie mit einem Halt in jeder Stadt.** Das Spiel geht die Halte der Linie durch und nimmt jeweils die Stadt des Halts; die Linie zählt, wenn mindestens ein Halt in jeder der beiden Städte liegt. Andere Halte, ihre Reihenfolge und der Fahrzeugtyp (Bus, Tram, Zug, Schiff, Flugzeug) spielen keine Rolle (`subvention_util.tl:561-592`).
- **Ein Passagier erfüllt ihn**: der erste Passagier nach Annahme des Angebots, der mit dieser Linie von einem Halt in der einen Stadt zu einem Halt in der anderen fährt, in beide Richtungen (`deliver_passengers.script.tl:252-274`, `deliver_passengers.script.tl:207-215`). Die Prüfung betrachtet nur diese Fahrt, ein Umstieg davor oder danach sollte also keine Rolle spielen.
- **Die Stadt eines Halts** ist die Stadt des ersten Bahnhofs seiner Bahnhofsgruppe (`town_util.tl:1844-1873`). Zu welcher Stadt ein Bahnhof gehört, entscheidet die Engine.
- **Kein Angebot**, wenn irgendeine Linie schon in jeder Stadt einen Halt hat, der Passagiere lädt, und ein Fahrzeug, das Passagiere befördert; jede solche Linie wird geprüft (`deliver_passengers.script.tl:76-85`). Eine reine Güterlinie zwischen ihnen blockiert das Angebot nicht.
- Der Vertrag endet als **Subvention entfernt**, wenn sich eine der beiden Städte oder die Linie, die ihn erfüllt hat, so ändert, dass das Spiel es als neue Version zählt (`deliver_passengers.script.tl:229-237`).

```engine
Zu welcher Stadt ein Bahnhof gehört (stationSystem.getTown), wann genau ein Passagier eine Linie „zu nutzen beginnt“ (OnStartedLineUsage) und welche Änderungen an einer Linie als neue Version zählen, liegt bei der Engine. Ob eine Änderung der Linie nach der Erfüllung den Effekt 2-faches Einkommen beendet, wurde nicht getestet.
```

## Belohnungen und Strafen

Jeder Vertrag hat drei Listen, auf seiner Karte als **Bei Annahme**, **Bei Erfüllung** und **Bei Misserfolg** angezeigt; die Skripte wenden sie bei Annahme, Erfüllung und Misserfolg an (`subvention_util.tl:449-471`). Bei Misserfolg wird alles zurückgenommen, was bei Annahme gegeben wurde, plus eine Strafe, bei Städte verbinden zwei, ein Reputationsverlust in jeder Stadt (`subvention_util.tl:457-463`, `deliver_cargo.script.tl:140-142`, `deliver_passengers.script.tl:118-121`).

| Vertrag | Bei Annahme | Bei Erfüllung | Bei Misserfolg | Quelle |
|---|---|---|---|---|
| Industrie beliefern | Geld | nur der Effekt **2-faches Einkommen** | Vorauszahlung zurück + Strafe | `deliver_cargo.script.tl:126-142` |
| Stadt versorgen | Geld **oder** Ruf in der Stadt | Stadterfahrung **oder** Geld, plus 2-faches Einkommen | Vorauszahlung zurück + Rufverlust **oder** Strafe | `deliver_cargo_town.script.tl:200-235` |
| Städte verbinden | Geld, mehr bei weit entfernten Städten | Erfahrung in **beiden** Städten, plus 2-faches Einkommen | Vorauszahlung zurück + Rufverlust in **beiden** Städten | `deliver_passengers.script.tl:112-126` |
| Transportiere Arbeiter | Geld | Geld | Vorauszahlung zurück + Strafe | `deliver_workers.script.tl:92-116` |

- **Geld**, vor der Jahresskalierung: Vorauszahlung 1,5 Mio. bis 3,75 Mio. × Risikofaktor (Keines ×2, Fair ×1, Riskant ×0,75, Sehr riskant ×0,5, oder ×0,625 bei Städte verbinden und Transportiere Arbeiter), bei Städte verbinden außerdem × Entfernungsfaktor (0,3 bis 3,0); Strafe 3 Mio. bis 6 Mio.; Zahlung bei Erfüllung 3,75 Mio. bis 11,25 Mio. (`deliver_cargo.script.tl:106-134`, `deliver_passengers.script.tl:89-113`, `deliver_workers.script.tl:64-104`). Jeder Geldbetrag wird außerdem mit einem Faktor der Basiskonfiguration multipliziert, `subventionFinancialRewardMultiplier` (`deliver_cargo.script.tl:126`), dessen Wert nicht in den Skripten steht.
- Geld wächst mit dem **Kalenderjahr**, nicht mit der Einstellung Inflation: ×1 im Jahr 1900, gleichmäßig steigend bis ×4 ab 2000, auf 10.000 aufgerundet (`finances_util.tl:87-90`). Es wird in den Finanzen als **Subventionen** gebucht (`subvention_util.tl:126-135`).
- **Stadt versorgen** kann eine Geldzahlung bei Erfüllung und eine Geldstrafe nur haben, wenn dein Konto beim Erstellen des Angebots unter 100 Mio. liegt; darüber nur noch 1 Angebot von 10, die anderen geben Stadterfahrung und nehmen stattdessen Reputation. Die Vorauszahlung ist nicht betroffen (`deliver_cargo_town.script.tl:200-235`).
- **Stadterfahrung** ist ein Anteil der aktuellen Stufe der Stadt: 20 % bis 100 % der XP zwischen ihrer Stufe und der nächsten (`deliver_cargo_town.script.tl:222`, `town_growth.script.tl:605-608`). Bei **Städte verbinden** wird sie mit dem Entfernungsfaktor multipliziert, 0,3 bei 1 km bis 3,0 bei 20 km: Weit entfernte Städte können mehrere Stufen gewinnen (`deliver_passengers.script.tl:101-103`, `deliver_passengers.script.tl:123-125`).
- Nach einem Misserfolg verlorener **Ruf** erscheint in der Ruf-Bewertung der Stadt als **Gescheiterte Subvention** (`towns.script.tl:310-331`). Bei Annahme gewonnener Ruf entfernt nur bestehende Abzüge, er geht nie über das Maximum (`town_util.tl:1644-1647`).

## Der Effekt 2-faches Einkommen

- Er dauert **60 Monate** (5 Jahre) nach der Erfüllung des Vertrags (`subvention_util.tl:286`, `subvention_util.tl:292`).
- **Industrie beliefern**: Lieferungen an diese Industrie, auf den Linien, die sie während des Vertrags beliefert haben (`deliver_cargo.script.tl:456-462`).
- **Stadt versorgen**: Lieferungen an jedes Gebäude der Stadt, **jede Fracht**, auf den Linien, die die Vertragsfracht geliefert haben (`deliver_cargo_town.script.tl:547-558`).
- **Städte verbinden**: Passagiere zwischen den beiden Städten, auf nur **einer** direkten Linie: der Linie, die den Vertrag erfüllt hat. Sie ändert sich nach der Erfüllung nicht mehr, auch nicht bei mehreren direkten Linien (`deliver_passengers.script.tl:252-299`).
- Die Karte nennt die Linien: "2x Income for {duration} on All Supplying Lines" für Industrie beliefern und Stadt versorgen (`deliver_cargo.script.tl:40-41`, `deliver_cargo_town.script.tl:44-45`), "2x Income for {duration} on First Established Connection" für Städte verbinden (`deliver_passengers.script.tl:48-51`).
- **Transportiere Arbeiter** hat keinen Einkommenseffekt (`deliver_workers.script.tl:189-190`).
- Bei Industrie beliefern und Stadt versorgen gilt: Eine Linie, die erst nach der Erfüllung zu liefern beginnt, bekommt nichts: Die Liste der Linien wird nur während des Vertrags gefüllt.
- Zwei Verträge verdoppeln dieselbe Zahlung nie zweimal: Passen mehrere, zählt nur die letzte Antwort (`subventions.script.tl:570-583`).

```tip scripts
**Doppeltes Einkommen von Industrie beliefern oder Stadt versorgen auf mehreren Linien? Lass alle liefern, bevor der Vertrag erfüllt ist.** Eine danach hinzugefügte Linie bekommt nichts. Städte verbinden verdoppelt nur eine Linie, die, die ihn erfüllt hat: Lass die Linie, die verdoppelt werden soll, den ersten Passagier befördern.
```

```engine
Wie sich das ×2 einer Subvention mit dem Multiplikator des Unternehmensrangs (Einstellung Inflation) verbindet, entscheidet die Engine: Beide Skripte geben nur einen Multiplikator pro Zahlung zurück. Was ein Zahlungseintrag ist (vermutlich eine Frachteinheit oder ein Passagier), entscheidet ebenfalls die Engine.
```

## Fristen

Die Frist beginnt mit der Annahme. Sie ist länger, wenn die Fracht weit reisen muss, und kürzer bei höherem Risiko (Risikofaktor Keines ×2, Fair ×1, Riskant ×0,75, Sehr riskant ×0,5, oder ×0,625 bei Passagier- und Arbeiterverträgen):

| Vertrag | Frist in Monaten | Verwendete Entfernung | Quelle |
|---|---|---|---|
| Industrie beliefern, Stadt versorgen | (6 + 32 × E) × Risikofaktor | zur nächsten Industrie, die die Fracht produziert | `deliver_cargo.script.tl:122-123` |
| Städte verbinden | (9 + 4 × E) × Risikofaktor | zwischen den beiden Städten | `deliver_passengers.script.tl:105-106` |
| Transportiere Arbeiter | (6 + 15 × E) × Risikofaktor × Epochenfaktor (×1,75 vor 1940, ×1,25 vor 1980) | zur nächsten Stadt | `deliver_workers.script.tl:75-87` |

E ist die Zeit, die ein Zug mit der Höchstgeschwindigkeit der Epoche (120 km/h ab 1900 bis 300 km/h ab 1981) für diese Entfernung braucht, aufgerundet, mindestens 1 (`subvention_util.tl:486-489`, `vehicle_util.tl:225-230`).

- Ein nicht angenommenes Angebot verschwindet nach etwa **6 Monaten** (150 bis 210 Tage), ohne Strafe (`subvention_util.tl:284`, `subvention_util.tl:290`).
- Solange ein Vertrag **Industrie beliefern** oder **Transportiere Arbeiter** läuft, kann die Zielindustrie nicht schließen: Eine geplante Schließung wird aufgehoben (`subvention_util.tl:473-484`).
- Verschwindet das Ziel während des Vertrags oder wird es neu gebaut, zeigt das Spiel **Subvention entfernt**, aber die Strafen werden wie bei einer verpassten Frist angewendet (`subventions.script.tl:172-190`, `subvention_util.tl:406-412`).
- Es gibt keinen Knopf, um einen angenommenen Vertrag abzubrechen.

```engine
Wie lang ein Spielmonat ist, und damit die echte Länge der Fristen, legt die Engine fest (getDefaultMonthDuration). Die Formeln oben sind in Monaten des Spielkalenders.
```

## Wie oft neue Angebote kommen

- **Verfügbarkeit von Subventionen**: Selten, Manchmal (Standard), Oft, Sehr oft geben alle 12, 6, 3 oder 1 Monate ein neues Angebot; **Nie** schaltet Subventionen ab (`subvention_util.tl:13-38`, `mod.script.tl:248-249`).
- Der Abstand wächst mit dem **Unternehmensrang**: ×1 bei Rang 1 bis ×2 bei Rang 15 (`subvention_util.tl:19-22`).
- Ein Angebot **abzulehnen** halbiert den nächsten Abstand; Annehmen oder ein neues Angebot setzt ihn zurück (`subventions.script.tl:429`, `subventions.script.tl:395`, `subventions.script.tl:118`).
- Kein neues Angebot, solange **5 Verträge** angenommen sind und laufen (`subventions.script.tl:23`, `subventions.script.tl:256-262`). Das erste Angebot kommt nach einem halben Monat (`subventions.script.tl:25`).
- Dasselbe Ziel (Industrie, Stadt und Fracht, Städtepaar) wird **nur einmal pro Spiel** angeboten, auch nach einem verpassten oder gescheiterten Vertrag (`subventions.script.tl:107-113`, `subventions.script.tl:186`).
- Schwierigkeitsvorgaben, Verfügbarkeit / Risiko (`difficulty_util.tl:104-105`, `difficulty_util.tl:132-133`, `difficulty_util.tl:159-160`, `difficulty_util.tl:186-187`): Einfach Oft / Keines, Normal Manchmal / Fair, Schwierig Selten / Riskant, **Sehr schwierig Nie**: gar keine Subventionen.
- Die Prüfung, die Subventionen nur in Städten mit der Bewertung Sehr gut erlauben würde, existiert, ist aber abgeschaltet (`town_util.tl:1574-1580`, `deliver_cargo_town.script.tl:278-281`).

## Gut zu wissen

- Nimm ruhig an, wenn das Ziel leicht ist: Ablehnen oder Ignorieren kostet nichts, aber **Scheitern** kostet die Vorauszahlung plus eine Strafe, die größer sein kann als die Vorauszahlung.
- Bei **Stadt versorgen** und **Industrie beliefern** liefere mit jeder Linie, die profitieren soll: Nur die Linien, die während des Vertrags geliefert haben, bekommen 5 Jahre lang das 2-fache Einkommen.
- **Städte verbinden** mit weit entfernten Städten bringt die meiste Stadterfahrung und braucht nur einen Passagier.
- **Industrie beliefern** zahlt bei Erfüllung nichts extra: Seine Belohnung ist allein das 2-fache Einkommen.

```check
official: "Accept an offer to begin the contract; declining it has no penalty." "Possible rewards include town experience, an additional payment, or a limited-time 2x income effect on eligible transport lines." "The upfront reward is reversed, and an additional fine or loss of town reputation may apply." ([Subsidies](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:subsidies))
scripts: Vier Arten; ein Passagier erfüllt Städte verbinden; das ×2 gilt 60 Monate auf den Linien, die während des Vertrags geliefert haben; Industrie beliefern gibt nur das ×2; Geld nach Jahr skaliert (×1 bis ×4); alle 1–12 Monate ein neues Angebot, seltener bei hohem Rang; höchstens 5 angenommen; jedes Ziel einmal pro Spiel.
result: refines
```
