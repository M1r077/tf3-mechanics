---
title: Industrien
summary: Produktionsregeln, Lager, Parzellen und Erweiterung, Booster-Fracht, warum eine Industrie nicht geboostet ist, und wann eine ungenutzte Industrie wirklich schließt.
domain: industries
official: gamemanual:simulation:industriescargos
status: verified
updated: 2026-11-15
fact: 5 Jahre | ohne Verladen oder Verbrauch machen eine Industrie zum Schließungskandidaten
fact: 1,1 % | Chance pro Jahr bei Selten (Standard), dann 730 Tage Countdown
fact: +50–150 % | Bonus der Booster-Fracht, pro Industrie fest
fact: 3 Monate | Bonus pro Charge Booster-Fracht
---

Jede Industrie arbeitet nach **Regeln**: „nimm dies aus den Eingangsbeständen, lege das in die Ausgangsbestände“, eine feste Anzahl Mal pro Jahr. Rohstoffindustrien (Bergwerke, Höfe, Quellen) brauchen keinen Eingang; ihre Größe kommt von ihren **Parzellen**. Zwei Boni können die Produktion vervielfachen: **Booster-Fracht** (nur Rohstoffindustrien) und **Arbeiter**.

## Produktionsregeln

- Eine Regel gibt die verbrauchte und erzeugte Fracht pro Durchlauf an und wie viele Durchläufe pro Jahr: ein Durchlauf dauert ein Jahr ÷ diese Zahl (`industry_react_util.tl:51-57`). Der Abschnitt Produktion im Industriefenster zeigt sie als kleine Zahlen.
- Die Zahl **Max.** im Fenster ist: pro Durchlauf × Durchläufe pro Jahr × die Boni × die Einstellung **Industrieproduktivität** (`industry_util.tl:310-379`).
- **Industrieproduktivität**: 50 %, 75 %, 100 %, 150 % oder 200 %. Voreinstellungen: Einfach 150 %, Normal 100 %, Schwierig 75 %, Sehr schwierig 50 % (`difficulty_util.tl:41`, `difficulty_util.tl:93`, `difficulty_util.tl:120`, `difficulty_util.tl:148`, `difficulty_util.tl:175`, `mod.script.tl:196-197`).
- Beispiel Stahlwerk: 6 Eisenerz + 6 Kohle → 3 Stahl + 4 Blech, 121,7 Durchläufe pro Jahr: 730 Eisenerz und 730 Kohle → 365 Stahl und 487 Blech (`steel_mill.con.lua:43-71`). Fehlt ein Eingang, steht die Regel.
- Die Konservenfabrik hat zwei Regeln: Fisch + Blech oder Fleisch + Blech (`food_factory.con.lua:43-74`).

```engine
Die Engine führt die Regeln aus. Sie kann einen Durchlauf verlängern: der Tooltip zeigt dann „(+ … aufgrund der Lieferzeit)“ (`industry_react_util.tl:61-76`). Wann und um wie viel steht nicht in den Skripten, daher kann die echte Produktion unter Max. bleiben.
```

## Lager

- Jede Fracht hat ihr eigenes Lager mit Grenze: z. B. hält ein Kohlebergwerk 100 Werkzeuge und 400 Kohle, ein Stahlwerk 800 Eisenerz, 800 Kohle, 400 Stahl und 500 Blech (`coal_mine.con.lua:44-67`, `steel_mill.con.lua:43-71`).
- Lager verfallen nie (`industryutil.lua:25-29`): Fracht wartet so lange wie nötig.
- Ein volles Ausgangslager stoppt die Produktion nicht: der Überschuss wird vernichtet (offizielles Wiki). Das Diagramm **Güterfluss** zeigt **Verbraucht**, **Produziert** und **Vernichtet** (`industry_eow.script.tl:804-816`).
- Mit dem Bauparameter **Eingang** auf Aus verlieren die Regeln ihre Eingänge und die Industrie hat keine Eingangsbestände (`industryutil.lua:280-287`, `industryutil.lua:383-387`, `industryutil.lua:432-441`).

## Parzellen und Erweiterung

- Rohstoffindustrien und der Viehzuchtbetrieb haben **Parzellen** (Felder, Schächte, Bohrtürme). Ihre Stufe ist ihre Zahl an Parzellen (`industryutil.lua:602-617`).
- Die Regel wächst mit den Parzellen: Produktion pro Durchlauf × Parzellen ÷ **alle Parzellen dieses Industrietyps**, gerundet, mindestens 1. Die Eingänge sinken im gleichen Verhältnis (`industryutil.lua:225-259`). Ein Kohlebergwerk (8 Parzellentypen) mit 4 Parzellen macht 8 statt 16 Kohle pro Durchlauf.
- Jede Industrie erhält ein Maximum: zufällig zwischen der Hälfte und allen Parzellen, oder Klein / Mittel / Groß (50 / 75 / 100 %) mit dem Parameter **Industriegrösse** (`industryutil.lua:519-537`). Ein Bergwerk mit Maximum 5 von 8 erreicht nie die volle Regel.
- Jedes halbe Jahr kann das Spiel **eine Parzelle** hinzufügen (`industries_config.res.lua:5`, `industries.script.tl:158-183`). Die Chance ist (Wertung − 25 %) ÷ 50 %, mit Wertung = Produktionswertung × dem Anteil der Produktion, den du abtransportierst (höchstens 1): 25 % oder weniger nie, 75 % oder mehr immer (`industries.script.tl:172-176`).
- Eine Industrie, deren Fracht du nicht abtransportierst, **wächst also nie**. Fabriken haben keine Parzellen und wachsen nie.
- Am Maximum zeigt das Fenster **Maximale Industrieerweiterung erreicht.**; stehen Gebäude, Gleise oder Straßen im Weg, **Industrieerweiterung ist blockiert.** (`industry_react_util.tl:588-602`, `industries.script.tl:13-38`). Kein Skript entfernt Parzellen; laut offiziellem Wiki senken abgerissene Parzellen die Produktion.

```engine
Die Produktionswertung (getProductionRating), die jährliche Produktion und die abtransportierte Menge (getCargoOutputPerYear, getCargoShippedPerYear) und wohin eine neue Parzelle kommt (makeIndustryExtendProposal) sind Werte der Engine.
```

## Booster-Fracht

Die 13 Rohstoffindustrien haben eine zweite Regel, den **Booster**: er nimmt 4-mal pro Jahr eine Charge Booster-Fracht aus dem Eingangslager und gibt einen Bonus, solange er läuft.

| Industrie | Parzellen | Bei voller Größe, pro Jahr | Booster-Charge (4 pro Jahr) | Quelle |
|---|---|---|---|---|
| Lehmgrube | 8 | 365 Lehm | 12 Werkzeuge | `clay_pit.con.lua:42-82` |
| Kohlebergwerk | 8 | 320 Kohle | 13 Werkzeuge | `coal_mine.con.lua:44-85` |
| Baumwollplantage | 21 | 274 Wolle | 17 Dünger | `cotton_farm.con.lua:42-98` |
| Bauernhof | 20 | 274 Getreide + 183 Gemüse | 17 Dünger | `farm.con.lua:44-106` |
| Fischzucht | 18 | 263 Fisch | 12 Werkzeuge | `fishing_grounds.con.lua:44-101` |
| Holzfällerlager | 20 | 243 Holz | 15 Maschinen | `forest.con.lua:44-99` |
| Eisenerzbergwerk | 8 | 365 Eisenerz | 15 Maschinen | `iron_ore_mine.con.lua:44-84` |
| Ölplattform | 9 | 365 Rohöl | 12 Maschinen | `oil_platform.con.lua:45-96` |
| Ölquelle | 14 | 548 Rohöl | 15 Maschinen | `oil_well.con.lua:44-94` |
| Steinbruch | 7 | 365 Stein | 12 Werkzeuge | `quarry.con.lua:44-83` |
| Gummiplantage | 23 | 365 Gummi | 17 Dünger | `rubber_farm.con.lua:41-102` |
| Sandbaggerschiff | 9 | 365 Sand | 15 Maschinen | `sand_excavator.con.lua:44-92` |
| Sandgrube | 8 | 365 Sand | 12 Werkzeuge | `sand_pit.con.lua:44-84` |

- Der Bonus wird einmal pro Industrie gezogen: **+50 % bis +150 %**, auf 1 % gerundet (`industryutil.lua:394-405`). Der Abschnitt Booster zeigt ihn als „+X %“ (`industry_util.tl:428-434`). Mit dem Parameter **Boost-Faktor** ist er stattdessen +50 %, +75 %, +100 %, +125 % oder +150 % (`industryutil.lua:289-299`).
- Das Fenster zeigt den Booster aktiv, solange seine letzte Charge läuft (3 Monate), oder sobald das Lager eine volle Charge enthält (`industry_util.tl:55-91`).
- Die Charge schrumpft **nicht** mit den Parzellen: ein kleines Bergwerk braucht so viele Werkzeuge wie ein großes (`industryutil.lua:227-229`).
- Beide Boni multiplizieren sich: Produktion × Arbeiterfaktor × (1 + Booster-Bonus) (`industry_util.tl:42-104`).

## Der Arbeiterbonus

Die Hälfte der Arbeitsplätze (10 von 20) muss mit Einwohnern besetzt sein, die in den letzten 2 Jahren **mit deinen Personenlinien angekommen** sind; der Faktor beträgt ×1,5 bis ×2,5, pro Industrie fest (`industry_productivity_util.tl:35-72`). Nur zugeteilte Arbeiter zählen nicht. Details: [Arbeiter und Arbeiterbonus](workers.html).

## Warum ist meine Industrie nicht geboostet?

1. **Keine Rohstoffindustrie**: Fabriken haben keine Booster-Regel, nur den Arbeiterbonus (`steel_mill.con.lua:61-70`).
2. **Charge unvollständig**: das Lager muss eine volle Charge enthalten, z. B. 13 Werkzeuge für ein Kohlebergwerk. Unter 4 Chargen pro Jahr (52 Werkzeuge) stoppt der Bonus zwischen den Lieferungen.
3. **Falsche Fracht**: Werkzeuge, Maschinen oder Dünger je nach Industrie (Tabelle oben).
4. **Arbeiter**: zugeteilt reicht nicht; der Abschnitt Booster zählt Ankünfte („12/10“) (`industry_react_util.tl:617-654`). Siehe [Arbeiter und Arbeiterbonus](workers.html).

## Wann schließt eine ungenutzte Industrie?

```diagram ind_closure
```

Die Prüfung läuft alle 100 Updates für jede Industrie (`industries.script.tl:84-85`):

1. **Kandidat**: keine Fracht in ein Fahrzeug **verladen** und keine **verbraucht** für **5 Jahre** (ab dem Bau, falls nie) (`industries.script.tl:104-119`, `industries_config.res.lua:6`). Nur Produzieren zählt nicht.
2. **Zufall**: jedes Jahr wird ein Kandidat mit der Chance der Einstellung **Häufigkeit von Industrieschliessungen** markiert (Tabelle unten) (`industries.script.tl:120-131`).
3. **Countdown**: die Meldung **Industrieschliessung** erscheint, mit 2 Jahren (730 Tagen) Frist (`industries_config.res.lua:7`, `industry_close.script.tl:53-67`). Danach wird die Industrie mit ihren eigenen Straßenstücken entfernt (`industries.script.tl:147-155`, `industry_util.tl:560-601`).
4. **Gerettet**: ein einziges Verladen oder ein Verbrauch während des Countdowns bricht ihn ab (`industries.script.tl:134-137`). Eine angenommene Subvention **Industrie beliefern** oder **Transportiere Arbeiter** für sie bricht ihn ebenfalls ab (`subvention_util.tl:473-484`).

| Häufigkeit von Industrieschliessungen | Chance pro Jahr als Kandidat | Hälfte der Kandidaten markiert nach | Voreinstellung | Quelle |
|---|---|---|---|---|
| Nie | 0 | nie | Einfach | `difficulty_util.tl:94` |
| Selten (Standard) | 1,1 % | etwa 63 Jahren | Normal | `difficulty_util.tl:121` |
| Manchmal | 2,2 % | etwa 32 Jahren | Schwierig | `difficulty_util.tl:149` |
| Oft | 4,4 % | etwa 16 Jahren | – | `difficulty_util.tl:37` |
| Sehr oft | 8,8 % | etwa 8 Jahren | Sehr schwierig | `difficulty_util.tl:176` |

Die Chance ist 0,011 pro Jahr × 0, 1, 2, 4 oder 8 (`mod.script.tl:171`, `mod.script.tl:202-203`, `difficulty_util.tl:37`). Industrien in deinem Besitz schließen nie, ebenso wenig Industrien mit manueller Entwicklung und keine Industrie während des Tutorials (`industries.script.tl:94-102`).

```engine
Was als „verladen“ und „verbraucht“ zählt (die Logs itemsLoaded und itemsConsumed, z. B. ob Booster-Fracht zählt), das Flag manualDevelopment und warum Industrien mit Depot ausgenommen sind (`industries.script.tl:140-146`), liegt in der Engine. Ebenso, was die Engine mit einer Booster-Regel ohne Eingang macht (Eingang aus).
```

## Neue Industrien

- Die Engine fügt mit der Zeit Industrien hinzu; die Skripte geben ihr nur eine Zielzeit von 50 Jahren, einen Exponenten von 3 und keine neuen Industrien im Karteneditor (`mod.script.tl:166-168`). Die Einstellung **Industrie-Zieldichte** skaliert das (`mod.script.tl:194-195`). Die Meldung heißt **Neue Industrie gegründet** (`industry_spawn.res.lua:6`).
- Der Firmen-Perk **Prospektion nach Ressourcen** sucht eine neue Industrie dieser Ressource nahe einer Stadt: ein Versuch pro Monat mit einer Chance von 20 % bis 60 %, 6 Monate lang; scheitert er, kommt die Genehmigung zurück (`company_util.tl:14-17`, `company.script.tl:96-142`, `company.script.tl:299-307`).

```engine
Wo und wann eine neue Industrie entsteht, und welcher Typ, entscheidet die Engine (makeIndustrySpawnProposal).
```

## Gut zu wissen

- Transportiere von jeder Rohstoffindustrie ab, die wachsen soll: nicht abtransportierte Produktion blockiert die Erweiterung, egal welche Boni.
- Gib Booster-Fracht den größten Bergwerken und Höfen: die Charge kostet gleich viel, der Bonus wächst mit den Parzellen.
- Lager verfallen nicht: du kannst Booster-Fracht im Voraus liefern, bis zur Lagergrenze (100).
- Boni erhöhen Lärm und Verschmutzung: ein Kohlebergwerk geht von 10 Verschmutzung auf 20 mit einem Bonus und 30 mit zwei (`coal_mine.con.lua:99-117`).
- Bei der Standardeinstellung schließt eine ungenutzte Industrie selten; bei Sehr oft lade ab und zu etwas.

```check
official: "No goods have been consumed/produced in the last 10 years. No goods have been shipped from this industry in the last 10 years. [...] For abandoned industries there is a countdown of 730 days before the industry is effectively closed." ([Industries and Cargo](https://wiki.transportfever3.com/doku.php?id=gamemanual:simulation:industriescargos))
scripts: 5 Jahre, nicht 10, und Produktion zählt nicht: nur in ein Fahrzeug verladene oder verbrauchte Fracht. Nach den 5 Jahren ist die Industrie nur Kandidat: jedes Jahr wird sie mit einer Chance von 1,1 % (Selten) bis 8,8 % (Sehr oft) markiert. Der Countdown dauert wie angegeben 730 Tage. Booster-Fracht gibt +50 % bis +150 % pro Industrie, in Chargen, die 3 Monate halten.
result: differs
```
