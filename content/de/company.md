---
title: Unternehmensrang, Vorteile und Hauptquartier
summary: Was deinen Unternehmensrang erhöht, was jeder Rang freischaltet, wie Genehmigungen und Prospektionen funktionieren, was das Hauptquartier wirklich bringt und was dich ein höherer Rang kostet.
domain: company
official: gamemanual:management:companyandfinances
status: verified
updated: 2026-11-17
game: 40425
fact: 15 | Unternehmensränge, von Junior bis Tycoon
fact: ×12,5 | Weltbevölkerung für Rang 15, verglichen mit dem Start
fact: ×0,75 | Einnahmen auf Rang 15 mit Inflation Normal
fact: 0 | verlorene Ränge, wenn die Bevölkerung sinkt
---

Dein Unternehmensrang kommt nicht von Geld oder Lieferungen, sondern von der **Bevölkerung der ganzen Karte**. Jeder neue Rang schaltet Vorteile frei (Wahrzeichen, Prospektionen, Marketingkampagnen, Industriebegrünung, Module des Hauptquartiers), und mit der Einstellung **Inflation** senkt er auch alle deine Einnahmen ein wenig.

## Was den Rang erhöht

- Das Spiel merkt sich die **Weltbevölkerung zu Spielbeginn**: die Einwohner aller Städte (`company.script.tl:392-396`, `company_util.tl:365-371`).
- Dann vergleicht es die **höchste** je erreichte Weltbevölkerung mit diesem Startwert (`company_growth.script.tl:25-27`). Der Wert steigt nur: Schrumpfende Städte kosten dich nie einen Rang.
- Rang 1 wird beim Startwert erreicht, Rang 15 bei etwa dem **12,5-Fachen** (`company_progression_util.tl:6-14`, `company_progression_util.tl:95-120`, `town_growth_function.tl:13-20`).
- In Kampagnenmissionen und im Karteneditor gibt es keinen Rang (`company_growth.script.tl:74-79`).

| Rang | Rolle | Weltbevölkerung, verglichen mit dem Start |
|---|---|---|
| 1 | Junior | ×1 |
| 2 | Mechaniker | ×1,02 |
| 3 | Ingenieur | ×1,08 |
| 4 | Koordinator | ×1,2 |
| 5 | Experte | ×1,4 |
| 6 | Teamleiter | ×1,7 |
| 7 | Bereichsleiter | ×2,1 |
| 8 | Manager | ×2,6 |
| 9 | Direktor | ×3,3 |
| 10 | Leitender Direktor | ×4,2 |
| 11 | CEO | ×5,3 |
| 12 | Vorsitzender | ×6,7 |
| 13 | Vize-Präsident | ×8,3 |
| 14 | Präsident | ×10,2 |
| 15 | Tycoon | ×12,5 |

Die Verhältnisse sind aus den Skripten für eine Startbevölkerung von 50.000 oder mehr berechnet (`company_progression_util.tl:6-14`, `company_static_util.tl:6-24`). Auf einer kleinen Karte liegen sie für die mittleren Ränge etwas höher (Rang 8 braucht ×2,85 bei 5.000 Einwohnern); Rang 1 und 15 bleiben bei ×1 und ×12,5.

- Der Rang folgt also dem **Stadtwachstum**: Städte wachsen durch deine Passagiere und Fracht, siehe [Stadtwachstum](towns.html).
- Die ersten Ränge kommen schnell, die letzten brauchen vielfach größere Städte.

## Ein neuer Rang wird im Unternehmensfenster angewendet

Wenn die Bevölkerung eine Schwelle überschreitet, erscheint eine **Rangaufstiegs-Benachrichtigung**; ein Klick darauf öffnet das Unternehmensfenster auf diesem Rang (`company_growth.script.tl:96-107`, `company_notification_rank_up.script.tl:8-9`).

- Die neuen Vorteile werden erst freigeschaltet, wenn dieser Rang **im Unternehmensfenster ausgewählt** wird: Das Fenster sendet dann die Freischaltung (`company.tl:420-423`, `company_growth.script.tl:55-62`). Die Baumenüs prüfen diesen angewendeten Rang (`company_util.tl:92`, `company_util.tl:171-178`).
- Der Einnahmenmultiplikator des nächsten Abschnitts folgt dem **erreichten** Rang, angewendet oder nicht (`company_growth.script.tl:47-48`).

```tip scripts
Klicke nach einem Rangaufstieg auf die Benachrichtigung (oder öffne das Unternehmensfenster und wähle den neuen Rang), um die Vorteile zu bekommen. Warten bringt nichts: Die Einnahmen sind schon gesenkt.
```

## Was ein höherer Rang kostet: die Einstellung Inflation

Mit **Inflation** sinken alle Fracht- und Passagiereinnahmen gleichmäßig von ×1 auf Rang 1 bis zu einem Minimum auf Rang 15 (`company_progression_util.tl:25-40`, `company_growth.script.tl:159-170`).

| Inflation | Einnahmen auf Rang 15 | Quelle |
|---|---|---|
| Aus | ×1 (keine Änderung) | `difficulty_util.tl:50`, `mod.script.tl:694-697` |
| Niedrig | ×0,9 | |
| Normal | ×0,75 | |
| Hoch | ×0,6 | |
| Sehr hoch | ×0,5 | |

- Bei Normal kostet jeder Rang etwa 1,8 % der Einnahmen: ×0,96 auf Rang 3, ×0,875 auf Rang 8, ×0,75 auf Rang 15.
- Inflation erhöht keine Kosten; die Kosten folgen dem Kalenderjahr (siehe [Kosten, Unterhalt und Kredite](costs.html)).
- Ein höherer Rang macht auch neue Vertragsangebote seltener (siehe [Verträge](subsidies.html)).

## Genehmigungen

Die meisten Vorteile sind durch **Genehmigungen** begrenzt. Ein Rang gibt Genehmigungen für einen Vorteil; jedes Gebäude oder jede Nutzung braucht eine (`company_util.tl:33-80`, `company_util.tl:206`).

- Genehmigungen **summieren sich** über die Ränge: Ein Vorteil, der 1 auf Rang 3 und 1 auf Rang 5 gibt, erlaubt ab Rang 5 zwei (`company_util.tl:51-56`).
- Ein Gebäude gibt seine Genehmigung beim Abriss zurück: Das Spiel zählt, was steht (`company_util.tl:143-163`, `company_util.tl:203-206`).
- Prospektionen, Marketingkampagnen und Begrünung verbrauchen beim Start eine Genehmigung (`company.script.tl:416-423`, `company.script.tl:459-462`, `company.script.tl:496-500`). Das Baumenü zeigt dann **Bereits verwendet** oder **Abklingzeit** (`company_util.tl:207-226`).
- Die **Marketing**-Genehmigung kommt **5 Jahre** nach jeder Kampagne zurück (`marketing.res.lua:6-7`, `company.script.tl:66-94`).

| Vorteil | Genehmigungen | Quelle |
|---|---|---|
| Hauptquartier | 1 auf Rang 1 | `hq.res.lua:6` |
| Marketingkampagne | 1 auf Rang 4, zurück nach 5 Jahren | `marketing.res.lua:6-7` |
| Industriebegrünung | je 1 auf Rang 3, 6, 9, 12 und 15 | `industry_greenify_tool.script.tl:101-102` |
| Reinigungsanlage | 15 auf Rang 10 | `pollution_cleanup_facility.con.lua:106-108` |
| Wahrzeichen | je eines: Amphitheater 2, Grosser Leuchtturm 5, Burg des weissen Reihers 7, Schifffahrtsmuseum 9, Schloss Neuschwanstein 10, Freiheitsstatue 11, Sommerpalast 13, Opernhaus 14, Parlament 15 | `arena.con.lua:39`, `lighthouse.con.lua:48`, `white_heron_castle.con.lua:47`, `ship_museum.con.lua:55`, `neuschwanstein.con.lua:55`, `statue_of_liberty.con.lua:57`, `summer_palace.con.lua:63`, `opera_house.con.lua:63`, `westminster.con.lua:79` |

Was jeder Vorteil bewirkt: [Ruf](reputation.html) (Marketingkampagne), [Verschmutzung und Lärm](emission.html) (Begrünung, Reinigungsanlage).

## Prospektionen

Eine Prospektion sucht eine Ressource nahe einer Stadt und gründet dort bei Erfolg eine neue Industrie.

| Ressource | Rang | Quelle |
|---|---|---|
| Fisch | 2 | `exploration_fish.res.lua:9-11` |
| Lehm | 3 | `exploration_clay.res.lua:9-11` |
| Rohöl | 4 | `exploration_crude_oil.res.lua:9-11` |
| Getreide, Gemüse | 4, **eine gemeinsame Genehmigung** (Industrie) | `exploration_grain.res.lua:9`, `exploration_vegetables.res.lua:9`, `permit_key_farm.res.lua:6` |
| Holz | 5 | `exploration_logs.res.lua:9-11` |
| Kohle, Eisenerz | 6 | `exploration_coal.res.lua:9-11`, `exploration_iron_ore.res.lua:9-11` |
| Stein, Wolle | 8 | `exploration_stone.res.lua:9-11`, `exploration_wool.res.lua:9-11` |
| Sand | 9 | `exploration_sand.res.lua:9-11` |
| Gummi | 12 | `exploration_rubber.res.lua:9-11` |

- Jede Ressource hat **eine** Genehmigung, die beim Start der Prospektion verbraucht wird (`company.script.tl:451-462`).
- Sie läuft bis zu **6 Monate**. Einmal im Monat versucht sie, die Industrie zu platzieren, mit einer Chance, die über die 6 Monate von 20 % auf 60 % steigt (`company_util.tl:14-17`, `company.script.tl:299-307`, `company.script.tl:130-142`).
- Ein Versuch scheitert auch, wenn das Spiel keinen Platz für diese Industrie nahe der Stadt findet (`company.script.tl:199-210`).
- Scheitert der letzte Versuch, **kommt die Genehmigung zurück** und eine Benachrichtigung meldet es (`company.script.tl:106-126`, `company.script.tl:170-181`).
- Pro Stadt und Ressource kann nur eine Prospektion gleichzeitig laufen (`company.script.tl:442-447`).

```engine
Wo die neue Industrie stehen darf (makeIndustrySpawnProposal nahe der Stadt), entscheidet die Engine: Eine Fischprospektion weit weg vom Wasser oder eine Stadt ohne freies Land ringsum scheitert einfach und gibt die Genehmigung zurück.
```

## Das Hauptquartier

| Was | Wert | Quelle |
|---|---|---|
| Preis und Unterhalt | kostenlos, kein Unterhalt | `headquarter.script.tl:526-527` |
| Genehmigung | 1, auf Rang 1 | `headquarter.con.lua:6-7`, `hq.res.lua:6` |
| Stadtwachstum | +5 % für die nächstgelegene Stadt | `headquarter.script.tl:510-515`, `landmark_util.tl:51-70` |
| Arbeitsplätze | 24 | `headquarter.con.lua:16`, `headquarter.script.tl:505-508` |

- Die +5 % sind ein Bonus auf die Wachstumsrate dieser Stadt und bewirken also nichts, wenn die Rate der Stadt 0 % ist (siehe [Stadtwachstum](towns.html)).
- **Module** kosten je 50.000 und sind durch Genehmigungen begrenzt, die mit dem Rang wachsen (`hq_module_m.module.lua:83`, `hq_module_m.module.lua:137`).
- Nur zwei Module haben in den Dateien einen Bonus: **Mittleres Gebäude** +1 % Stadtwachstum (`hq_module_m.module.lua:139-142`) und **Grosses Gebäude** +1 % Rufwiederherstellung (`hq_module_l.module.lua:169-172`). Den Wiederherstellungsbonus liest keine Stadtbewertung (siehe [Ruf](reputation.html)). Die anderen Module sind Dekoration.
- Jede Moduldatei beginnt außerdem mit einer Tabelle, die +5 % Stadtwachstum gibt, aber nichts in der Datei nutzt sie (`hq_corner_l.module.lua:148-159`, `hq_statue.module.lua:46-57`). Nur der Bonus in den `metadata` des Moduls wird addiert (`headquarter_addon.script.tl:18-29`).

| Modul | Genehmigungen gewonnen auf Rang (×2 = zwei) | Summe auf Rang 15 |
|---|---|---|
| Bodenflagge | 1 ×2, 6, 7, 8, 9, 11, 12, 13, 14 | 10 |
| Eckgebäude | 3, 5, 7 ×2, 9, 11, 13, 15 | 8 |
| Mittleres Gebäude | 2, 4, 10 ×2, 15 ×2 | 6 |
| Grosses Gebäude | 5, 6, 10, 12 | 4 |
| Balkon | 8 ×2, 14 ×2 | 4 |
| Grosser Springbrunnen | 10 ×2, 14 ×2 | 4 |
| Kuppel | 6, 15 ×2 | 3 |
| Dachflagge | 7, 10, 13 | 3 |
| Tennisplatz | 11, 12, 14 | 3 |
| Alter Baum | 13, 15 ×2 | 3 |
| Statue | 14 ×2 | 2 |
| Schwimmbad | 15 | 1 |

Quellen: die Zeile `rankAndPermits` jeder Moduldatei (`hq_corner_l.module.lua:247`, `hq_flag_ground.module.lua:79`, `hq_pool.module.lua:111`).

```tip scripts
Stelle das Hauptquartier in die Stadt, die am schnellsten wachsen soll, und füge dort Mittlere Gebäude hinzu: Sie sind die einzigen Module mit Wachstumsbonus.
```

## Gut zu wissen

- Um im Rang aufzusteigen, lass die Städte wachsen: mehr Passagiere und Fracht zu mehr Städten, mit guten Bewertungen. Geld auf der Bank zählt nicht.
- Plane deine Wahrzeichen und Prospektionen: Jedes kommt nur einmal, auf einem festen Rang.
- Auf einer Karte mit Inflation ist ein Rangaufstieg gut für die Vorteile und schlecht für die Einnahmen. Bei Normal kostet der ganze Weg bis Rang 15 ein Viertel aller Einnahmen.

```check
official: "The company rank depends on the population of the map. … Once the population passes the next threshold, the company will level up." "Headquarters upgrades are sometimes purely decorative, but most add-on modules either increase the reputation recovery or the town growth of the capital." ([Company and Finances](https://wiki.transportfever3.com/doku.php?id=gamemanual:management:companyandfinances))
scripts: Gleiche Regel: die höchste erreichte Weltbevölkerung, verglichen mit der Startbevölkerung, ×12,5 für Rang 15; nie verloren. Ein neuer Rang muss im Unternehmensfenster ausgewählt werden, um seine Vorteile freizuschalten, während Inflation die Einnahmen sofort senkt. Nur zwei Module haben einen Bonus (Mittleres Gebäude +1 % Wachstum, Grosses Gebäude +1 % Rufwiederherstellung, die keine Bewertung liest); die anderen sind Dekoration.
result: refines
```
